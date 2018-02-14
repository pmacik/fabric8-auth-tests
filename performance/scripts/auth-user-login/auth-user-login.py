import json
import os
import threading
import time
import urllib

from locust import HttpLocust, TaskSet, task, events
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

_serverScheme = "@@SERVER_SCHEME@@"
_serverHost = "@@SERVER_HOST@@"

_userNames = []
_userPasswords = []
_currentUser = 0
_userLock = threading.RLock()

usenv = os.getenv("USERS_PROPERTIES")
lines = usenv.split('\n')

_users = len(lines)

for u in lines:
    up = u.split('=')
    _userNames.append(up[0])
    _userPasswords.append(up[1])


class UserScenario(TaskSet):
    timeout = 60
    taskUser = -1
    taskUserName = ""
    taskUserPassword = ""

    start = -1
    stop = -1

    def on_start(self):
        global _currentUser, _users, _userLock, _userNames, _userPasswords
        _userLock.acquire()
        self.taskUser = _currentUser
        if _currentUser < _users - 1:
            _currentUser += 1
        else:
            _currentUser = 0
        _userLock.release()
        self.taskUserName = _userNames[self.taskUser]
        self.taskUserPassword = _userPasswords[self.taskUser]

    def tick_timer(self):
        self.stop = time.time()
        ret_val = (self.stop - self.start) * 1000
        self.start = self.stop
        return ret_val

    def reset_timer(self):
        self.start = time.time()

    @task
    def loginUserAuth(self):
        request_type = "loginUserAuth"
        opts = webdriver.ChromeOptions()
        opts.add_argument("--headless")
        opts.add_argument("--window-size=1280,960")

        driver = webdriver.Chrome(chrome_options=opts)

        self.reset_timer()
        driver.get(self.locust.host + "/api/login?redirect=http%3A%2F%2Flocalhost%3A8090%2Flink.html")

        events.request_success.fire(request_type=request_type, name="open-login-page-time", response_time=self.tick_timer(), response_length=0)

        WebDriverWait(driver, self.timeout).until(
            EC.element_to_be_clickable((By.ID, "kc-login"))
        )

        driver.find_element_by_id("username").send_keys(self.taskUserName)
        passwd = driver.find_element_by_id("password")
        passwd.send_keys(self.taskUserPassword)
        self.reset_timer()
        passwd.submit()
        WebDriverWait(driver, self.timeout).until(
            EC.url_contains("access_token")
        )
        events.request_success.fire(request_type=request_type, name="login-time", response_time=self.tick_timer(), response_length=0)

        try:
            token_json = json.loads(urllib.splitquery(urllib.unquote(driver.current_url))[1].split("=")[1])
        # print token_json["access_token"] + ";" + token_json["refresh_token"]
        except ValueError:
            events.request_failure.fire(request_type=request_type, name="login-time", response_time=self.tick_timer(), response_length=0)
        driver.quit()


class UserLocust(HttpLocust):
    task_set = UserScenario
    host = _serverScheme + "://" + _serverHost
    min_wait = 1000
    max_wait = 1000

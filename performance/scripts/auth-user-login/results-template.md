# Results (@@JOB_BASE_NAME@@ #@@BUILD_NUMBER@@ @@TIMESTAMP@@)
## Summary
The following tables show the final results taken and computed from a single test run - i.e. after and by running the login phase and the 5 minutes of the load phase.

The summary results of each run are uploaded to the
[Zabbix](https://zabbix.devshift.net:9443/zabbix/screens.php?elementid=32&fullscreen=1)
monitoring system to track the results' history.

### Load Test
| Scenario | Minimal (Auth) | Minimal (OAuth2) | Median (Auth) | Median (OAuth2) | Maximal (Auth) |Maximal (OAuth2) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| `open-login-page-time` | @@OPEN_LOGIN_PAGE_TIME_MIN@@ ms | @@OAUTH2_OPEN_LOGIN_PAGE_TIME_MIN@@ ms | @@OPEN_LOGIN_PAGE_TIME_MEDIAN@@ ms | @@OAUTH2_OPEN_LOGIN_PAGE_TIME_MEDIAN@@ ms | @@OPEN_LOGIN_PAGE_TIME_MAX@@ ms | @@OAUTH2_OPEN_LOGIN_PAGE_TIME_MAX@@ ms |
| `get-code-time` | - | @@OAUTH2_GET_CODE_TIME_MIN@@ ms | - | @@OAUTH2_GET_CODE_TIME_MEDIAN@@ ms | - | @@OAUTH2_GET_CODE_TIME_MAX@@ ms |
| `get-token-time` | - | @@OAUTH2_GET_TOKEN_TIME_MIN@@ ms | - | @@OAUTH2_GET_TOKEN_TIME_MEDIAN@@ ms | - | @@OAUTH2_GET_TOKEN_TIME_MAX@@ ms |
| `login-time` | @@LOGIN_TIME_MIN@@ ms | @@OAUTH2_LOGIN_TIME_MIN@@ ms | @@LOGIN_TIME_MEDIAN@@ ms | @@OAUTH2_LOGIN_TIME_MEDIAN@@ ms | @@LOGIN_TIME_MAX@@ ms | @@OAUTH2_LOGIN_TIME_MAX@@ ms |

## Test charts
The charts bellow show the whole duration of all the phases for each scenario - i.e. what lead to the final results shown above in the summary.

### Load Test
In these charts, the value shown in each point of time is the metric (minimal, median, maximal and average value) of the response time
computed for a time window from the start to the respective point of time. So it is a floating metric.

That is the reason for the values of the maximals always go up.
#### `open-login-page-time` Response Time
![open-login-page-time-reponse-time](./@@JOB_BASE_NAME@@-@@BUILD_NUMBER@@-loginUserAuth_open-login-page-time-response-time.png)
![open-login-page-time-minimal-reponse-time](./@@JOB_BASE_NAME@@-@@BUILD_NUMBER@@-loginUserAuth_open-login-page-time-minimal-response-time.png)
![open-login-page-time-median-reponse-time](./@@JOB_BASE_NAME@@-@@BUILD_NUMBER@@-loginUserAuth_open-login-page-time-median-response-time.png)
![open-login-page-time-maximal-reponse-time](./@@JOB_BASE_NAME@@-@@BUILD_NUMBER@@-loginUserAuth_open-login-page-time-maximal-response-time.png)
![open-login-page-time-average-reponse-time](./@@JOB_BASE_NAME@@-@@BUILD_NUMBER@@-loginUserAuth_open-login-page-time-average-response-time.png)
![open-login-page-time-rt-histo](./@@JOB_BASE_NAME@@-@@BUILD_NUMBER@@-loginUserAuth_open-login-page-time-rt-histo.png)
#### `open-login-page-time` Failures
![open-login-page-time-failures](./@@JOB_BASE_NAME@@-@@BUILD_NUMBER@@-loginUserAuth_open-login-page-time-failures.png)

#### `login-time` Response Time
![login-time-reponse-time](./@@JOB_BASE_NAME@@-@@BUILD_NUMBER@@-loginUserAuth_login-time-response-time.png)
![login-time-minimal-reponse-time](./@@JOB_BASE_NAME@@-@@BUILD_NUMBER@@-loginUserAuth_login-time-minimal-response-time.png)
![login-time-median-reponse-time](./@@JOB_BASE_NAME@@-@@BUILD_NUMBER@@-loginUserAuth_login-time-median-response-time.png)
![login-time-maximal-reponse-time](./@@JOB_BASE_NAME@@-@@BUILD_NUMBER@@-loginUserAuth_login-time-maximal-response-time.png)
![login-time-average-reponse-time](./@@JOB_BASE_NAME@@-@@BUILD_NUMBER@@-loginUserAuth_login-time-average-response-time.png)
![login-time-rt-histo](./@@JOB_BASE_NAME@@-@@BUILD_NUMBER@@-loginUserAuth_login-time-rt-histo.png)
#### `login-time` Failures
![login-time-failures](./@@JOB_BASE_NAME@@-@@BUILD_NUMBER@@-loginUserAuth_login-time-failures.png)

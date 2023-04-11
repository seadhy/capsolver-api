import requests
import time
from typing import Dict, Literal
from .exceptions import CapsolverException


class Capsolver:
    def __init__(self, client_key: str, task_type: str = None):
        self.task_type = task_type
        self.client_key = client_key
        self.api_url = 'https://api.capsolver.com'
        self.retries_number = 60

        self.exceptions = {
            'ERROR_KEY_DOES_NOT_EXIST': 'The clientkey you provided is incorrect.',
            'ERROR_SERVICE_UNAVALIABLE': 'It is possible that the server pressure is high, please try again later, if it continues to appear please contact customer service.',
            'ERROR_RATE_LIMIT': 'Service packages request rate limit. When this error occurs, you have exceeded the rate limit.',
            'ERROR_INVALID_TASK_DATA': 'Data parsing failure.',
            'ERROR_BAD_REQUEST': 'Request error, if it persists please contact customer service.',
            'ERROR_TASKID_INVALID': 'Wrong ID was requested, or the ID no longer exists.',
            'ERROR_TASK_TIMEOUT': 'If the recognition is still not successful in 120 seconds, a timeout error will be reported.',
            'ERROR_SETTLEMENT_FAILED': 'Please check your balance or contact customer service.',
            'ERROR_KEY_DENIED_ACCESS': 'Please check if your clientKey key is correct, get it in the personal center.',
            'ERROR_ZERO_BALANCE': 'The account balance is not enough to offset the consumption, please top up.',
            'ERROR_TASK_NOT_SUPPORTED': 'Captcha type is incorrect or not yet supported.',
            'ERROR_CAPTCHA_UNSOLVABLE': 'No deduction, please try again.',
            'ERROR_UNKNOWN_QUESTION': 'Normaly the task cannot be processed.',
            'ERROR_PROXY_BANNED': 'Proxy IP banned by target service.',
            'ERROR_INVALID_IMAGE': 'Invalid image.',
            'ERROR_PARSE_IMAGE_FAIL': 'Please check if the image BASE64 encoding is correct.',
            'ERROR_IP_BANNED': 'If a large number of errors (up to 1000 times) occur within a short period of time (within 1 minute), the system will automatically blocked for 30 minutes. Please check your error information and try again.',
            'ERROR_KEY_TEMP_BLOCKED': 'Due to too many error, requests have been blocked and will be automatically unblocked in 5 minutes, please try again later.',
        }

        self.intervals = {
            'HCaptcha': [1, 10],
            'FunCaptcha': [1, 20],
            'GeeTest': [3, 10],
            'ReCaptcha': [1, 10],
            'MtCaptcha': [5, 30],
            'Datadome': [1, 20],
            'Cloudflare': [1, 20]
        }

    def make_request(self, url_path: Literal['/createTask', '/getTaskResult', '/getBalance'], payload: Dict) -> requests.Response:
        req = requests.post(self.api_url + url_path, json=payload)

        return req
    def get_solution(self, task_id: str):
        time.sleep(self.intervals[self.task_type][0])
        for _ in range(self.intervals[self.task_type][1] * 3):
            r = self.make_request('/getTaskResult', {"clientKey": self.client_key, "taskId": task_id})
            if r.status_code == 200:
                if r.json()['status'] == 'ready':
                    return r.json()['solution']
                elif r.json()['status'] == 'processing':
                    time.sleep(1)
                elif r.json()['status'] == 'failed':
                    self.error_handle(r.json()['errorDescription'])

    def error_handle(self, error: str):
        raise CapsolverException(error)

    def get_balance(self):
        data = self.make_request('/getBalance', {"clientKey": self.client_key})
        if data.status_code == 200:
            return data.json()

        self.error_handle(self.exceptions[data.json()['errorCode']])

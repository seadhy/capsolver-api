from typing import Optional, Literal
from ..capsolver_api import Capsolver


class GeeTestTask(Capsolver):
    def __init__(self, client_key: str):
        super().__init__(client_key, 'GeeTest')

    def create_task(self,
                    task_type: Literal['GeeTestTask', 'GeeTestTaskProxyLess'] = None,
                    website_url: str = None,
                    website_key: str = None,
                    gt: str = None,
                    challenge: Optional[str] = None,  # optional as it is not always certain: 'If you need to solve Geetest V3 you must use this parameter, don't need if you need to solve GeetestV4'
                    captcha_id: Optional[str] = None,
                    api_server_subdomain: Optional[str] = None,
                    proxy: Optional[str] = None
                    ):

        if all((task_type, website_url, website_key, gt)):
            payload = {
              "clientKey": self.client_key,
              "task": {
                "type": task_type,
                "websiteURL": website_url,
                "gt": gt
              }
            }

            payload['task'].update({'challenge': challenge} if challenge else {})
            payload['task'].update({'captchaId': captcha_id} if captcha_id else {})
            payload['task'].update({'geetestApiServerSubdomain': api_server_subdomain} if api_server_subdomain else {})
            payload['task'].update({'proxy': proxy} if proxy else {})

            create_task_req = self.make_request('/createTask', payload)
            if create_task_req.status_code == 200:
                return create_task_req.json()['taskId']
            else:
                print('Error: ' + create_task_req.text)
        else:
            return 'Please give the values of task_type, website_url and website_key and try again.'

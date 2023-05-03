from typing import Optional, Literal
from ..capsolver_api import Capsolver


class FunCaptchaTask(Capsolver):
    def __init__(self, client_key: str):
        super().__init__(client_key, 'FunCaptcha')

    def create_task(self,
                    task_type: Literal['FunCaptchaTask', 'FunCaptchaTaskProxyLess'] = None,
                    website_url: str = None,
                    website_key: str = None,
                    api_js_subdomain: Optional[str] = None,
                    data: Optional[str] = None,
                    proxy: Optional[str] = None
                    ):

        if all((task_type, website_url, website_key)):
            payload = {
              "clientKey": self.client_key,
              "task": {
                "type": task_type,
                "websiteURL": website_url,
                "websiteKey": website_key,
              }
            }

            payload['task'].update({'funcaptchaApiJSSubdomain': api_js_subdomain} if api_js_subdomain else {})
            payload['task'].update({'data': data} if data else {})
            payload['task'].update({'proxy': proxy} if proxy else {})

            create_task_req = self.make_request('/createTask', payload)
            if create_task_req.status_code == 200:
                return create_task_req.json()['taskId']
            else:
                print('Error: ' + create_task_req.text)
        else:
            return 'Please give the values of task_type, website_url and website_key and try again.'

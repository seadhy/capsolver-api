from typing import Optional, Literal
from ..capsolver_api import Capsolver


class MtCaptchaTask(Capsolver):
    def __init__(self, client_key: str):
        super().__init__(client_key, 'MtCaptcha')

    def create_task(self,
                    task_type: Literal['MtCaptchaTask', 'MtCaptchaTaskProxyLess'] = None,
                    website_url: str = None,
                    website_key: str = None,
                    proxy: Optional[str] = None,
                    ):

        if all((task_type, website_url, website_key)):
            payload = {
              "clientKey": self.client_key,
              "task": {
                "type": task_type,
                "websiteURL": website_url,
                "websiteKey": website_url
              }
            }

            payload['task'].update({'proxy': proxy} if proxy else {})

            create_task_req = self.make_request('/createTask', payload)
            if create_task_req.status_code == 200:
                return create_task_req.json()['taskId']
            else:
                print('Error: ' + create_task_req.text)
        else:
            return 'Please give the values of task_type, website_url and website_key and try again.'

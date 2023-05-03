from typing import Literal
from ..capsolver_api import Capsolver


class DatadomeTask(Capsolver):
    def __init__(self, client_key: str):
        super().__init__(client_key, 'Datadome')

    def create_task(self,
                    task_type: Literal['DataDomeSliderTask'] = None,
                    website_url: str = None,
                    captcha_url: str = None,
                    proxy: str = None,
                    useragent: str = None
                    ):

        if all((task_type, website_url, captcha_url, proxy, useragent)):
            payload = {
              "clientKey": self.client_key,
              "task": {
                "type": task_type,
                "websiteURL": website_url,
                "captchaUrl": captcha_url,
                "proxy": proxy,
                "userAgent": useragent
              }
            }


            create_task_req = self.make_request('/createTask', payload)
            if create_task_req.status_code == 200:
                return create_task_req.json()['taskId']
            else:
                print('Error: ' + create_task_req.text)
        else:
            return 'Please give the values of task_type, website_url, website_key, captcha_url, proxy and useragent and try again.'

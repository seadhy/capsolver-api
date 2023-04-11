from typing import Optional, Literal
from ..capsolver_py import Capsolver


class HCaptchaTask(Capsolver):
    def __init__(self, client_key: str):
        super().__init__(client_key, 'HCaptcha')

    def create_task(self,
                    task_type: Literal['HCaptchaTask', 'HCaptchaTaskProxyLess',
                                       'HCaptchaEnterpriseTask', 'HCaptchaEnterpriseTaskProxyLess',
                                       'HCaptchaTurboTask', 'HCaptchaTurboTaskProxyLess'] = None,
                    website_url: str = None,
                    website_key: str = None,
                    is_invisible: Optional[bool] = False,
                    proxy: Optional[str] = None,
                    enable_ipv6: Optional[bool] = False,
                    enterprise_payload: Optional[dict] = None,
                    user_agent: Optional[str] = None
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

            payload['task'].update({'isInvisible': is_invisible} if is_invisible else {})
            payload['task'].update({'enterprisePayload': enterprise_payload} if enterprise_payload else {})
            payload['task'].update({'proxy': proxy} if proxy else {})
            payload['task'].update({'enableIPV6': enable_ipv6} if enable_ipv6 else {})
            payload['task'].update({'userAgent': user_agent} if user_agent else {})

            create_task_req = self.make_request('/createTask', payload)
            if create_task_req.status_code == 200:
                return create_task_req.json()['taskId']
            else:
                print('Error: ' + create_task_req.text)
        else:
            return 'Please give the values of task_type, website_url and website_key and try again.'

from typing import Optional, Literal
from ..capsolver_api import Capsolver


class ReCaptchaV3Task(Capsolver):
    def __init__(self, client_key: str):
        super().__init__(client_key, 'ReCaptcha')

    def create_task(self,
                    task_type: Literal['ReCaptchaV3Task', 'ReCaptchaV3TaskProxyLess', 'ReCaptchaV3EnterpriseTask', 'ReCaptchaV3EnterpriseTaskProxyLess'] = None,
                    website_url: str = None,
                    website_key: str = None,
                    page_action: str = None,
                    min_score: Optional[float] = None,
                    proxy: Optional[str] = None,
                    api_domain: Optional[str] = None,
                    enterprise_payload: Optional[dict] = None,
                    user_agent: Optional[str] = None,
                    cookies: Optional[list] = None
                    ):

        if all((task_type, website_url, website_key, page_action)):
            payload = {
              "clientKey": self.client_key,
              "task": {
                "type": task_type,
                "websiteURL": website_url,
                "websiteKey": website_url,
                "pageAction": page_action
              }
            }

            payload['task'].update({'minScore': min_score} if min_score else {})
            payload['task'].update({'enterprisePayload': enterprise_payload} if enterprise_payload else {})
            payload['task'].update({'proxy': proxy} if proxy else {})
            payload['task'].update({'apiDomain': api_domain} if api_domain else {})
            payload['task'].update({'userAgent': user_agent} if user_agent else {})
            payload['task'].update({'cookies': cookies} if cookies else {})

            create_task_req = self.make_request('/createTask', payload)
            if create_task_req.status_code == 200:
                return create_task_req.json()['taskId']
            else:
                print('Error: ' + create_task_req.text)
        else:
            return 'Please give the values of task_type, website_url and website_key and try again.'

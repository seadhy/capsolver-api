from typing import Literal
from ..capsolver_py import Capsolver


class CloudflareChallengeTask(Capsolver):
    def __init__(self, client_key: str):
        super().__init__(client_key, 'Cloudflare')

    def create_task(self,
                    task_type: Literal['AntiCloudflareTask'] = None,
                    website_url: str = None,
                    metadata: dict = None,
                    html: str = None,
                    proxy: str = None
                    ):

        if all((task_type, website_url, metadata, html, proxy)):
            payload = {
                "clientKey": self.client_key,
                "task": {
                    "type": task_type,
                    "websiteURL": website_url,
                    "metadata": metadata,
                    "html": html,
                    "proxy": proxy,
                }
            }

            create_task_req = self.make_request('/createTask', payload)
            if create_task_req.status_code == 200:
                return create_task_req.json()['taskId']
            else:
                print('Error: ' + create_task_req.text)
        else:
            return 'Please give the values of task_type, website_url and website_key and try again.'

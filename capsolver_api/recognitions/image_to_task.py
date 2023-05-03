from typing import Optional
from ..capsolver_api import Capsolver


class ImageToTextTask(Capsolver):
    def __init__(self, client_key: str):
        super().__init__(client_key)

    def create_task(self,
                    body: str = None,
                    module: Optional[str] = None,
                    score: Optional[float] = None,
                    case: Optional[bool] = None
                    ):

        if body:
            payload = {
              "clientKey": self.client_key,
              "task": {
                "type": 'ImageToTextTask',
                "body": body,
              }
            }

            payload['task'].update({'module': module} if module else {})
            payload['task'].update({'score': score} if score else {})
            payload['task'].update({'case': case} if case else {})

            create_task_req = self.make_request('/createTask', payload)
            if create_task_req.status_code == 200:
                return create_task_req.json()['solution'] if create_task_req.json()['status'] == 'ready' else {}
            else:
                print('Error: ' + create_task_req.text)
        else:
            return 'Please give the values of task_type, website_url and website_key and try again.'

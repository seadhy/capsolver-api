from typing import List
from ..capsolver_api import Capsolver


class HCaptchaClassification(Capsolver):
    def __init__(self, client_key: str):
        super().__init__(client_key)

    def create_task(self,
                    queries: List[str] = None,
                    question: str = None,
                    ):

        if all((queries, question)):
            payload = {
              "clientKey": self.client_key,
              "task": {
                "type": 'HCaptchaClassification',
                "queries": queries,
                "question": question
              }
            }


            create_task_req = self.make_request('/createTask', payload)
            if create_task_req.status_code == 200:
                return create_task_req.json()['solution'] if create_task_req.json()['status'] == 'ready' else {}
            else:
                print('Error: ' + create_task_req.text)
        else:
            return 'Please give the values of task_type, website_url and website_key and try again.'

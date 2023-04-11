import capsolver_api

capsolver = capsolver_api.HCaptchaTask('your_capsolver_api_key')

print(capsolver.get_balance())

task_id = capsolver.create_task(task_type='HCaptchaTaskProxyLess',
                                website_url='https://accounts.hcaptcha.com/demo',
                                website_key='a5f74b19-9e45-40e0-b45d-47ff91b7a6c2'
                                )

print(capsolver.get_solution(task_id))


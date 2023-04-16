from capsolver_api import HCaptchaTask

capsolver = HCaptchaTask('your_capsolver_api_key')

task_id = capsolver.create_task(task_type='HCaptchaTaskProxyLess',
                                website_url='https://accounts.hcaptcha.com/demo',
                                website_key='a5f74b19-9e45-40e0-b45d-47ff91b7a6c2'
                                )

captcha_key = capsolver.get_solution(task_id)
print(captcha_key)

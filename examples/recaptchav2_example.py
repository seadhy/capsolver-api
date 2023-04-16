from capsolver_api import ReCaptchaV2Task


capsolver = ReCaptchaV2Task('your_capsolver_api_key')

task_id = capsolver.create_task(task_type='ReCaptchaV2TaskProxyLess',
                                website_url='https://www.google.com/recaptcha/api2/reload?k=6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-',
                                website_key='6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-',
                                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'  # optional
                                )

captcha_key = capsolver.get_solution(task_id)
print(captcha_key)

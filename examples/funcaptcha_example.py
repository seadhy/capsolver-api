from capsolver_api import FunCaptchaTask


capsolver = FunCaptchaTask('your_capsolver_api_key')

task_id = capsolver.create_task(task_type='FunCaptchaTaskProxyLess',
                                website_url='https://api.funcaptcha.com/tile-game-lite-mode/fc/api/nojs/',
                                website_key='69A21A01-CC7B-B9C6-0F9A-E7FA06677FFC'
                                )

captcha_key = capsolver.get_solution(task_id)
print(captcha_key)

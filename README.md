<h3>
        <h3>CapSolver.com</h3>
        <br>
        <a href="https://dashboard.capsolver.com/passport/register?inviteCode=G2QOL-c1l_7z">
            <img src="https://cdn.discordapp.com/attachments/1105172394655625306/1105180101802471575/20221207-160749.gif" alt="Capsolver's Banner">
        </a>
</h3>
<br>
At the lowest price on the market, you may receive a variety of solutions, including reCAPTCHA V2, reCAPTCHA V3, hCaptcha, hCaptcha Click, FunCaptcha, picture-to-text, and more. With this service, 0.1s is the slowest speed ever measured.
<hr>


# Capsolver API for Python 
Captcha solution api for capsolver.com

## Download
``python -m pip install capsolver-api``

## Examples

### Hcaptcha
````python
from capsolver_api import HCaptchaTask

capsolver = HCaptchaTask('your_capsolver_api_key')


task_id = capsolver.create_task(task_type='HCaptchaTaskProxyLess',
                                website_url='https://accounts.hcaptcha.com/demo',
                                website_key='a5f74b19-9e45-40e0-b45d-47ff91b7a6c2'
                                )

captcha_key = capsolver.get_solution(task_id)
print(captcha_key)
````

### Funcaptcha
````python
from capsolver_api import HCaptchaTask

capsolver = HCaptchaTask('your_capsolver_api_key')


task_id = capsolver.create_task(task_type='HCaptchaTaskProxyLess',
                                website_url='https://accounts.hcaptcha.com/demo',
                                website_key='a5f74b19-9e45-40e0-b45d-47ff91b7a6c2'
                                )

captcha_key = capsolver.get_solution(task_id)
print(captcha_key)
````

### RecaptchaV2
````python
from capsolver_api import ReCaptchaV2Task


capsolver = ReCaptchaV2Task('your_capsolver_api_key')


task_id = capsolver.create_task(task_type='ReCaptchaV2TaskProxyLess',
                                website_url='https://www.google.com/recaptcha/api2/reload?k=6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-',
                                website_key='6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-',
                                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'  # optional
                                )

captcha_key = capsolver.get_solution(task_id)
print(captcha_key)
````

### And others:
- Cloudflare (Turnstile / Challenge)
- Datadome
- Geetest
- Mtcaptcha
- Other recognitions
- More information for [docs](https://docs.capsolver.com/guide/getting-started.html)

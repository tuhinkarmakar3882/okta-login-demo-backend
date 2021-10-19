# okta-login-demo-backend

How to run the app?

- Clone the repo
- Make sure you have python 3
- Make sure you have virtualenv
  - In case if you do not have it, run `pip install virtualenv`
- `virtualenv venv`
- if you are on windows,
  - ./venv/Scripts/activate
- if you're on linux/mac
  - source venv/bin/activate

- Install the deps by `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py runserver`

> Lastly, Make sure to replace the values at `okta_login_backend/views.py`

```python
client_secret = 'your-okta-client-secret-goes-here'
client_id = 'your-okta-client-id-goes-here'
domain_url = 'your-okta-domain-url-goes-here'
```
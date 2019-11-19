# nan_blog_sprint_final


```python
import  requests
import json
acces = 'EAAe1kaMBgKUBAIuSGkSOcVy5pjkfOCFyJZAmQwJn576q6K0GxGeabs0FCfWGXwtD9HNS54Onc5vRtuHRmE1bYcw0XdX3h23PGMaZBXZAKaNkFLlabR0TuCIkqGDUbhWEp89PUOWHbVZAxAvUBA8gEAJFRv7ZCyliTS3rsNZC5kYDwOZAYkQWLH1fFOz3kPWrrZCxkSXgTkWVPR8sFGZBvzoraOaOtBvWNnfHtbOpVoTSuzwZDZD'

url_me='https://graph.facebook.com/v5.0/me?access_token={}'.format(acces)
url_friends='https://graph.facebook.com/v5.0/me/friends?access_token={}'.format(acces)
url_search='https://graph.facebook.com/v5.0/search?q=willy coby&type=user&access_token={}'.format(acces)
response = requests.get(url_me)
print(response.status_code)
print(response.text)
```

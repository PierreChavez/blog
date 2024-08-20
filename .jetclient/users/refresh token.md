```toml
name = 'refresh token'
method = 'POST'
url = 'http://localhost:8003/api/auth/login/'
sortWeight = 4000000
id = '177c4167-1e68-4510-8e58-c56b1312623c'

[[headers]]
key = 'Content-Type'
value = 'application/json'

[body]
type = 'JSON'
raw = '''
{
  "email": "testeee@examplrtt.com",
  "password": "1234567867"
}'''
```

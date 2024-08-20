```toml
name = 'get token'
method = 'POST'
url = 'http://localhost:8003/api/auth/login/'
sortWeight = 3000000
id = '0fc146f4-6153-4401-9561-4d309b7f33e1'

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

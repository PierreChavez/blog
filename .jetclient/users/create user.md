```toml
name = 'create user'
method = 'POST'
url = 'http://localhost:8003/api/auth/register/'
sortWeight = 1000000
id = '84dd5c0c-a59f-4868-8ced-cc181c29c387'

[[headers]]
key = 'Content-Type'
value = 'multipart/form-data'

[[body.formData]]
key = 'password'
value = '1234567867'

[[body.formData]]
key = 'username'
value = 'pierre3456ggrr3'

[[body.formData]]
key = 'email'
value = 'testeee@examplrtt.com'
```

```toml
name = 'create user'
method = 'POST'
url = 'http://localhost:8003/api/users/'
sortWeight = 1000000
id = '84dd5c0c-a59f-4868-8ced-cc181c29c387'

[[headers]]
key = 'Content-Type'
value = 'multipart/form-data'

[[body.formData]]
key = 'password'
value = '12345'

[[body.formData]]
key = 'username'
value = 'pierre34'

[[body.formData]]
key = 'email'
value = 'test@exampl.com'
```

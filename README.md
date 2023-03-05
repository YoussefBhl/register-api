# register-api

## Description

This project is an API for register api That contains two endpoints `/users` (register & send an email confirmation code to user) and `/users/confirm-code` (to confirm user's code with expiration time 1 minute)

## Project structure 

![Project structure](./docs/project_structure.png)

**tests**: unit tests  
**api**: contains different routes with its dependencies  
**builders**: query builder which help to create sql queries (we didn't use ORM)  
**constants**: global constants used in the globaly in the project  
**core**: contains database connection and password hashing  
**managers**: manager that contains CRUD operation for each table  
**models**: different table models  
**repositories**: contains services like (db operations, external API calls ...)   
**schemas**: contains different routes schemas  

## Database 
for this project we used a Mysql database with one table `users`

![Project structure](./docs/users_db.png)

## Run and test locally

**Run API**
```bash
register-api$ make docker-start
```

- *Before calling the API you need to get your local IP (type ifconfig on your terminal). My local ip is 10.0.2.15 you need to put yours in the host*

- *you can use Swagger docs on a navigator or just copy and paste curls commands*



**POST \users**

```bash
register-api$ curl -L -X POST \
  http://10.0.2.15:8000/users \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{
"email": "testsaq@test.com",
"password": "test"
}'
```
*You will find the code confirmation in the console, copy it and past*

**POST users/confirm-code**

```bash
register-api$ curl -L -X POST \
  http://10.0.2.15:8000/users/confirm-code \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'authorization: Basic dGVzdEB0ZXN0LmNvbTp0ZXN0' \
  -d '{
"code": XXXX
}'
```

*PS: you have only one minute to confirm your code. Also, if you changed the email or the password (in the example) you need to change the authorization header*

## Unit tests

Tests are defined in the `tests` folder in this project.

```bash
exam-api$ make unit-test
```
## Improvements

Because of lack of time, there are some improvements to consider

- Add more unit test, no all use cases have been implemented and add asynchronous test library
- Add constraints to Password
- The generated code is between 1000 and 9999 so we can't generate code that starts with 0. therefore we can add logic to generate codes that starts with

# Dawson's SAS Interview
**Dawson Webb coding project for SAS Interview**

## Table of Contents  
[Requirements](#requirements)

[Information](#info)

[Docker File](#docker)



<a name="requirements"/>

## Requirements:
>BASE_URL = https://reqres.in/api
#### Your test script should perform the following verifications, minimally:
1. Attempt to login via a POST request to $BASE_URL/login
    - Verify response when a successful POST request is submitted
    - Verify response when a POST request is submitted is incomplete
2. GET a list of users from the $BASE_URL/users endpoint
    - Verify response, and report on the number of users returned, for a successful GET request is submitted.
3. GET information on a specific user
    - Verify response and correctly structured JSON is data returned for a specific, valid user.
    - Verify response when an invalid user is requested.
4. POST to $BASE_URL/users to create a new user
    - Create user and verify response is given with the expected JSON attributes
5. DELETE a user
    - Verify proper response is received

Test application should report on the pass/fail status of each test.

<a name="info"/>

## Information
### Main.py
Runs the test application. When running `python3 main.py` in the command line it will prompt the user with input to select which test to run. When running in a docker container the program will detect that and run through some sample test cases.
### User.py
#### &nbsp;&nbsp;&nbsp; Global Variables: 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **SECRET_KEY** is a boolean that will check if the dockerfile env variable which if it is in a docker container will result in True. \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **BASE_URL** is a string of the API base URL "_https://reqres.in/api/_"


<a name="docker"/>

## Docker File
_Program will check to see if it is in a Docker Container when ran_
```
# DockerFile, Image, Container
FROM python:3.8

ADD main.py .

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

ENV IN_DOCKER_CONTAINER Yes

CMD [ "python", "./main.py" ]

```

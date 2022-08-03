# Dawson's SAS Interview
**Dawson Webb coding project for SAS Interview**

## Information / Requirements:
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

Your test application should report on the pass/fail status of each test.

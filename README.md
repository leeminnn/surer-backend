# How to run

### Step 1

### `docker-compose up -d`

This command installs a package and any packages that it depends on.

### Step 2

### `pip install -r requirements.txt`

Install the needed packages with the specified version

### Step 3

### `python app.py`

Run app.py

### Step 4

### Open postman and test endpoints

1. Test for registration

Go to file > import > Raw text

Enter `curl --location --request POST 'http://0.0.0.0:5000/registration' \ --header 'Content-Type: application/json' \ --data-raw '{ "first_name": "test", "last_name": "test", "email": "test@test.com", "password": "test" }' `

Once done click continue and import. Then just press send in orange button.

2. Test for Login

Go to file > import > Raw text

Enter `curl --location --request POST 'http://0.0.0.0:5000/login' \ --header 'Content-Type: application/json' \ --data-raw '{ "email": "test@test.com", "password": "test" }' `

Once done click continue and import. Then just press send in orange button.

3. Test for viewing members details

Go to file > import > Raw text

Enter `curl --location --request GET 'http://0.0.0.0:5000/carpark_availability' \ --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyOTIxMzM5NSwianRpIjoiYTJlODU0NGMtMDQ4Ni00N2FiLTk0ZGItNTE1ZDBkYzhmMGFmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRlc3RAdGVzdC5jb20iLCJuYmYiOjE2MjkyMTMzOTUsImV4cCI6MTYyOTIxNDI5NX0.XLl0hbU7Mh6AAhFWgBnUSNN_L2TI3Q8ZtgwW02Hs3Yk'`

Once done click continue and import. Then just press send in orange button.

4. Test for carpark availability

Enter `curl --location --request GET 'http://0.0.0.0:5000/carpark_availability' \ --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyOTIxMzM5NSwianRpIjoiYTJlODU0NGMtMDQ4Ni00N2FiLTk0ZGItNTE1ZDBkYzhmMGFmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRlc3RAdGVzdC5jb20iLCJuYmYiOjE2MjkyMTMzOTUsImV4cCI6MTYyOTIxNDI5NX0.XLl0hbU7Mh6AAhFWgBnUSNN_L2TI3Q8ZtgwW02Hs3Yk'`

Once done click continue and import. Then just press send in orange button.

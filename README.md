# tech-challenge
Simple API for querying user data

# Implemented Route
### Check User by CPF
URL: http://localhost:8000/api/v1/user/{user_cpf}
The simulated data is available in /mocks/seed.json.

# Execution Instructions
1. **Run mock APIs.** Run commands in parent directory. Each should be run in a different terminal. Port forwarded to localhost ports 8001 and 8002.
```
tech-challenge$ python3 ./mocks/cheap_api.py
tech-challenge$ python3 ./mocks/premium_api.py
```
2. **Run developed API.** Port forwarded to localhost port 8001.
```
tech-challenge$ python3 ./api/app.py
```
3. **Access FastAPI interface.** Open your preferred browser and open http://localhost:8000/docs/. This interface allows the user to test the API's available routes and check its responses.

3. **Alternative** You may also use software such as Postman to test the API, using the same URL for the route.

# Testing Instruction
1. **Run Pytest.** Run command in parent directory.
```
tech-challenge$ pytest
```


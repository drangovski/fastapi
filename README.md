# FastAPI CRUD

This is a simple FastAPI CRUD application. In order to try it out, please follow the instructions bellow:


##### 1. Clone the repo in your Projects folder
```git clone https://github.com/drangovski/fastapi-crud.git```


##### 2. Create a virtual environment in the project's folder
```python3 -m venv ./venv"```


##### 3. Activate the virtual environment
```source ./venv/bin/activate```


##### 4. Install the requirements
```pip install -r requirements.txt```


##### 5. Create Database
Create Postgres ```fastapi``` database

##### 6. Create **'local_settings.py'** file in the **'blog'** folder with the following settings:
```
SECRET_KEY = "<ADD SECRET KEY>"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
SQLALCHEMY_DATABASE_URL = "postgresql://<USER>:<PASS>@localhost:<PORT>/fastapi"
```

Note: You can generate secret key by using ```openssl rand -hex 32``` command in your terminal.


##### 7. Run uvicorn
```uvicorn blog.main:app --reload```


##### 8. Access the API in your browser (through the FastAPI docs)
```localhost:8000/docs/```


##### 9. Create an user. Authentication is required for all other endpoints.
NOTE: For username use the email address provided in the user creation process.

# NSFW Api

Python API

## Resources

| Dependency Name | Documentation                | Description                                                                            |
| --------------- | ---------------------------- | -------------------------------------------------------------------------------------- |
| FastAPI         | https://fastapi.tiangolo.com | FastAPI framework, high performance, easy to learn, fast to code, ready for production |
---

## Run Locally
This api was made using python 3.8.10, different versions might give different results and/or conflicts

To run locally run:

```
bash ./create_virtualenv.sh
uvicorn app.api:app --reload
```
Open your browser, type http://localhost:8000/docs to view the OpenAPI UI.
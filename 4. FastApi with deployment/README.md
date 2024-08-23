# Container MLOps Template repository

Learn how to create a container and package it with GitHub Actions. This repository template gives you a good starting point for a Dockerfile, GitHub Actions workflow, and Python code.

Depending on the type of model you need, you will need different workflow steps and most definitely a different `main.py` file. The default uses FastApi

### How to run

```
cd webapp
uvicorn --host 0.0.0.0 main:app
```

### Notes

- Routing to `docs` shows you the swagger ui documentation of the API
- You can also have it make the requests for you.
    - When you click on "Execute", it will execute the POST / GET request for you, along with showing you a curl command of how you can achieve the same.

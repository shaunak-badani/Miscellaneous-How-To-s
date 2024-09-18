# Nginx + WSGI (flask)

### How to use:

To start all services using docker-compose
```
sudo docker-compose up -d
```


After having made changes to some files, use this command to rebuild images and start containers.
```
sudo docker-compose up --build --force-recreate -d
```

Template obtained from [here](https://github.com/docker/awesome-compose). Flask version was updated due to errors, and size limits were commented out due to 400 bad requests on nginx on non-incognito browsers.
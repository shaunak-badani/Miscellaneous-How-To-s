# Docker tutorial

- Need a Dockerfile to build an image
- An image can use an existing image as a dependency
- `FROM <image>` sets the base image to `image`.
- All instructions that follow are executed in this base image.
- The notation for image is `name:tag` e.g. `ubuntu:22.04`

- The default directory when running any commands is `/`
- COPY copies files from the directory on the docker host (vm) to the image.
- `COPY <src> <dest>` will create a directory called <dest> in the image, and copy contents of src into <dest>.

- The `EXPOSE 8000` command ensures that our container has a listening port on 8000
- `CMD` is run when the `docker run` command is triggered, not run when the image is built.
- The command is stored in the image. It is run when the user starts a container based on this image.

Building the image:
```
cd webapi
sudo docker build -t test:latest .
```
Running a container based on the image:
```
sudo docker run -p 127.0.0.1:80:8000 test:latest
```
- The above command connects localhost and port 80 of the VM / docker host to the container port 8000. So if you wanted to host it on the VM for all IPs to listen to,
```
sudo docker run -p 0.0.0.0:80:8000 test:latest
```

[Build context](https://docs.docker.com/build/concepts/context/) is the set of files your build can access.

## Other docker commands

`docker image ls` - list all docker images, can also be achieved by `docker images`
`docker images -f "dangling=true"` filters out all images with no tags.
`docker images -f "dangling=true" -q` will show you only image ids of dangling images.
`sudo docker rmi $(docker images -f "dangling=true" -q)` will delete all dangling images.

`sudo docker container ls -a` lists all docker containers
`sudo docker container prune` deletes all stopped containers


# Nginx (Static files)

To start an nginx container directly from the web image of container, run:

```bash
sudo docker run -it --rm -d -p 8080:80 --name web nginx
```

To stop the container:
```bash
sudo docker stop web
```

If you have the following directory tree:
```
.
└── site-content
    └── index.html
```
You can run the following command to create a [bind mount volume](https://docs.docker.com/engine/storage/bind-mounts/). So when you change contents of `index.html`, since the container has a link to the file on the docker host (vm), the site is updated in real-time.

```bash
sudo docker run -it --rm -d -p 8080:80 --name web -v ./site-content:/usr/share/nginx/html nginx
```

#### Building custom nginx images

COPY this in a dockerfile:

```Dockerfile
FROM nginx:latest
COPY ./index.html /usr/share/nginx/html/index.html
```

Build the image: `sudo docker build -t webserver .`

Run the image: `sudo docker run -it --rm -d -p 8080:80 --name web webserver`

While building the image, it will copy the html files into the container. 
So this process is more static, and changing the html file on the docker host will not change the deployed website.

#### How to execute commands on a container after it is deployed (debugging):

```bash
sudo docker exec -i -t festive_allen bash
```

# Reverse proxy (nginx + flask)

Docker compose useful commands:

To start a docker compose configuration,
```
sudo docker-compose up -d
```


After having made changes to some files, use this command to rebuild images and start containers.
```
sudo docker-compose up --build --force-recreate -d
```
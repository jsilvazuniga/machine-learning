# Basic projet using FLASK in DOCKER

## Build application docker
```docker command
docker build -t img-flask .
```

## Run application
```docker command
docker run --name api-flask -d -p 5001:5000 img-flask
```

## Test application
Open your browser : http://localhost:5001

[Visite localhost:5001](http://localhost:5001)


> **📌 Importante:** You need to rebuild and run docker if you modify your code.

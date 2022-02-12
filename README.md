# Python Flask - Nginx microservices with Docker

- Install Docker Engine & Docker Compose

```
  $ sudo apt-get update
  $ sudo apt-get install docker-ce docker-ce-cli containerd.io

  $ sudo curl -L "https://github.com/docker/compose/releases/download/1.28.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  $ sudo chmod +x /usr/local/bin/docker-compose
```

### Docker

```
- Start the Docker daemon (if needed), or desktop app in Windows
$ sudo systemctl start docker. or sudo service docker start

docker-compose up --build --scale master=2 to create 2 mainApis(servers) and use Nginx's load balancer

docker-compose down (to kill and stop docker images)

```

- Sample http requests in terminal

```
curl -XGET "localhost/weather?city=athens"
curl -XGET "localhost/news?country=gb"
```

- Architecture Overview \*Outdated: Added nginx between client and main Api\

![Arch](https://github.com/manos-fr/News_Weather_Services_Python_Docker/blob/master/files/Screenshot_1.jpg?raw=true)

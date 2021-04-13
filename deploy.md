# deploy on lightsail

### create AWS lightsail instance

- ubuntu 20.4(focal)

### install dependencies and set configuration in lightsail

- install default dependencies

```sh
sudo apt-get update
sudo apt-get install -y --no-install-recommends tzdata g++ git curl
```

- install java

```sh
sudo add-apt-repository ppa:openjdk-r/ppa
sudo apt-get update
sudo apt-get install -y openjdk-8-jdk
```

- set JAVA_HOME path

```sh
# set JAVA_HOME path
JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk
source /etc/environment && export JAVA_HOME
```

- install python

```sh
sudo apt-get install -y python3-pip python3-dev
```

- create symlink python3 -> python, pip3 -> pip

```sh
cd /usr/local/bin
sudo ls -s /usr/bin/python3 python
sudo ln -s /usr/bin/pip3 pip
pip3 install --upgrade pip
```

- clean

```sh
sudo apt-get clean
sudo rm -rf /var/lib/apt/lists/*
```

- clone git repo

```sh
git clone <this-repo-name>
cd <this-repo-name>
```

- install python packages

```sh
pip install -r requirements.txt

# uvloop, httptools: for uvicorn.workers.UvicornWorker
# gunicorn: process manager
pip install gunicorn uvloop httptools
```

### http proxi: nginx

[reference: (how to install nginx in Ubuntu 20.04)](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04)

- install nginx

```sh
sudo apt-get update
sudo apt-get install nginx
sudo systemctl start nginx
```

- chmod nginx file writable : `sudo chmod 775 /etc/nginx/sites-available`
- add nginx config: `cd /etc/nginx/sites-available && vim tagging`

```
server{
       server_name <your-site-domain>;
       location / {
           include proxy_params;
           proxy_pass http://127.0.0.1:8000;
       }
}
```

- add symlink: `sudo ln -s /etc/nginx/sites-available/tagging /etc/nginx/sites-enabled/`
- restart nginx: `sudo systemctl restart nginx.service`
- move workdirectory: `sudo mv ~/<your-dir-name> /var/www/<your-dir-name>`

### run in background

- `cd /var/www/<your-dir-name>`
- run in background fastapi app

```sh
python3 -m gunicorn -k uvicorn.workers.UvicornWorker main:app --daemon --access-logfile ./gunicorn-access.log
```

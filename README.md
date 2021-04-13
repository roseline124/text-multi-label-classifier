# multi-label-classifier

### vscode lint error

- https://stackoverflow.com/a/51010506
- select 'python interpreter': use linter in virtual env

### manage package

- to freeze packages (l option is 'local': freeze only packages installed in virutal env): `pip freeze -l > requirements.txt`
- to install packages: `pip install -r requirements.txt` (or use pip3)

### run

- run app: `uvicorn main:app --reload`
- run file: `python3 ./classfier/<file_name>.py`

### module import

- https://stackoverflow.com/questions/4383571/importing-files-from-different-folder

### todo

- [x] terminal styling: surpress warnings, colorful logs
- [x] build Dockerfile (for local)
- [x] deploy tagging server
- [ ] use graphql
- [ ] refactor

### docker

[docker with java and python](https://stackoverflow.com/questions/51121875/how-to-run-docker-with-python-and-java)

- docker image build: `docker build -t <your-image-name> .`
- start container: `docker run -d --name <your-container-name> -p 80:80 <your-image-name>`
- docker debug: `docker logs <container-id>`
- docker execute in shell: `docker exec it <container-id> sh`

you can pull `konlpy-fastapi` docker image from docker hub.

- pull docker image: `docker pull roseline124/konlpy-fastapi`
- start container: `docker run -d --name <your-container-name> -p 80:80 roseline124/konlpy-fastapi`

### deploy

- create AWS lightsail instance - ubuntu 20.4(focal)
- install dependencies and set configuration in lightsail

```sh
sudo apt-get update
sudo apt-get install -y --no-install-recommends tzdata g++ git curl

# install java
sudo apt-get install -y openjdk-8-jdk

# set JAVA_HOME path
JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk
source /etc/environment && export JAVA_HOME

# install python
sudo apt-get install -y python3-pip python3-dev

# create symlink python3 -> python, pip3 -> pip
cd /usr/local/bin
sudo ls -s /usr/bin/python3 python
sudo ln -s /usr/bin/pip3 pip
pip3 install --upgrade pip

# clean
sudo apt-get clean
sudo rm -rf /var/lib/apt/lists/*
```

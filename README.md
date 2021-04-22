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
- [x] fetch live target data from db

### docker

[docker with java and python](https://stackoverflow.com/questions/51121875/how-to-run-docker-with-python-and-java)

- docker image build: `docker build -t <your-image-name> .`
- start container: `docker run -d --name <your-container-name> -p 80:80 <your-image-name>`
- docker debug: `docker logs <container-id>`
- docker execute in shell: `docker exec it <container-id> sh`

you can pull `konlpy-fastapi` docker image from docker hub.

- pull docker image: `docker pull roseline124/konlpy-fastapi`
- start container: `docker run -d --name <your-container-name> -p 80:80 roseline124/konlpy-fastapi`

### get live data from db (db engine: postgresql)

- create dataframe after query: `pd.read_sql(<sql_statement>, <connection_address>)`

\*connection_address ex) postgresql://<user>:<password>@<host>/<db-name>

### requirements

- .env
- queries.py

```python
from sqlalchemy import text

get_target_data_doc = text(
  """
  select t.id, t.name from "Table" t
  """
)
```

# supple tagging

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
- [ ] deploy tagging server
- [ ] docker-compose
- [ ] use graphql
- [ ] refactor

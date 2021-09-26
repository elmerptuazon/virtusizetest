# api
- Run cli using linux environment. For windows use **Git Bash**
- Install **virtualenv** package `pip install virtualenv` If ubuntu `sudo apt install python3-venv`.
- Run `python -m venv env`.
- Copy/Paste *requirements.txt* and *secrets.sh* outside root directory project. Make sure to remove *.dist* extension.
- Run `source env/bin/activate`.
- Run `pip install -r requirements.txt`.
- Run `touch secrets.sh`
- Exit from virtualenv by typing `deactivate`
- Go to root directory project `cd virtusizetest`
- Copy `virtusize.config.dist` then paste as `virtusize.config` file
- Inside the file, paste the following and enter your postgres password
- Run `python manage.py makemigrations`
- Run `python manage.py migrate`
- Run `python manage.py runserver`

# run unit test
- Go to root directory project `cd virtusizetest`
- Run `./manage.py test`

**OPTIONAL**
- Create super user run `python manage.py createsuperuser` to login admin site
- Updating *requirements.txt* run `pip freeze > requirements.txt`


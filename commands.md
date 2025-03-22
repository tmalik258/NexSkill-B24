# Git
- git init (for initializing local project into a git repo)
- git add . (to add all files/folders in the current folder for tracking)
- git commit -m "message" (to commit the changes with a meaningful message)
- git remote add origin <repo-url> (to link the local repo with the remote repo)
- git branch -M main
- git push -u origin main (to push the local repo to the remote repo and set the upstream tracking information)


- git pull (to retrieve updated changes on online/remote repo)


<!-- Next time you modify your files and try to commit, use this command -->
- git add . (only to add new files into track)
- git commit -am "message"
<!-- And after commiting, use this command to push -->
- git push


# Django
- pip list (to check which packages are installed)
- pip install virtualenv
- virtualenv venv (venv is your virtual environment name)
- venv/scripts/activate (to activate environment)
- Set-ExecutionPolicy RemoteSigned -Scope CurrentUser (if error occurs while activating venv)
- pip install django
- django-admin startproject base (to create a new project)
- django-admin startproject base .  (to create only main app along with manage.py and not project folder)

- python manage.py runserver (to start the development server)
- ctrl + c (to stop the server)

- python manage.py makemigrations (to create migrations for models)
- python manage.py migrate (to apply migrations to the database)
- python manage.py createsuperuser (to create a superuser)

- python manage.py startapp appname (to create a new app)
- django-admin startapp appname (to create a new app) (both are good)

# To add Model
- create model class in models.py
- run py manage.py makemigrations (to create migration file)
- run py manage.py migrate (to execute migration file and reflect your model in database)
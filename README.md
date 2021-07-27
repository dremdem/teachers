# Teachers Directory

## Description

The detailed description [in the PDF-file](Tech_Test.pdf)

## Installation

### Prerequisites 

- Python >=3.7
- Pipenv 

### Clone the repo

```shell script
git clone git@github.com:dremdem/teachers.git
cd teachers
```

### Install dependencies

```shell script
pipenv install
pipenv shell
```

### Run migrations

```shell script
python manage.py migrate --skip-checks
```

### Create superuser

```shell script
export DJANGO_SUPERUSER_PASSWORD=test
python manage.py createsuperuser --noinput --username admin --skip-checks --email admin@admin.com
```

### Run the server

```shell script
python manage.py runserver 0.0.0.0:8000
```


## Instructions

- open 0.0.0.0:8000

### Bulk upload

- Select CSV and ZIP files (the **data** folder) for uploading and click Submit
    - The system didn't allow to do it if you didn't log in.
    - Login as admin/test and try again
- Enter first letter and/or subject for filter teachers
- Click on the teacher's name for detail information

## Links

https://docs.djangoproject.com/en/3.2/
https://djangobook.com/mdj2-django-structure/
https://stackoverflow.com/questions/64237/when-to-create-a-new-app-with-startapp-in-django
https://softwareengineering.stackexchange.com/questions/160777/django-application-strategy
https://www.toptal.com/django/django-top-10-mistakes
https://stackoverflow.com/questions/18270898/django-best-practice-for-splitting-up-project-into-apps
https://www.stavros.io/posts/how-replace-django-model-field-property/
https://stackoverflow.com/questions/2898711/django-model-fields-getter-setter/11108157
https://docs.djangoproject.com/en/3.2/topics/forms/
https://docs.djangoproject.com/en/3.2/howto/static-files/

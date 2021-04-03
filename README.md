# tas
travel agency system

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/ejaj/tas.git
$ cd tas
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```


Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py migrate
(env)$ python manage.py createsuperuser
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.
To get initial data browse `http://127.0.0.1:8000/initial_news_api`

## Dependencies

```sh
- Database: MySQL
```
# data-loader

The app provides API for handling with users' uploaded images and files.

There are 3 subscription plans for users: Basic, Premium and Enterprise.

Endpoints:

| Endpoint | Method | Description |
|----------|---------|---------|
| /users | GET |  Returns a list of users. |
| /users/sign-up | POST |  Creates a user. |
| /users/token | GET |  Returns a user's token. |
| /users/'<int:pk>' | GET |  Returns a user. |
| /users/'<int:pk>' | PUT |  Updates a user. |
| /users/'<int:pk>' | PATCH |  Partialle updates a user. |
| /users/'<int:pk>' | DELETE |  Deletes a user. |
| /resources/images/image-upload | POST |  User can upload an image if he is authenticated. |
| /resources/images/'<int:pk>'/thumbnail200 | GET | Is available for users with subscription plan. Returns a 200px height thumbnail of the image with given pk. |
| /resources/images/'<int:pk>'/thumbnail400 | GET |  Is available for users with subscription plans Premium or Enterprise. Returns a 400px height thumbnail of the image with given pk. |
| /resources/images/'<int:pk>'/original | GET |  Is available for users with subscription plans Premium or Enterprise. Returns the original image with given pk. |
| /resources/images/'<int:pk>'/'<int:expiring_time>' | GET |  Is available for users with subscription plan Enterprise. Returns the link to the original image with given pk and given expiring time between 300 and 30000 seconds. |
| /resources/images/'<int:pk>'/'<str:url_str>' | GET |  Returns the original image with given pk, if the link was generated for the user with Enterprise plan (see the step before). |
| /resources/files/file-upload | POST |  User can upload a file if he is authenticated. |
| /resources/files/my-files | GET |  Returns the information about files (metadata) for the authenticated user. |
| /resources/docs | GET |  API documentation with Swagger/OpenAPI 2.0 specifications. |
| /resources/admin | GET |  Admin interface. |


The expiring links are cleaned up with the Celery scheduled tasks.

<a href="https://codeclimate.com/github/Dddarknight/data-loader/test_coverage"><img src="https://api.codeclimate.com/v1/badges/9faa086cfca0e7cb50d9/test_coverage" /></a>


## Links
This project was built using these tools:
| Tool | Description |
|----------|---------|
| [Django ](https://www.djangoproject.com/) |  "A high-level Python web framework" |
| [Django REST framework](https://www.django-rest-framework.org/) |  "A powerful and flexible toolkit for building Web APIs" |
| [Celery](https://docs.celeryq.dev/en/stable/index.html) | "A task queue with focus on real-time processing, while also supporting task scheduling" |
| [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/readme.html) |  "Generate real Swagger/OpenAPI 2.0 specifications from a Django Rest Framework API." |
| [poetry](https://python-poetry.org/) |  "Python dependency management and packaging made easy" |


## Installation

**Copy a project**
```
$ git clone git@github.com:Dddarknight/data-loader.git
$ cd data-loader
```

**Set up environment variables**
``` 
$ touch .env

# You have to fill .env file. See .env.example.
# You will have to:
# 1) You have to write into .env file SECRET_KEY for Django app.
# To get SECRET_KEY for Django app:
$ python manage.py shell
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
# 2) fill username and password fields for RabbitMQ. If you don't have these credentials, please follow the instructions in the official documentation.
```

**Set up the environment**
```
$ pip install poetry
$ make install
```

**Launch API server**
```
$ make run
```

**Launch Celery**
```

# Launch Celery scheduled tasks
$ celery -A data_loader.celery_tasks beat --loglevel=info

# Launch the Celery worker
$ celery -A data_loader.celery_tasks worker --loglevel=info --pool solo
```

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
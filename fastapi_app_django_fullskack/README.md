# 

## install python packages

Install some python packages.

```shell
# django
pip django
pip install django-allauth

# FastAPI https://fastapi.tiangolo.com/
pip install fastapi
pip install "uvicorn[standard]"
pip install jinja2

# FastAPI OAuth2 with Password (and hashing), Bearer with JWT tokens 
# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
pip install "python-jose[cryptography]"
pip install "passlib[bcrypt]"

# FastAPI database case MySQL
sudo apt-get install -y libmysqlclient-dev
pip install mysqlclient

# FastAPI database case PostgreSQL
sudo apt-get install python-dev libpq-dev
pip install psycopg2

# FastAPI asynchronous database for MySQL Databases
# https://www.encode.io/databases/
pip install databases[mysql]

# FastAPI asynchronous database for PostgreSQL asyncpg
# https://magicstack.github.io/asyncpg
pip install asyncpg

# sqlalchemy
pip install sqlalchemy
```

## setup django-allauth

### settings.py

```python: mysite/settings.py
INSTALLED_APPS = [
    # ・・・・
    'django.contrib.staticfiles',
    'accounts',                #追加
    'django.contrib.sites',    #追加
    'allauth',                 #追加
    'allauth.account',         #追加
    'allauth.socialaccount',   #追加    
]
```

### urls.py

```python: mysite/urls.py
from django.contrib import admin
from django.urls import include, path                   
#includeを追加
from django.views.generic import TemplateView as tv     #追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tv.as_view(template_name='home.html'), name='home'),          #追加
    path('index/', tv.as_view(template_name='index.html'), name='index'),  #追加
    path('accounts/', include('allauth.urls')),                            #追加
]
```

## setup FastAPI


```python: main.py
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi_app_django_fullskack.wsgi import application as django_app
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/v2")
def read_main():
    return {"message": "Hello World"}

app.mount("", WSGIMiddleware(django_app))
```

## migrate

```shell
python manage.py migrate
python manage.py createsuperuser
# ユーザー名 (leave blank to use 'user'): 
# メールアドレス: user@example.com
# Password: 
# Password (again): 
# Superuser created successfully.
```

## migrate

```
python manage.py collectstatic
```


```sql
create table public.department (
  id serial not null
  , name character varying(64) not null
  , created_at timestamp(6) without time zone default CURRENT_TIMESTAMP not null
  , updated_at timestamp(6) without time zone default CURRENT_TIMESTAMP not null
  , primary key (id)
);

insert into department (name) values 
('人事部'),
('経理部'),
('総務部'),
('法務部'),
('情報システム部'),
('技術部'),
('営業部')

create table public.employee (
  id serial not null
  , name character varying(64)
  , birthday date
  , department_id integer not null
  , foreign key (department_id) references department(id)
  , created_at timestamp(6) without time zone default CURRENT_TIMESTAMP not null
  , updated_at timestamp(6) without time zone default CURRENT_TIMESTAMP not null
  , primary key (id)
);
```

## setup javascript framework files

This sample makes use of some javascriprt frameworks.Download [UIKIT](https://getuikit.com/docs/introduction), [AGGrid](https://www.ag-grid.com/javascript-data-grid/download/) and [JSpreadsheet-ce](https://bossanova.uk/jspreadsheet) and setup files like this:

├── fastapi_app_django_fullskack
│   ├── static
│   │   ├── aggrid
│   │   │   ├── ag-grid-community.min.noStyle.js
│   │   │   └── styles
│   │   │       ├── ag-grid.min.css
│   │   │       ├── ag-theme-alpine-dark.min.css
│   │   │       ├── ag-theme-alpine.min.css
│   │   │       ├── ag-theme-balham-dark.min.css
│   │   │       ├── ag-theme-balham.min.css
│   │   │       ├── ag-theme-blue.min.css
│   │   │       ├── ag-theme-bootstrap.min.css
│   │   │       ├── ag-theme-dark.min.css
│   │   │       ├── ag-theme-fresh.min.css
│   │   │       ├── ag-theme-material.min.css
│   │   │       ├── generate-web-fonts.js
│   │   │       ├── package.json
│   │   │       └── scss-template.hbs
│   │   ├── jspreadsheet-ce
│   │   │   ├── jexcel.css
│   │   │   ├── jexcel.js
│   │   │   ├── jsuites.css
│   │   │   └── jsuites.js
│   │   └── uikit
│   │       ├── css
│   │       │   ├── uikit-rtl.css
│   │       │   ├── uikit-rtl.min.css
│   │       │   ├── uikit.css
│   │       │   └── uikit.min.css
│   │       └── js
│   │           ├── uikit-icons.min.js
│   │           └── uikit.min.js

# This application is one of the samples to mount Django with FastAPI.

## install

```shell
# django
pip install -r requirements.txt
cd fastapi_app_django_fullskack
```

## Edit the configuration file

### database settings

#### using postgreSQL

```python: fastapi_app_django_fullskack/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangodb',
        'USER': 'testuser',
        'PASSWORD': 'testuser', 
        'HOST': '127.0.0.1',
        'PORT': '5432',        
    }
}
```

#### using MySQL

```python: fastapi_app_django_fullskack/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangodb',
        'USER': 'testuser',
        'PASSWORD': '*****************',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

### logging settings

```python: apis/logging_settings.py
_LOGURU_CONFIG = {
    'handlers': [
        {
            'sink': sys.stdout, 
        },
        {
            'sink': 
            'logs/application.log' , 
            'rotation': '1 days', 
            'retention': 5
        }
    ]
}
```

## migrate

```bash
python manage.py makemigration
python manage.py migrate

```

## create superuser

```bash
python manage.py createsuperuser
```

## start application

```bash
./test.sh
```

```sql
create table public.department (
  id serial not null
  , name character varying(64) not null
  , created_at timestamp(6) without time zone default CURRENT_TIMESTAMP not null
  , updated_at timestamp(6) without time zone default CURRENT_TIMESTAMP not null
  , primary key (id)
);

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

insert into department (name) values 
('人事部'),
('経理部'),
('総務部'),
('法務部'),
('情報システム部'),
('技術部'),
('営業部')

```

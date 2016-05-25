import os

SECRET_KEY = '+2dto*1_pr&vq2w3)jr2&9e-lt#idvyfcmtaq1ob0uidgz%w9c'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True

import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'something-secretive-^^'
    ADMINS = ["inotives@gmail.com"]

class ProdConfig(object):
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'something-secretive-^^'
    ADMINS = ["inotives@gmail.com"]
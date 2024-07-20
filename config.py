import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:adminroot@123@localhost/dashboard_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

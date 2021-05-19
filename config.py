import os

base_dir = os.path.dirname(os.path.abspath(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'notes.db')
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1@127.0.0.1:5432/flask_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SALT = 'my_sJHLHLHKLаваыпuper_s!alt_#4$4344'

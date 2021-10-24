class DebugConfig:
    SECRET_KEY = '123456' # Secret key - replace with your own
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db?charset=utf8mb4'  # "///" -> relative path from this file
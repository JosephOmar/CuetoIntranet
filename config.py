class Config:
    SECRET_KEY = 'Kvothe1Denna'


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig
}

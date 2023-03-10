import configparser


config = configparser.ConfigParser()
config.read('config.ini')


def get_configuration():
    return {'email': config['APP']['email'], 'password': config['APP']['password']}

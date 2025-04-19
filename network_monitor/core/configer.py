import configparser

class ConfManager:
    
    def read_config():
        config = configparser.ConfigParser()

        config.read('config/config.ini')

        subnet = config.get('Network', 'subnet')
        port_range = config.get('Network', 'port_range')
        db_name = config.get('Database', 'db_name')

        config_values = {
            'subnet': subnet,
            'port_range': port_range,
            'db_name': db_name
        }
        return config_values

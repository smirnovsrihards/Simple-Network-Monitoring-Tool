import configparser

class ConfManager:
    
    def read_config():
        config = configparser.ConfigParser()

        config.read('config/config.ini')

        subnet = config.get('Network', 'subnet')
        port_range = config.get('Network', 'port_range')
        db_name = config.get('Database', 'db_name')
        port = config.get('SMTP', 'port')
        smtp_server = config.get('SMTP', 'smtp_server')
        sender_email = config.get('SMTP', 'sender_email')
        receiver_email = config.get('SMTP', 'receiver_email')
        app_password = config.get('SMTP', 'app_password')
        
        config_values = {
            'subnet': subnet,
            'port_range': port_range,
            'db_name': db_name
            'port': port,
            'smtp_server': smtp_server,
            'sender_email': sender_email,
            'receiver_email': receiver_email,
            'app_password': app_password
        }
        return config_values

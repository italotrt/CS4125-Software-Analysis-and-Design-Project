# todo: we should be using our singleton

from utilities.configuration.config import Config

# Singleton instance
class ConfigurationManager:
    instance = None

    def __new__(cls):
        if cls.instance is None: # If instance is not created, create it
            cls.instance = super(ConfigurationManager, cls).__new__(cls)
            cls.instance.config = Config()
            return cls.instance
        return cls.instance

    def get_config(self):
        return self.config


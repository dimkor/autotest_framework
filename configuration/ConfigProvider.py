import configparser

global_config = configparser.ConfigParser()
global_config.read('test_config.ini')

class ConfigProvider:
    
    def __init__(self) -> None:
        self.config = global_config
    
    def get(self, section:str, prop: str) -> str:
        return self.config[section].get(prop)
  
    def getint(self, section:str, prop: str) -> int:
        return self.config[section].getint(prop)
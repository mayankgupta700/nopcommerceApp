import configparser                             # this code from lie 1 to 3 is used to read the data from config file
config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")
class ReadConfig():
    @staticmethod       # we can access static methods w/o creating any object, only with class name
    def getApplicationURL():
        url = config.get("common info", "base_url")
        return url

    @staticmethod  # we can access static methods w/o creating any object, only with class name
    def getusername():
        username = config.get("common info", "username")
        return username

    @staticmethod  # we can access static methods w/o creating any object, only with class name
    def getpassword():
        password = config.get("common info", "password")
        return password
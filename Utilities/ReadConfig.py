import configparser

config = configparser.RawConfigParser()
filepath = "D:\\Python\\Revision 1\\Amazon\\configuraton\\config.ini"
config.read(filepath)


class ReadConfig:
    @staticmethod
    def GetUserName():
        username = config.get('common data', 'email_id')
        return username

    @staticmethod
    def GetPassword():
        password = config.get('common data', 'password')
        return password

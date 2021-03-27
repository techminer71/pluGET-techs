import os
import sys
import configparser
from pathlib import Path

from utils.consoleoutput import oColors


class configurationValues:
    def __init__(self):
        config = configparser.ConfigParser()
        config.sections()
        config.read("config.ini")
        localPluginFolder = config['General']['LocalPluginFolder']
        self.pathToPluginFolder = Path(config['General']['PathToPluginFolder'])
        seperateDownloadPath = config['General']['SeperateDownloadPath']
        self.pathToSeperateDownloadPath = Path(config['General']['PathToSeperateDownloadPath'])

        self.sftp_server = config['SFTP - Remote Server']['Server']
        self.sftp_user = config['SFTP - Remote Server']['Username']
        self.sftp_password = config['SFTP - Remote Server']['Password']
        sftp_port = config['SFTP - Remote Server']['Port']
        self.sftp_folderPath = config['SFTP - Remote Server']['PluginFolderOnServer']
        sftp_seperateDownloadPath = config['SFTP - Remote Server']['SeperateDownloadPath']
        self.sftp_pathToSeperateDownloadPath = config['SFTP - Remote Server']['PathToSeperateDownloadPath']

        self.sftp_port = int(sftp_port)
        if localPluginFolder == 'True':
            self.localPluginFolder = True
        else:
            self.localPluginFolder = False

        if seperateDownloadPath == 'True':
            self.seperateDownloadPath = True
        else:
            self.seperateDownloadPath = False

        if sftp_seperateDownloadPath == 'True':
            self.sftp_seperateDownloadPath = True
        else:
            self.sftp_seperateDownloadPath = False


def checkConfig():
    configAvailable = os.path.isfile("config.ini")
    if not configAvailable:
        createConfig()
        print(oColors.brightRed + "Config created. Edit config before executing again!" + oColors.standardWhite)
        input("Press any key + enter to exit...")
        sys.exit()


def createConfig():
    config = configparser.ConfigParser(allow_no_value=True)
    config['General'] = {}
    config['General'][';'] = 'If a local plugin folder exists (True/False): (If False SFTP will be used)'
    config['General']['LocalPluginFolder'] = 'True'
    config['General']['PathToPluginFolder'] = 'C:/Users/USER/Desktop/plugins'
    config['General'][';_'] = 'If you want a different folder to store the updated plugins change to (True/False) and the path below'
    config['General']['SeperateDownloadPath'] = 'False'
    config['General']['PathToSeperateDownloadPath'] = 'C:/Users/USER/Desktop/plugins'

    config['SFTP - Remote Server'] = {}
    config['SFTP - Remote Server']['Server'] = '0.0.0.0'
    config['SFTP - Remote Server']['Username'] = 'user'
    config['SFTP - Remote Server']['Password'] = 'password'
    config['SFTP - Remote Server'][';'] = 'Normally you won*t need to change anything below this line'
    config['SFTP - Remote Server']['Port'] = '22'
    config['SFTP - Remote Server']['PluginFolderOnServer'] = '.\\plugins'
    config['SFTP - Remote Server'][';_'] = 'If you want a different folder to store the updated plugins change to (True/False) and the path below'
    config['SFTP - Remote Server']['SeperateDownloadPath'] = 'False'
    config['SFTP - Remote Server']['PathToSeperateDownloadPath'] = '.\\plugins'


    with open('config.ini', 'w') as configfile:
        config.write(configfile)

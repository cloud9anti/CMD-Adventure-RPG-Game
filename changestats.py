from configparser import ConfigParser

import configparser
import os, sys


#path = 'c:/users/antic/rpg/'
path = os.path.dirname(os.path.abspath(__file__)) + '\\'
os.chdir(path)

def modify(stat, modification):

    #Read config.ini file
    config_object = ConfigParser()
    config_object.read("config.ini")
    
    #Get the Character section
    character = config_object["CHARACTER"]
    
    #Update the stat
    character[stat] = modification
    
    #Write changes back to file
    with open('config.ini', 'w') as conf:
        config_object.write(conf)
    return modification
        
def read(stat):

    #Read config.ini file
    config_object = ConfigParser()
    config_object.read("config.ini")
    
    #Read the stat
    character = config_object["CHARACTER"]
    print("Your",stat,"is {}".format(character[stat]))

def get(stat):

    #Read config.ini file
    config_object = ConfigParser()
    config_object.read("config.ini")
    
    #Get the stat
    character = config_object["CHARACTER"]
    return(character[stat])
temp1=''

def save(temp, varName):
    temp1 = str(temp)
    temp1 = temp1.replace("'", "").replace("[", "").replace("]", "")
    modify(varName,temp1)
import configparser
import sys

config = ConfigParser.ConfigParser()
section = input("Please input which section to edit. 0 for development, 1 for releace: ")
if section is None:
	section == "0"
confname = input("Please input the name of config to change: ")
if confname is None:
	sys.exit()
confsetting = input("Please input what to set for " + confname + ": ")
if confsetting is None:
	sys.exit()
if section == "0":
	section0 = 'development'
	config.add_section(section1)
	config.set(section0, confname, confsetting)
if section == "1":
	section1 = 'production'
	config.add_section(section2)
	config.set(section1, confname, confsetting)

with open('/root/dismona-setting.conf', 'w') as file:
	config.write(file)

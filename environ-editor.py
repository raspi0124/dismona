import os
import sys
#TESTACTION
os.environ["TEST"] = "test2"

action = input("Enter action [0 for adding, 1 for deleting, 2 for checking and 3 for debuging]: ")
if action == "0":
	keyname = input("Please first enter keyname for enviroment: ")
	keycontent = input("Now, Please enter key content for keyname above: ")
	os.environ["keyname"] = "keycontent"
if action == "1":
	keyname = input("Please enter keyname you want to delete: ")
	sure = input("Are you sure you want to remove keyname " + keyname + "? If so, Please enter y or else, please enter n: ")
	if sure == "y":
		print("Now, removing " + keyname + " from os environ..")
		del os.environ[keyname]
		print("Succeeded!")
	else:
		print("ok, now exiting process..")
		sys.exit()
if action == "2":
	keyname = input("Please enter keyname you want to check: ")
	if keyname != "":
		print("ok, now printing..")
		print(os.getenv(keyname))
	else:
		print("Please specify keyname.")
if action == "3":
	print("Debuging info will be shown below.")
	print("os.environ")
	print(os.environ)
	print("os.environ[LANG]")
	print(os.environ['LANG'])
	print("os.environ.get[LANG]")
	print(os.environ.get('LANG'))

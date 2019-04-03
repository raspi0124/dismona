import subprocess
import time
import schedule

timestamp = str(time.time())
cmd = "pgrep -a python | grep '/root/dismona/faucet.py'"
process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
stderr=subprocess.PIPE)
my_pid, err = process.communicate()

path_w = '/var/log/dismona.log'
if len(my_pid.splitlines()) >0:
	print("Running")
	s = '' + timestamp + ' Faucet module is running.\n'
	with open(path_w, mode='w') as f:
		f.write(s)
	exit()
else:
	print("Not Running!")
	print("Restarting faucet process..")
	s = '' + timestamp + ' ERROR: Faucet module not running! Restarting..\n'
	with open(path_w, mode='w') as f:
		f.write(s)
	cmd = "startfaucet"
	subprocess.Popen(cmd)


timestamp = str(time.time())
cmd = "pgrep -a python | grep '/root/dismona/main.py'"
process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
stderr=subprocess.PIPE)
my_pid, err = process.communicate()

path_w = '/var/log/dismona.log'
if len(my_pid.splitlines()) >0:
	print("Main module:Running")
	s = '' + timestamp + ' Main module is running.\n'
	with open(path_w, mode='w') as f:
		f.write(s)
	exit()
else:
	print("Main Module Not Running!")
	print("Restarting main module process..")
	s = '' + timestamp + ' ERROR: Main module not running! Restarting..\n'
	with open(path_w, mode='w') as f:
		f.write(s)
	cmd = "refresh"
	subprocess.Popen(cmd)

import subprocess

cmd = "pgrep -a python | grep '/root/dismona/faucet.py'"
process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
stderr=subprocess.PIPE)
my_pid, err = process.communicate()

if len(my_pid.splitlines()) >0:
   print("Running")
   exit()
else:
  print("Not Running!")
  print("Restarting faucet process..")
  cmd = "startfaucet"
  rut = subprocess.check_output( cmdlib.split(" ") )

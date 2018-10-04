import json
import falcon


class isrunning(object):

	def on_get(self, req, resp):
		cmd = "pgrep -a python | grep '/root/dismona/main.py'"
		process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
		stderr=subprocess.PIPE)
		my_pid, err = process.communicate()
		if len(my_pid.splitlines()) >0:
			sm = "1"
		else:
			sm = "0"
		cmd = "pgrep -a python | grep '/root/dismona/faucet.py'"
		process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
		stderr=subprocess.PIPE)
		my_pid, err = process.communicate()
		if len(my_pid.splitlines()) >0:
			sf = "1"
		else:
			sf = "0"
		msg = {
			"Main": "{0}"
			"Faucet": "{1}"
		}.format(sm, sf)
		resp.body = json.dumps(msg)

app = falcon.API()
app.add_route("/", isrunning())


if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("127.0.0.1", 8124, app)
    httpd.serve_forever()

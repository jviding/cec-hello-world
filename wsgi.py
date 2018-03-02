import socket, datetime
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
	try:
		f = open("/mnt/access.log", "a+")
		f.write("<p>Hello World! Greetings from "+socket.gethostname()+" @ "+str(datetime.datetime.now())+"\n</p>")
		f.close()
	except Exception as e:
		return str(e)

	try:
		with open("/mnt/access.log", "r") as myfile:
			data = myfile.read()
	except Exception as e:
		return str(e)

	return "<html><head></head><body>"+data+"</body></html>"


if __name__ == "__main__":
	application.run()

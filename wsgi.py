import socket, datetime
from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
    try:
		f = open("/mnt/access.log", "a+")
		f.write("Hello World! Greetings from "+socket.gethostname()+" @ "+datetime.datetime.now()+"\n")
		f.close()
    except:
    	return "Write failed"

    try:
		with open("/mnt/access.log", "r") as myfile:
			data = myfile.read()
    except:
    	return "Read failed"

	return data


if __name__ == "__main__":
    application.run()

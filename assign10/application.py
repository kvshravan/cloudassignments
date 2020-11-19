from flask_oauth import OAuth
from flask import *
application = Flask(__name__)
@application.route('/', methods=['GET', 'POST'])

def basic():
	return render_template('https://localhost:9443/oauth2/authorize?response_type=code&redirect_uri=http://localhost:5000/oauth&client_id=kzU7WQrN5YcBr0iWC2nySEr1KoEa')


if __name__ == '__main__':
	application.debug = True
	application.run()

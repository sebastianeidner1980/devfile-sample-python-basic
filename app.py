from flask import Flask
from flask import request
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == "POST":
       data = request.get_json()
       print(data)
       return "Post"
    else:
      return request.method

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')

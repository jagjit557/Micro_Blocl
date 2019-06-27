from app import app
@app.route('/')
@app.route('/index')
def index():
      return '<html> <head><tital>Hello World,<tital> </head> <body>This is Jagjit Singh.</body> </htmal>'

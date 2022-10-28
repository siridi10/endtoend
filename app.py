from distutils.log import debug
from flask import Flask

app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    return "Starting a new Project"

if __name__=='__main__':
    app.run(port=5300,debug=True)
import json
from flask import Flask, render_template, request, jsonify   
from math import lcm

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")        

@app.route("/add", methods=["POST"])
def ADD(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    sum=a+b
    response = "sum of 2 numbers = " + str(sum)
    return response
    

@app.route("/bitwiseXor", methods=["POST"])
def bitwiseXor(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    
    # Logic for function assigned to you as in pdf
    xor=a^b
    response = "Bitwise Xor of 2 numbers = " + str(xor)
    return response

@app.route("/subtract", methods=["POST"])
def subtract(a,b):
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    return a-b
    
@app.route("/lcm", methods=["POST"])
def subtract(a,b):
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr)
    a=int(jsonObj['N1'])
    b=int(jsonObj['N2'])
    return lcm(a,b)
    

if __name__== "__main__":
    app.run()

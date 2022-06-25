from re import L
import schedule
import random
from flask import Flask, jsonify, request
import linecache

todaysIntegral = ""

def generateIntegral():
    with open(r"ActiveIntegrals.txt", "r") as fp:
        for count, line in enumerate (fp): #  count how many integrals are left
            pass
        print("Integrals left: " + count)
        if count <= 50: print("RUNNING OUT OF INTEGRALS!")
        todaysLine = random.randint(1, count)
        todaysIntegral = linecache.getline(r"ActiveIntegrals.txt", todaysLine)
        lines = []
        lines = fp.readlines()

    with open(r"ActiveIntegrals.txt", 'w') as fp:
        for number, line in enumerate(lines):
            if number not in [todaysLine]:
                fp.write(line)
    
 
app = Flask(__name__)

@app.route("/integral", methods=['GET'])   

def integral():
    data = request.get_json()
    schedule.every().day.at("00:00").do(generateIntegral)
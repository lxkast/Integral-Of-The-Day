from re import L
from apscheduler.schedulers.background import BackgroundScheduler
import random
from flask import Flask, jsonify, request
import linecache

todaysIntegral = "http://i.ytimg.com/vi/YI1x2bgAwAA/maxresdefault.jpg"
usedIntegrals = [137]

def schedulerTest():
    print("scheduler works !!")

def generateIntegral():
    with open(r"ActiveIntegrals.txt", "r") as fp:
        total = 579
        
        repeat = False
        freshIntegral = False
        while freshIntegral == False:
            todaysLine = random.randint(1, total)
        
            for i in range(0,len(usedIntegrals)):
                if usedIntegrals[i] == todaysLine:
                    repeat = True
                    break
            if repeat == False: freshIntegral = True


        todaysIntegral = linecache.getline(r"ActiveIntegrals.txt", todaysLine)
        lines = []
        lines = fp.readlines()
        print(usedIntegrals)
        

    #with open("ActiveIntegrals.txt", "w") as f:
    #    for line in lines:
    #        if line.strip("\n") != todaysIntegral:
    #            f.write(line)
    #
    #
    # WHY CANT I DELETE A SPECIFIC LINE FROM A TEXT FILE IT JUST DELETES EVERYTHING
    #
    # NOW IM GOING TO MAKE IT SUPER INEFFICIENT
    #
    # I AM GOIN G INSANE
    #
    
    usedIntegrals.append(todaysLine)
    

sched = BackgroundScheduler(daemon=True)
sched.add_job(generateIntegral,'interval',seconds=2)
sched.start()

app = Flask(__name__)

@app.route("/integral", methods=['GET'])   

def integral():
    data = request.get_json()
    return jsonify({"integral": todaysIntegral})

if __name__ == "__main__":
    app.run()
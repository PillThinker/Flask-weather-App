from flask import Flask,render_template,request,redirect
import requests
import os
import math
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/search",methods=['GET','POST'])
def hello_world():
    getname=request.form.get('searchs')
    # getname.upper()
    print(getname)
    city=getname
    url=f'https://www.metaweather.com/api/location/search/?query={city}'
    data=requests.get(url).json()
    if len(data)==0:
        print("not working")
        return redirect("/")
    getDict=data[0]
    getwWoeid=getDict["woeid"]
    name=getDict["title"]
    # print(getwWoeid)

    Mainurl=f'https://www.metaweather.com/api/location/{getwWoeid}'
    weather=requests.get(Mainurl).json()
    # print()
    currweather=list(weather.values())[0]
    currweather=currweather[0]
    temperature=math.trunc(currweather["the_temp"])
    speed=math.trunc(currweather["wind_speed"])
    temp={'name':name,'state':currweather["weather_state_name"],'temper':temperature,
    'windSpeed':speed,'hum':currweather["humidity"]}

    # print(temp)
    return render_template('index.html',currw=temp)


@app.route("/")
def app():
    # getname=request.form.get('search')
    # print(getname)
    city="india"
    url=f'https://www.metaweather.com/api/location/search/?query={city}'
    data=requests.get(url).json()
    getDict=data[0]
    getwWoeid=getDict["woeid"]
    print(getwWoeid)

    Mainurl=f'https://www.metaweather.com/api/location/{getwWoeid}'
    weather=requests.get(Mainurl).json()
    # print()
    currweather=list(weather.values())[0]
    currweather=currweather[0]
    temperature=math.trunc(currweather["the_temp"])
    speed=math.trunc(currweather["wind_speed"])
    temp={'name':'INDIA','state':currweather["weather_state_name"],'temper':temperature,
    'windSpeed':speed,'hum':currweather["humidity"]}

    # print(temp)
    return render_template('index.html',currw=temp)


if __name__ =="__main __":
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 4444)))
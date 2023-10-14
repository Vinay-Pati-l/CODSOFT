import requests
from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.route('/home', methods = ['post','get'])
def home():
    if request.method == 'GET':
        return render_template("home.html")
    else:
        location = request.form['location']
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": location,
            "appid": "3729289753d894a59e63776499262902",
            "units": "metric"  
        }

        response = requests.get(base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            error = None
        else:
            data = None
            error = "Error fetching data"

        if data is not None:
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            description = data['weather'][0]['description']

            return render_template('home.html',error=error,temperature=temperature, humidity=humidity, wind_speed=wind_speed, description=description, Location=location)

        else:
            return render_template('home.html',error=error)


if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, request, jsonify
import util1

app = Flask(__name__)


@app.route('/get_column_names')
def get_column_names():
    response = {'Columns': util1.column_names()}
    return response


@app.route('/get_predict_result', methods=['POST'])
def get_predict_result():
    location = float(request.form['LOCATION'])
    mintemp = float(request.form['MINTEMP'])
    maxtemp = float(request.form['MAXTEMP'])
    rainfall = float(request.form['RAINFALL'])
    evaporation = float(request.form['EVAPORATION'])
    sunshine = float(request.form['SUNSHINE'])
    windgustdir = float(request.form['WINDGUSTDIR'])
    windgustspeed = float(request.form['WINDGUSTSPEED'])
    winddir9am = float(request.form['WINDDIR9AM'])
    winddir3pm = float(request.form['WINDDIR3PM'])
    windspeed9am = float(request.form['WINDSPEED9AM'])
    windspeed3pm = float(request.form['WINDSPEED3PM'])
    humidity9am = float(request.form['HUMIDITY9AM'])
    humidity3pm = float(request.form['HUMIDITY3PM'])
    pressure9am = float(request.form['PRESSURE9AM'])
    pressure3pm = float(request.form['PRESSURE3PM'])
    cloud9am = float(request.form['CLOUD9AM'])
    cloud3pm = float(request.form['CLOUD3PM'])
    temp9am = float(request.form['TEMP9AM'])
    temp3pm = float(request.form['TEMP3PM'])
    raintoday = request.form['RAINTODAY']
    month = float(request.form['MONTH'])
    day = float(request.form['DAY'])
    year = float(request.form['YEAR'])
    predicted=int(util1.get_predicted_result(location, mintemp, maxtemp, rainfall, evaporation, sunshine, windgustdir, windgustspeed, winddir9am,
                       winddir3pm, windspeed9am, windspeed3pm, humidity9am, humidity3pm, pressure9am, pressure3pm, cloud9am, cloud3pm, temp9am, temp3pm, raintoday, month, day, year))
    if predicted==1:
        response=jsonify({'prediction':'It will rain tomorrow.'})
    else:
        response=jsonify({'prediction':'It will not rain tomorrow.'})
    #response = jsonify({'prediction': util1.get_predicted_result(location, mintemp, maxtemp, rainfall, evaporation, sunshine, windgustdir, windgustspeed, winddir9am,
                       #winddir3pm, windspeed9am, windspeed3pm, humidity9am, humidity3pm, pressure9am, pressure3pm, cloud9am, cloud3pm, temp9am, temp3pm, raintoday, month, day, year)})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


app.run(host='0.0.0.0', port='5000')

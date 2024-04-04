from flask import Flask, render_template, redirect, url_for, request
import weather


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/answer/<weatherData>")
def answer(weatherData):
    weatherData = weatherData.replace('\n', '<br>')
    return render_template("result.html",value=weatherData)

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['loc']
    weatherResult = weather.getResult(text)
    return redirect(url_for("answer", weatherData=weatherResult))



if __name__== '__main__':
    app.run(port=3000,debug=True)
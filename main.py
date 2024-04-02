
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/weather')
def weather():
  return render_template('weather_display.html')

if __name__ == '__main__':
  app.run(debug=True)

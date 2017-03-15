from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        lat = request.form['lat']
        lng = request.form['long']
        conn = requests.get("https://api.what3words.com/v2/reverse?coords=" + \
                        lat + "%2C" + lng  +"&key=WVZ71D9D&lang=en& \
                        format=json&display=full")
        what3words = conn.json()
        word = what3words['words']
        w3w_map = what3words['map']
        search_loc = lat + "," + lng
        return render_template('index.html', word=word, w3w_map=w3w_map, \
                               search_loc=search_loc, lat=lat, lng=lng)
    return render_template('index.html')


@app.route('/import_url')
def import_url():
    return render_template('import.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)

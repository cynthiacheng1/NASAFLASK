from flask import Flask, render_template
import urllib2
import json

app = Flask(__name__)

@app.route('/')
def root():
    u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=JVYm9dNCMIhiBHPQasTxNNgtIpNmvyY4v4TwwX1r")
    data = json.loads(u.read())
    pic = data['url']
    caption = data['explanation']
    return render_template('index.html', img=pic, content=caption)

if __name__ == '__main__':
    app.debug = True
    app.run()

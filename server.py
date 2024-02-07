
import os
import flask


# Create a simple Flask app to allow the HTML content to be loaded
app = flask.Flask(__name__)

@app.route('/<path:path>')
def send_html(path):
    return flask.send_from_directory(os.getcwd(), path)


app.run(port=5000,debug=True)





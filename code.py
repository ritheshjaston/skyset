from flask import*
from flask import send_from_directory

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("code.html")

@app.route('/images/<filename>')
def images(filename):
    return send_from_directory('images/', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
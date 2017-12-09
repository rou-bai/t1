from flask import *
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap=Bootstrap(app)

@app.route("/")
def oneindex():
    return 'success'

@app.route("/ex1", methods=['POST', 'GET'])
def login():
    error = None
    if request.method=='GET':
        return send_file('templates/ex1.html')

    elif request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin123':
            error = "sorry"
        else:
            return redirect(url_for('index'))
    return render_template('ex1.html', error=error)


@app.route("/index")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(
        host="192.168.1.157",
        port=3306,
        debug=True)




















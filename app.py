from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/sample')
def speech():
    return render_template('sample.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

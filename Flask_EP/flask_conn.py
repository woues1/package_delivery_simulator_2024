from flask import Flask, render_template, request


app = Flask(__name__)
@app.route('/')
def index():
    


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='3000')

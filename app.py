from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("home.html")


if __name__ == '__main__':
    print('sfdsffdf')
    app.run(host='0.0.0.0', port=80, debug=True)

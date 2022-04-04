from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def LoginPage():
    return render_template("loginpage.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == "__main__":
    app.run()
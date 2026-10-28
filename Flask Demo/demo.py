from flask import Flask, render_template

app=Flask(__name__)
@app.route("/signin")
def login():
    return render_template("login.html")
    # return "I am login method"

@app.route("/verify")
def verify():
    return "I am verify method, I will verify login credentials"

@app.route("/signup")
def register():
    return "I am register method"

if __name__=="__main__":
    app.run()     #Start the server



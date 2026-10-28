from flask import Flask, render_template, request

app=Flask(__name__)
@app.route("/signin")
def login():
    return render_template("login1get.html")
    # return "I am login method"

@app.route("/verify")
def verify():
    uname=request.args["uname"]
    pwd=request.args["pwd"]
    if uname == "vedika" and pwd=="123":
        return "Login Successful"
    else:
        return "Login Failed"


    # return "I am verify method, I will verify login credentials"

@app.route("/signup")
def register():
    return "I am register method"

if __name__=="__main__":
    app.run(debug=True)     #Start the server



from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/login" , methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login2get&post.html")
    else:
        uname=request.form["uname"]
        pwd=request.form["pwd"]
        if uname == "vedika" and pwd=="123":
            return "Login Successful"
        else:
            return "Login Failed"

if __name__=="__main__":
    app.run(debug=True)     #Start the server



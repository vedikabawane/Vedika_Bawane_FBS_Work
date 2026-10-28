from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/login3")
def displayName():
   name="Vedika Bawane"
   return render_template("login3.html", uname=name)

if __name__=="__main__":
    app.run(debug=True)     #Start the server



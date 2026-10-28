from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/login3_name")
def displayName():
   firstname="Vedika"
   secondname="Bawane"
   return render_template("login3_name.html",firstname=firstname,secondname=secondname)

if __name__=="__main__":
    app.run(debug=True)     #Start the server



from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/login4_addNumbers.html",methods=["GET","POST"])
def getSum():
    if request.method=="GET":
        return render_template("login4_addNumbers.html")
    else:
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        result=num1+num2
        return render_template()


if __name__=="__main__":
    app.run(debug=True)     #Start the server



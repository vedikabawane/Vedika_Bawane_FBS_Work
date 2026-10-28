from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/login3_nested_list")
def displayList():
    data=[[101,'om',78],[103,'ved',79],[104,'vedika',90],[105,'amisha',88]]
    return render_template("login3_nested_list.html",data=data)

if __name__=="__main__":
    app.run(debug=True)     #Start the server



from flask import Flask

app=Flask(__name__)
@app.route("/signin")
def login():
    return "I am login method"

@app.route("/signup")
def register():
    return "I am register method"

if __name__=="__main__":
    app.run()     #Start the server




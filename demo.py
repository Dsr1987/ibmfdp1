from flask import Flask, url_for, redirect

app = Flask (__name__)
@app.route("/home")
def home():
    return "Welcome!"

@app.route("/hello")
def hello():
    return "Good Work!"

@app.route("/hi")
def smile():
    return "HI! Keep Smiling."

@app.route("/user/<enter>")
def user (enter):
    if enter == "hello":
        return redirect(url_for("hello"))
    elif enter == "home" :
        return redirect(url_for("home"))
    else:
        return redirect(url_for("hi"))
    


if __name__=="__main__":
    app.run(debug= True)
from flask import Flask,render_template,url_for

app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template("home.html")


@app.route('/desserts')
def routing():
    return render_template("dessertspage.html")

if __name__ == '__main__':
    app.run(debug=True)
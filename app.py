from flask import Flask,render_template

app=Flask(__name__)

@app.route('/desserts')
def routing():
    return render_template("dessertspage.html")

if __name__ == '__main__':
    app.run(debug=True)
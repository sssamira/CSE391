from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("signup.html")
app.run(debug=True)


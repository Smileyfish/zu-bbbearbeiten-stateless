import helper
from flask import Flask, request, Response, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
    # Hier werden die Daten an index.html übergeben
    todos = helper.get_all()
    return render_template('index.html', todos=todos)

# Hier wird definiert, auf welche URLs die Applikation reagiert
@app.route('/add', methods=["POST"])
def add():
    title = request.form.get("title")
    helper.add(title)
    return redirect(url_for("index"))


@app.route('/update/<int:index>')
def update(index):
    helper.update(index)
    return redirect(url_for("index"))
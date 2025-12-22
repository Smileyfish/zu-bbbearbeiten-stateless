import helper
from flask import Flask, request, Response, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/download")
def get_csv():
    return Response(
        helper.get_csv(),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=zu-bbbearbeiten.csv"},
    )


@app.route("/")
def index():
    items = helper.get_all()
    return render_template('index.html', items=items)



@app.route("/add", methods=["POST"])
def add():
    text = request.form.get("text")
    date = request.form.get("deadline")
    category = request.form.get("category")
    description = request.form.get("description")
    helper.add(text, date=date, category=category, description=description)
    return redirect(url_for("index"))


@app.route('/update/<int:index>')
def update(index):
    helper.update(index)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0")


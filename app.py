from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def banana():
    return "Hello this is the route page."

@app.route("/status/<string:id>")
def apple(id):
    return render_template("index.html", id=id)

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def page1():
    return "My first page of project"

if __name__=="__main__":
    app.run(debug=True)
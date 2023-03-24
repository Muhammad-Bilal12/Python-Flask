from flask import Flask, render_template

app = Flask(__name__)  # app_name


# render template used to render the html file
@app.route("/")  # to define route
def hello_world():  # to define what to do
    return render_template('index.html')


@app.route("/about")
def hello_about():
    name = "bilal"
    return render_template("about.html", name2=name)


app.run(debug=True)  # to run the project and run debugging


# static folder is for public
# template folder is for private

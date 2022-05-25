from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task
# above we import these classes in order to generate our database next


# to get the app running we create a basic app
# route using the route level directory of flask
# this is used to target a function called home  
# which will return the rendered tcemplate
@app.route("/")
def home():
    return render_template("tasks.html")
    # update this from base to tasks.  tasks will now become the home page
    # so when a user comes to the site they will be taken there and it will
    # extend all the content from the base page

# remember when you use the url_for method you call the python function def
# categories not the app.route even though they are often the same name
@app.route("/categories")
def categories():
    return render_template("categories.html")

# this app. route has get and post methods since we will be submitting a form
# to the database.  the function name is add_category which matches the the
# link function on the categories page 
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")


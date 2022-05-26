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
    categories = Category.query.order_by(Category.category_name).all()
    return render_template("categories.html", categories=categories)

    #First, let's define a new variable within the categories function, which will also be
    # called categories to keep things consistent.
    # We just need to query the 'Category' model that is imported at the top of the file from
    # our models.py file, and we can do that by simply typing:
    # Category.query.all()
    # Sometimes though, categories might be added at different times, so this would have the
    # default method of sorting by the primary key when things get added.
    # Let's go ahead and use the .order_by() method, and have it sort by the key of 'category_name'.
    # We also need to make sure that we tell it the specific model as well, even though it
    # might seem redundant, it's possible to use other sorting methods.
    # You need to make sure the quantifier, which is .all() in this case, is at the end of the
    # query, after the .order_by() method.
    # Whenever we call this function by clicking the navbar link for Categories, it will query
    # the database and retrieve all records from this table, then sort them by the category name.
    # Now, all that's left to do here is to pass this variable into our rendered template,
    # so that we can use this data to display everything to our users.
    # By using the .all() method, this is actually what's known as a Cursor Object, which is
    # quite similar to an array or list of records.
    # Even if the result comes back with a single record, it's still considered a Cursor Object,
    # and sometimes Cursor Objects can be confusing when using them on front-end templates.
    # Thankfully, there's a simple Python method that can easily convert this Cursor Object
    # into a standard Python list, by wrapping the variable inside of 'list()'.
    # You might be slightly confused as to what 'categories=categories' represents, so let's quickly explain this part.
    # The first declaration of 'categories' is the variable name that we can now use within the HTML template.
    # The second 'categories', which is now a list(), is the variable defined within our function
    # above, which is why, once again, it's important to keep your naming convention quite similar.

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


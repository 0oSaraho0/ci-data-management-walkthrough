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

"""
Let's go over to the routes.py file, and we are going to create a new function.
For the app route URL, let's call this "/edit_category", and once again, we 
will be using this as adual-purpose for both the "GET" and "POST" methods.
The function name will match, so that will be "edit_category". To start with,
we will only focus on the "GET" method, which will get the template, and render
it on screen for us. We can simply return render_template using the new file 
we created, "edit_category.html".However, we need some sort of mechanism for
the app to know which specific category we intend to update. In order to
understand this, let's open the template for all categories, which contains
the for-loop we built in the last video.
"""

"""
Now, we can head back over to the routes.py file, and since we've given an argument of
'category_id' when clicking the 'Edit' button, this also needs to appear in our app.route.
These types of variables being passed back into our Python functions must be wrapped
inside of angle-brackets within the URL.
We know that all of our primary keys will be integers, so we can cast this as an 'int'.
We also need to pass the variable directly into the function as well, so we have the
value available to use within this function.
If you have attempted to save these changes and load the page, then you're going to get an error.
This is a very common error, and something that all developers should know how to understand,
so let's save everything, and load the live preview.
Once that's loaded, navigate to the Categories page,
"""

"""
try clicking on one of the Edit buttons, and you'll notice the Werkzeug Error.
"Could not build url endpoint 'edit_category'. Did you forget to specify values ['category_id']?"
The really fantastic thing with any Flask error, is that it will always tell you exactly
which file and line number is causing the specific error.
Normally, this can be found towards the bottom of the error lines, and you want to look for
the code in the blue rows that matches your own code.
As you can see here, we're calling the URL for the edit_category function, which is listed
on the edit_category.html template, from line 7.
Essentially what happened is once we added the primary key of ID into our app.route function,
it will now always expect this for any link that calls this function.
Let's go back to the edit_category template, and sure enough on line 7 we have the url_for method.
"""

"""
In order for this function to know which specific category to load, we need to attempt to find
one in the database using the ID provided from the URL.
The template is expecting a variable 'category', so let's create that new variable now.
Using the imported Category model from the top of the file, we need to query the database,
and this time we know a specific record we'd like to retrieve.
There's a SQLAlchemy method called '.get_or_404()', which takes the argument of 'category_id'.
What this does is query the database and attempts to find the specified record using the data
provided, and if no match is found, it will trigger a 404 error page.
Now, we can pass that variable into the rendered template, which is expecting it to be called
'category', and that will be set to the defined 'category' variable above.
The page should load now without any errors, however, if you notice, it doesn't show us
the current value of our category, and the form doesn't do anything just yet.
"""

"""
The final step now, is to add the "POST" functionality so the database actually gets updated with the requested changes.
Back within our routes.py file, just after the 'category' variable being defined, let's
conditionally check if the requested method is equal to "POST".
If so, then we want to update the category_name for our category variable, and we'll set that
to equal the form's name-attribute of 'category_name'.
After that, we need to commit the session over to our database.
Finally, if that's all successful, we should redirect the users back to the categories
function, which will display all of them in the cards once again.
Save all of your changes, and let's go back to the live preview.
"""

@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)
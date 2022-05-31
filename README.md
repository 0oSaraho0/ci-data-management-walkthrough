# Lesson 1

Hi, and welcome to the Relational Database Management System mini-project.
My name is Tim Nelson, and in this project, we are going to create a task manager application.
This task manager will be built using Flask, the SLQAlchemy ORM, and a frontend framework called Materialize.
For the Learning Outcomes, we will learn how to perform full CRUD functionality, which
allows us to create, read, update, and delete items on our database.
This will be done in the context of a Flask application.
We will also create HTML-based user interfaces to demonstrate these CRUD calls in action.
In the spirit of good user experience, we will style these interfaces using the Materialize framework.
Let's have a look at the project we are going to build together.
The home page of our task manager application displays a summary of tasks.
That summary information consists of the task name, due date, whether or not it's an urgent task,
and once we click to expand more, we see the task category, and a description.
Users will be able to create new tasks, view their tasks, edit tasks, and finally, delete their tasks.
In addition to performing CRUD functionality for tasks, users will also be able to perform
the same thing with various categories.
The app will be fully responsive due to the fact that we will use the Materialize framework grid-based classes.
Materialize is another framework similar to Bootstrap, based off of Google's Material Design concept.
Due to the fact that Materialize and Bootstrap share common features and functionalities,
it is highly recommended to avoid using both frameworks together in one application.
If you prefer Bootstrap, but like the Material Design aspect of Materialize, then there's
a third framework to consider called Bootstrap Material Design.
Remember, do not mix the frameworks, as they often use the same elements, IDs, and class
names, so your app will get confused and not render properly.
Let's navigate to MaterializeCSS.com, and explore some of their built-in features.
The current version of Materialize is 1.0.0, which can be selected from their main page.
It might be possible that the version has been updated at the time you're watching this
video, so pay careful attention to the version when working with their components.
The easiest way to work with Materialize is by using their CDN links on the "Getting Started" page for both CSS and JavaScript.
Most of their components have support for jQuery if you decide to also include it, but
all components can be used with pure vanilla JavaScript.
Similar to Bootstrap, Materialize operates their responsive behaviors based on the standard
12-column grid system using containers, rows, and columns.
You can see their various breakpoint sizes, with a few examples of how the grid is used.
One of the benefits of using Google's Material Design is that they have over 200 custom color
classes that you can use for backgrounds and text.
Simply add the color class names to your element, excluding the HEX value, and then decide if
it's meant for text by adding "-text" to the helper class name.
I encourage you to explore the various pages and elements that Materialize has to offer,
but for now, we are only going to focus on the components that we will use with this mini-project.
Cards are a wonderful way to display content that contains varied types of objects, such
as headers, paragraphs, links, buttons, and even images.
There are several navbar elements to choose from, all of which come with full responsive behavior out of the box.
The collapsible element is what we will use to display each of our tasks on the main page,
and can be opened or closed when clicked.
Since our users will be able to build their own tasks, we will be using various form elements,
such as switches, datepickers, selectors, and the standard input boxes.
This was just a small sample of components that Materialize provides, so take a few minutes
to get familiar with their site, and play around with the various elements to see how they work.
Now that we've seen a sneak peek of what's to come, let's dive right in and start building our Task Manager application.

# Lesson 2

This video assumes that you are using our recommended development environment, and have
already created your new repository.
The very first thing that we need to do is install two Python packages.
pip3 install Flask-SQLAlchemy psycopg2
Previously, we've learned how to use Flask to build the Thorin project, and SQLAlchemy to work with Postgres databases.
By installing Flask-SQLAlchemy, this actually comes with both Flask and the SQLAlchemy requirements together in one download.
In order to work with the Postgres database, as you may recall, we need to have psycopg2 installed as well.
Next, we will be storing some sensitive data, and we need to hide them using environment
variables hidden within a new file called 'env.py'.
Make sure to have a .gitignore file that contains any files and folders which should be ignored by GitHub, such as an env.py file.
Since these variables should be available system-wide on our application, we need to import the operating system itself.
To set up default environment variables, it takes two arguments, the key and the value,
both within quotes, and for this project we need six different variables, so copy that line six times.
Those six variables are: IP, PORT, SECRET_KEY, DEBUG, DEVELOPMENT, and DB_URL.
IP is 0.0.0.0
PORT is 5000 for Flask applications.
SECRET_KEY can be any random string you'd like.
DEBUG will be set to True for now, but make sure you set DEBUG to False prior to your actual project submissions.
DEVELOPMENT will also be set to True for now, and this is what we'll use to distinguish
between our local environment, and our deployed application later.
DB_URL will point to our database, which we don't currently have, but when working locally,
we'll use the local Postgres environment.
The three slashes represent the fact that our database is local within our workspace,
and we'll be creating a new database called 'taskmanager'.
Remember to save the file once we're done.
Next, the entire application will need to be its own Python package, so to make this
a package, we need a new folder which we will simply call taskmanager/.
Inside of that, a new file called __init__.py
This will make sure to initialize our taskmanager application as a package, allowing us to use
our own imports, as well as any standard imports.
We will start by importing the following:
import os from flask import Flask
from flask_sqlalchemy import SQLAlchemy
In order to actually use any of our hidden environment variables, we need to import the 'env' package.
However, since we are not pushing the env.py file to GitHub, this file will not be visible
once deployed to Heroku, and will throw an error.
This is why we need to only import 'env' if the OS can find an existing file path for the env.py file itself.
Now we can create an instance of the imported Flask() class, and that will be stored in
a variable called 'app', which takes the default Flask __name__ module.
Then, we need to specify two app configuration variables, and these will both come from our environment variables.
app.config SECRET_KEY and app.config SQLALCHEMY_DATABASE_URI, both wrapped in square brackets and quotes.
Each of these will be set to get their respective environment variable, which is SECRET_KEY,
and the short and sweet DB_URL for the database location which we'll set up later.
Then, we need to create an instance of the imported SQLAlchemy() class, which will be
assigned to a variable of 'db', and set to the instance of our Flask 'app'.
Finally, from our taskmanager package, we will be importing a file called 'routes' which we'll create momentarily.
Once you save the file, you'll notice we have a couple linting issues.
First, it says that we've imported 'env', but it's unused.
It's also complaining about our custom import not being added at the top of the file with the other imports.
The reason this is being imported last, is because the 'routes' file, that we're about
to create, will rely on using both the 'app' and 'db' variables defined above.
If we try to import routes before 'app' and 'db' are defined, then we'll get circular-import
errors, meaning those variables aren't yet available to use, as they're defined after the routes.
These linting warnings are technically not accurate, so to stop the warnings, we can
add a comment at the end of each line, # noqa for 'No Quality Assurance'.
Now we can create the new 'routes.py' file within our taskmanager package.
We're going to start using some Flask functionality, so we can import render_template from flask to start with.
Then, from our main taskmanager package, let's import both 'app' and 'db'.
For simplicity to get the app running, we'll create a basic app route using the root-level directory of slash.
This will be used to target a function called 'home', which will just return the rendered_template
of "base.html" that we will create shortly.
Save the file, and now it's time to create the main Python file that will actually run the entire application.
This will be at the root level of our workspace, not part of the taskmanager package itself.
Since it will run the whole application, let's just call it run.py in that case.
We need to import os once again, in order to utilize environment variables within this file.
We also need to import the 'app' variable that we've created within our taskmanager
package, defined in the init file.
The last step to run our application is to tell our app how and where to run the application.
This is the same process we've seen before, checking that the 'name' class is equal to
the default 'main' string, wrapped in double underscores.
If it's a match, then we need to have our app running, which will take three arguments:
'host', 'port', and 'debug'.
Each of these, as you may recall, are stored in the environment variables, so we need to
use os.environ.get().
The host is the IP, the port is obviously PORT, but that needs to be converted into
an integer, and then debug is of course DEBUG.
Finally, we need to render some sort of front-end template to verify that the application is running successfully.
Within our taskmanager package, let's create a new directory called 'templates', which
is where Flask looks for any HTML templates to be rendered.
Then, within this templates directory, we will create a new file called base.html, which
is what will be rendered from our routes.py file.
We'll keep it simple for now, and generate a basic HTML template by typing html:5, then hitting the tab key.
Update the title to 'Task Manager', and then let's simply add "Hello World!" within the body.
Save all files if you haven't already, and let's go ahead and attempt to run this application from within the Terminal.
We can type python3 run.py in order to launch our main file, which will import the necessary
taskmanager package and all of its dependencies we've specified.
If you happen to see a warning about Track Modifications for SQLAlchemy, this can be
ignored, as they will eventually disable this in the future.
Let's go ahead and open the browser using the exposed Port, but it might take a moment
to load, or require a quick refresh of the page.
Excellent, you can see that we have 'Hello World!' showing on our site, so the application is running successfully!
We've learned how to set up a basic Flask application using the Flask-SQLAlchemy package.
In our next video, we'll start setting up the actual database schema by defining our
models, so for now, go ahead and push your changes to GitHub, and I'll see you in the next lesson.

# Lesson 3
Now that we have the basic Flask application set up and running, it's time to start creating
our database schema by defining our models.
We'll start by creating a new file called models.py within our taskmanager package.
Since we will be defining the database, we obviously need to import db from the main taskmanager package.
For the purposes of these videos, we will be creating two separate tables, which will
be represented by class-based models using SQLAlchemy's ORM.
The first table will be for various categories, so let's call this class 'Category', which
will use the declarative base from SQLAlchemy's model.
The second table will be for each task created, so we'll call this class 'Task', also using the default db.Model.
We want each of these tables to have a unique ID, acting as our primary key, so let's create
a new column variable of 'id' for both of these tables.
These will be columns on our tables, and each will be Integers, with primary_key set to
True, which will auto-increment each new record added to the database.
If you recall from the last few lessons, we had to specifically import each column type at the top of the file.
However, with Flask-SQLAlchemy, the 'db' variable contains each of those already, and we can
simply use dot-notation to specify the data-type for our columns.
For each model, we also need to create a function called __repr__ that takes itself as the argument,
similar to the 'this' keyword in JavaScript.
This is a standard Python function meaning 'represent’, which means to represent the class objects as a string.
Another function that you might see out there, is the __str__ function that behaves quite
similar, and either should be suitable to use.
For now, let's just return self for those, but we'll come back to these momentarily.
Within our Category table, let's add a new column of 'category_name', which will be set to a standard db.Column().
This will be the type of 'string', with a maximum character count of 25, but you can
make these larger or smaller if needed.
We also want to make sure each new Category being added to the database is unique, so we'll set that to True.
Then, we also need to make sure it's not empty or blank, so by setting nullable=False this
enforces that it's a required field.
Now that we have a category_name, we can simply return self.category_name in our function.
For our Task table, we'll add a new column of 'task_name', which will also be a standard db.Column().
This will also be the type of 'string', with a maximum character count of 50, which should
also be unique for each record, and required, so nullable=False.
Then, we'll create a new column for 'task_description', and this time we'll use db.Text instead of
string, which allows longer strings to be used, similar to textareas versus inputs.
Next, we'll create a new column for 'is_urgent', but this will be a Boolean field, with a default
set to False, and nullable=False.
Then, the next column will be 'due_date', and this data-type will be db.Date with nullable=False,
but if you need to include time on your database, then db.DateTime or db.Time are suitable.
By the way, you can see a full list of column and data types from the SQLAlchemy docs, which
include Integer, Float, Text, String, Date, Boolean, etc.
The final column we need for our tasks is a foreign key pointing to the specific category, which will be our category_id.
This will use db.Integer of course, and for the data-type we need to use db.ForeignKey
so our database recognizes the relationship between our tables, which will also be nullable=False.
The value of this foreign key will point to the ID from our Category class, and therefore
we need to use lowercase 'category.id' in quotes.
In addition to this, we are going to apply something called ondelete="CASCADE" for this foreign key.
Since each of our tasks need a category selected, this is what's known as a one-to-many relationship.
One category can be applied to many different tasks, but one task cannot have many categories.
If we were to apply many categories to a single task, this would be known as a many-to-many relationship.
Let's assume that we have 10 tasks on our database, and 2 categories, with these two
categories being assigned to 5 tasks each.
Later, we decide to delete 1 of those categories, so any of the 5 tasks that have this specific
category linked as a foreign key, will throw an error, since this ID is no longer available.
This is where the ondelete="CASCADE" comes into play, and essentially means that once
a category is deleted, it will perform a cascading effect and also delete any task linked to it.
If these aren't deleted, and a task contains an invalid foreign key, then you will get errors.
In order to properly link our foreign key and cascade deletion, we need to add one more field to the Category table.
We'll call this variable 'tasks' plural, not to be confused with the main Task class, and
for this one, we need to use db.relationship instead of db.Column.
Since we aren't using db.Column, this will not be visible on the database itself like
the other columns, as it's just to reference the one-to-many relationship.
To link them, we need to specify which table is being targeted, which is "Task" in quotes.
Then, we need to use something called 'backref' which establishes a bidirectional relationship
in this one-to-many connection, meaning it sort of reverses and becomes many-to-one.
It needs to back-reference itself, but in quotes and lowercase, so backref="category".
Also, it needs to have the 'cascade' parameter set to 'all, delete' which means it will find
all related tasks and delete them.
The last parameter here is lazy=True, which means that when we query the database for
categories, it can simultaneously identify any task linked to the categories.
The final thing that we need to do with our class-based models, is to return some sort of string for the Task class.
We could simply return self.task_name, but instead, let's utilize some of Python's formatting to include different columns.
We'll use placeholders of {0}, {1}, and {2}, and then the Python .format() method to specify
that these equate to self.id, self.task_name, and self.is_urgent.
Go ahead and save the file, and let's return back to our routes.py file now.
At the top of the routes, we need to import these classes in order to generate our database next.
Save this file, but don't worry if you get any linting warnings about unused values.
We'll come back to these in the next lessons, but it's required to have our database schema
created within Postgres.
If you recall from our environment variables, we've specified that our database will be
called 'taskmanager', not to be confused with our 'taskmanager' Python package.
This would be similar to the 'chinook' database we created in the previous lessons, so we
will need to also create this 'taskmanager' database.
Let's navigate to the Terminal, and login to the Postgres CLI by typing 'psql' and hitting enter.
To create the database, we can simply type:
CREATE DATABASE taskmanager;
Once that's created, we'll switch over to that connection by typing:
\c taskmanager;
We don't need to do anything else within the Postgres CLI now that we have the database
created, so let's come out of the CLI by typing \q.
Next, we need to use Python to generate and migrate our models into this new database.
This will take the models that we've created for Category and Task, and build the database
schema using the details we've provided.
It's important to note, that if you were to modify your models later, then you'll need
to migrate these changes each time the file is updated with new context.
For example, if you added a new column on the Task table for 'task_owner', once the
file is saved, you'll need to make your migrations once again, so the database knows about these changes.
Let's go ahead and access the Python interpreter by typing "python3" and enter.
From here, we need to import our 'db' variable found within the taskmanager package, so type:
from taskmanager import db
Now, using db, we need to perform the .create_all() method:
That's it, pretty simple enough, our Postgres database should be populated with these two
tables and their respective columns and relationships.
Let's exit the Python interpreter by typing exit().
Congratulations, you now have your database models and schema migrated into the database.
You should go ahead and push your changes to GitHub now for version control.
However, if you'd like to confirm that these tables exist within your database, then follow
these instructions listed on the screen.
I'll see you in the next lesson, where we are going to start creating some of the front-end
templates with the Materialize CSS framework!

# Lesson 4

In the last video, we managed to get our database schema created and migrated to Postgres.
Before we can do any data manipulation using CRUD functionality, we need some sort of front-end
user interface to interact with the database.
If you recall from the previous lessons using Flask on the Thorin project, we used something called template inheritance.
This allows us to extend various HTML templates, to avoid duplicating code, such as a navbar
or footer that's identical across all pages.
Also, in the introduction video, we discussed the use of a CSS framework called Materialize,
which we will be using throughout this project.
This will allow us to make use of their responsive behaviors using the grid system, similar to
Bootstrap, and various components to make our application more user-friendly.
At the time of recording, the latest version of Materialize is 1.0.0 as you can see in the top-left corner of their site.
The first thing that we need to do, is to grab the CDN link and script tags from the 'Getting Started' page.
We'll paste the CSS link within our base template head element, and then paste the JavaScript
script tag at the bottom of our body element.
With Materialize, you can use their components with or without jQuery, so if you decide to
use jQuery, you'll want to include that just before the Materialize script.
In addition to using Materialize, we are going to incorporate some of our own custom CSS and JavaScript.
When using a templating language such as Flask, any assets that we use such as images, CSS,
and JavaScript, need to be stored in a directory called 'static'.
Let's create this new folder within our taskmanager package, and we'll also want to add the css/
and js/ folders within this static directory.
As with tradition, we'll call our CSS file 'style.css', and our JavaScript file 'script.js' in their respective folders.
Now, in order to link to any static file that we have, it's important to note that we must use the correct syntax.
You should be rather familiar with just adding the standard front-end method.
However, with templating languages, this method can cause errors or the files not loading properly.
We must use double curly brackets, and then use the 'url_for()' method, which takes two values.
The first value is the 'static' directory, so it knows to look within this main folder.
Separate the values with a comma, then we need to use filename='css/style.css', and
make sure to watch out for the double vs single quotes.
As you can see, I'm using the double-quotes to wrap the entire href property.
Then, for anything within the href, I've used single-quotes, because by using double-quotes
again, it will think that our href is finished, and throw a syntax error.
Let's do the same exact thing for our JavaScript file.
The script source will use double-quotes, wrapping everything in double curly-brackets,
and the url_for() method points to our static file in single-quotes.
Then, a comma to separate the filename, which is equal to 'js/script.js' in single-quotes,
pointing to our js/ folder and the file itself.
You don't need to use this method for any external CDN links, such as the Materialize links for example.
It's only needed for any files that we actually own within our workspace or project, including images.
This is due to the fact that you’re working with a framework, which relies on using “url_for()”
methods to find the relevant files locally to your own project.
Also, quite often when working with a templating language, if you make changes to your CSS
or JavaScript files, and then reload the page, it might not show your changes.
This is very likely an issue to do with caching, so here are three steps to always remember to check.
First, try a hard-reload, which is generally CTRL+SHIFT+R in most cases, but depending
on your computer and which browser you use, it could be one of these combinations on screen.
Second, if that doesn't work, open a new Incognito window with your project URL, and if you do
see the changes, it's certainly a caching issue, since Incognito doesn't store cache.
Finally, if neither of those options work, stop the application in your terminal from
running, and just restart it.
This may sound asinine, but quite often with Flask and Django, a fresh restart of the app
is required to take effect of any new additions to your code.
Now that we have our static files connected to the base template, let's start adding a
few components, such as a navbar.
From the Materialize docs, click on Components to expand it, then click Navbar.
We'll be using the Mobile Collapse option, which will make a responsive navbar for smaller screens.
Copy the code, and let's paste this within a header tag, which will replace our text of 'Hello World'.
The reason why it shows the unordered list twice, is because one is for the navbar on
the top of the page, and the other is for our mobile side navbar.
If you recall from the introduction video, Materialize has a variety of colors to choose
from, whether it's for text or elements.
I'm going to change the default pink navbar to include a class of light-blue darken-1,
but feel free to use any color you’d like.
For the logo, we'll just call the project Task Manager, and have it load our main page when clicked.
Similar to our static files, we need to use the url_for() method for any links within our project.
Double curly-brackets, url_for(), and then in single-quotes the name of our Python function to call, which is 'home'.
If you recall from our routes.py file, this is the only route that we've created so far,
and we've called it 'home', which will render the base.html template.
We don't need to include the 'static' or 'filename' properties, since this is calling an actual function.
Again, using this approach is very important, so if you only type href="base.html", then
your project won't compile properly by Flask, and you'll likely get an error.
We're going to have 3 links within our navbar, so we'll remove their sample links.
These links will be: Home, New Task, and Categories.
We already have the function created for our 'Home' link, so we can copy that, and paste it within the hrefs.
Since we haven't created the other two functions or routes yet, then we cannot include those as placeholder links.
If we try to load the site using placeholder links, Flask will throw an error saying that
it can't find the intended function you're attempting to call.
For the mobile menu icon, the Materialize docs include Google's Material Design icons,
so you're welcome to those as well, but be sure to include the CDN link from the 'Icons' page.
However, Font-Awesome contains over a thousand more icons to choose from, so I'll include
the Font-Awesome CDN link from the CDNJS library site.
I'll copy the link tag, and paste it within my head element before the Materialize CDN
link, then replace the menu icon with a Font-Awesome icon instead.
Next, even though we don't have the Python functions created, I'm going to duplicate
the Home link, and create empty links for the others now.
The second link will be for adding a New Task, and the final link will be for all Categories.
Remember, these need to be blank href links for now, so we'll delete the paths, and then
we can go ahead and copy these two new links, then paste them below in the sidenav list.
In order for the sidenav to work, we need to initialize the JavaScript functionality from Materialize.
Let's copy the initialization code, either the vanilla JavaScript snippet, or if you're
using jQuery, the snippet below, then let's paste it within our script.js file.
We are actually going to be using a few different elements from Materialize, so let's give our
variables a more unique name.
The querySelector will be 'sidenav', and then we'll just initialize that without defining any variable.
The next section will be where all of our main content will be injected, so we'll use
the Template Inheritance {% block %} element.
Let's wrap this inside of a semantic main element with the Materialize class of 'container'.
In exactly the same way that we did on our previous Flask lessons, we'll call this block
element 'content', making sure to close the {% endblock %} tag as well.
Before we create any template that extends this, we'll quickly add a Materialize footer.
Paste the footer below the main element, and you can style this any way you'd like,
but I'll keep it simple and clean by removing some unnecessary bulk.
It'll be 'blue darken-3', removing the container link section, adding 'For educational purposes
only', then a link to Code Institute in a new blank tab.
Since we've been using semantic HTML elements such as header, nav, main, and footer, we
can simply force the footer to stay at the bottom of the page by using the 'Sticky Footer' CSS code.
Paste that into your CSS file, and this will make the footer always stay at the bottom
of the page, no matter how much or how little content is on each page.
Now we can start using the template inheritance functionality, and extend our base template across various files.
Let's create a new template in the templates directory, and call it 'tasks.html', which
is where we will display any task that will be stored within our database later.
This will use the {% extends %} block, which will extend our base.html template.
This means that by extending from the base template, anything created on our base template
will display on this page as well, which includes our navbar and footer.
Then, we'll inject anything from this tasks template into the 'content' block element,
making sure to close the {% endblock %} as well.
We will add the content for this page in a later video, so for now, let's simply just
add an h3 element for 'Tasks', with some of the Materialize helper classes.
Finally, let's go back to our routes.py file, and update the rendered template to be 'tasks.html' instead.
This will become our home page now, so that when a user visits our site, they're brought
to the tasks page, which will automatically extend all of the content from our base template.
Save all of your files, and if your app isn't currently running, go ahead and start it within
the terminal by typing 'python3 run.py' and then open your browser.
Remember to hard-reload the page or use Incognito Mode if your static files with the CSS or
JavaScript aren't working for you, otherwise check for a possible typo on your code.
Everything looks great so far, and behaves as expected, even our mobile navbar if we
decrease the width of the page.
We now have the basic front-end template set up with a navbar, a footer, and a tasks template
that uses Template Inheritance to extend from the base file.
In the next lesson, we are going to start working with the database, and performing some CRUD functionality.
For now, go ahead and push your code to GitHub, and I'll see you on the next video.

# Lesson 5

In the previous video, we used template inheritance to connect our tasks file with our base template,
and set up the main layout using Materialize.
Before we can start adding tasks to our database, we first need to have some functionality that handles the categories.
If you recall from when we built the database schema in a previous video, each Task must
have a Category assigned, which makes it the foreign key to the Category model.
In this video, we'll build a front-end template that then allows us to add new categories to the database.
Let's start by creating a couple new templates; categories.html and then another template called add_category.html.
Both of these files will of course be extended from the base template, and have their code
injected into the 'content' {% block %}, so we can simply copy/paste from the 'tasks' template.
Then, update the
title for each, which will be "Categories" and "Add Category".
For now, we aren't going to focus on viewing each of the categories, we will cover that
in the next video, but we do need a button that will bring us to the form to add a new category.
To make this responsive, we'll use the Materialize grid helper classes and layout.
First, start with a row, which has a column that spans all 12 spaces, and is center-aligned.
Within this column, we'll add a link that will use the Materialize 'btn-large' class,
which will make it a larger button than their default button size.
It will also have some helper color classes to make it light-blue and darken-2.
The link will be "Add Category", and include an icon of your choosing, so I'll add a generic Font-Awesome 'plus' symbol.
As for the href, since we'll be targeting a file within our own project, we must use
the double curly-brackets and url_for() method.
We haven't built this function yet, but let's go ahead and assign the URL to be 'add_category'.
Let's then open the routes.py file, and create some functions that will generate these templates.
In our navbar, we have a link for "Categories", so we need a function that will populate the
new categories template that we've just created.
The app route will be "/categories", and for the function name itself, that will be consistent,
so we'll also call that "categories".
Whenever you use the url_for() method on your links, it's important to note that these are
calling the actual Python functions, not the app.route, even though these are often the same name.
For now, we don't have any data from the database yet, so we can simply just return the rendered template of 'categories.html'.
Let's quickly link that navbar button to this function, so open your base.html template, and find the navbar links.
Copy the href for our 'Home' link, and paste it within the href for 'Categories'.
Since our new function is called 'categories', let's update this to reflect that, and then
we can copy this new href and paste it below into the mobile sidenav link.
Go back to the routes.py file, and now we'll create a new route that will render our template for adding a new category.
The app route will be "/add_category", and this time we need to include a list of the
two methods "GET" and "POST", since we will be submitting a form to the database.
Our function name will match 'add_category', which, if you recall, is the same name we
added to the link href to target this function that we're creating now.
When a user clicks to add a new category, it should render the template that contains
a form, and by displaying the form to users, this uses the "GET" method to 'get' the page.
We can copy the render template line from one of the functions above, and just replace
the template name with 'add_category.html'.
However, when a user eventually submits this form, the form will attempt to 'post' the
data into the database, and this is why we need to specify both methods in the app route.
Don't worry about this part too much right now, because we will come back to this function
in a couple minutes, and go into a bit more detail.
Now that the basic routes are created for each template, start the application in your
terminal using python3 run.py, just to confirm everything is working fine.
Clicking on the Categories button in our navbar opens up the 'categories.html’ template,
and shows the 'Add Category' button, so let's click that.
Wonderful, that's behaving perfectly, so let's go ahead and start building the form to allow
users to add a new category to the database.
Taking a look at our Category model, the only real form element we need to collect is the
'category_name', since the ID will be set by default, and 'tasks' gets applied behind the scenes.
Let's navigate to the Materialize page under 'Forms' called 'Text Inputs', and copy the entire code snippet provided.
We'll paste that within the 'add_category.html' template, and let's remove all but one input row.
If you recall from the introduction video, one of the Materialize components is a 'card',
and there are a few different card types to choose from.
We don't need anything fancy at this stage, so we'll just utilize the 'card-panel' class
for a basic card motif, and apply that to the main 'row'.
I'm also going to apply a light grey color to the card, just so it stands out a bit more on our white background.
The form itself will use the "POST" method once submitted, and for the action, that's
going to point back to the same function of 'add_category'.
Let's make sure this input spans all 12 spaces on the grid, so update the column class from 's6' to 's12'.
If you wanted the input to have an icon before the box, then we can simply use the 'prefix'
class on an icon, using any icon you'd like.
In order for Python to recognize the form data, we need to use the name-attribute, and
it's considered best practice to have the name, ID, and label-for all matching.
This box will be for our 'category name' field on the database, so let's call it 'category_name'
for each of those, removing the placeholder text as well.
Then, let's make this field required, and add a minimum length of 3, with a max length of 25.
After the row for our category_name, let's add one more row, with a column spanning 12
spaces once again, and this time it will be center aligned.
This will be for our submit button on the form, and we're going to give it a class of
'btn-large' plus any Materialize color class you'd like.
The button will read 'Add Category', and I'm going to add another Font-Awesome icon here
on the right-hand side of the button.
We're actually finished with this template now, it's fairly short, but if we attempt
to submit the form, it will not work, due to the fact that we haven't created the POST method yet.
Let's return to the route.py file, and now we can add the POST method functionality for
users to add a new category to the database.
If the requested method is equal to POST, then we will create a new variable called
'category', which will be set to a new instance of the Category() model imported at the top of the file.
By using the 'request' method, we need to also import that from Flask at the top here.
We need to make sure that this Category model uses the same exact keys that the model is
expecting, so when in doubt, copy from the model directly.
For this category_name field, we can then use the requested form being posted to retrieve the name-attribute.
This is why it's important to keep the naming convention consistent, which means our name-attribute
matches that of our database model.
Once we've grabbed the form data, we can then 'add' and 'commit' this information to the
SQLAlchemy database variable of 'db' imported at the top of the file.
This will use the database sessionmaker instance that we learned about in some of the previous videos.
After the form gets submitted, and we're adding and committing the new data to our database,
we could redirect the user back to the 'categories' page.
We'll need to import the 'redirect' and 'url_for' classes at the top of the file from our flask import.
That completes our function, so let's quickly recap what's happening here.
When a user clicks the "Add Category" button, this will use the "GET" method and render the 'add_category' template.
Once they submit the form, this will call the same function, but will check if the request
being made is a “POST“ method, which posts data somewhere, such as a database.
Anything that needs to be handled by the POST method, should be indented properly within this condition.
By default, the normal method is GET, so it will behave as the 'else' condition since
it's not part of the indented POST block.
If you wanted to, technically you could separate this into two separate functions, which would
handle the GET and POST methods completely apart.
Also, in a real-world scenario in a production environment, you'd probably want to consider
adding defensive programming to handle brute-force attacks, along with some error handling.
But for now, it's the moment of truth, so go ahead and save all of your files, and start
the application in the terminal if it isn’t running anymore.
After that loads, navigate to the Categories page, and then click on the button to add a new category.
I'm going to call my category 'Travel', and hit the button to submit the form.
As you can see, the page submits, and redirects me back to the Categories page without any errors.
Assuming that worked properly due to the fact that there weren't any errors, it should've
added "Travel" to the database.
Currently, we have no way to verify that submitted properly, unless we access the Postgres database on the CLI.
Instead of using the CLI, in the next video, we are going to learn how to extract data
from the database, and display it to our users.
Go ahead and push your code to GitHub, and I'll see you on the next lesson.

# Lesson 6

In the previous video, we managed to add a new category into our database, which is just
one part of performing CRUD functionality.
The C in CRUD means to Create, by creating a new category and having it post to the database.
In this video we are going to focus on the R in CRUD, which means to Read from the database.
If your application isn't currently running, go ahead and start it in the terminal by typing
'python3 run.py' and navigate to the Categories page from the navbar.
On this page, we'd like to retrieve all of the categories listed in the database, and
display them to our users here.
Currently, from the previous video, we've only added a single category so far, which
was "Travel", but we don't see it displayed here yet.
From the introduction video, we mentioned the Materialize 'card' component, and we used
the card class in the last video on our form.
This time, we are going to include some buttons in the card, and we need to use a different
version of the card component, so let's head over to the Materialize site.
From the Cards page within the Materialize components, we are going to use the Basic
Card at the top, which already comes with two links.
Go ahead and copy the entire code snippet, and let's paste this into our categories template,
just underneath the row that contains the 'Add Category' button.
The current grid sizes listed from this code show that the card will display across the
entire screen on small devices, and only half the screen on medium devices and up.
We don't necessarily need the cards to be that big on larger devices, so let's add another grid class of 'l3'.
This means, for larger devices, the card should occupy 25% of the parent element, since the
number of spaces available per row is 12, and means it can contain 4 cards per row.
We can design the card however we'd like, so choose any color combination from the helper
color classes, making sure that your text and background don't contrast each other.
Also, since this will only contain the name of the category itself, then I'm going to
add the helper class of 'center-align', and remove the paragraph tag entirely.
We aren't finished yet, but let's save the file, and reload the page to see how things are looking.
As you can see, the card is indeed spanning only 25% of the parent element, which, if
you recall, is our main-container class from the base template.
If we check the responsiveness using the Developer Tools, the card flows smoothly, only spanning
50% of the width on medium devices, and on smaller devices, the entire width.
However, if you notice, the links that we have so far are rather squashed, and this
happens when the content in those links are too long, but the card is set to specific size.
For this project, these links will actually become buttons, and the text will be much
shorter, since they will be the buttons for Editing and Deleting our categories later.
Let's go back to the workspace, and update those links accordingly.
The first link will be 'Edit', and the second link will be 'Delete'.
I mentioned that these will be buttons instead of links, so let's apply the Materialize class
of 'btn' to make these styled like buttons.
We will then style the buttons using more of the Materialize helper classes, just make
sure the background and text don't have color contrast issues.
Now, it's time to start building the code that will extract the data from within our
database, so let's head over to the routes.py file.
In the previous video, we added a temporary placeholder route, which allows us to pull
up the categories template itself.
All we need to do here now, is add some code to query the database so we can use that within our template.
First, let's define a new variable within the categories function, which will also be
called categories to keep things consistent.
We just need to query the 'Category' model that is imported at the top of the file from
our models.py file, and we can do that by simply typing:
Category.query.all()
Sometimes though, categories might be added at different times, so this would have the
default method of sorting by the primary key when things get added.
Let's go ahead and use the .order_by() method, and have it sort by the key of 'category_name'.
We also need to make sure that we tell it the specific model as well, even though it
might seem redundant, it's possible to use other sorting methods.
You need to make sure the quantifier, which is .all() in this case, is at the end of the
query, after the .order_by() method.
Whenever we call this function by clicking the navbar link for Categories, it will query
the database and retrieve all records from this table, then sort them by the category name.
Now, all that's left to do here is to pass this variable into our rendered template,
so that we can use this data to display everything to our users.
By using the .all() method, this is actually what's known as a Cursor Object, which is
quite similar to an array or list of records.
Even if the result comes back with a single record, it's still considered a Cursor Object,
and sometimes Cursor Objects can be confusing when using them on front-end templates.
Thankfully, there's a simple Python method that can easily convert this Cursor Object
into a standard Python list, by wrapping the variable inside of 'list()'.
You might be slightly confused as to what 'categories=categories' represents, so let's quickly explain this part.
The first declaration of 'categories' is the variable name that we can now use within the HTML template.
The second 'categories', which is now a list(), is the variable defined within our function
above, which is why, once again, it's important to keep your naming convention quite similar.
Perfect, now that we have this template variable available to us, let's go back to our categories.html
template, and start incorporating it into our cards.
Eventually, we are going to have more than one category listed here, but so far we've
only added the single category of 'Travel'.
However, let's prepare the code to recognize multiple cards, by using the Jinja syntax of a for-loop.
We don't want each card to stack on top of each other, but instead, to flow within the
same row, each having their own column.
Make sure to add the for-loop just inside of the row, so everything within the row is repeated and looped.
The closing {% endfor %} should be just after the div for this column, so follow that down,
and add the closing element there.
Similar to JavaScript, we need to define a new index for each iteration of this loop,
so to keep things consistent, we will call ours 'category'.
This means that for each 'category' in the ‘list of categories' being passed over from
our Python function, it will generate a new column and card.
Finally, we need to display the actual category name that's stored within our database, so
we can update the card-title.
Since we are within a for-loop, we need to use the newly defined index variable of 'category'.
We also need to use dot-notation and tell it which key should be printed here, so in
this case, it should be 'category.category_name', which means, “this category’s key of category_name”.
If you wanted to show the primary key instead, that's stored within our database as 'id',
so it would be 'category.id' for example.
That's all there is to it, so make sure all of your files are saved now, then go ahead
and reload the preview page.
Wonderful, you can see that we now have a card for the 'Travel' category that we added
in the previous video, which confirms that it was indeed added successfully.
Let's go ahead and put that to the test, by adding a few more new categories now.
Pause the video, and add some of your own custom Categories.
Welcome back, I hope you managed to add a few more categories to your database, like
you can see I have here on the screen now.
As you can see, each category is successfully adding to the database, as well as displaying
the card for each one, and sorting them alphabetically by the category name.
We have now covered 50% of CRUD functionality, allowing users to Create and Read records from the database.
In the next video, we are going to focus on the U in CRUD, which will allow users to Update
the category name by clicking the 'Edit' button.
For now though, make sure to push your changes to GitHub, and I'll see you on the next video.

# Lesson 7 Updating Categories


Now that we have the ability to create and retrieve categories, we need to be able to update a category as well.
The first thing we need to do is make a duplicate copy of the 'add_category' template, and let's
rename this to 'edit_category.html' instead.
Anywhere that you see 'Add Category' on this template, go ahead and replace that with 'Edit Category',
which should be a total of three times, plus a quick update to the icon.
The form is almost complete, but if you notice, the form's action attribute is pointing to
a new function called 'edit_category', which we haven't created yet.
Let's go over to the routes.py file, and we are going to create a new function.
For the app route URL, let's call this "/edit_category", and once again, we will be using this as a
dual-purpose for both the "GET" and "POST" methods.
The function name will match, so that will be "edit_category".
To start with, we will only focus on the "GET" method, which will get the template, and render it on screen for us.
We can simply return render_template using the new file we created, "edit_category.html".
However, we need some sort of mechanism for the app to know which specific category we intend to update.
In order to understand this, let's open the template for all categories, which contains
the for-loop we built in the last video.
If you recall, within this for-loop, we have the variable of 'category' that is used for
each iteration of this loop, and we have targeted the 'category_name' field.
Due to the fact that our 'Edit' and 'Delete' buttons are still within the for-loop, we
can use that variable to identify the specific category primary key using '.id'.
Let's go ahead and create the href url_for() method, which will be wrapped in double curly-brackets.
This behaves in the same way that we called the navbar links, or the CSS and JavaScript
files from within our static directory.
In addition to calling our new 'edit_category' function, we need to pass another argument
to specify which particular category we are attempting to update.
Make sure you add a comma after the single-quotes, which identifies that we are calling the function with some data included.
For the argument name, it can be whatever we'd like, and since we need to use something
unique, it's best to use the primary key of the ID.
I'm going to call this 'category_id', and we can now set that equal to the current 'category.id' using dot-notation again.
Since we originally added the 'Travel' category as the first record on our database, its ID will be '1'.
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
Once that's loaded, navigate to the Categories page, and then hover over any of the 'Edit'
buttons for some of the categories we've created.
If you notice in the bottom-left corner, you can see that the href for the 'Travel' card
shows our new function of '/edit_category', and then the number '1'.
You can do this same thing, by using the Developer Tools and inspect the Edit button in the DOM.
Jinja has converted the url_for() method into an actual href, and injected the respective
ID into the argument we added of 'category_id'.
It's the same for any of these cards, each with their own ID applied.
However, try clicking on one of the Edit buttons, and you'll notice the Werkzeug Error.
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
All we need to do is provide the same exact argument of 'category_id' like we did on the href for the Edit button.
Again, separate the argument with a comma after the single-quotes, and the variable
name we assigned was 'category_id'.
This will be set to 'category.id' as well for the value.
Even though we added this to the URL now and saved the file, you will still get an error
saying "'category' is undefined".
You might be wondering where this 'category' value comes from, since this isn't part of
a for-loop like on the categories template.
That's the next step, so go ahead and return to your routes.py file.
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
Within the edit_category template, now that we have the category retrieved from the database,
we need to add its value into the input field.
This is a variable, so we need to wrap it inside of double curly-brackets, and then
we can target the 'category_name' from this variable of 'category' using dot-notation again.
If you save those changes, and then reload the page and click on any of the Edit buttons
now, it should pre-fill the form with the existing value from our database.
The final step now, is to add the "POST" functionality so the database actually gets updated with the requested changes.
Back within our routes.py file, just after the 'category' variable being defined, let's
conditionally check if the requested method is equal to "POST".
If so, then we want to update the category_name for our category variable, and we'll set that
to equal the form's name-attribute of 'category_name'.
After that, we need to commit the session over to our database.
Finally, if that's all successful, we should redirect the users back to the categories
function, which will display all of them in the cards once again.
Save all of your changes, and let's go back to the live preview.
For this demonstration, I'm going to quickly add a new test category, which we can manipulate and update all we want.
Once that's added to the database, go ahead and click the Edit button for that category.
So far so good, and the existing value is listed as 'Test'.
Let's update that to something different, such as 'Miscellaneous', and then click the button to submit the form.
Wonderful, no errors this time, and we're redirected back to the list of all categories,
which confirms that the original 'Test' card is now updated to be 'Miscellaneous'.
By now, you should be fairly comfortable with Creating, Reading, and now Updating records.
We only have one more section from the CRUD functionality remaining, which is D for Deleting
items from the database, which is what we'll be doing in the next lesson.
Go ahead and push your code to GitHub, and I'll see you on the next video.

# Lesson 8 Deleting Categories

So far, we've learned 3 of the 4 CRUD functionalities, to Create, Read, and Update records from our database.
The final CRUD method is to give users the ability to Delete records, which is what we will cover in this video.
In order to allow users to delete a record from the database, we actually don't need to create a new template.
The entire functionality is done from within our back-end function on the routes.py file, so let's open that file.
This will be a brand new function, so let's create a new app.route and call it "/delete_category".
As is tradition by now, our function name will take the same name, "delete_category".
In the same exact way that we specified which category we wanted to edit from our last video, we need to do the same thing here.
This function needs to know which particular category we would like to delete from the data base.
Let's actually copy a few things from the 'edit' function above.
First, we need to pass the category ID into our app route and function, and once again,
we are casting it as an integer.
Next, we should attempt to query the Category table using this ID, and store it inside of a variable called 'category'.
If there isn't a matching record found, then it should automatically return an error 404 page.
Then, using the database session, we need to perform the .delete() method using that
'category' variable, and then commit the session changes.
Finally, once that's been deleted and our session has been committed, we can simply
redirect the user back to the function above called "categories".
The only thing that's left to do now, is to update our href link from the categories template.
The pattern is identical to the Edit button, so as a challenge, I want you to pause the
video here, and see if you can figure this out yourself.
Hopefully you've managed that on your own, but if not, all we need to do is simply copy
the Edit button href, and then paste it into the href for the delete button.
The only difference though, is that we need to update the function name to "delete_category".
As you can see, since we are within the for-loop of all categories, it's using the current
iteration variable of 'category', and then targeting the key of 'id' from that record.
The 'category_id' assigned is just the variable name we're passing into the app.route function
that we just created within the routes.py file.
Make sure you save all changes to your files, and then if your app isn't currently running, go ahead and start it now.
Once the page is loaded, navigate to the Categories page, and hover over any of the 'Delete' buttons.
You can see the URL that will generate if the button is clicked.
Before we actually go ahead and click this delete button, I want to go over a few very
important things to consider when creating any projects.
The first thing you should remember, is that once the delete button is clicked, then it
will completely delete the record from the database for good.
This is considered bad practice, since there isn't any form of defensive programming in place.
Ideally, you should include some sort of blocking mechanism that first has the user confirm
whether or not they'd actually like to delete the record.
A common method for this would be to use a modal for example.
Instead of calling the 'delete_category' function within the href, what it should do is to trigger the modal to open up.
Within this modal, you'll have some message to the user to confirm their action of deleting the record.
If they definitely want to delete the record, then the button within the modal would be
the actual href to call the delete function.
Also, something to note when using modals, is that they generally have a custom ID attached
to them in order to open the modal on screen.
You can see from the Materialize documentation here, the href to call the modal uses the
same ID name to launch the actual modal.
If you use this method within your Jinja for-loop of all categories, then it will only work
for the very first category, and the other modals will not open.
This is because IDs should always be unique, one per page.
The trick around that, is to use something unique within the for-loop to identify the
appropriate modal being generated per category.
We already know that each category has a unique primary key, so we can simply have each modal
being generated within this for-loop to utilize that primary key as well.
The example here would be to call the ID "modal-{{category.id}}" so each modal generated would be transpiled
to the HTML as modal-1, modal-2, modal-3, and so on.
The other important thing to make note of on your projects, is considering user authentication.
In an ideal world, you wouldn't want just any random stranger to be able to edit and delete your database records.
You would normally only show these edit and delete buttons if the owner of those categories was the one viewing the page.
For example, if Bob added the Category of "Travel", and Bob is currently logged in to
his profile, then only Bob should be able to see these buttons.
That way, any guest other than Bob, such as Mary, would be able to see all categories,
but not have access to manipulate that data on the database.
This is why user authentication can be something to consider later, and there are several ways
to accomplish that on a project.
Now that I've mentioned both defensive programming and user authentication, it's finally time
to go ahead and delete one of these categories.
For this demonstration, I'm going to delete the category that we updated in the last video.
Go ahead and click on the Delete button for 'Miscellaneous'.
If everything is properly linked up, then the page should reload, and our category should
now be successfully deleted, which it is.
Wonderful, we now have the full CRUD functionality working perfectly.
Users can create new records, retrieve existing records, update records, and finally, they can now delete records.
We have made great progress on this application so far, but we still need to allow CRUD functionality for our Tasks model.
In the next lesson, we will allow users to create new Tasks.
For now though, go ahead and push your code to GitHub, and I'll see you on the next lesson.

# Lesson 9 Adding Tasks

Start of transcript. Skip to the end.
Now that we have full CRUD functionality set up for the Categories table, we need to start
building our CRUD functionality for our Tasks.
Let's start by opening the categories.html template, and copy the first row underneath
the h3, which is for the button to add a new category.
Then, open the existing tasks.html template, and let's paste that beneath that h3 header.
Go ahead and update the text to be "Add Task", and then update the function to match, "add_task".
This will also be the same URL that we apply to the navbar link, so open the base.html template.
Copy any of the existing url_for() methods from an existing href, and paste it into the link for 'New Task'.
Let's update that function to match the other file, which was "add_task", making sure to
also copy and paste that below into the sidenav as well.
Now, let's open up the routes.py file, and create this function that will render a new template for users to add a new Task.
It's actually quite similar to the 'add_category' function, so let's just copy the entire function,
and paste it as a brand new one at the bottom of the file.
Then, we can start updating the app route and function name to "add_task" instead of category.
If you recall from the video where we designed our database schema, each task actually requires
the user to select a category for that task.
In order to do that, we first need to extract a list of all of the categories available from the database.
We've previously done this on the 'categories' function, so go ahead and copy that line above,
and paste it before the POST method.
This time, however, we aren't going to be inserting a new category into the database, but rather a new task.
From our models.py file, each task must have a few different elements, including a task
name, description, due date, category, and whether or not it's urgent.
That means we need to update the POST method to reflect each of the fields that will be
added from the form that we will create shortly.
Make sure to separate each field with a comma at the end of the line, to signify the end of that particular field.
Task name will be set to the form's name attribute of 'task_name'.
Task description will use the form's 'task_description' field
The 'is_urgent' field will be a Boolean, either true or false, so we'll make it True if the
form data is toggled on, otherwise it will be set to False by default.
Due date will of course be the form's 'due_date' input box.
Then finally, the last column for each Task will be the selected Category ID, which will
be generated as a dropdown list to choose from, using the 'categories' list above.
Once the form is submitted, we can add that new 'task' variable to the database session,
and then immediately commit those changes to the database.
If successful, then we can redirect the user back to the 'home' page where each task will eventually be displayed.
That concludes the POST functionality when users add a new Task to the database.
If, however, the method isn't POST, and a user is trying to add a new task, they need
to be displayed with the page that contains the form.
This should render the template for "add_task.html", and in order for the dropdown list to display
each available category, we need to pass that variable into the template.
As a reminder, the first 'categories' listed is the variable name that we will be able
to use on the template itself.
The second 'categories' is simply the list of categories retrieved from the database defined above.
That's all we need for the 'add_task' function, which will render the template for new tasks,
and then commit those new tasks to the database if the form is submitted.
The next thing we need to do is build that template which allows users to add new tasks.
The easiest method for this, is to make a copy of the 'add_category.html' template,
and then rename the duplicate copy 'add_task.html'.
Let's update any instance of the word 'category' to 'task', which should be a total of about 8 places on this file.
If you'd like, you're welcome to change the icon to something different, as well as the
minimum and maximum values permitted for the Task Name.
The next required field for each task is the 'task_description', so copy the entire row
for the 'task_name' and paste it below that row.
Update any instance of 'task_name' to 'task_description', and since this will be a longer string of
text, let's modify this from an input to be a textarea instead.
Don't forget to add your closing /textarea to the end of the line as well.
I'm going to use a different icon for this field, and increase the maximum length to be 200 instead of 50.
This will also use the Materialize helper class of 'materialize-textarea' so that it
receives some custom styles using the framework.
If the lines are becoming too long, feel free to break them into two lines if needed.
The next field will be the 'due_date' of the task, so let's copy the entire row once again for the task name.
This time, however, instead of having users put a minimum or maximum value, we are going
to use another one of the Materialize helper classes called 'datepicker'.
Even though this is a standard input field, by using the 'datepicker' helper class, we
need to also initialize the datepicker using JavaScript.
From the Materialize documentation, let's copy the code snippet for the datepicker and
paste it into our custom JavaScript file.
I'm going to call this variable 'datepickers', and we can initialize that variable with some additional options.
Back on the Materialize site, you can see that they've got several options to include on the datepicker.
Let's keep this simple, so we are only going to include a few custom options.
First, we need to make sure that all tasks have a consistent date format, which uses the 'format' key.
For this project, I'm going to specify the date format of "dd mmmm, yyyy", which would
be for example, "01 February, 2024".
If you wanted, you could also include other options, such as the 'yearRange' to only show
3 years at a time, or the 'showClearBtn' as 'true'.
For demonstration purposes, I will also include the 'i18n' option, which itself will contain
a dictionary of elements.
The 'i18n' is the nickname given for 'internationalization' since there are 18 letters in the middle of
that word, starting with I and ending with N.
It allows programmers to customize text when dealing with foreign languages, if you want
the datepicker element to be translated into Gaelic or Klingon for example.
In this case, I'd like to change the text on the 'Done' button, instead of showing 'OK',
I want it to show 'Select'.
Using the list provided, you can change any of these, such as the months, dates, days of the week, etc.
We're almost done, we just have two more fields to add.
The next field is going to be a toggle, or switch, which will be for the database entry of 'is_urgent'.
For this one, copy the row for the task name once again, and update the text from task_name
to 'is_urgent' where applicable.
You can update the icon to something different, and remove the minimum and maximum fields.
Using the Materialize docs from the 'Switches' page, you can see that the toggle is wrapped
inside of a div with the class of 'switch', and uses the type of 'checkbox'.
Also, the input is physically inside of the label this time, and has a span with the class of 'lever'.
Since this is an optional field, either it's urgent or not, let's remove the class of validate,
and the 'required' attribute.
The final field will be for our dropdown list to select the category applicable to this task.
Back within the Materialize docs, navigate to the 'Select' page for forms, and we're
only going to focus on the basic dropdown element at the top.
You'll notice that it's similar to a standard select element, nothing too fancy here, so
I'm going to copy the task_name one more time, and adjust the required elements.
This will be for 'category_id', so we can adjust that throughout this row, and update the icon if desired.
Since this will be a select element, I'll update that to be select, making sure to include
the closing /select tag as well, and removing the min, max, and type attributes.
For the category options, we'll start with a basic option that is disabled and selected
by default, which reads 'Choose Category' displayed to the users.
Then, we need to create a Jinja for-loop over the list of all categories that are being
retrieved from the database.
{% for category in categories %} making sure to also include the {% endfor %} block.
For each category in this loop, we need to create a new 'option' in the dropdown.
The value for each option will be the category's unique ID, but obviously the ID won't make
much sense to our users, so we'll use the 'category.category_name' for display purposes.
If you recall, whenever submitting a form to the back-end, Python uses the name="" attribute
to grab the data being stored within the database.
For select elements, the actual data being stored is the value of the selected option,
which will be the category ID, whether it's 1, 2, 3, 4, and so on.
The final step we need to do for the dropdown to work, is to initialize it via JavaScript,
and that's because Materialize has a custom design for the select elements.
Copy the initialization code from their documentation, and paste it within your JavaScript file.
I'm going to call this variable 'selects' for any select element found, and then initialize those below.
That's it, everything should be ready now, so go ahead and save all of your files, and
start the application in your Terminal if it's not already running.
Click on the button or navbar link to add a new Task, and you should see all fields are now populated.
Due to the fact that we've already created the GET and POST methods on our function,
this form should fully work, and insert new tasks into the database.
Let's go ahead and add our first task now.
My task name will be 'Renew Passport', and the description will be 'Must renew at least
6 months prior to expiry'.
You can pick any random date in the future, and you'll notice that it's populated the
Materialize datepicker window.
Also, once you've selected the date, the format should match that of the format we've specified.
For demonstration purposes, I'm going to mark this as urgent, and for the category, I'm
going to use the option of 'Travel'.
Once finished, click on the button to add the new task.
Wonderful, the page submitted, and redirected me back to the Tasks page.
We haven't created any functionality to retrieve the tasks yet, however, if you look in the
terminal, you'll notice the green POST method with a status of 302.
This tells us that the POST method was successful, and redirected us back to the respective template.
In the next lesson, we are going to allow users to retrieve tasks from the database,
but using collapsibles instead of Materialize cards.
Feel free to add another task to the database if you'd like, and when you're ready, go ahead
and push your code to GitHub, and I'll see you on the next lesson.

# Lesson 10 Adding Tasks

Now that we have full CRUD functionality set up for the Categories table, we need to start
building our CRUD functionality for our Tasks.
Let's start by opening the categories.html template, and copy the first row underneath
the h3, which is for the button to add a new category.
Then, open the existing tasks.html template, and let's paste that beneath that h3 header.
Go ahead and update the text to be "Add Task", and then update the function to match, "add_task".
This will also be the same URL that we apply to the navbar link, so open the base.html template.
Copy any of the existing url_for() methods from an existing href, and paste it into the link for 'New Task'.
Let's update that function to match the other file, which was "add_task", making sure to
also copy and paste that below into the sidenav as well.
Now, let's open up the routes.py file, and create this function that will render a new
template for users to add a new Task.
It's actually quite similar to the 'add_category' function, so let's just copy the entire function,
and paste it as a brand new one at the bottom of the file.
Then, we can start updating the app route and function name to "add_task" instead of category.
If you recall from the video where we designed our database schema, each task actually requires
the user to select a category for that task.
In order to do that, we first need to extract a list of all of the categories available from the database.
We've previously done this on the 'categories' function, so go ahead and copy that line above,
and paste it before the POST method.
This time, however, we aren't going to be inserting a new category into the database, but rather a new task.
From our models.py file, each task must have a few different elements, including a task
name, description, due date, category, and whether or not it's urgent.
That means we need to update the POST method to reflect each of the fields that will be
added from the form that we will create shortly.
Make sure to separate each field with a comma at the end of the line, to signify the end of that particular field.
Task name will be set to the form's name attribute of 'task_name'.
Task description will use the form's 'task_description' field
The 'is_urgent' field will be a Boolean, either true or false, so we'll make it True if the
form data is toggled on, otherwise it will be set to False by default.
Due date will of course be the form's 'due_date' input box.
Then finally, the last column for each Task will be the selected Category ID, which will
be generated as a dropdown list to choose from, using the 'categories' list above.
Once the form is submitted, we can add that new 'task' variable to the database session,
and then immediately commit those changes to the database.
If successful, then we can redirect the user back to the 'home' page where each task will eventually be displayed.
That concludes the POST functionality when users add a new Task to the database.
If, however, the method isn't POST, and a user is trying to add a new task, they need
to be displayed with the page that contains the form.
This should render the template for "add_task.html", and in order for the dropdown list to display
each available category, we need to pass that variable into the template.
As a reminder, the first 'categories' listed is the variable name that we will be able
to use on the template itself.
The second 'categories' is simply the list of categories retrieved from the database defined above.
That's all we need for the 'add_task' function, which will render the template for new tasks,
and then commit those new tasks to the database if the form is submitted.
The next thing we need to do is build that template which allows users to add new tasks.
The easiest method for this, is to make a copy of the 'add_category.html' template,
and then rename the duplicate copy 'add_task.html'.
Let's update any instance of the word 'category' to 'task', which should be a total of about 8 places on this file.
If you'd like, you're welcome to change the icon to something different, as well as the
minimum and maximum values permitted for the Task Name.
The next required field for each task is the 'task_description', so copy the entire row
for the 'task_name' and paste it below that row.
Update any instance of 'task_name' to 'task_description', and since this will be a longer string of
text, let's modify this from an input to be a textarea instead.
Don't forget to add your closing /textarea to the end of the line as well.
I'm going to use a different icon for this field, and increase the maximum length to be 200 instead of 50.
This will also use the Materialize helper class of 'materialize-textarea' so that it
receives some custom styles using the framework.
If the lines are becoming too long, feel free to break them into two lines if needed.
The next field will be the 'due_date' of the task, so let's copy the entire row once again for the task name.
This time, however, instead of having users put a minimum or maximum value, we are going
to use another one of the Materialize helper classes called 'datepicker'.
Even though this is a standard input field, by using the 'datepicker' helper class, we
need to also initialize the datepicker using JavaScript.
From the Materialize documentation, let's copy the code snippet for the datepicker and
paste it into our custom JavaScript file.
I'm going to call this variable 'datepickers', and we can initialize that variable with some additional options.
Back on the Materialize site, you can see that they've got several options to include on the datepicker.
Let's keep this simple, so we are only going to include a few custom options.
First, we need to make sure that all tasks have a consistent date format, which uses the 'format' key.
For this project, I'm going to specify the date format of "dd mmmm, yyyy", which would
be for example, "01 February, 2024".
If you wanted, you could also include other options, such as the 'yearRange' to only show
3 years at a time, or the 'showClearBtn' as 'true'.
For demonstration purposes, I will also include the 'i18n' option, which itself will contain
a dictionary of elements.
The 'i18n' is the nickname given for 'internationalization' since there are 18 letters in the middle of
that word, starting with I and ending with N.
It allows programmers to customize text when dealing with foreign languages, if you want
the datepicker element to be translated into Gaelic or Klingon for example.
In this case, I'd like to change the text on the 'Done' button, instead of showing 'OK',
I want it to show 'Select'.
Using the list provided, you can change any of these, such as the months, dates, days of the week, etc.
We're almost done, we just have two more fields to add.
The next field is going to be a toggle, or switch, which will be for the database entry of 'is_urgent'.
For this one, copy the row for the task name once again, and update the text from task_name
to 'is_urgent' where applicable.
You can update the icon to something different, and remove the minimum and maximum fields.
Using the Materialize docs from the 'Switches' page, you can see that the toggle is wrapped
inside of a div with the class of 'switch', and uses the type of 'checkbox'.
Also, the input is physically inside of the label this time, and has a span with the class of 'lever'.
Since this is an optional field, either it's urgent or not, let's remove the class of validate,
and the 'required' attribute.
The final field will be for our dropdown list to select the category applicable to this task.
Back within the Materialize docs, navigate to the 'Select' page for forms, and we're
only going to focus on the basic dropdown element at the top.
You'll notice that it's similar to a standard select element, nothing too fancy here, so
I'm going to copy the task_name one more time, and adjust the required elements.
This will be for 'category_id', so we can adjust that throughout this row, and update the icon if desired.
Since this will be a select element, I'll update that to be select, making sure to include
the closing /select tag as well, and removing the min, max, and type attributes.
For the category options, we'll start with a basic option that is disabled and selected
by default, which reads 'Choose Category' displayed to the users.
Then, we need to create a Jinja for-loop over the list of all categories that are being
retrieved from the database.
{% for category in categories %} making sure to also include the {% endfor %} block.
For each category in this loop, we need to create a new 'option' in the dropdown.
The value for each option will be the category's unique ID, but obviously the ID won't make
much sense to our users, so we'll use the 'category.category_name' for display purposes.
If you recall, whenever submitting a form to the back-end, Python uses the name="" attribute
to grab the data being stored within the database.
For select elements, the actual data being stored is the value of the selected option,
which will be the category ID, whether it's 1, 2, 3, 4, and so on.
The final step we need to do for the dropdown to work, is to initialize it via JavaScript,
and that's because Materialize has a custom design for the select elements.
Copy the initialization code from their documentation, and paste it within your JavaScript file.
I'm going to call this variable 'selects' for any select element found, and then initialize those below.
That's it, everything should be ready now, so go ahead and save all of your files, and
start the application in your Terminal if it's not already running.
Click on the button or navbar link to add a new Task, and you should see all fields are now populated.
Due to the fact that we've already created the GET and POST methods on our function,
this form should fully work, and insert new tasks into the database.
Let's go ahead and add our first task now.
My task name will be 'Renew Passport', and the description will be 'Must renew at least
6 months prior to expiry'.
You can pick any random date in the future, and you'll notice that it's populated the
Materialize datepicker window.
Also, once you've selected the date, the format should match that of the format we've specified.
For demonstration purposes, I'm going to mark this as urgent, and for the category, I'm
going to use the option of 'Travel'.
Once finished, click on the button to add the new task.
Wonderful, the page submitted, and redirected me back to the Tasks page.
We haven't created any functionality to retrieve the tasks yet, however, if you look in the
terminal, you'll notice the green POST method with a status of 302.
This tells us that the POST method was successful, and redirected us back to the respective template.
In the next lesson, we are going to allow users to retrieve tasks from the database,
but using collapsibles instead of Materialize cards.
Feel free to add another task to the database if you'd like, and when you're ready, go ahead
and push your code to GitHub, and I'll see you on the next lesson.

from taskmanager import db
# in the last lessons we had to manualy import
# integer float string etc each column type at the top of
# the file.  with Flask-Sql-Alchemy the db variable contains them 
# so we can use dot notation for the collumns


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    # above is the first column of the table, the id
    # column.  it is an integer with the pimary key = True
    # this will auto increment each new record on the table
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    # above the category of name, a string with 25 charactors. we want to make 
    # sure that each new category is unique so that is set to true, 
    # nullable=False ensures it can't be left blank
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)
    # this does not show because its a task not a category.  it creates a
    # relationship between the tables. it targets task in quotes and backref
    # itself to establish a bidirectional relationship. cascade all delete
    # finds all related tasks and deletes them

    # below we need to creat a function called repr that takes
    # self as an argument.  Similar to the this keyword in js
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category_name


class Task(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    # here we have used .Text instad of string as this will allow for
    # a larger area of text like a text area verses an input
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    # if you needed to include a date on the database db.DateTime or 
    # db.Time would be fine.
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)
    # This column as a foreign key that connects our tables. it needs to point to 
    # the specific category in this case our category.id from the other table in quotes.
    # ondelete cascade means id the categoet id is deleted it will delete the task linked to it.
    # an error would occur otherwise
    
    # below we need to creat a function called repr that takes 
    # self as an argument.  Similar to the this keyword in js
    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )
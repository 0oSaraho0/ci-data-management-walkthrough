import os
from taskmanager import app

# Here we are telling our application how and 
# where to run the application . checking the name
# class is equal to the main struing wrapped in double
# underscores and quotes.  If it is a match then we 
# need to have our app running wich takes 3 arguements
# host port and debug. these are stored in the environment
# variables so we use environ.get
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG")
    )
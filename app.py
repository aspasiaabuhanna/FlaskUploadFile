import os

from flask import *

# define a flask app
app = Flask(__name__)
#defining the app_root of this application, we get the string or file path of our application
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

#defining routes, use the route to tell flask what URL should trigger our function
#this is the base route
@app.route("/")
def index():
    # return what will be displayed in the user's browsers
    #render template will render the html file passed as an argument
    #create upload.html in template folder
    return render_template("upload.html")


#in the function upload we will define the necessary mechanism
@app.route("/upload", methods=["POST"])
def upload():
    # upload_file is the folder we want to store our files in
    target = os.path.join(APP_ROOT, 'upload_file/')
    print(target) #for debugging purpose

    if not os.path.isdir(target):
        os.mkdir(target)
    print(request.files.getlist("file"))

        
    for file in request.files.getlist("file"):
        print(file)
        print("{} is the file name".format(file.filename))
        filename = file.filename
        #set a destination, for server to upload this specific file to this location with specific name 
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        #to save file
        file.save(destination)

    # add complete.html to templates folder
    return render_template("complete.html", file_name =filename)

#to make sure that the app runs when it is called on its own
if __name__ == "__main__":
    app.run(debug=True)

import os

from flask import *

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():

    target = os.path.join(APP_ROOT, 'upload_file/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)
    print(request.files.getlist("file"))

    for file in request.files.getlist("file"):
        print(file)
        print("{} is the file name".format(file.filename))
        filename = file.filename
        destination = "/".join([target, filename])
        print("Accept incoming file:", filename)
        print("Save it to:", destination)
        file.save(destination)

    # return send_from_directory("file", filename, as_attachment=True)
    return render_template("complete.html", file_name =filename)


if __name__ == "__main__":
    app.run(debug=True)
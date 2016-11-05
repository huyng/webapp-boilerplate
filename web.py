import sys
import os.path as pth

from flask import Flask
from flask import make_response
from flask import request
from flask import render_template
from flask import send_file
from flask import send_from_directory

app = Flask(__name__,
            static_folder="ui/dist",
            static_url_path="/static")


@app.route("/")
def index_page():
    return send_file("ui/index.html")


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8889)







# =======================================



# register additional static paths
# blueprint = Blueprint('site', __name__, static_url_path='/static/site', static_folder='path/to/files')
# app.register_blueprint(blueprint)

# safely send file with user generated string
# @app.route("/photos/fname.jpg")
# def photo_files(fname):
#     return send_from_directory(dpath, fname)

# send  any file
# @app.route("/photos/fname.jpg")
# def photo_files(fname):
#     return send_file(fname)

# @app.route("/images/view/")
# def image_view():
#     img_id = request.args.get("img_id").strip()
#     print img_id
#     rec = rdd.lookup(img_id)
#     response = make_response(rec[0].decode("base64"))
#     response.headers['Content-Type'] = 'image/jpeg'
#     return response

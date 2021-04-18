import os
from flask import Blueprint, render_template, request, url_for, abort, send_from_directory
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from . import db, create_app

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


def allowed_image(filename):

    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    return ext in app.config['UPLOAD_EXTENSIONS']

@main.route('/upload_image', methods=['GET', 'POST'])
@login_required
def upload_image():

    if request.method == 'POST':
        if request.files:
            image = request.files['file']
            
            if image.filename == '':
                return redirect(request.url)

            if allowed_image(image.filename):
                print (image.filename)
                filename = secure_filename(image.filename)
                return redirect(request.url)
        else:
            print ("No image found")

    return render_template('upload_image.html')

@main.route('/choice')
@login_required
def choice():
    return render_template('choice.html')

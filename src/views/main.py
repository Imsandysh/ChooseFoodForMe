import os
from flask import Blueprint, render_template, request, url_for, abort, send_from_directory
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from . import db, create_app

main = Blueprint('main', __name__)
app = create_app()

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/upload_image')
@login_required
def upload():
    return render_template('upload_image.html')

@main.route('/upload_image', methods=['POST'])
@login_required
def upload_image():    
    uploaded_image = request.files['file']
    print (uploaded_image)
    filename = secure_filename(upload_image.filename)
    print (filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        # uploaded_image.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    
    return redirect(url_for('upload'))
from flask import Blueprint,render_template,request,flash,jsonify
# import methods to check user session exist
from flask_login import current_user,login_required
#import note model
from .models import Note 
import json
from . import db

views = Blueprint("views",__name__)

# define routes for views

@views.route("/",methods=["GET","POST"])
@login_required
def home():
    if request.method == 'POST':
        str_note = request.form.get('note')
        print(f"---------------${str_note}:============${current_user.id}")
        if len(str_note.strip()) < 1:
            flash("NOTE_IS_TOO_SHORT",category="error")
        else:
            new_note = Note(data=str_note,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            print("NOTE_ADDED_SUCCESSFULLY")
            flash("NOTE_ADDED_SUCCESSFULLY",category='success')
    return render_template("home.html",user = current_user)


# delete note 
 
@views.route("/delete_note",methods=["POST"])
@login_required
def delete_note():
    data = json.loads(request.data)
    note_id = data['noteId']
    note = Note.query.get(note_id)
    if note and  note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})
    
    
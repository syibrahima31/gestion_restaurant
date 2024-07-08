from flask import Blueprint, render_template, request, flash , redirect, url_for, abort
from gestion_restaurant.models import User, Role  
from gestion_restaurant import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import  login_user, logout_user, current_user, login_required


admin_bp = Blueprint('admin', __name__, template_folder="templates", url_prefix="/admin")



@admin_bp.route("/admin")
@login_required
def dashboard(): 
    if current_user.role != Role.ADMIN:
        abort(401)
    return render_template("admin/admin.html")
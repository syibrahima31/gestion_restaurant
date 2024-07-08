from flask import Blueprint, render_template, request, flash , redirect, url_for, abort
from gestion_restaurant.models import User, Role  
from gestion_restaurant import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import  login_user, logout_user, current_user, login_required


auth_bp = Blueprint('auth', __name__, template_folder="templates", url_prefix="/auth")


@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

@auth_bp.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST": 
        email  = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            flash("connexion etablie")
            login_user(user)
            return redirect(url_for("menu.index"))
        else: 
            flash("Erreur de connexion")
            return redirect(url_for("auth.login"))
    return render_template("auth/login.html")

@auth_bp.route("/logout")
@login_required
def logout():  
    logout_user()
    return redirect(url_for('auth.login'))



@auth_bp.route("/register", methods=["POST", "GET"])
def register(): 
    if request.method == "POST": 
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        comfirm_password = request.form.get("confirm_password")

        if comfirm_password == password:
            user = User.query.filter_by(nom=username).first()
            if user: 
                flash("user exite deja")
                return redirect(url_for('auth.register'))
            else: 
                new_user = User(nom=username, email=email, password=generate_password_hash(password))
                db.session.add(new_user)
                db.session.commit()
                flash("user avec succes")
                return redirect(url_for('auth.login'))
        else: 
            print(password==comfirm_password)
            flash("Erreur saisi le meme mot de passe")
            return redirect(url_for("auth.register"))

    return render_template("auth/register.html")


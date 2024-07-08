from flask import Blueprint, render_template, request, session, redirect, url_for, abort
from gestion_restaurant.models import Menu, Plat, Role 
from gestion_restaurant import db 
from flask_login import login_required, current_user


menu_bp = Blueprint("menu", __name__, template_folder="templates", static_folder="static", url_prefix="/menu")

@menu_bp.route("/")
def index():
    menus = Menu.query.all()
    return render_template("menu/menu.html", menus=menus)

@menu_bp.route("/recherche", methods=["GET"])
def recherche_menus():
    criteres = request.args.get("criteres", "")
    if criteres.isdigit():
        # Si criteres est un nombre, on filtre aussi par le prix
        criteres_prix = float(criteres)
        menu_filtered = Menu.query.filter(
            (Menu.nom.ilike(f"%{criteres}%")) |
            (Menu.description.ilike(f"%{criteres}%")) |
            (Menu.prix < criteres_prix)
        ).all()
    else:
        # Sinon, on ne filtre que par nom et description
        menu_filtered = Menu.query.filter(
            (Menu.nom.ilike(f"%{criteres}%")) |
            (Menu.description.ilike(f"%{criteres}%"))
        ).all()

    return render_template("menu/menu.html", menus=menu_filtered, criteres=criteres)

@menu_bp.route("/detials/<int:menu_id>")
def details(menu_id):
    menu = db.get_or_404(Menu, menu_id)
    return render_template("menu/menu_details.html", plats=menu.plats, menu=menu)

@menu_bp.route('/ajoutpanier/<int:menu_id>', methods=["GET", "POST"])
@login_required
def ajout_panier(menu_id):
    quantite = int(request.form.get("quantite", 1))
    panier = session.get("panier", {})

    menu_id = str(menu_id)
    if menu_id in panier: 
        panier[menu_id] += quantite
    else: 
        panier[menu_id] = quantite
    
    session["panier"] = panier
   
    return redirect(url_for('menu.index'))
 
@menu_bp.route("/panier")
@login_required
def affiche_panier(): 
    panier = session.get("panier", {})
    articles = []

    for meunu_id, quantite in panier.items():
        menu = db.get_or_404(Menu, int(meunu_id))
        if menu: 
            articles.append({"menu":menu, "quantite":quantite})
    return render_template("cart.html", articles=articles)

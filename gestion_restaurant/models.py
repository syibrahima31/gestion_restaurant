from . import db 
from flask_login import UserMixin

class Role: 
    ADMIN  = 1 
    CLIENT = 2 
    USER = 3 



class User(db.Model, UserMixin): 
    id  = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    role = db.Column(db.Integer,  unique=True, default=Role.USER)
    password = db.Column(db.String)
    commandes = db.relationship('Commande', backref='user', lazy=True)

commande_plat = db.Table(
    "commande_plat",
    db.Column("commande_id", db.Integer, db.ForeignKey("commande.id")),
    db.Column("plat_id", db.Integer, db.ForeignKey("plat.id")),
)


class Commande(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    total = db.Column(db.String)
    statut = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    plats  = db.relationship("Plat", secondary=commande_plat, back_populates="commandes")
    
class Plat(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String)
    ingredients = db.Column(db.String)
    prix = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    menu_id = db.Column(db.Integer, db.ForeignKey('menu.id'),
        nullable=False)
    commandes  = db.relationship("Commande", secondary=commande_plat, back_populates="plats")
    menu = db.relationship('Menu', back_populates='plats')
    

class Menu(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String)
    description = db.Column(db.String(300))
    prix = db.Column(db.Float)
    disponibilite = db.Column(db.Boolean)
    plats = db.relationship('Plat', back_populates='menu', lazy=True)
    






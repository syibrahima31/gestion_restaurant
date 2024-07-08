from gestion_restaurant import create_app
from gestion_restaurant.models import db, Menu, Plat

def insert_menus_and_plats():
    # Création des menus
    menus = [
        Menu(nom='Menu Italien', description='Pâtes fraîches et pizzas artisanales', prix=25.99, disponibilite=True),
        Menu(nom='Menu Asiatique', description='Sushis, ramen et plats sautés', prix=30.50, disponibilite=True),
        Menu(nom='Menu Français', description='Escargots, coq au vin et baguettes', prix=40.00, disponibilite=True),
        Menu(nom='Menu Mexicain', description='Tacos, burritos et quesadillas', prix=20.75, disponibilite=True),
        Menu(nom='Menu Indien', description='Curry, naan et riz basmati', prix=22.50, disponibilite=True),
        Menu(nom='Menu Américain', description='Burgers, frites et milkshakes', prix=18.99, disponibilite=True),
        Menu(nom='Menu Méditerranéen', description='Salades, houmous et falafels', prix=24.00, disponibilite=True),
        Menu(nom='Menu Thaï', description='Pad thaï, curry vert et rouleaux de printemps', prix=28.00, disponibilite=True),
        Menu(nom='Menu Végétarien', description='Plats végétariens variés et savoureux', prix=19.99, disponibilite=True),
        Menu(nom='Menu de la Mer', description='Poissons et fruits de mer frais', prix=35.00, disponibilite=True),
    ]

    db.session.bulk_save_objects(menus)
    db.session.commit()

    menus_dict = {menu.nom: menu for menu in Menu.query.all()}

    # Exemple de user_id, vous devez remplacer par un ID valide existant dans votre base de données
    user_id = 1

    plats = [
        Plat(nom='Pâtes Carbonara', ingredients='Pâtes, oeuf, lardons, parmesan', prix=12.50, menu=menus_dict['Menu Italien'], user_id=user_id),
        Plat(nom='Pizza Margherita', ingredients='Tomate, mozzarella, basilic', prix=13.00, menu=menus_dict['Menu Italien'], user_id=user_id),
        Plat(nom='Sushis', ingredients='Riz, poisson, algue', prix=15.00, menu=menus_dict['Menu Asiatique'], user_id=user_id),
        Plat(nom='Ramen', ingredients='Nouilles, bouillon, porc', prix=12.00, menu=menus_dict['Menu Asiatique'], user_id=user_id),
        Plat(nom='Escargots', ingredients='Escargots, beurre, persil', prix=20.00, menu=menus_dict['Menu Français'], user_id=user_id),
        Plat(nom='Coq au Vin', ingredients='Poulet, vin rouge, champignons', prix=25.00, menu=menus_dict['Menu Français'], user_id=user_id),
        Plat(nom='Tacos', ingredients='Tortilla, boeuf, légumes', prix=10.00, menu=menus_dict['Menu Mexicain'], user_id=user_id),
        Plat(nom='Burritos', ingredients='Tortilla, riz, haricots', prix=11.00, menu=menus_dict['Menu Mexicain'], user_id=user_id),
        Plat(nom='Poulet Tikka Masala', ingredients='Poulet, sauce tomate, épices', prix=14.00, menu=menus_dict['Menu Indien'], user_id=user_id),
        Plat(nom='Naan', ingredients='Farine, yaourt, levure', prix=4.00, menu=menus_dict['Menu Indien'], user_id=user_id),
        Plat(nom='Cheeseburger', ingredients='Boeuf, fromage, pain', prix=10.00, menu=menus_dict['Menu Américain'], user_id=user_id),
        Plat(nom='Frites', ingredients='Pommes de terre, huile', prix=3.00, menu=menus_dict['Menu Américain'], user_id=user_id),
        Plat(nom='Salade Grecque', ingredients='Tomates, concombre, feta', prix=8.00, menu=menus_dict['Menu Méditerranéen'], user_id=user_id),
        Plat(nom='Houmous', ingredients='Pois chiches, tahini, ail', prix=6.00, menu=menus_dict['Menu Méditerranéen'], user_id=user_id),
        Plat(nom='Pad Thaï', ingredients='Nouilles, crevettes, cacahuètes', prix=15.00, menu=menus_dict['Menu Thaï'], user_id=user_id),
        Plat(nom='Curry Vert', ingredients='Poulet, lait de coco, épices', prix=13.00, menu=menus_dict['Menu Thaï'], user_id=user_id),
        Plat(nom='Ratatouille', ingredients='Légumes, huile d\'olive, herbes', prix=10.00, menu=menus_dict['Menu Végétarien'], user_id=user_id),
        Plat(nom='Tofu Sauté', ingredients='Tofu, légumes, sauce soja', prix=9.00, menu=menus_dict['Menu Végétarien'], user_id=user_id),
        Plat(nom='Saumon Grillé', ingredients='Saumon, citron, herbes', prix=20.00, menu=menus_dict['Menu de la Mer'], user_id=user_id),
        Plat(nom='Crevettes à l\'ail', ingredients='Crevettes, ail, beurre', prix=15.00, menu=menus_dict['Menu de la Mer'], user_id=user_id)
    ]

    for plat in plats:
        db.session.add(plat)
    
    db.session.commit()
    print("Menus et plats fictifs insérés avec succès")

if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        insert_menus_and_plats()

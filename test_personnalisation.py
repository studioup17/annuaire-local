"""
Script de test pour vérifier la personnalisation des textes
"""

from config import (
    BREADCRUMB_HOME_TEXT,
    WHY_CHOOSE_TITLE,
    WHY_CHOOSE_BLOCKS,
    ZONE_TITLE,
    ZONE_DESCRIPTION,
    GEOGRAPHIC_ZONES,
    COVERAGE_TYPES
)

def test_personnalisation():
    print("=" * 60)
    print("TEST DE PERSONNALISATION DES TEXTES")
    print("=" * 60)
    print()

    # Test 1 : Fil d'ariane
    print("[1] Fil d'ariane (Breadcrumb)")
    print(f"   Texte : {BREADCRUMB_HOME_TEXT}")
    print()

    # Test 2 : Section "Pourquoi nous choisir"
    print("[2] Section 'Pourquoi nous choisir'")
    print(f"   Titre : {WHY_CHOOSE_TITLE}")
    print(f"   Nombre de blocs : {len(WHY_CHOOSE_BLOCKS)}")
    for i, block in enumerate(WHY_CHOOSE_BLOCKS, 1):
        print(f"   Bloc {i}:")
        print(f"      - Titre : {block['title']}")
        print(f"      - Description : {block['description']}")
        print(f"      - Icone : {block['icon']}")
        print(f"      - Couleur : {block['color']}")
    print()

    # Test 3 : Zone d'intervention
    print("[3] Zone d'intervention")
    print(f"   Titre : {ZONE_TITLE}")
    print(f"   Description : {ZONE_DESCRIPTION}")
    print()

    # Test 4 : Zones géographiques
    print("[4] Zones geographiques")
    print(f"   Nombre de zones : {len(GEOGRAPHIC_ZONES)}")
    for i, zone in enumerate(GEOGRAPHIC_ZONES, 1):
        print(f"   Zone {i}:")
        print(f"      - Titre : {zone['title']}")
        print(f"      - Description : {zone['description']}")
        try:
            print(f"      - Icone : {zone['icon']}")
        except:
            print(f"      - Icone : [emoji]")
    print()

    # Test 5 : Types de communes
    print("[5] Types de communes")
    print(f"   Nombre de types : {len(COVERAGE_TYPES)}")
    for i, coverage in enumerate(COVERAGE_TYPES, 1):
        print(f"   Type {i}:")
        print(f"      - Titre : {coverage['title']}")
        print(f"      - Description : {coverage['description']}")
        try:
            print(f"      - Icone : {coverage['icon']}")
        except:
            print(f"      - Icone : [emoji]")
    print()

    # Résumé
    print("=" * 60)
    print("RESULTAT")
    print("=" * 60)
    print("[OK] Toutes les variables sont correctement chargees !")
    print()
    print("Pour appliquer ces changements sur le site :")
    print("   1. Ctrl + C (arreter l'application)")
    print("   2. python app.py (relancer)")
    print("   3. F5 (rafraichir le navigateur)")
    print("=" * 60)

if __name__ == "__main__":
    test_personnalisation()

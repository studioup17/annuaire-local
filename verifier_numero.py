#!/usr/bin/env python3
"""
Script de vérification du numéro de téléphone
Vérifie que le bon numéro est configuré et affiché partout
"""

from config import PHONE_NUMBER, PHONE_NUMBER_RAW
from content_generator import ContentGenerator

def test_numero():
    print("=" * 60)
    print("VERIFICATION DU NUMERO DE TELEPHONE")
    print("=" * 60)
    print()

    # 1. Vérifier la configuration
    print("[1] Configuration (config.py)")
    print(f"   PHONE_NUMBER: {PHONE_NUMBER}")
    print(f"   PHONE_NUMBER_RAW: {PHONE_NUMBER_RAW}")
    print()

    # 2. Vérifier le générateur de contenu
    print("[2] Generateur de contenu")
    generator = ContentGenerator()

    # Simuler une commune
    test_commune = {
        'nom_commune': 'Bordeaux',
        'code_postal': '33000',
        'category': 'plombier'
    }

    content = generator.generate_content(test_commune)

    # Vérifier si le numéro apparaît dans la conclusion
    conclusion = content['conclusion']
    if PHONE_NUMBER in conclusion:
        print(f"   [OK] Le numero {PHONE_NUMBER} apparait dans la conclusion")
        print(f"   Extrait: ...{conclusion[conclusion.find(PHONE_NUMBER)-20:conclusion.find(PHONE_NUMBER)+30]}...")
    else:
        print(f"   [ERREUR] Le numero {PHONE_NUMBER} N'apparait PAS dans la conclusion")
        print(f"   Conclusion: {conclusion}")
    print()

    # 3. Résumé
    print("=" * 60)
    print("RESUME")
    print("=" * 60)
    if PHONE_NUMBER in conclusion:
        print("[OK] Tout est OK ! Le numero est correctement configure.")
        print(f"[OK] Votre numero {PHONE_NUMBER} s'affichera partout.")
    else:
        print("[ERREUR] PROBLEME DETECTE !")
        print("[ERREUR] Le numero ne s'affiche pas dans le contenu genere.")
        print()
        print("SOLUTION:")
        print("   1. Arretez l'application (Ctrl+C)")
        print("   2. Relancez: python app.py")
        print("   3. Rafraichissez le navigateur (F5)")
    print("=" * 60)

if __name__ == "__main__":
    test_numero()

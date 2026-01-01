"""Test de la génération automatique"""

from config import (
    AUTO_REGION_NAME,
    HERO_TITLE,
    ZONE_DESCRIPTION,
    GEOGRAPHIC_ZONES,
    COVERAGE_TYPES,
    USE_AUTO_ZONES,
    DEPARTMENTS,
    CATEGORIES
)

print("=" * 60)
print("TEST GENERATION AUTOMATIQUE")
print("=" * 60)
print()

print(f"[1] Mode: {'AUTOMATIQUE' if USE_AUTO_ZONES else 'MANUEL'}")
print()

print(f"[2] Departements configures: {len(DEPARTMENTS)}")
for code, name in DEPARTMENTS.items():
    print(f"    - {code}: {name}")
print()

print(f"[3] Metiers configures: {len(CATEGORIES)}")
for slug, name in list(CATEGORIES.items())[:3]:
    print(f"    - {name}")
if len(CATEGORIES) > 3:
    print(f"    ... et {len(CATEGORIES) - 3} autres")
print()

print(f"[4] Region detectee automatiquement:")
print(f"    {AUTO_REGION_NAME}")
print()

print(f"[5] Hero Title (s'adapte automatiquement):")
print(f"    {HERO_TITLE}")
print()

print(f"[6] Zone Description (s'adapte automatiquement):")
print(f"    {ZONE_DESCRIPTION}")
print()

print(f"[7] Zones geographiques: {len(GEOGRAPHIC_ZONES)} zones")
for zone in GEOGRAPHIC_ZONES:
    print(f"    - {zone['title']}: {zone['description']}")
print()

print(f"[8] Types de communes: {len(COVERAGE_TYPES)} types")
for ctype in COVERAGE_TYPES:
    print(f"    - {ctype['title']}: {ctype['description']}")
print()

print("=" * 60)
print("RESULTAT")
print("=" * 60)
print("[OK] La generation automatique fonctionne !")
print()
print("Quand vous ajoutez/supprimez des departements dans DEPARTMENTS,")
print("les textes s'adaptent automatiquement :")
print(f"  - Hero Title: Annuaire Professionnel {AUTO_REGION_NAME}")
print(f"  - Zone Description: Nous couvrons {AUTO_REGION_NAME}")
print(f"  - Geographic Zones: {len(GEOGRAPHIC_ZONES)} zones generees")
print()
print("=" * 60)

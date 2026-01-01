# 🤖 Adaptation Automatique des Textes

## ✨ Nouveauté : Tout s'adapte automatiquement !

Votre site s'adapte maintenant **automatiquement** en fonction des départements et métiers que vous configurez dans `config.py`.

---

## 🎯 Ce Qui S'Adapte Automatiquement

### 1. Nom de la Région

**Détecté automatiquement** depuis vos départements configurés !

```python
# Vous configurez ces départements :
DEPARTMENTS = {
    '16': 'Charente',
    '17': 'Charente-Maritime',
    '79': 'Deux-Sèvres',
    '86': 'Vienne',
}

# ✅ Le système détecte automatiquement : "Nouvelle-Aquitaine"
```

**Exemples :**
- Départements 75, 77, 78, 91, 92, 93, 94, 95 → "Île-de-France"
- Départements 06, 13, 83, 84 → "Provence-Alpes-Côte d'Azur"
- Départements 59, 62, 80 → "Hauts-de-France"
- Départements de plusieurs régions → "Nouvelle-Aquitaine et Occitanie"

---

### 2. Titre de la Page d'Accueil (HERO_TITLE)

**S'adapte automatiquement** à votre région !

```python
# Avant (manuel) :
HERO_TITLE = "Annuaire Professionnel du Sud-Est"

# ✅ Maintenant (automatique) :
HERO_TITLE = f"Annuaire Professionnel {AUTO_REGION_NAME}"
# Résultat : "Annuaire Professionnel Nouvelle-Aquitaine"
```

**Changez vos départements → Le titre change automatiquement !**

Exemples :
- Si vous activez Paris (75) → "Annuaire Professionnel Île-de-France"
- Si vous activez Nice (06) → "Annuaire Professionnel Provence-Alpes-Côte d'Azur"

---

### 3. Description Zone d'Intervention (ZONE_DESCRIPTION)

**S'adapte automatiquement** à votre région !

```python
# ✅ Automatique :
ZONE_DESCRIPTION = f"Nous couvrons l'ensemble de la région {AUTO_REGION_NAME}"
# Résultat : "Nous couvrons l'ensemble de la région Nouvelle-Aquitaine"
```

**Changez vos départements → La description change automatiquement !**

---

### 4. Zones Géographiques (GEOGRAPHIC_ZONES)

**Générées automatiquement** depuis vos départements !

```python
# Vous activez :
DEPARTMENTS = {
    '16': 'Charente',
    '17': 'Charente-Maritime',
    '79': 'Deux-Sèvres',
    '86': 'Vienne',
}

# ✅ Le système génère automatiquement :
GEOGRAPHIC_ZONES = [
    {
        'title': 'Charente & Charente-Maritime',
        'icon': '📍',
        'description': 'Tous les professionnels de Charente et Charente-Maritime'
    },
    {
        'title': 'Deux-Sèvres & Vienne',
        'icon': '📍',
        'description': 'Tous les professionnels de Deux-Sèvres et Vienne'
    }
]
```

**Les départements sont groupés par 2 automatiquement !**

---

### 5. Liste des Métiers (Hero Section)

**Générée automatiquement** depuis CATEGORIES !

```python
# Vous configurez :
CATEGORIES = {
    'graphiste': 'Graphiste',
    'web-designer': 'Web Designer',
    'illustrateur': 'Illustrateur'
}

# ✅ Affichage automatique sur la page d'accueil :
# "Graphiste, Web Designer, Illustrateur - Plus de 1234 communes référencées"
```

**Ajoutez un métier → Il apparaît automatiquement dans la liste !**

---

## 🔧 Comment Ça Fonctionne ?

### Mode Automatique (par défaut)

Dans `config.py` ligne 57 :

```python
USE_AUTO_ZONES = True  # ✅ Mode automatique activé
```

**En mode automatique :**
- ✅ `HERO_TITLE` s'adapte à vos départements
- ✅ `ZONE_DESCRIPTION` s'adapte à vos départements
- ✅ `GEOGRAPHIC_ZONES` générées depuis vos départements
- ✅ `COVERAGE_TYPES` générés automatiquement
- ✅ Liste des métiers générée depuis CATEGORIES

---

### Mode Manuel (si vous préférez personnaliser)

```python
USE_AUTO_ZONES = False  # Mode manuel
```

**En mode manuel :**
- Vous personnalisez `GEOGRAPHIC_ZONES_MANUAL`
- Vous personnalisez `COVERAGE_TYPES_MANUAL`
- Mais `HERO_TITLE` et `ZONE_DESCRIPTION` restent automatiques

---

## 🎯 Exemples Concrets

### Exemple 1 : Vous Passez de Nouvelle-Aquitaine à Île-de-France

**Avant :**
```python
DEPARTMENTS = {
    '16': 'Charente',
    '17': 'Charente-Maritime',
}
```
Résultat :
- HERO_TITLE : "Annuaire Professionnel Nouvelle-Aquitaine"
- ZONE_DESCRIPTION : "Nous couvrons l'ensemble de la région Nouvelle-Aquitaine"
- GEOGRAPHIC_ZONES : 1 zone (Charente & Charente-Maritime)

**Après :**
```python
DEPARTMENTS = {
    '75': 'Paris',
    '92': 'Hauts-de-Seine',
    '93': 'Seine-Saint-Denis',
    '94': 'Val-de-Marne',
}
```
Résultat automatique :
- ✅ HERO_TITLE : "Annuaire Professionnel Île-de-France"
- ✅ ZONE_DESCRIPTION : "Nous couvrons l'ensemble de la région Île-de-France"
- ✅ GEOGRAPHIC_ZONES : 2 zones auto-générées

**Aucune autre modification nécessaire !**

---

### Exemple 2 : Vous Ajoutez des Métiers

**Avant :**
```python
CATEGORIES = {
    'plombier': 'Plombier',
    'électricien': 'Électricien',
}
```
Liste affichée : "Plombier, Électricien - Plus de 1234 communes"

**Après :**
```python
CATEGORIES = {
    'plombier': 'Plombier',
    'électricien': 'Électricien',
    'serrurier': 'Serrurier',
    'chauffagiste': 'Chauffagiste',
}
```
Liste affichée automatiquement : "Plombier, Électricien, Serrurier, Chauffagiste - Plus de 1234 communes"

**Aucune autre modification nécessaire !**

---

### Exemple 3 : Vous Couvrez Plusieurs Régions

```python
DEPARTMENTS = {
    '16': 'Charente',        # Nouvelle-Aquitaine
    '17': 'Charente-Maritime', # Nouvelle-Aquitaine
    '31': 'Haute-Garonne',   # Occitanie
    '34': 'Hérault',         # Occitanie
}
```

Résultat automatique :
- ✅ HERO_TITLE : "Annuaire Professionnel Nouvelle-Aquitaine et Occitanie"
- ✅ ZONE_DESCRIPTION : "Nous couvrons l'ensemble de la région Nouvelle-Aquitaine et Occitanie"
- ✅ GEOGRAPHIC_ZONES : 2 zones auto-générées

---

## 🧪 Tester l'Adaptation Automatique

### Script de Test

```bash
python test_auto_generation.py
```

Ce script affiche :
- ✅ Mode (Automatique ou Manuel)
- ✅ Départements configurés
- ✅ Métiers configurés
- ✅ Région détectée automatiquement
- ✅ Hero Title généré
- ✅ Zone Description générée
- ✅ Zones géographiques générées

---

## 📝 Que Devez-Vous Configurer ?

### Obligatoire

**1. Départements (ligne 279)**
```python
DEPARTMENTS = {
    '16': 'Charente',
    '17': 'Charente-Maritime',
    # ... ajoutez vos départements
}
```

**2. Métiers (ligne 123)**
```python
CATEGORIES = {
    'plombier': 'Plombier',
    'électricien': 'Électricien',
    # ... ajoutez vos métiers
}
```

**3. Numéro de téléphone (ligne 12)**
```python
PHONE_NUMBER = '0665137710'
PHONE_NUMBER_RAW = '0665137710'
```

### Automatique (ne touchez pas)

- ✅ `HERO_TITLE` (ligne 297)
- ✅ `ZONE_DESCRIPTION` (ligne 298)
- ✅ `GEOGRAPHIC_ZONES` (ligne 291)
- ✅ `COVERAGE_TYPES` (ligne 292)
- ✅ `AUTO_REGION_NAME` (ligne 294)

---

## ⚙️ Configuration Avancée

### Si Vous Voulez Personnaliser le Titre

```python
# Au lieu de laisser automatique, vous pouvez forcer :
HERO_TITLE = "Mon Titre Personnalisé"

# Ou mixer auto + personnalisation :
HERO_TITLE = f"Les Meilleurs Artisans de {AUTO_REGION_NAME}"
# Résultat : "Les Meilleurs Artisans de Nouvelle-Aquitaine"
```

### Si Vous Voulez Personnaliser les Zones

```python
# Passer en mode manuel :
USE_AUTO_ZONES = False

# Puis personnaliser :
GEOGRAPHIC_ZONES_MANUAL = [
    {
        'title': 'Ma Zone Personnalisée',
        'icon': '🎯',
        'description': 'Description personnalisée'
    }
]
```

---

## ✅ Checklist de Personnalisation

Quand vous configurez un nouveau site :

1. [ ] **Modifiez DEPARTMENTS** avec vos départements
2. [ ] **Modifiez CATEGORIES** avec vos métiers
3. [ ] **Modifiez PHONE_NUMBER** avec votre numéro
4. [ ] **Vérifiez USE_AUTO_ZONES = True** (recommandé)
5. [ ] **Redémarrez** : `Ctrl+C` puis `python app.py`
6. [ ] **Testez** : `python test_auto_generation.py`
7. [ ] **Vérifiez** le rendu sur http://localhost:8989

**C'est tout !** Tous les textes s'adapteront automatiquement.

---

## 🔍 Variables Automatiques Disponibles

Dans tout le système, ces variables sont générées automatiquement :

- **`AUTO_REGION_NAME`** : Nom de la région (ex: "Nouvelle-Aquitaine")
- **`HERO_TITLE`** : Titre de la page d'accueil
- **`ZONE_DESCRIPTION`** : Description de la zone d'intervention
- **`GEOGRAPHIC_ZONES`** : Liste des zones géographiques
- **`COVERAGE_TYPES`** : Types de communes

Utilisez-les dans vos propres textes :

```python
# Exemple :
MY_CUSTOM_TEXT = f"Bienvenue dans notre annuaire {AUTO_REGION_NAME} !"
# Résultat : "Bienvenue dans notre annuaire Nouvelle-Aquitaine !"
```

---

## 🎉 Résultat Final

**Configurez une seule fois :**
1. DEPARTMENTS (vos départements)
2. CATEGORIES (vos métiers)
3. PHONE_NUMBER (votre numéro)

**Et tout s'adapte automatiquement :**
- ✅ Titre de la page d'accueil
- ✅ Description de la zone
- ✅ Zones géographiques
- ✅ Liste des métiers affichée
- ✅ Nombre de communes
- ✅ SEO optimisé

**Sans toucher au code HTML ou aux templates !** 🚀

---

**Prochaine étape :** Testez avec `python test_auto_generation.py` !

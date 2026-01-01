# 🎨 Guide Complet de Personnalisation

## 🚀 Démarrage Rapide

Votre site s'adapte **automatiquement** en fonction de 3 configurations seulement :

1. **DEPARTMENTS** - Vos départements
2. **CATEGORIES** - Vos métiers
3. **PHONE_NUMBER** - Votre numéro

**Tout le reste s'adapte automatiquement !**

---

## ⚡ Configuration en 3 Étapes

### Étape 1 : Ouvrez `config.py`

### Étape 2 : Modifiez ces 3 sections

#### A. Votre numéro de téléphone (ligne 12)
```python
PHONE_NUMBER = '0665137710'  # ← Modifiez ici
PHONE_NUMBER_RAW = '0665137710'  # ← Même numéro
```

#### B. Vos départements (ligne 279)
```python
DEPARTMENTS = {
    '16': 'Charente',           # ← Ajoutez vos départements
    '17': 'Charente-Maritime',  # ← Un par ligne
    '79': 'Deux-Sèvres',
    '86': 'Vienne',
}
```

#### C. Vos métiers (ligne 123)
```python
CATEGORIES = {
    'plombier': 'Plombier',     # ← Ajoutez vos métiers
    'electricien': 'Électricien',  # ← Un par ligne
    'serrurier': 'Serrurier',
}
```

### Étape 3 : Redémarrez

```bash
Ctrl + C
python app.py
F5
```

**C'EST TOUT ! Tout le reste s'adapte automatiquement.**

---

## ✨ Ce Qui S'Adapte Automatiquement

### 1. Textes de la Page d'Accueil

- **Titre** : "Annuaire Professionnel [Votre Région]"
- **Liste des métiers** : Générée depuis CATEGORIES
- **Zone d'intervention** : Adaptée à vos départements

### 2. Zones Géographiques

Générées automatiquement depuis vos départements :
- Groupées par 2
- Avec icônes
- Avec descriptions

### 3. Toutes les Pages

- Numéro de téléphone partout
- Fil d'ariane
- Meta descriptions SEO
- Contenu unique par page

---

## 📊 Exemples de Configuration

### Exemple 1 : Île-de-France

```python
PHONE_NUMBER = '0123456789'
PHONE_NUMBER_RAW = '0123456789'

DEPARTMENTS = {
    '75': 'Paris',
    '77': 'Seine-et-Marne',
    '78': 'Yvelines',
    '91': 'Essonne',
    '92': 'Hauts-de-Seine',
    '93': 'Seine-Saint-Denis',
    '94': 'Val-de-Marne',
    '95': 'Val-d\'Oise',
}

CATEGORIES = {
    'plombier': 'Plombier',
    'electricien': 'Électricien',
    'serrurier': 'Serrurier',
}
```

**Résultat automatique :**
- Titre : "Annuaire Professionnel Île-de-France"
- Description : "Nous couvrons l'ensemble de la région Île-de-France"
- 4 zones géographiques générées
- 3 métiers affichés

---

### Exemple 2 : PACA

```python
PHONE_NUMBER = '0987654321'
PHONE_NUMBER_RAW = '0987654321'

DEPARTMENTS = {
    '04': 'Alpes-de-Haute-Provence',
    '05': 'Hautes-Alpes',
    '06': 'Alpes-Maritimes',
    '13': 'Bouches-du-Rhône',
    '83': 'Var',
    '84': 'Vaucluse',
}

CATEGORIES = {
    'peintre': 'Peintre en bâtiment',
    'maçon': 'Maçon',
    'carreleur': 'Carreleur',
    'couvreur': 'Couvreur',
}
```

**Résultat automatique :**
- Titre : "Annuaire Professionnel Provence-Alpes-Côte d'Azur"
- Description : "Nous couvrons l'ensemble de la région Provence-Alpes-Côte d'Azur"
- 3 zones géographiques générées
- 4 métiers affichés

---

## 🔧 Personnalisation Avancée (Optionnel)

Si vous voulez personnaliser davantage, consultez :

### Fichiers de Documentation

1. **ADAPTATION_AUTOMATIQUE.md** - Comment fonctionne l'adaptation automatique
2. **NOUVELLES_PERSONNALISATIONS.md** - Personnaliser Hero, FAQ, Zones
3. **PERSONNALISATION_TEXTES.md** - Personnaliser tous les textes
4. **TOUTES_PERSONNALISATIONS.txt** - Récapitulatif complet

### Scripts de Test

```bash
python test_auto_generation.py    # Voir l'adaptation automatique
python test_personnalisation.py   # Voir toutes les variables
python verifier_numero.py          # Vérifier le numéro de téléphone
```

---

## 📝 Variables Personnalisables

### Textes Personnalisables (Optionnel)

Si vous voulez changer les textes par défaut :

```python
# Fil d'ariane (ligne 17)
BREADCRUMB_HOME_TEXT = "Accueil"

# Page d'accueil (ligne 101-103)
HERO_SUBTITLE = "Trouvez les meilleurs professionnels près de chez vous"
HERO_CTA_TEXT = "Appelez-nous : {phone_number}"
HERO_CTA_SUBTEXT = "Devis gratuit - Réponse sous 24h"

# Pages catégories (ligne 106-108)
CATEGORY_WHY_CHOOSE_TITLE = "Pourquoi choisir nos professionnels ?"
CATEGORY_FAQ_TITLE = "Questions Fréquentes"
CATEGORY_ZONE_TITLE = "Notre Zone d'Intervention"
```

### Mode Auto vs Manuel

Par défaut : **Mode Automatique** (recommandé)

```python
USE_AUTO_ZONES = True  # Les zones s'adaptent automatiquement
```

Si vous préférez tout personnaliser :

```python
USE_AUTO_ZONES = False  # Mode manuel
# Puis éditez GEOGRAPHIC_ZONES_MANUAL et COVERAGE_TYPES_MANUAL
```

---

## ✅ Checklist Complète

### Configuration Initiale

- [ ] Modifié `PHONE_NUMBER` (ligne 12)
- [ ] Modifié `DEPARTMENTS` (ligne 279) - Au moins 1 département
- [ ] Modifié `CATEGORIES` (ligne 123) - Au moins 1 métier
- [ ] Vérifié `USE_AUTO_ZONES = True` (ligne 57)

### Test

- [ ] Redémarré l'application : `Ctrl+C` puis `python app.py`
- [ ] Testé la génération : `python test_auto_generation.py`
- [ ] Vérifié le site : http://localhost:8989

### Vérifications

- [ ] Le titre affiche la bonne région
- [ ] Les métiers s'affichent correctement
- [ ] Le numéro de téléphone est partout
- [ ] Les zones géographiques correspondent

---

## 🎯 Cas d'Usage Courants

### Ajouter un Département

```python
# Dans DEPARTMENTS (ligne 279)
DEPARTMENTS = {
    '16': 'Charente',
    '33': 'Gironde',  # ← Ajoutez cette ligne
}
```

Redémarrez → La zone s'adapte automatiquement !

### Ajouter un Métier

```python
# Dans CATEGORIES (ligne 123)
CATEGORIES = {
    'plombier': 'Plombier',
    'menuisier': 'Menuisier',  # ← Ajoutez cette ligne
}
```

Redémarrez → Le métier apparaît partout automatiquement !

### Changer de Région

```python
# Remplacez tous les départements
DEPARTMENTS = {
    '75': 'Paris',
    '92': 'Hauts-de-Seine',
}
```

Redémarrez → Tout s'adapte à Île-de-France automatiquement !

---

## 🚨 Problèmes Courants

### L'application ne démarre pas

**Erreur :** `SyntaxError` ou `NameError`

**Solutions :**
1. Vérifiez les virgules dans `DEPARTMENTS` et `CATEGORIES`
2. Vérifiez que tous les `{` ont leur `}`
3. Consultez le fichier de backup : `config.py.backup`

### Les textes ne changent pas

**Solutions :**
1. Arrêtez l'application : `Ctrl+C`
2. Relancez : `python app.py`
3. Videz le cache navigateur : `Ctrl+Shift+R`

### Le numéro ne s'affiche pas

**Solution :**
1. Vérifiez `PHONE_NUMBER` ligne 12
2. Redémarrez l'application
3. Testez : `python verifier_numero.py`

---

## 📚 Pour Aller Plus Loin

### Déploiement

Consultez **DEPLOIEMENT_NETLIFY.md** pour déployer sur :
- Vercel (recommandé)
- Render
- PythonAnywhere

### GitHub

Consultez **GITHUB_GUIDE.md** pour mettre sur GitHub

### Ajout de Métiers

Consultez **AJOUTER_METIER.md** pour ajouter des templates de contenu spécifiques

---

## 🎉 Résumé

**Configurez 3 variables :**
1. PHONE_NUMBER
2. DEPARTMENTS
3. CATEGORIES

**Et obtenez :**
- ✅ Site complet multi-départements
- ✅ Textes adaptés automatiquement
- ✅ SEO optimisé
- ✅ Prêt à déployer

**Sans toucher au code HTML !**

---

**Besoin d'aide ?** Consultez les fichiers de documentation ou testez avec `python test_auto_generation.py` ! 🚀

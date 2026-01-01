# 🎨 Personnalisation des Textes

## 📝 Vue d'ensemble

Tous les textes affichés sur le site peuvent maintenant être personnalisés depuis le fichier **`config.py`**.

---

## 🔧 Configuration dans config.py

### 1. Fil d'Ariane (Breadcrumb)

**Ligne 17** - Remplacez "Accueil" par le texte de votre choix :

```python
BREADCRUMB_HOME_TEXT = "Accueil"  # Modifiez ce texte
```

**Exemples :**
```python
BREADCRUMB_HOME_TEXT = "Page d'accueil"
BREADCRUMB_HOME_TEXT = "Retour à l'accueil"
BREADCRUMB_HOME_TEXT = "Accueil Annuaire"
```

---

### 2. Section "Pourquoi nous choisir ?"

**Ligne 20** - Titre de la section :

```python
WHY_CHOOSE_TITLE = "Pourquoi choisir nos professionnels ?"
```

**Lignes 21-40** - Les 3 blocs d'avantages :

```python
WHY_CHOOSE_BLOCKS = [
    {
        'icon': 'fa-certificate',      # Icône FontAwesome
        'title': 'Qualifiés & Certifiés',
        'description': 'Artisans expérimentés avec garanties professionnelles',
        'color': 'green'               # Couleur : green, blue, purple, red, yellow, indigo
    },
    {
        'icon': 'fa-bolt',
        'title': 'Intervention Rapide',
        'description': 'Devis gratuits et interventions dans les meilleurs délais',
        'color': 'blue'
    },
    {
        'icon': 'fa-map-marker-alt',
        'title': 'Proximité',
        'description': 'Professionnels locaux dans tous les départements',
        'color': 'purple'
    }
]
```

**Icônes disponibles** (FontAwesome) :
- `fa-certificate` : Certification
- `fa-bolt` : Éclair (rapidité)
- `fa-map-marker-alt` : Localisation
- `fa-shield-alt` : Protection
- `fa-star` : Étoile
- `fa-check-circle` : Validation
- `fa-clock` : Horloge
- `fa-users` : Groupe
- `fa-phone-alt` : Téléphone
- `fa-wrench` : Clé à molette
- `fa-home` : Maison

**Couleurs disponibles** :
- `green` : Vert
- `blue` : Bleu
- `purple` : Violet
- `red` : Rouge
- `yellow` : Jaune
- `indigo` : Indigo
- `pink` : Rose
- `orange` : Orange

---

### 3. Zone d'Intervention

**Lignes 43-44** - Titre et description :

```python
ZONE_TITLE = "Notre Zone d'Intervention"
ZONE_DESCRIPTION = "Nous couvrons l'ensemble des départements de Nouvelle-Aquitaine"
```

**Lignes 47-58** - Zones géographiques :

```python
GEOGRAPHIC_ZONES = [
    {
        'title': 'Charente & Charente-Maritime',
        'icon': '🌊',
        'description': 'Angoulême, La Rochelle, Saintes, Cognac et leurs environs'
    },
    {
        'title': 'Deux-Sèvres & Vienne',
        'icon': '🏞️',
        'description': 'Niort, Poitiers et toutes les communes environnantes'
    }
]
```

**Lignes 61-82** - Types de communes :

```python
COVERAGE_TYPES = [
    {
        'title': 'Métropoles',
        'icon': '🏙️',
        'description': 'Poitiers, La Rochelle, Angoulême'
    },
    {
        'title': 'Villes moyennes',
        'icon': '🏘️',
        'description': 'Niort, Saintes, Châtellerault, Cognac'
    },
    {
        'title': 'Zones rurales',
        'icon': '🌾',
        'description': 'Villages et communes de campagne'
    },
    {
        'title': 'Littoral Atlantique',
        'icon': '🏖️',
        'description': 'Stations balnéaires et communes côtières'
    }
]
```

---

## 🎯 Exemples de Personnalisation

### Exemple 1 : Région Île-de-France

```python
BREADCRUMB_HOME_TEXT = "Accueil IDF"

WHY_CHOOSE_TITLE = "Pourquoi choisir nos artisans franciliens ?"

ZONE_TITLE = "Notre Zone d'Intervention en Île-de-France"
ZONE_DESCRIPTION = "Nous couvrons l'ensemble des départements d'Île-de-France"

GEOGRAPHIC_ZONES = [
    {
        'title': 'Paris & Petite Couronne',
        'icon': '🗼',
        'description': 'Paris, Hauts-de-Seine, Seine-Saint-Denis, Val-de-Marne'
    },
    {
        'title': 'Grande Couronne',
        'icon': '🌳',
        'description': 'Seine-et-Marne, Yvelines, Essonne, Val-d\'Oise'
    }
]

COVERAGE_TYPES = [
    {
        'title': 'Paris intra-muros',
        'icon': '🏛️',
        'description': 'Tous les arrondissements de Paris'
    },
    {
        'title': 'Banlieue proche',
        'icon': '🏙️',
        'description': 'Nanterre, Créteil, Bobigny, etc.'
    },
    {
        'title': 'Communes périurbaines',
        'icon': '🏘️',
        'description': 'Melun, Versailles, Pontoise, Évry'
    }
]
```

### Exemple 2 : PACA (Provence-Alpes-Côte d'Azur)

```python
BREADCRUMB_HOME_TEXT = "Accueil"

WHY_CHOOSE_TITLE = "Pourquoi faire appel à nos artisans du Sud ?"

WHY_CHOOSE_BLOCKS = [
    {
        'icon': 'fa-sun',
        'title': 'Expertise Méditerranéenne',
        'description': 'Artisans habitués au climat et aux spécificités locales',
        'color': 'yellow'
    },
    {
        'icon': 'fa-shield-alt',
        'title': 'Garantie Décennale',
        'description': 'Tous nos professionnels sont assurés',
        'color': 'blue'
    },
    {
        'icon': 'fa-star',
        'title': 'Qualité Premium',
        'description': 'Sélection rigoureuse des meilleurs artisans',
        'color': 'purple'
    }
]

ZONE_TITLE = "Couverture Provence-Alpes-Côte d'Azur"
ZONE_DESCRIPTION = "Du littoral méditerranéen aux Alpes du Sud"

GEOGRAPHIC_ZONES = [
    {
        'title': 'Côte d\'Azur',
        'icon': '🏖️',
        'description': 'Nice, Cannes, Antibes, Menton'
    },
    {
        'title': 'Bouches-du-Rhône',
        'icon': '⚓',
        'description': 'Marseille, Aix-en-Provence, Arles'
    },
    {
        'title': 'Var & Arrière-pays',
        'icon': '🌲',
        'description': 'Toulon, Fréjus, Draguignan'
    }
]

COVERAGE_TYPES = [
    {
        'title': 'Grandes villes',
        'icon': '🏙️',
        'description': 'Marseille, Nice, Toulon'
    },
    {
        'title': 'Littoral',
        'icon': '🌊',
        'description': 'Toute la côte méditerranéenne'
    },
    {
        'title': 'Arrière-pays',
        'icon': '⛰️',
        'description': 'Villages provençaux et Alpes'
    }
]
```

---

## ✅ Application des Modifications

### Étapes :

1. **Ouvrez** `config.py`
2. **Modifiez** les textes selon vos besoins
3. **Redémarrez** l'application :
   ```bash
   Ctrl + C
   python app.py
   ```
4. **Rafraîchissez** le navigateur (F5 ou Ctrl+R)

---

## 📍 Où sont affichés ces textes ?

### Fil d'ariane (`breadcrumb_home`)
Apparaît sur :
- ✅ Pages de catégories
- ✅ Pages de départements
- ✅ Pages de villes
- ✅ Fiches détaillées
- ✅ Plan du site

### Section "Pourquoi nous choisir ?" (`why_choose_*`)
Apparaît sur :
- ✅ Page d'accueil uniquement

### Zone d'intervention (`zone_*`, `geographic_zones`, `coverage_types`)
Apparaît sur :
- ✅ Page d'accueil uniquement

---

## 🎨 Conseils de Personnalisation

### Pour le Fil d'Ariane
- Restez court (1-3 mots max)
- Exemples : "Accueil", "Home", "Annuaire", "Retour"

### Pour la Section "Pourquoi nous choisir"
- **3 blocs** recommandés (mais vous pouvez en mettre plus ou moins)
- Variez les couleurs pour un rendu visuel agréable
- Mettez en avant vos **vrais avantages**

### Pour la Zone d'Intervention
- Adaptez aux **départements activés** dans `DEPARTMENTS`
- Mentionnez les **grandes villes** de votre zone
- Soyez **précis** et **rassurant**

---

## ⚠️ Important

- **Redémarrage obligatoire** après chaque modification de config.py
- Les textes sont en **HTML-safe** (pas besoin d'échapper les caractères)
- Utilisez des **guillemets simples** pour les clés du dictionnaire
- Respectez la **syntaxe Python** (indentation, virgules)

---

## 🐛 En cas d'erreur

Si l'application ne démarre plus après modification :

1. **Vérifiez la syntaxe Python** (virgules, crochets, accolades)
2. **Vérifiez les guillemets** (utilisez des guillemets simples pour les clés)
3. **Consultez l'erreur** dans le terminal

**Erreur courante :**
```
SyntaxError: invalid syntax
```
→ Vérifiez les virgules et les accolades manquantes

---

**Besoin d'aide ?** Consultez les exemples ci-dessus ou le fichier `config.py` directement ! 🚀

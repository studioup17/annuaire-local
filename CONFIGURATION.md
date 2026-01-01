# Guide de Configuration

Ce document explique comment configurer et personnaliser votre annuaire professionnel.

## 📞 Configuration du numéro de téléphone

Le numéro de téléphone est maintenant centralisé dans le fichier `config.py` :

```python
# Configuration contact
PHONE_NUMBER = '04 58 10 57 19'  # Modifiez ce numéro selon vos besoins
PHONE_NUMBER_RAW = '0458105719'  # Version sans espaces pour les liens tel:
```

### Comment modifier le numéro de téléphone

1. Ouvrez le fichier `config.py`
2. Modifiez les deux lignes :
   - `PHONE_NUMBER` : version affichée avec espaces
   - `PHONE_NUMBER_RAW` : version sans espaces pour les liens cliquables
3. Redémarrez l'application

**Le numéro sera automatiquement mis à jour partout :**
- Dans l'en-tête du site
- Dans le menu de navigation
- Dans le footer
- Dans tous les contenus générés

---

## 🗺️ Configuration des départements

Tous les départements français sont maintenant disponibles dans `config.py` (ligne 43+).

### Départements actuellement actifs

Par défaut, **tous les 101 départements** (96 métropolitains + 5 DOM) sont activés :

- **Auvergne-Rhône-Alpes** : 12 départements
- **Bourgogne-Franche-Comté** : 8 départements
- **Bretagne** : 4 départements
- **Centre-Val de Loire** : 6 départements
- **Corse** : 2 départements
- **Grand Est** : 10 départements
- **Hauts-de-France** : 5 départements
- **Île-de-France** : 8 départements
- **Normandie** : 5 départements
- **Nouvelle-Aquitaine** : 12 départements
- **Occitanie** : 13 départements
- **Pays de la Loire** : 5 départements
- **Provence-Alpes-Côte d'Azur** : 6 départements
- **DOM** : 5 départements (Guadeloupe, Martinique, Guyane, Réunion, Mayotte)

### Comment désactiver certains départements

Si vous ne souhaitez pas couvrir tous les départements, commentez simplement les lignes correspondantes :

```python
DEPARTMENTS = {
    # Auvergne-Rhône-Alpes
    '01': 'Ain',
    # '03': 'Allier',  # Commenté = désactivé
    '07': 'Ardèche',
    # ...
}
```

### Comment ajouter un département spécifique

Si vous souhaitez n'activer que certains départements, supprimez ou commentez les autres :

```python
DEPARTMENTS = {
    # Uniquement région parisienne
    '75': 'Paris',
    '77': 'Seine-et-Marne',
    '78': 'Yvelines',
    '91': 'Essonne',
    '92': 'Hauts-de-Seine',
    '93': 'Seine-Saint-Denis',
    '94': 'Val-de-Marne',
    '95': "Val-d'Oise",
}
```

### Impact sur les données

- Le fichier JSON contient **toutes les communes de France**
- Le système filtre automatiquement les communes selon les départements activés dans `DEPARTMENTS`
- Nombre d'entrées générées = `Communes filtrées × Nombre de catégories`

**Exemple :**
- Si vous activez uniquement Paris (75) : ~20 arrondissements × 5 métiers = ~100 pages
- Si vous activez tous les départements : ~35 000 communes × 5 métiers = ~175 000 pages

---

## 🛠️ Configuration des métiers

Les métiers sont configurés dans `config.py` (ligne 15+).

### Métiers actuellement actifs

```python
CATEGORIES = {
    'couvreur': 'Couvreur',
    'pisciniste': 'Pisciniste',
    'plombier': 'Plombier',
    'vitrier': 'Vitrier',
    'architecte-interieur': "Architecte d'intérieur"
}
```

### Comment ajouter un nouveau métier

1. **Ajoutez le métier dans `config.py`** :

```python
CATEGORIES = {
    'couvreur': 'Couvreur',
    'pisciniste': 'Pisciniste',
    'plombier': 'Plombier',
    'vitrier': 'Vitrier',
    'architecte-interieur': "Architecte d'intérieur",
    'electricien': 'Électricien',  # NOUVEAU
    'serrurier': 'Serrurier',      # NOUVEAU
}
```

**Format :** `'slug-url': 'Nom affiché'`
- Le slug sera utilisé dans les URLs (ex: `/category/electricien`)
- Le nom sera affiché sur le site

2. **Ajoutez les templates de contenu dans `content_generator.py`** (optionnel mais recommandé) :

Ouvrez `content_generator.py` et ajoutez des templates spécifiques pour votre métier :

```python
# Dans intro_templates_by_category (ligne ~17)
'electricien': [
    "Vous recherchez un électricien à {city} ? Les professionnels du {postal_code} interviennent...",
    "À {city}, faites appel à un électricien qualifié du secteur {postal_code}...",
    # ... ajoutez 3-4 variations
],

# Dans description_templates_by_category (ligne ~50)
'electricien': [
    "Les électriciens de {city} assurent tous vos travaux électriques...",
    "Installation électrique, dépannage, mise aux normes : à {city} ({postal_code})...",
    # ... ajoutez 3-4 variations
],

# Dans expertise_templates_by_category (ligne ~85)
'electricien': [
    "Nos électriciens à {city} maîtrisent l'ensemble des installations électriques...",
    # ... ajoutez 2-3 variations
],

# Dans conclusion_templates_by_category (ligne ~130)
'electricien': [
    f"Pour tous vos besoins en électricité à {{city}}, contactez un professionnel du {{postal_code}}. Appelez le {PHONE_NUMBER}.",
    # ... ajoutez 3-4 variations
],
```

3. **Redémarrez l'application**

Les nouvelles catégories apparaîtront automatiquement :
- Dans le menu de navigation
- Sur la page d'accueil
- Dans toutes les pages générées

### Exemples de métiers à ajouter

Voici des suggestions déjà préparées dans `config.py` (commentées) :

```python
# 'electricien': 'Électricien',
# 'serrurier': 'Serrurier',
# 'chauffagiste': 'Chauffagiste',
# 'paysagiste': 'Paysagiste',
# 'peintre': 'Peintre en bâtiment',
# 'menuisier': 'Menuisier',
# 'macon': 'Maçon',
# 'carreleur': 'Carreleur',
# 'charpentier': 'Charpentier',
# 'ravalement-facade': 'Ravalement de façade',
```

Décommentez simplement ceux que vous souhaitez activer !

### Comment supprimer un métier

Supprimez ou commentez la ligne correspondante dans `CATEGORIES` :

```python
CATEGORIES = {
    'couvreur': 'Couvreur',
    # 'pisciniste': 'Pisciniste',  # DÉSACTIVÉ
    'plombier': 'Plombier',
}
```

---

## 🚀 Processus de mise à jour

### Ordre recommandé

1. **Modifiez `config.py`** (départements, métiers, téléphone)
2. **Si nouveaux métiers :** ajoutez les templates dans `content_generator.py`
3. **Redémarrez l'application** : `python app.py`
4. **Vérifiez les données** : au démarrage, l'application affiche :
   ```
   ✅ 35123 communes chargées depuis le JSON
   📊 175615 entrées créées (35123 communes × 5 catégories)
   ```

### Temps de chargement

- **23 départements (actuel)** : ~2-3 secondes (~6 500 communes)
- **Tous les départements** : ~5-10 secondes (~35 000 communes)
- **Île-de-France uniquement** : <1 seconde (~1 300 communes)

---

## 📋 Checklist de configuration

### Configuration initiale

- [ ] Modifier le numéro de téléphone dans `config.py`
- [ ] Choisir les départements à couvrir
- [ ] Choisir les métiers à proposer
- [ ] Ajouter les templates de contenu pour les nouveaux métiers
- [ ] Tester l'application en local

### Ajout d'un nouveau métier

- [ ] Ajouter le métier dans `CATEGORIES` (config.py)
- [ ] Créer 4+ templates d'introduction (content_generator.py)
- [ ] Créer 4+ templates de description
- [ ] Créer 3+ templates d'expertise
- [ ] Créer 4+ templates de conclusion (avec numéro de téléphone)
- [ ] Redémarrer l'application
- [ ] Vérifier l'affichage sur le site

---

## ⚙️ Configuration avancée

### Fichier JSON des communes

Le fichier `communes-france-avec-polygon-2025 (1).json` contient :
- **Toutes les communes de France** (~35 000)
- Code INSEE
- Nom de la commune
- Code postal
- Coordonnées GPS
- Population
- Département

**Vous n'avez pas besoin de le modifier.** Le filtrage se fait automatiquement via `DEPARTMENTS`.

### Variables disponibles dans les templates

Dans `content_generator.py`, vous pouvez utiliser ces variables :

- `{city}` : Nom de la ville (ex: "Lyon")
- `{postal_code}` : Code postal (ex: "69001")
- `{profession}` : Nom du métier avec majuscule (ex: "Plombier")
- `{profession_lower}` : Nom du métier en minuscule (ex: "plombier")

Ces variables sont automatiquement remplacées lors de la génération du contenu.

---

## 🆘 Aide et support

### Problèmes courants

**Q: Le numéro de téléphone ne s'affiche pas**
- Vérifiez que vous avez redémarré l'application après modification
- Vérifiez que `PHONE_NUMBER` et `PHONE_NUMBER_RAW` sont bien définis dans config.py

**Q: Les nouveaux départements n'apparaissent pas**
- Vérifiez la syntaxe dans `DEPARTMENTS` (virgules, guillemets)
- Redémarrez l'application
- Vérifiez les logs au démarrage pour voir le nombre de communes chargées

**Q: Les nouveaux métiers ne génèrent pas de contenu**
- Si vous n'avez pas ajouté de templates spécifiques, le système utilise les templates génériques
- Pour un meilleur SEO, ajoutez des templates spécifiques dans `content_generator.py`

**Q: L'application est lente au démarrage**
- Normal si vous avez activé tous les départements (~35 000 communes)
- Envisagez de n'activer que les départements nécessaires
- Le chargement se fait une seule fois au démarrage

---

## 📝 Exemples de configuration

### Configuration "Région Parisienne"

```python
DEPARTMENTS = {
    '75': 'Paris',
    '77': 'Seine-et-Marne',
    '78': 'Yvelines',
    '91': 'Essonne',
    '92': 'Hauts-de-Seine',
    '93': 'Seine-Saint-Denis',
    '94': 'Val-de-Marne',
    '95': "Val-d'Oise",
}

CATEGORIES = {
    'plombier': 'Plombier',
    'electricien': 'Électricien',
    'serrurier': 'Serrurier',
}
```

### Configuration "Artisans du bâtiment"

```python
CATEGORIES = {
    'plombier': 'Plombier',
    'electricien': 'Électricien',
    'couvreur': 'Couvreur',
    'macon': 'Maçon',
    'menuisier': 'Menuisier',
    'carreleur': 'Carreleur',
    'peintre': 'Peintre en bâtiment',
    'charpentier': 'Charpentier',
}
```

### Configuration "France entière, tous métiers"

```python
# Gardez tous les départements dans DEPARTMENTS

CATEGORIES = {
    'couvreur': 'Couvreur',
    'pisciniste': 'Pisciniste',
    'plombier': 'Plombier',
    'vitrier': 'Vitrier',
    'architecte-interieur': "Architecte d'intérieur",
    'electricien': 'Électricien',
    'serrurier': 'Serrurier',
    'chauffagiste': 'Chauffagiste',
    'paysagiste': 'Paysagiste',
    'peintre': 'Peintre en bâtiment',
    'menuisier': 'Menuisier',
    'macon': 'Maçon',
    'carreleur': 'Carreleur',
    'charpentier': 'Charpentier',
    'ravalement-facade': 'Ravalement de façade',
}
```

**Résultat :** ~35 000 communes × 15 métiers = **~525 000 pages** ! 🚀

---

**Dernière mise à jour :** Janvier 2026

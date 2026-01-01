# 🎨 Nouvelles Personnalisations Ajoutées

## ✅ Ce qui a été ajouté

Vous pouvez maintenant personnaliser **tous les textes** qui s'affichent automatiquement sur toutes les pages du site depuis `config.py`.

---

## 📝 Nouvelles Variables Configurables

### 1. Page d'Accueil - Section Hero

**Lignes 85-88 de config.py**

```python
HERO_TITLE = "Annuaire Professionnel de Nouvelle-Aquitaine"
HERO_SUBTITLE = "Trouvez les meilleurs professionnels près de chez vous"
HERO_CTA_TEXT = "Appelez-nous : {phone_number}"
HERO_CTA_SUBTEXT = "Devis gratuit - Réponse sous 24h"
```

**Ce qui change automatiquement :**
- ✅ Le titre principal de la page d'accueil
- ✅ Le sous-titre
- ✅ Le texte du bouton d'appel
- ✅ Le texte sous le bouton

**Note :** `{phone_number}` sera automatiquement remplacé par votre numéro de téléphone

---

### 2. Pages Catégories - Sections Personnalisables

**Lignes 91-93 de config.py**

```python
CATEGORY_WHY_CHOOSE_TITLE = "Pourquoi choisir nos professionnels ?"
CATEGORY_FAQ_TITLE = "Questions Fréquentes"
CATEGORY_ZONE_TITLE = "Notre Zone d'Intervention"
```

**Ce qui change automatiquement :**
- ✅ Titre de la section "Pourquoi nous choisir" sur les pages catégories
- ✅ Titre de la section FAQ
- ✅ Titre de la section Zone d'intervention

---

### 3. Pages Catégories - Questions Fréquentes (FAQ)

**Lignes 96-113 de config.py**

```python
DEFAULT_FAQ = [
    {
        'question': "Quels sont vos tarifs ?",
        'answer': "Nos tarifs varient selon la nature des travaux..."
    },
    {
        'question': "Intervenez-vous en urgence ?",
        'answer': "Oui, nos professionnels sont disponibles... {phone_number}..."
    },
    # ... 2 autres questions
]
```

**Ce qui change automatiquement :**
- ✅ Les questions et réponses affichées sur toutes les pages de catégories
- ✅ Vous pouvez ajouter/supprimer/modifier les questions

**Note :** Utilisez `{phone_number}` dans les réponses pour afficher automatiquement votre numéro

---

### 4. Pages Villes - Sections Personnalisables

**Lignes 116-118 de config.py**

```python
CITY_EXPERTISE_TITLE_TEMPLATE = "Notre expertise {profession_lower}"
CITY_EXPERTISE_DESCRIPTION_TEMPLATE = "Les spécialistes de {city} assurent un service complet et personnalisé pour vos projets."
CITY_SERVICES_TITLE_TEMPLATE = "Nos services {profession_lower} à {city}"
```

**Variables disponibles :**
- `{profession_lower}` : Nom du métier en minuscules (ex: "graphiste")
- `{city}` : Nom de la ville (ex: "Angoulême")

**Ce qui change automatiquement :**
- ✅ Titre de la section expertise sur chaque page ville
- ✅ Description sous l'expertise
- ✅ Titre de la section services

---

## 🔧 Comment Personnaliser ?

### Étape 1 : Modifier config.py

Ouvrez `config.py` et modifiez les lignes 85 à 118 selon vos besoins.

**Exemple pour l'Île-de-France :**

```python
# Page d'accueil
HERO_TITLE = "Annuaire Professionnel Île-de-France"
HERO_SUBTITLE = "Trouvez les meilleurs artisans franciliens"
HERO_CTA_TEXT = "Contactez-nous : {phone_number}"
HERO_CTA_SUBTEXT = "Devis gratuit - Intervention rapide"

# Pages catégories
CATEGORY_WHY_CHOOSE_TITLE = "Pourquoi faire appel à nos artisans ?"
CATEGORY_FAQ_TITLE = "Vos Questions - Nos Réponses"
CATEGORY_ZONE_TITLE = "Nos Zones d'Intervention"

# FAQ personnalisée
DEFAULT_FAQ = [
    {
        'question': "Quels arrondissements couvrez-vous ?",
        'answer': "Nous intervenons dans tous les arrondissements de Paris ainsi qu'en petite et grande couronne."
    },
    {
        'question': "Quel est le délai d'intervention ?",
        'answer': "Nous intervenons sous 24h en Île-de-France. Pour les urgences, appelez le {phone_number}."
    },
    {
        'question': "Proposez-vous des devis gratuits ?",
        'answer': "Oui, tous nos devis sont gratuits et sans engagement."
    }
]

# Pages villes
CITY_EXPERTISE_TITLE_TEMPLATE = "L'excellence {profession_lower} à {city}"
CITY_EXPERTISE_DESCRIPTION_TEMPLATE = "Nos artisans de {city} sont reconnus pour leur savoir-faire et leur professionnalisme."
CITY_SERVICES_TITLE_TEMPLATE = "Services {profession_lower} disponibles à {city}"
```

---

### Étape 2 : Redémarrer l'Application

```bash
# 1. Arrêter
Ctrl + C

# 2. Relancer
python app.py

# 3. Rafraîchir le navigateur
F5
```

---

## 📍 Où Sont Affichés Ces Textes ?

### Page d'Accueil (/)
- ✅ `HERO_TITLE` - Titre principal
- ✅ `HERO_SUBTITLE` - Sous-titre
- ✅ `HERO_CTA_TEXT` - Bouton d'appel
- ✅ `HERO_CTA_SUBTEXT` - Texte sous le bouton
- ✅ Liste automatique de tous les métiers configurés

### Pages Catégories (/category/graphiste)
- ✅ `CATEGORY_WHY_CHOOSE_TITLE` - Titre section "Pourquoi nous choisir"
- ✅ `WHY_CHOOSE_BLOCKS` - 3 blocs d'avantages
- ✅ `CATEGORY_FAQ_TITLE` - Titre section FAQ
- ✅ `DEFAULT_FAQ` - Questions et réponses
- ✅ `CATEGORY_ZONE_TITLE` - Titre zone d'intervention
- ✅ `ZONE_DESCRIPTION` - Description de la zone
- ✅ `GEOGRAPHIC_ZONES` - Zones géographiques
- ✅ `COVERAGE_TYPES` - Types de communes

### Pages Villes (/address/graphiste/angouleme)
- ✅ `CITY_EXPERTISE_TITLE_TEMPLATE` - Titre expertise
- ✅ `CITY_EXPERTISE_DESCRIPTION_TEMPLATE` - Description expertise
- ✅ `CITY_SERVICES_TITLE_TEMPLATE` - Titre services

---

## 🎯 Exemples Complets

### Exemple 1 : Région PACA

```python
# Page d'accueil
HERO_TITLE = "Annuaire des Artisans Provence-Alpes-Côte d'Azur"
HERO_SUBTITLE = "Les meilleurs professionnels du Sud"
HERO_CTA_TEXT = "Appelez-nous : {phone_number}"
HERO_CTA_SUBTEXT = "Intervention rapide - Devis gratuit"

# Pages catégories
CATEGORY_WHY_CHOOSE_TITLE = "Pourquoi choisir nos artisans du Sud ?"
CATEGORY_FAQ_TITLE = "Questions Fréquentes"
CATEGORY_ZONE_TITLE = "Notre Couverture PACA"

DEFAULT_FAQ = [
    {
        'question': "Couvrez-vous toute la région PACA ?",
        'answer': "Oui, nous intervenons sur toute la région : Alpes-Maritimes, Var, Bouches-du-Rhône, Vaucluse, Alpes-de-Haute-Provence et Hautes-Alpes."
    },
    {
        'question': "Vos artisans sont-ils certifiés ?",
        'answer': "Tous nos professionnels sont certifiés RGE et disposent des assurances obligatoires."
    },
    {
        'question': "Proposez-vous des interventions d'urgence ?",
        'answer': "Oui, appelez-nous au {phone_number} pour une intervention urgente."
    },
    {
        'question': "Comment obtenir un devis ?",
        'answer': "Contactez-nous au {phone_number} ou via notre formulaire. Nos devis sont gratuits et personnalisés."
    }
]

# Pages villes
CITY_EXPERTISE_TITLE_TEMPLATE = "Expertise {profession_lower} à {city}"
CITY_EXPERTISE_DESCRIPTION_TEMPLATE = "Nos artisans de {city} mettent leur savoir-faire méditerranéen à votre service."
CITY_SERVICES_TITLE_TEMPLATE = "Prestations {profession_lower} disponibles à {city}"
```

---

### Exemple 2 : Région Grand Est

```python
# Page d'accueil
HERO_TITLE = "Annuaire Professionnel Grand Est"
HERO_SUBTITLE = "Artisans qualifiés en Alsace, Lorraine et Champagne"
HERO_CTA_TEXT = "Contactez-nous : {phone_number}"
HERO_CTA_SUBTEXT = "Réponse sous 24h - Devis gratuit"

# Pages catégories
CATEGORY_WHY_CHOOSE_TITLE = "Pourquoi nos artisans du Grand Est ?"
CATEGORY_FAQ_TITLE = "Foire Aux Questions"
CATEGORY_ZONE_TITLE = "Zone de Couverture Grand Est"

DEFAULT_FAQ = [
    {
        'question': "Dans quels départements intervenez-vous ?",
        'answer': "Nous couvrons les 10 départements du Grand Est : Bas-Rhin, Haut-Rhin, Moselle, Meurthe-et-Moselle, Meuse, Vosges, Marne, Haute-Marne, Aube et Ardennes."
    },
    {
        'question': "Travaillez-vous avec des artisans locaux ?",
        'answer': "Oui, tous nos professionnels sont des artisans locaux qui connaissent les spécificités régionales."
    },
    {
        'question': "Quels sont vos tarifs ?",
        'answer': "Nos tarifs varient selon les prestations. Contactez-nous au {phone_number} pour un devis personnalisé gratuit."
    }
]

# Pages villes
CITY_EXPERTISE_TITLE_TEMPLATE = "Savoir-faire {profession_lower} à {city}"
CITY_EXPERTISE_DESCRIPTION_TEMPLATE = "À {city}, nos artisans allient tradition et modernité pour vos projets."
CITY_SERVICES_TITLE_TEMPLATE = "Services {profession_lower} proposés à {city}"
```

---

## 🔄 Variables Automatiquement Remplacées

### {phone_number}
- Remplacé par votre numéro (ex: "0665137710")
- Utilisable dans : `HERO_CTA_TEXT`, `DEFAULT_FAQ` réponses

### {profession_lower}
- Remplacé par le nom du métier en minuscules (ex: "graphiste")
- Utilisable dans : `CITY_EXPERTISE_TITLE_TEMPLATE`, `CITY_SERVICES_TITLE_TEMPLATE`

### {city}
- Remplacé par le nom de la ville (ex: "Angoulême")
- Utilisable dans : `CITY_EXPERTISE_DESCRIPTION_TEMPLATE`, `CITY_SERVICES_TITLE_TEMPLATE`

---

## ✅ Checklist de Personnalisation

Avant de déployer, vérifiez :

- [ ] **Hero Section** : Titre et sous-titre adaptés à votre région
- [ ] **CTA Texts** : Boutons d'appel personnalisés
- [ ] **FAQ** : Questions adaptées à votre activité (3-5 recommandées)
- [ ] **Sections catégories** : Titres pertinents
- [ ] **Templates villes** : Textes adaptés à votre ton
- [ ] **Variables** : `{phone_number}`, `{profession_lower}`, `{city}` utilisées correctement
- [ ] **Test** : Application redémarrée et pages vérifiées

---

## 🐛 En Cas de Problème

### L'application ne démarre pas

**Erreur :** `SyntaxError` ou `NameError`

**Solution :**
- Vérifiez les virgules dans `DEFAULT_FAQ`
- Vérifiez que tous les crochets `[]` et accolades `{}` sont fermés
- Vérifiez les guillemets `"` ou `'`

**Exemple d'erreur courante :**
```python
# ❌ ERREUR - Virgule manquante
DEFAULT_FAQ = [
    {
        'question': "Test ?",
        'answer': "Réponse"  # <- Virgule manquante
    }
    {  # <- Erreur ici
        'question': "Test 2 ?",
        'answer': "Réponse 2"
    }
]

# ✅ CORRECT
DEFAULT_FAQ = [
    {
        'question': "Test ?",
        'answer': "Réponse"
    },  # <- Virgule présente
    {
        'question': "Test 2 ?",
        'answer': "Réponse 2"
    }
]
```

---

### Les textes ne changent pas

**Solution :**
1. Arrêtez l'application : `Ctrl + C`
2. Relancez : `python app.py`
3. Videz le cache : `Ctrl + Shift + R`

---

### {phone_number} s'affiche littéralement

**Problème :** Le texte `{phone_number}` s'affiche au lieu du numéro.

**Solution :**
- C'est normal dans `config.py`
- L'application remplace automatiquement `{phone_number}` par votre numéro
- Si le problème persiste, redémarrez l'application

---

## 📚 Récapitulatif des Fichiers Modifiés

1. ✅ `config.py` - Nouvelles variables (lignes 84-118)
2. ✅ `app.py` - Injection des variables dans les templates
3. ✅ `templates/home.html` - Hero section personnalisable
4. ✅ `templates/category.html` - Sections Why Choose, FAQ, Zone
5. ✅ `templates/city.html` - Sections expertise et services personnalisables

---

## 🎉 Résultat Final

Avec toutes ces personnalisations, votre site est maintenant :

- ✅ **100% personnalisable** depuis config.py
- ✅ **Adapté à votre région** (Sud-Est, PACA, Île-de-France, etc.)
- ✅ **Professionnel** avec FAQ et sections riches
- ✅ **SEO-friendly** avec contenu unique par page
- ✅ **Évolutif** sans toucher au code HTML

---

**Prêt à personnaliser ?** Ouvrez `config.py` et commencez ! 🚀

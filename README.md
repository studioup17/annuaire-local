# 🏠 Annuaire Professionnel Multi-Métiers - France Entière

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.x-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-Private-red.svg)]()

> Annuaire professionnel programmatique **configurable** couvrant **jusqu'à 35 000 communes** de toute la France, avec génération automatique de contenu SEO pour **un nombre illimité de métiers**.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)

---

## 📋 Table des matières

- [Aperçu](#-aperçu)
- [Fonctionnalités](#-fonctionnalités)
- [Catégories de métiers](#-catégories-de-métiers)
- [Couverture géographique](#-couverture-géographique)
- [Architecture technique](#-architecture-technique)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Utilisation](#-utilisation)
- [Structure du projet](#-structure-du-projet)
- [API Endpoints](#-api-endpoints)
- [SEO & Référencement](#-seo--référencement)
- [Personnalisation](#-personnalisation)
- [Dépendances](#-dépendances)
- [Roadmap](#-roadmap)

---

## 🎯 Aperçu

Ce projet est un **générateur d'annuaire professionnel local** conçu pour le référencement SEO. Il génère automatiquement des milliers de pages optimisées pour les moteurs de recherche, chacune ciblant une combinaison **métier + ville**.

### Cas d'usage

- **Agences SEO** : Création de sites satellites pour le référencement local
- **Artisans** : Présence web multi-villes sans effort
- **Marketplaces locales** : Base pour un annuaire professionnel
- **Lead generation** : Captation de prospects par zone géographique

### Statistiques du projet

| Métrique | Valeur par défaut | Maximum possible |
|----------|-------------------|------------------|
| Communes couvertes | ~35 000 | ~35 000 |
| Départements | 101 (tous) | 101 |
| Régions | 13 (toutes) | 13 |
| Catégories métiers | 5 (modifiable) | Illimité |
| Pages générées | ~175 000 | Illimité |

---

## ✨ Fonctionnalités

### 🔍 Recherche avancée
- **Meilisearch** : Moteur de recherche ultra-rapide (optionnel)
- **Fallback Pandas** : Recherche fonctionnelle sans Meilisearch
- **Filtres** : Par catégorie, département, ville
- **API JSON** : Intégration facile avec d'autres applications

### 📄 Génération de contenu
- **Contenu spinné** : Textes uniques générés automatiquement
- **Templates variés** : 4+ variations par section
- **Personnalisation locale** : Données INSEE intégrées (population, densité, etc.)
- **SEO-friendly** : Balises optimisées, Schema.org

### 🗺️ Navigation hiérarchique
```
Accueil
  └── Catégorie (ex: Architecte d'intérieur)
       └── Département (ex: Haute-Savoie)
            └── Ville (ex: Annecy)
                 └── Fiche détaillée
```

### 📊 Données enrichies
- Population et densité
- Superficie et altitude
- Classification INSEE (grille de densité)
- Niveau d'équipements et services
- Unité urbaine
- Gentilé
- Liens Wikipedia

### 🎨 Interface utilisateur
- Design responsive (mobile-first)
- TailwindCSS pour le styling
- Icônes Font Awesome
- Cartes interactives Leaflet/OpenStreetMap

---

## 👷 Catégories de métiers

| Catégorie | Slug | Icône | Description |
|-----------|------|-------|-------------|
| **Couvreur** | `couvreur` | 🏠 | Toiture, zinguerie, charpente, isolation |
| **Pisciniste** | `pisciniste` | 🏊 | Construction, entretien, rénovation piscines |
| **Plombier** | `plombier` | 🔧 | Plomberie, chauffage, sanitaires |
| **Vitrier** | `vitrier` | 🪟 | Vitrerie, miroiterie, double vitrage |
| **Architecte d'intérieur** | `architecte-interieur` | 🛋️ | Design, décoration, aménagement |

### Ajouter une nouvelle catégorie

**Voir le guide complet :** [CONFIGURATION.md](CONFIGURATION.md)

1. Modifier `config.py` :
```python
CATEGORIES = {
    # ... catégories existantes ...
    'nouveau-metier': 'Nouveau Métier'
}
```

2. Ajouter les templates dans `content_generator.py` (optionnel mais recommandé)
3. Redémarrer l'application

**Métiers prêts à activer** (déjà dans config.py, commentés) :
- Électricien
- Serrurier
- Chauffagiste
- Paysagiste
- Peintre en bâtiment
- Menuisier
- Maçon
- Carreleur
- Charpentier
- Ravalement de façade

---

## 🗺️ Couverture géographique

### 🇫🇷 Tous les départements français

Le projet couvre maintenant **tous les départements français** :
- **96 départements métropolitains**
- **5 départements d'Outre-Mer** (Guadeloupe, Martinique, Guyane, Réunion, Mayotte)

**Total :** 101 départements, 13 régions, ~35 000 communes

### Configuration personnalisée

Vous pouvez activer/désactiver les départements dans `config.py` :

```python
DEPARTMENTS = {
    '01': 'Ain',          # Activé
    # '02': 'Aisne',     # Désactivé (commenté)
    '03': 'Allier',       # Activé
    # ...
}
```

**Voir le guide complet :** [CONFIGURATION.md](CONFIGURATION.md)

### Exemples de régions disponibles

#### 🏔️ Auvergne-Rhône-Alpes (12 départements)
Ain, Allier, Ardèche, Cantal, Drôme, Isère, Loire, Haute-Loire, Puy-de-Dôme, Rhône, Savoie, Haute-Savoie

#### 🌴 Provence-Alpes-Côte d'Azur (6 départements)
Alpes-de-Haute-Provence, Hautes-Alpes, Alpes-Maritimes, Bouches-du-Rhône, Var, Vaucluse

#### 🏙️ Île-de-France (8 départements)
Paris, Seine-et-Marne, Yvelines, Essonne, Hauts-de-Seine, Seine-Saint-Denis, Val-de-Marne, Val-d'Oise

#### 🌊 Occitanie (13 départements)
Ariège, Aude, Aveyron, Gard, Haute-Garonne, Gers, Hérault, Lot, Lozère, Hautes-Pyrénées, Pyrénées-Orientales, Tarn, Tarn-et-Garonne

#### 🌊 Nouvelle-Aquitaine (12 départements)
Charente, Charente-Maritime, Corrèze, Creuse, Dordogne, Gironde, Landes, Lot-et-Garonne, Pyrénées-Atlantiques, Deux-Sèvres, Vienne, Haute-Vienne

**+ 9 autres régions disponibles** (voir config.py)

---

## 🏗️ Architecture technique

```
┌─────────────────────────────────────────────────────────────┐
│                        CLIENT                                │
│                   (Navigateur Web)                           │
└─────────────────────────┬───────────────────────────────────┘
                          │ HTTP
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                     FLASK APP                                │
│                      (app.py)                                │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │   Routes    │  │  Templates  │  │   Static Files      │  │
│  │  (Views)    │  │   (Jinja2)  │  │   (CSS/JS/Images)   │  │
│  └──────┬──────┘  └──────┬──────┘  └─────────────────────┘  │
│         │                │                                   │
│         ▼                ▼                                   │
│  ┌─────────────────────────────────────────────────────┐    │
│  │              DATA PROCESSOR                          │    │
│  │           (data_processor_json.py)                   │    │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │    │
│  │  │   Pandas    │  │  Meilisearch│  │   Calculs   │  │    │
│  │  │  DataFrame  │  │   (option)  │  │  Distance   │  │    │
│  │  └──────┬──────┘  └──────┬──────┘  └─────────────┘  │    │
│  └─────────┼────────────────┼──────────────────────────┘    │
│            │                │                                │
│            ▼                ▼                                │
│  ┌─────────────────┐  ┌─────────────────┐                   │
│  │  CONTENT GEN    │  │   CONFIG        │                   │
│  │ (content_gen.py)│  │  (config.py)    │                   │
│  └─────────────────┘  └─────────────────┘                   │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                      DATA SOURCES                            │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  communes-france-avec-polygon-2025.json (62 Mo)     │    │
│  │  - 6477 communes du Sud-Est                         │    │
│  │  - Données INSEE complètes                          │    │
│  │  - Coordonnées GPS                                  │    │
│  └─────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Installation

### Prérequis

- Python 3.10+
- pip
- Git LFS (pour les fichiers volumineux)

### Étapes

```bash
# 1. Cloner le repository
git clone https://github.com/lkmeldv/annuaire-ville-plusieurs-metiers.git
cd annuaire-ville-plusieurs-metiers

# 2. Récupérer les fichiers LFS
git lfs pull

# 3. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Lancer l'application
python app.py
```

L'application sera accessible sur : **http://127.0.0.1:8989**

### Installation avec Meilisearch (optionnel)

```bash
# Installer Meilisearch (Mac)
brew install meilisearch

# Lancer Meilisearch
meilisearch --master-key="votre_clé_secrète"

# Configurer dans config.py
MEILISEARCH_URL = 'http://localhost:7700'
MEILISEARCH_KEY = 'votre_clé_secrète'
```

---

## ⚙️ Configuration

### 📘 Guide complet

**Voir le guide de configuration détaillé :** [CONFIGURATION.md](CONFIGURATION.md)

Ce guide explique comment :
- Modifier le numéro de téléphone
- Activer/désactiver des départements
- Ajouter de nouveaux métiers
- Personnaliser le contenu généré

### Configuration rapide

#### 1. Numéro de téléphone

Modifiez dans `config.py` :

```python
# Configuration contact
PHONE_NUMBER = '04 58 10 57 19'      # Numéro affiché
PHONE_NUMBER_RAW = '0458105719'      # Pour les liens tel:
```

#### 2. Départements

Activez/désactivez les départements souhaités :

```python
DEPARTMENTS = {
    '01': 'Ain',          # Activé
    # '02': 'Aisne',     # Désactivé (commenté)
    '75': 'Paris',        # Activé
    # ...
}
```

#### 3. Métiers

Ajoutez vos métiers dans `config.py` :

```python
CATEGORIES = {
    'couvreur': 'Couvreur',
    'plombier': 'Plombier',
    # Ajoutez le vôtre :
    'electricien': 'Électricien',
}
```

#### 4. Meilisearch (optionnel)

```python
MEILISEARCH_URL = os.getenv('MEILISEARCH_URL', 'http://localhost:7700')
MEILISEARCH_KEY = os.getenv('MEILISEARCH_KEY', '')
```

---

## 📖 Utilisation

### Démarrage rapide

```bash
# Activer l'environnement virtuel
source venv/bin/activate

# Lancer le serveur
python app.py
```

### URLs principales

| URL | Description |
|-----|-------------|
| `/` | Page d'accueil |
| `/category/{slug}` | Liste des départements par catégorie |
| `/category/{slug}/department/{code}` | Villes d'un département |
| `/address/{slug}/{commune}` | Fiche détaillée d'une commune |
| `/search` | Page de recherche |
| `/sitemap` | Plan du site |
| `/sitemap.xml` | Sitemap XML pour Google |
| `/sitemap-html` | Sitemap HTML navigable |

### Exemples d'URLs

```
/category/architecte-interieur
/category/architecte-interieur/department/74
/address/architecte-interieur/annecy
/search?q=Lyon&category=plombier
```

---

## 📁 Structure du projet

```
annuaire-ville-plusieurs-metiers/
│
├── 📄 app.py                      # Application Flask principale
├── 📄 config.py                   # Configuration globale
├── 📄 content_generator.py        # Générateur de contenu spinné
├── 📄 data_processor_json.py      # Traitement des données communes
├── 📄 data_processor.py           # Processeur alternatif (CSV)
├── 📄 generator.py                # Générateur de pages statiques
├── 📄 requirements.txt            # Dépendances Python
├── 📄 .gitignore                  # Fichiers ignorés par Git
├── 📄 .gitattributes              # Configuration Git LFS
├── 📄 README.md                   # Documentation
│
├── 📂 templates/                  # Templates Jinja2
│   ├── 📄 base.html               # Template de base (header, footer, nav)
│   ├── 📄 home.html               # Page d'accueil
│   ├── 📄 departments.html        # Liste des départements
│   ├── 📄 department_cities.html  # Villes par département
│   ├── 📄 city.html               # Liste des adresses par ville
│   ├── 📄 address_detail.html     # Fiche détaillée (⭐ page principale)
│   ├── 📄 search.html             # Page de recherche
│   ├── 📄 sitemap.html            # Plan du site
│   ├── 📄 sitemap_html.html       # Sitemap HTML
│   └── 📄 category.html           # Page catégorie
│
├── 📂 static/                     # Fichiers statiques (CSS, JS, images)
│
├── 📂 generated/                  # Pages HTML générées (optionnel)
│
└── 📂 venv/                       # Environnement virtuel Python
```

### Description des fichiers clés

#### `app.py`
Application Flask avec toutes les routes :
- Routes de navigation (catégories, départements, villes)
- Route de recherche avec fallback
- API JSON pour recherche AJAX
- Génération dynamique des sitemaps

#### `content_generator.py`
Génération de contenu unique par page :
- Templates d'introduction (4+ variations)
- Templates de description (4+ variations)
- Templates d'expertise par métier
- Templates de conclusion avec CTA

#### `data_processor_json.py`
Traitement des données :
- Chargement du JSON des communes
- Filtrage par département
- Calcul des distances (Haversine)
- Indexation Meilisearch
- Recherche textuelle

---

## 🔌 API Endpoints

### Recherche JSON

```http
GET /api/search?q={query}&category={category}&limit={limit}
```

| Paramètre | Type | Description |
|-----------|------|-------------|
| `q` | string | Terme de recherche |
| `category` | string | Filtre par catégorie (optionnel) |
| `limit` | int | Nombre de résultats (défaut: 10) |

**Exemple de réponse :**

```json
{
  "results": [
    {
      "id": "74010",
      "nom_commune": "Annecy",
      "code_postal": "74000",
      "department": "74",
      "category": "architecte-interieur",
      "population": 128422,
      "lat": 45.899247,
      "lon": 6.129384
    }
  ]
}
```

### Sitemap XML

```http
GET /sitemap.xml
```

Retourne un sitemap XML valide pour Google Search Console.

---

## 🔍 SEO & Référencement

### Optimisations intégrées

#### Balises Meta
- Title dynamique : `{Commune} - {Métier}`
- Description unique par page
- Canonical URL

#### Schema.org
```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Architecte d'intérieur - Annecy",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Annecy",
    "postalCode": "74000"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": 45.899247,
    "longitude": 6.129384
  }
}
```

#### Sitemaps
- **XML** : `/sitemap.xml` - Pour Google Search Console
- **HTML** : `/sitemap-html` - Pour le crawl interne

#### Maillage interne
- Liens vers communes proches (rayon 20km)
- Liens entre catégories de métiers
- Fil d'Ariane (breadcrumb)
- Footer avec liens sitemaps

### Contenu unique

Chaque page génère un contenu unique grâce au système de templates :

```python
# 4 introductions × 4 descriptions × 4 expertises × 4 conclusions
# = 256 combinaisons possibles par catégorie
```

---

## 🎨 Personnalisation

### Modifier le design

Le projet utilise **TailwindCSS** via CDN. Pour personnaliser :

1. Modifier les classes dans les templates HTML
2. Ou ajouter du CSS custom dans `static/css/`

### Modifier les couleurs

Dans `templates/base.html` :

```html
<style>
    .gradient-bg {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
</style>
```

### Ajouter une région

1. Ajouter les codes départements dans `config.py` :

```python
DEPARTMENTS = {
    # ... existants ...
    '75': 'Paris',
    '92': 'Hauts-de-Seine',
}
```

2. Le système chargera automatiquement les communes correspondantes

### Modifier les templates de contenu

Dans `content_generator.py`, modifier ou ajouter des templates :

```python
self.intro_templates_by_category['nouveau-metier'] = [
    "Template personnalisé pour {city}...",
    "Autre template pour {postal_code}..."
]
```

---

## 📦 Dépendances

### requirements.txt

```
flask
pandas
meilisearch
python-slugify
```

### Détail des packages

| Package | Version | Usage |
|---------|---------|-------|
| Flask | 3.x | Framework web |
| Pandas | 2.x | Traitement des données |
| Meilisearch | 0.31+ | Moteur de recherche (optionnel) |
| python-slugify | 8.x | Génération de slugs URL |

### CDN utilisés

| Ressource | Usage |
|-----------|-------|
| TailwindCSS | Framework CSS |
| Font Awesome 6 | Icônes |
| Leaflet.js | Cartes interactives |
| OpenStreetMap | Tiles de carte |

---

## 🗓️ Roadmap

### Version actuelle (1.0)

- [x] 5 catégories de métiers
- [x] 6477 communes
- [x] Recherche Meilisearch + fallback
- [x] Sitemap XML et HTML
- [x] Contenu spinné SEO
- [x] Avis clients
- [x] Maillage interne
- [x] Cartes OpenStreetMap

### Prochaines versions

- [ ] **v1.1** : Export statique HTML (génération de site statique)
- [ ] **v1.2** : Système de vrais avis clients avec modération
- [ ] **v1.3** : Formulaire de contact par professionnel
- [ ] **v1.4** : Dashboard admin
- [ ] **v1.5** : Multi-langue (EN, ES, DE)
- [ ] **v2.0** : Extension nationale (toute la France)

---

## 📄 Licence

Ce projet est **privé**. Tous droits réservés.

---

## 👤 Auteur

Développé avec ❤️ et [Claude Code](https://claude.com/claude-code)

---

## 🆘 Support

Pour toute question ou problème :
1. Ouvrir une issue sur le repository
2. Consulter la documentation ci-dessus

---

<p align="center">
  <strong>🏠 Annuaire Professionnel Multi-Métiers</strong><br>
  <em>Générez des milliers de pages SEO en quelques secondes</em>
</p>

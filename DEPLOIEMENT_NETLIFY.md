# 🌐 Déploiement sur Netlify / Vercel / Render

## ⚠️ IMPORTANT : Flask et Netlify

**Netlify** est conçu pour les sites **statiques** (HTML/CSS/JS).
**Votre projet Flask** est une application **dynamique** (Python).

### ❌ Netlify ne supporte PAS Flask directement

### ✅ Solutions possibles :

1. **Vercel** (recommandé pour Flask) - Gratuit
2. **Render** (simple et gratuit) - Gratuit avec limitations
3. **Générer un site statique** puis Netlify - Complexe
4. **Heroku** - Payant maintenant
5. **Railway** - Gratuit avec limitations

---

## 🚀 Solution 1 : Vercel (RECOMMANDÉ)

**Pourquoi Vercel ?**
- ✅ Support natif de Python/Flask
- ✅ Gratuit
- ✅ HTTPS automatique
- ✅ Déploiement automatique depuis Git
- ✅ Nom de domaine personnalisé gratuit

### Étapes

#### 1. Préparer le projet

Créez un fichier `vercel.json` :

```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

Créez un fichier `requirements.txt` si pas déjà fait :
```
Flask==3.0.0
pandas==2.1.0
python-slugify==8.0.1
meilisearch==0.31.0
```

#### 2. Pousser sur GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/VOTRE_USERNAME/annuaire2.git
git push -u origin main
```

#### 3. Déployer sur Vercel

1. Allez sur https://vercel.com
2. Connectez-vous avec GitHub
3. Cliquez sur "New Project"
4. Sélectionnez votre repo `annuaire2`
5. Vercel détecte automatiquement Python
6. Cliquez sur "Deploy"

**C'est tout !** Votre site sera accessible sur : `https://annuaire2.vercel.app`

#### 4. Ajouter votre domaine (optionnel)

1. Dans les paramètres du projet
2. Allez dans "Domains"
3. Ajoutez votre domaine personnalisé
4. Suivez les instructions DNS

---

## 🎨 Solution 2 : Render (SIMPLE)

**Pourquoi Render ?**
- ✅ Très simple à configurer
- ✅ Support natif Flask
- ✅ Gratuit
- ⚠️ Se met en veille après 15min inactivité

### Étapes

#### 1. Créer un fichier `render.yaml`

```yaml
services:
  - type: web
    name: annuaire-pro
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.11
```

#### 2. Ajouter gunicorn au requirements.txt

```
Flask==3.0.0
pandas==2.1.0
python-slugify==8.0.1
meilisearch==0.31.0
gunicorn==21.2.0
```

#### 3. Modifier app.py (dernière ligne)

```python
if __name__ == '__main__':
    app.run(host=SERVER_HOST, port=SERVER_PORT, debug=False)
```

#### 4. Déployer

1. Allez sur https://render.com
2. Créez un compte
3. "New +" → "Web Service"
4. Connectez GitHub
5. Sélectionnez votre repo
6. Render détecte automatiquement Python
7. Cliquez sur "Create Web Service"

**URL** : `https://annuaire-pro.onrender.com`

---

## 🔧 Solution 3 : PythonAnywhere (TRÈS SIMPLE)

**Le plus simple pour débuter !**

### Étapes

#### 1. Créer un compte

https://www.pythonanywhere.com (gratuit)

#### 2. Uploader les fichiers

- Allez dans "Files"
- Uploadez tous vos fichiers
- Ou clonez depuis Git

#### 3. Créer une Web App

1. Allez dans "Web"
2. "Add a new web app"
3. Choisissez "Flask"
4. Python 3.10
5. Chemin vers app.py : `/home/VOTRE_USERNAME/annuaire2/app.py`

#### 4. Configurer le WSGI file

Éditez le fichier WSGI généré :

```python
import sys
path = '/home/VOTRE_USERNAME/annuaire2'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

#### 5. Recharger

Cliquez sur "Reload" dans l'onglet Web.

**URL** : `https://VOTRE_USERNAME.pythonanywhere.com`

### Ajouter votre domaine

- Gratuit : impossible sur plan gratuit
- Payant (5$/mois) : possible

---

## 📦 Solution 4 : Générer un site statique (COMPLEXE)

Si vous voulez vraiment utiliser Netlify, il faut générer toutes les pages en HTML.

### Créer un script de génération

Créez `generate_static.py` :

```python
from app import app, data_processor
from config import CATEGORIES, DEPARTMENTS
import os

output_dir = 'static_site'
os.makedirs(output_dir, exist_ok=True)

# Générer toutes les pages
with app.test_client() as client:
    # Page d'accueil
    response = client.get('/')
    with open(f'{output_dir}/index.html', 'w', encoding='utf-8') as f:
        f.write(response.data.decode('utf-8'))

    # Pages de catégories
    for category_slug in CATEGORIES.keys():
        response = client.get(f'/category/{category_slug}')
        os.makedirs(f'{output_dir}/category/{category_slug}', exist_ok=True)
        with open(f'{output_dir}/category/{category_slug}/index.html', 'w', encoding='utf-8') as f:
            f.write(response.data.decode('utf-8'))

    # Pages de villes (exemple)
    # ... (il faudrait générer toutes les ~7000 pages)
```

**Problèmes** :
- ❌ Très long à générer (7000+ pages)
- ❌ Recherche ne fonctionnera pas
- ❌ Pas de contenu dynamique
- ❌ Mise à jour complexe

**→ Pas recommandé pour ce projet**

---

## 🆚 Comparaison des solutions

| Solution | Prix | Facilité | Performance | Domaine perso | Recommandé |
|----------|------|----------|-------------|---------------|------------|
| **Vercel** | Gratuit | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ Gratuit | ✅ **OUI** |
| **Render** | Gratuit* | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ✅ Gratuit | ✅ Oui |
| **PythonAnywhere** | Gratuit* | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ❌ Payant | ⭐ Débutant |
| **Railway** | Gratuit* | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ✅ Gratuit | ⭐ Oui |
| **Netlify** | Gratuit | ❌ | ❌ | ✅ | ❌ **NON** |

*Limité en trafic/performances sur plan gratuit

---

## 🎯 Ma recommandation : VERCEL

**Pourquoi ?**
1. ✅ Gratuit sans limitations importantes
2. ✅ Très rapide
3. ✅ HTTPS automatique
4. ✅ Domaine personnalisé gratuit
5. ✅ Déploiement en 2 minutes
6. ✅ Parfait pour Flask

### Setup complet Vercel

#### Fichiers à créer :

**1. `vercel.json`** (à la racine)
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

**2. Modifier `app.py`** (à la fin)
```python
# Pour Vercel
if __name__ != '__main__':
    # En production (Vercel)
    app = app
else:
    # En développement local
    if __name__ == '__main__':
        app.run(host=SERVER_HOST, port=SERVER_PORT, debug=True)
```

**3. Pousser sur GitHub**
```bash
git add vercel.json
git commit -m "Add Vercel config"
git push
```

**4. Déployer sur Vercel**
1. https://vercel.com → Sign up with GitHub
2. Import project
3. Select repo
4. Deploy

**Terminé !** 🎉

URL : `https://your-project.vercel.app`

---

## 📱 Avec votre domaine personnalisé

Une fois déployé sur Vercel/Render :

### 1. Acheter un domaine

- OVH : ~10€/an (.fr)
- Namecheap : ~10$/an (.com)
- Google Domains : ~12$/an

### 2. Configurer le DNS

Dans votre registrar, ajoutez :

**Pour Vercel :**
```
Type: CNAME
Name: @
Value: cname.vercel-dns.com
```

**Pour Render :**
```
Type: CNAME
Name: @
Value: votreapp.onrender.com
```

### 3. Ajouter le domaine dans la plateforme

- **Vercel** : Settings → Domains → Add
- **Render** : Settings → Custom Domain → Add

**Délai :** 5-30 minutes pour la propagation DNS

---

## 🚀 Checklist de déploiement

### Avant de déployer

- [ ] `requirements.txt` est à jour
- [ ] Le numéro de téléphone est correct
- [ ] Les départements souhaités sont activés
- [ ] L'app fonctionne en local

### Choix de la plateforme

- [ ] **Vercel** (recommandé) ← Commencez par ici
- [ ] Render (alternative simple)
- [ ] PythonAnywhere (pour débuter)
- [ ] Railway (moderne)

### Après déploiement

- [ ] Le site est accessible
- [ ] Les pages se chargent
- [ ] Le numéro s'affiche correctement
- [ ] (Optionnel) Domaine personnalisé configuré

---

## 🆘 Problèmes courants

### "Application error" sur Vercel

Vérifiez :
- `vercel.json` est présent
- `requirements.txt` est complet
- Logs dans Vercel Dashboard

### Le site se met en veille (Render)

Normal sur plan gratuit. Solutions :
- Passer au plan payant (7$/mois)
- Utiliser un service de "ping" (UptimeRobot)
- Migrer vers Vercel

### "Module not found"

Ajoutez le module manquant dans `requirements.txt`

---

**Prêt à déployer ?** Suivez le guide Vercel ci-dessus ! 🚀

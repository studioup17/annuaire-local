# 🚀 Guide : Mettre le projet sur GitHub

## 📋 Prérequis

- [ ] Avoir un compte GitHub (créez-en un sur https://github.com si besoin)
- [ ] Git est installé sur votre PC

### Vérifier si Git est installé

Ouvrez PowerShell et tapez :
```bash
git --version
```

Si vous voyez `git version X.X.X`, c'est bon ✅

Si erreur, installez Git : https://git-scm.com/download/win

---

## 🎯 Méthode 1 : Via GitHub Desktop (FACILE - Recommandé)

### Étape 1 : Installer GitHub Desktop

1. Téléchargez : https://desktop.github.com/
2. Installez
3. Connectez-vous avec votre compte GitHub

### Étape 2 : Créer un nouveau repository

1. Dans GitHub Desktop : `File` → `Add local repository`
2. Sélectionnez le dossier `C:\Users\djsad\annuaire2`
3. Cliquez sur "create a repository"
4. Repository name : `annuaire-professionnel` (ou autre nom)
5. Description : "Annuaire professionnel multi-métiers France entière"
6. Cochez "Initialize with README" si vous voulez
7. Cliquez sur "Create Repository"

### Étape 3 : Faire le premier commit

1. GitHub Desktop montre tous les fichiers
2. En bas à gauche, écrivez le message : "Initial commit - Annuaire complet"
3. Cliquez sur "Commit to main"

### Étape 4 : Publier sur GitHub

1. Cliquez sur "Publish repository"
2. Décochez "Keep this code private" si vous voulez que ce soit public
3. Cliquez sur "Publish repository"

**✅ Terminé !** Votre code est sur GitHub !

URL : `https://github.com/VOTRE_USERNAME/annuaire-professionnel`

---

## 🎯 Méthode 2 : Via la ligne de commande (Terminal)

### Étape 1 : Initialiser Git dans votre projet

Ouvrez PowerShell dans `C:\Users\djsad\annuaire2` :

```bash
cd C:\Users\djsad\annuaire2
git init
```

### Étape 2 : Ajouter tous les fichiers

```bash
git add .
```

### Étape 3 : Faire le premier commit

```bash
git commit -m "Initial commit - Annuaire professionnel France entière"
```

### Étape 4 : Créer le repository sur GitHub

1. Allez sur https://github.com
2. Cliquez sur le bouton **+** en haut à droite
3. Choisissez **"New repository"**
4. Repository name : `annuaire-professionnel`
5. Description : "Annuaire professionnel multi-métiers - 101 départements français"
6. Choisissez **Public** ou **Private**
7. **NE COCHEZ PAS** "Initialize with README" (on l'a déjà)
8. Cliquez sur **"Create repository"**

### Étape 5 : Connecter votre projet local à GitHub

GitHub vous donne des commandes, copiez-les. Exemple :

```bash
git remote add origin https://github.com/VOTRE_USERNAME/annuaire-professionnel.git
git branch -M main
git push -u origin main
```

**Remplacez `VOTRE_USERNAME`** par votre nom d'utilisateur GitHub !

### Étape 6 : Envoyer le code

```bash
git push -u origin main
```

Si demandé, entrez vos identifiants GitHub.

**✅ Terminé !** Votre code est sur GitHub !

---

## 📝 Commandes Git courantes

### Vérifier l'état de Git

```bash
git status
```

### Ajouter des modifications

```bash
# Ajouter tous les fichiers modifiés
git add .

# Ajouter un fichier spécifique
git add config.py
```

### Faire un commit

```bash
git commit -m "Description de vos modifications"
```

### Envoyer sur GitHub

```bash
git push
```

### Récupérer les changements depuis GitHub

```bash
git pull
```

---

## 🔐 Problème d'authentification

### Si Git demande username/password à chaque fois

Utilisez un Personal Access Token :

#### 1. Créer un token sur GitHub

1. GitHub → Settings → Developer settings
2. Personal access tokens → Tokens (classic)
3. Generate new token
4. Cochez "repo"
5. Générez et **COPIEZ LE TOKEN** (vous ne le reverrez plus !)

#### 2. Utiliser le token

Quand Git demande le mot de passe, collez le **token** (pas votre mot de passe GitHub).

#### 3. Sauvegarder les identifiants (Windows)

```bash
git config --global credential.helper wincred
```

La prochaine fois, Git se souviendra de vos identifiants.

---

## 📂 Structure du repository sur GitHub

Votre repository contiendra :

```
annuaire-professionnel/
├── app.py
├── config.py
├── content_generator.py
├── data_processor_json.py
├── requirements.txt
├── templates/
├── README.md
├── CONFIGURATION.md
├── DEPLOIEMENT.md
├── GUIDE_RAPIDE.md
├── vercel.json
└── communes-france-avec-polygon-2025 (1).json (si < 100MB)
```

### ⚠️ Fichier JSON trop gros pour GitHub ?

Le fichier JSON fait 62 MB. GitHub limite à 100 MB, donc ça devrait passer.

Si problème, utilisez **Git LFS** :

```bash
git lfs install
git lfs track "*.json"
git add .gitattributes
git add "communes-france-avec-polygon-2025 (1).json"
git commit -m "Add large JSON file with Git LFS"
git push
```

---

## 🎨 Améliorer votre README.md sur GitHub

Créez/modifiez `README.md` pour que votre projet soit attractif :

```markdown
# 🏠 Annuaire Professionnel - France Entière

Annuaire professionnel programmatique couvrant **101 départements français** avec génération automatique de contenu SEO.

## ✨ Fonctionnalités

- 📍 **101 départements** français (métropole + DOM)
- 🛠️ **Génération automatique de contenu** pour tous les métiers
- 📞 **Configuration centralisée** (numéro, départements, métiers)
- 🚀 **~350 000 pages** générables
- 🔍 **Recherche intégrée** (Meilisearch/Pandas)
- 📊 **SEO optimisé** (sitemaps, meta tags, Schema.org)

## 🚀 Installation

\`\`\`bash
git clone https://github.com/VOTRE_USERNAME/annuaire-professionnel.git
cd annuaire-professionnel
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
\`\`\`

## 📖 Documentation

- [Configuration](CONFIGURATION.md)
- [Déploiement](DEPLOIEMENT.md)
- [Guide rapide](GUIDE_RAPIDE.md)

## 🌐 Déploiement

Compatible avec :
- ✅ Vercel (recommandé)
- ✅ Render
- ✅ PythonAnywhere
- ✅ Railway

Voir [DEPLOIEMENT.md](DEPLOIEMENT.md) pour les détails.

## 📊 Statistiques

- Départements : 101
- Communes : ~35 000
- Métiers configurables : Illimité
- Pages générables : ~350 000+

## 📄 Licence

Private
\`\`\`

---

## 🔄 Workflow de travail

### Quand vous modifiez le code

```bash
# 1. Vérifier ce qui a changé
git status

# 2. Ajouter les modifications
git add .

# 3. Commit avec un message clair
git commit -m "Ajout du métier électricien"

# 4. Envoyer sur GitHub
git push
```

### Exemples de messages de commit

✅ **Bons messages :**
- `"Ajout de la génération automatique de contenu"`
- `"Fix: Correction du numéro de téléphone dans les templates"`
- `"Feature: Support de tous les départements français"`
- `"Update: Amélioration du README"`

❌ **Mauvais messages :**
- `"update"`
- `"fix"`
- `"changes"`

---

## 🎯 Déploiement automatique avec Vercel

Une fois sur GitHub, connectez à Vercel :

1. Allez sur https://vercel.com
2. "New Project"
3. Import depuis GitHub
4. Sélectionnez `annuaire-professionnel`
5. Deploy

**Vercel redéploiera automatiquement** à chaque `git push` ! 🚀

---

## 🛡️ Fichiers à NE PAS envoyer sur GitHub

Le fichier `.gitignore` exclut automatiquement :

- ✅ `venv/` (environnement virtuel)
- ✅ `__pycache__/` (cache Python)
- ✅ `*.pyc` (fichiers compilés)
- ✅ `.env` (variables d'environnement sensibles)
- ✅ `*.log` (logs)

**Vérifiez avant de push :**
```bash
git status
```

---

## 📞 Besoin d'aide ?

### Problèmes courants

**Erreur : "fatal: not a git repository"**
```bash
# Vous n'êtes pas dans le bon dossier
cd C:\Users\djsad\annuaire2
git init
```

**Erreur : "Permission denied"**
```bash
# Problème d'authentification
# Utilisez un Personal Access Token (voir section ci-dessus)
```

**Erreur : "File too large"**
```bash
# Utilisez Git LFS (voir section ci-dessus)
git lfs install
git lfs track "*.json"
```

**Conflit lors du push**
```bash
# Récupérez d'abord les changements
git pull
# Résolvez les conflits si besoin
git push
```

---

## ✅ Checklist finale

Avant de push :

- [ ] `.gitignore` créé
- [ ] `git init` exécuté
- [ ] Tous les fichiers ajoutés (`git add .`)
- [ ] Premier commit fait (`git commit -m "..."`)
- [ ] Repository créé sur GitHub
- [ ] Remote ajouté (`git remote add origin ...`)
- [ ] Code envoyé (`git push`)

**C'est bon !** Votre projet est maintenant sur GitHub ! 🎉

---

## 🌐 URL de votre projet

Votre projet sera accessible sur :
```
https://github.com/VOTRE_USERNAME/annuaire-professionnel
```

Partagez cette URL pour que d'autres puissent voir ou cloner votre projet !

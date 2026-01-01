# 🚀 Guide Rapide - Annuaire Professionnel

## ✅ État actuel de votre projet

- ✅ Numéro configuré : **0665137710**
- ✅ Départements actifs : **Charente (16), Charente-Maritime (17)**
- ✅ Métiers : **5 catégories**
- ✅ Le code est prêt et fonctionnel

---

## 🔧 Pour que le numéro s'affiche correctement

### Important : Redémarrer l'application

Après toute modification de `config.py`, vous DEVEZ redémarrer :

```bash
# Dans le terminal où l'app tourne
Ctrl + C

# Relancer
python app.py
```

Puis **rafraîchir le navigateur** : `F5` ou `Ctrl + R`

---

## 📞 Changer le numéro de téléphone

### Étape 1 : Modifier config.py

Ouvrez `C:\Users\djsad\annuaire2\config.py`

Modifiez les lignes 12-13 :
```python
PHONE_NUMBER = 'NOUVEAU_NUMERO'      # Ex: '0612345678'
PHONE_NUMBER_RAW = 'NOUVEAU_NUMERO'  # Ex: '0612345678'
```

### Étape 2 : Redémarrer

```bash
Ctrl + C
python app.py
```

### Étape 3 : Vérifier

Rafraîchir le navigateur (F5)

---

## 🗺️ Modifier les départements

### Activer tous les départements de France

Ouvrez `config.py`, **décommentez** tous les départements :

```python
DEPARTMENTS = {
    # Auvergne-Rhône-Alpes
    '01': 'Ain',
    '03': 'Allier',
    # ... etc
    # Enlevez les # devant chaque ligne
}
```

### N'activer que certains départements

**Exemple : Uniquement Nouvelle-Aquitaine**

Commentez tous les autres avec `#` :
```python
DEPARTMENTS = {
    # '01': 'Ain',  # Commenté = désactivé
    '16': 'Charente',  # Activé
    '17': 'Charente-Maritime',  # Activé
    # ...
}
```

Redémarrez l'application.

---

## 🛠️ Ajouter un métier

### Étape 1 : config.py

```python
CATEGORIES = {
    'couvreur': 'Couvreur',
    'plombier': 'Plombier',
    'electricien': 'Électricien',  # NOUVEAU
}
```

### Étape 2 : Redémarrer

```bash
Ctrl + C
python app.py
```

Le nouveau métier apparaît automatiquement !

---

## 🌐 Mettre en ligne sur un nom de domaine

### Option 1 : VPS (Recommandé) - ~70€/an

**Ce qu'il vous faut :**
1. Un VPS (ex: OVH ~5€/mois)
2. Un nom de domaine (ex: OVH ~10€/an)

**Guide complet :** Voir `DEPLOIEMENT.md`

**Résumé :**
1. Acheter un VPS + domaine
2. Se connecter en SSH : `ssh root@VOTRE_IP`
3. Installer les dépendances
4. Uploader le projet
5. Configurer Nginx
6. Installer SSL (HTTPS gratuit)

**Temps estimé :** 30-60 minutes

### Option 2 : Hébergement gratuit (Limité)

**PythonAnywhere** (gratuit mais limité)
- Site : https://www.pythonanywhere.com
- Gratuit jusqu'à 512MB trafic/jour
- Domaine : `votre-nom.pythonanywhere.com`
- Temps setup : 15 minutes

**Render** (gratuit mais se met en veille)
- Site : https://render.com
- Gratuit
- Se met en veille après 15min inactivité
- Temps setup : 10 minutes

---

## 📊 Vérifications rapides

### Tester que le numéro est OK

```bash
python verifier_numero.py
```

Résultat attendu :
```
[OK] Tout est OK ! Le numero est correctement configure.
[OK] Votre numero 0665137710 s'affichera partout.
```

### Voir les logs en temps réel

Pendant que l'app tourne, vous verrez :
```
✅ 1234 communes chargées depuis le JSON
📊 6170 entrées créées (1234 communes × 5 catégories)
* Running on http://0.0.0.0:8989
```

---

## 🆘 Problèmes fréquents

### Le numéro ne change pas

**Solution :**
1. Vérifiez `config.py` (lignes 12-13)
2. Arrêtez l'application (`Ctrl+C`)
3. Relancez (`python app.py`)
4. Rafraîchissez le navigateur (`F5`)

### L'application ne démarre pas

**Erreur de syntaxe :**
```
SyntaxError: '{' was never closed
```
**Solution :** Vérifiez que tous les `{` ont un `}` correspondant dans `config.py`

**Module manquant :**
```
ModuleNotFoundError: No module named 'flask'
```
**Solution :**
```bash
pip install -r requirements.txt
```

### Pas de communes chargées

**Vérifiez :** Le fichier JSON existe :
```bash
ls "communes-france-avec-polygon-2025 (1).json"
```

**Si absent :**
```bash
git lfs pull
```

---

## 📈 Statistiques de votre configuration actuelle

| Métrique | Valeur |
|----------|--------|
| Départements actifs | 2 |
| Communes estimées | ~1 200 |
| Métiers | 5 |
| Pages générables | ~6 000 |

### Si vous activez tous les départements

| Métrique | Valeur |
|----------|--------|
| Départements | 101 |
| Communes | ~35 000 |
| Métiers | 5 |
| Pages générables | **~175 000** |

---

## 🎯 Prochaines étapes recommandées

### 1. Tester localement (fait ✅)
- Application lancée
- Numéro correct
- Navigation fluide

### 2. Choisir votre hébergement

**Pour un usage professionnel :**
→ VPS + domaine (~70€/an)

**Pour tester :**
→ PythonAnywhere (gratuit)

### 3. Déployer

Suivez le guide : `DEPLOIEMENT.md`

### 4. Optimisation SEO

- Soumettre le sitemap à Google Search Console
- Créer un compte Google My Business
- Ajouter des backlinks
- Créer du contenu supplémentaire

---

## 📚 Documentation

| Fichier | Description |
|---------|-------------|
| `README.md` | Documentation complète du projet |
| `CONFIGURATION.md` | Guide de configuration détaillé |
| `DEPLOIEMENT.md` | **Guide pour mettre en ligne** |
| `GUIDE_RAPIDE.md` | Ce fichier (résumé) |
| `CHANGELOG_v3.md` | Historique des modifications |

---

## ✅ Checklist finale

Avant de déployer :

- [ ] Le numéro est correct : `python verifier_numero.py`
- [ ] Les départements voulus sont activés
- [ ] Les métiers sont configurés
- [ ] L'app fonctionne en local
- [ ] Vous avez choisi un hébergement
- [ ] Vous avez lu `DEPLOIEMENT.md`

**Vous êtes prêt ! 🚀**

---

**Besoin d'aide ?** Relisez ce guide ou consultez `DEPLOIEMENT.md` pour la mise en ligne.

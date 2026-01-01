# ✅ Comment redémarrer l'application après modification

## 🔄 Après avoir modifié config.py

Chaque fois que vous modifiez le fichier `config.py`, vous devez redémarrer l'application pour que les changements prennent effet.

---

## 📋 Étapes à suivre

### 1. Arrêter l'application

Dans votre terminal PowerShell où l'application tourne, appuyez sur :

```
Ctrl + C
```

Vous verrez quelque chose comme :
```
^C
KeyboardInterrupt
(venv) PS C:\Users\djsad\annuaire2>
```

---

### 2. Relancer l'application

```bash
python app.py
```

Attendez de voir :
```
✅ 1234 communes chargées depuis le JSON
📊 9872 entrées créées
 * Running on http://0.0.0.0:8989
```

---

### 3. Rafraîchir le navigateur

Dans votre navigateur, appuyez sur :

**Option 1 : Rafraîchissement simple**
```
F5
```

**Option 2 : Rafraîchissement complet (avec vidage du cache)**
```
Ctrl + Shift + R   (Windows/Linux)
Cmd + Shift + R    (Mac)
```

---

## ✨ Résumé rapide

```
1. Ctrl + C          (arrêter)
2. python app.py     (relancer)
3. F5                (rafraîchir)
```

---

## 🎯 Quand redémarrer ?

Vous devez redémarrer l'application quand vous modifiez :

- ✅ **config.py** (numéro de téléphone, départements, métiers, textes personnalisés)
- ✅ **content_generator.py** (templates de contenu)
- ✅ **app.py** (routes et logique)
- ✅ **data_processor_json.py** (traitement des données)

Vous **n'avez PAS besoin** de redémarrer pour :

- ❌ Fichiers HTML dans `templates/` (rafraîchir le navigateur suffit)
- ❌ Fichiers CSS/JS dans `static/` (rafraîchir le navigateur suffit)
- ❌ Fichiers Markdown (.md)

---

## 🐛 En cas de problème

### L'application ne démarre pas

**Erreur :**
```
SyntaxError: invalid syntax
```

**Solution :**
- Vérifiez votre dernière modification dans `config.py`
- Cherchez les virgules manquantes, crochets mal fermés, etc.

---

### Le numéro ne change pas

**Problème :** Vous avez modifié `PHONE_NUMBER` mais l'ancien numéro s'affiche toujours.

**Solution :**
1. Arrêtez l'application (Ctrl+C)
2. Relancez : `python app.py`
3. Videz le cache du navigateur : `Ctrl + Shift + R`

---

### L'application se ferme toute seule

**Problème :** Vous avez fermé le terminal.

**Solution :**
- Rouvrez PowerShell
- Activez l'environnement virtuel :
  ```bash
  .\venv\Scripts\Activate.ps1
  ```
- Relancez l'application :
  ```bash
  python app.py
  ```

---

## 📞 Modifications courantes

### Changer le numéro de téléphone

**config.py ligne 12-13 :**
```python
PHONE_NUMBER = 'NOUVEAU_NUMERO'
PHONE_NUMBER_RAW = 'NOUVEAU_NUMERO'
```

**Puis :**
```bash
Ctrl + C
python app.py
F5
```

---

### Ajouter un département

**config.py ligne 38+ :**
```python
DEPARTMENTS = {
    '16': 'Charente',
    '17': 'Charente-Maritime',
    '33': 'Gironde',  # NOUVEAU
}
```

**Puis :**
```bash
Ctrl + C
python app.py
F5
```

---

### Modifier les textes personnalisés

**config.py ligne 17+ :**
```python
BREADCRUMB_HOME_TEXT = "Mon Texte"
WHY_CHOOSE_TITLE = "Mon Titre"
# etc.
```

**Puis :**
```bash
Ctrl + C
python app.py
F5
```

---

**C'est tout !** 🎉

Redémarrer l'application est simple et rapide (environ 3-5 secondes).

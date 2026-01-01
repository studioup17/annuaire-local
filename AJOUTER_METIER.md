# 🛠️ Guide : Ajouter un nouveau métier

## ✅ Ce qui a été fait pour "Graphiste"

Le métier **Graphiste** a été ajouté avec succès avec tous les templates de contenu nécessaires.

---

## 📝 Pour ajouter un nouveau métier

### Étape 1 : Ajouter dans config.py

Ouvrez `config.py` et ajoutez votre métier dans `CATEGORIES` (ligne 18+) :

```python
CATEGORIES = {
    'couvreur': 'Couvreur',
    'plombier': 'Plombier',
    'graphiste': 'Graphiste',
    'electricien': 'Électricien',  # NOUVEAU MÉTIER
}
```

**Format :** `'slug-url': 'Nom affiché'`

---

### Étape 2 : Ajouter les templates (OPTIONNEL mais recommandé)

Pour un meilleur contenu SEO, ajoutez des templates dans `content_generator.py`.

#### A. Templates d'introduction (ligne ~17)

Dans `self.intro_templates_by_category`, ajoutez :

```python
'electricien': [
    "Besoin d'un électricien à {city} ? Les professionnels du {postal_code}...",
    "À {city}, les électriciens interviennent pour...",
    "Faites appel aux électriciens de {city} ({postal_code}) pour...",
    "Les spécialistes électricité à {city} assurent..."
],
```

#### B. Templates d'expertise (ligne ~92)

Dans `self.expertise_templates`, ajoutez :

```python
'electricien': [
    "Les électriciens de {city} maîtrisent toutes les installations électriques...",
    "Dans le secteur du {postal_code}, les professionnels de l'électricité...",
    "Les spécialistes électricité de {city} proposent..."
],
```

#### C. Templates de conclusion (ligne ~130)

Dans `self.conclusion_templates_by_category`, ajoutez :

```python
'electricien': [
    "Pour tous vos besoins en électricité à {city}, contactez un professionnel du {postal_code}. Devis gratuit et intervention rapide. Appelez le {phone_number}.",
    "Les électriciens de {city} sont disponibles pour vos dépannages urgents...",
    "Faites confiance aux artisans électriciens de {city}...",
    "Améliorez la sécurité de votre installation électrique à {city}..."
],
```

---

### Étape 3 : Redémarrer l'application

```bash
Ctrl + C
python app.py
```

Le nouveau métier apparaît automatiquement :
- ✅ Sur la page d'accueil
- ✅ Dans le menu de navigation
- ✅ Génération de pages pour toutes les villes

---

## 🎯 Exemple complet : Ajouter "Électricien"

### 1. config.py

```python
CATEGORIES = {
    'couvreur': 'Couvreur',
    'plombier': 'Plombier',
    'graphiste': 'Graphiste',
    'electricien': 'Électricien',
}
```

### 2. content_generator.py

Ajoutez ces 3 blocs :

**Intros :**
```python
'electricien': [
    "Vous recherchez un électricien qualifié à {city} ? Les professionnels du {postal_code} interviennent pour toutes vos installations électriques, dépannages urgents et mises aux normes.",
    "À {city}, les électriciens certifiés du secteur {postal_code} assurent des interventions rapides et sécurisées. Installation, rénovation, dépannage : ils répondent à tous vos besoins.",
    "Faites appel aux électriciens de {city} ({postal_code}) pour garantir la sécurité de votre installation. Devis gratuit, intervention rapide et travaux garantis.",
    "Les spécialistes de l'électricité à {city} maîtrisent les normes en vigueur. Dans le {postal_code}, profitez d'un service professionnel pour tous vos travaux électriques."
],
```

**Expertise :**
```python
'electricien': [
    "Les électriciens de {city} maîtrisent toutes les installations électriques : tableaux électriques, éclairage, domotique et systèmes de sécurité.",
    "Dans le secteur du {postal_code}, les professionnels de l'électricité proposent des solutions modernes : bornes de recharge, panneaux solaires et économies d'énergie.",
    "Les spécialistes électricité de {city} assurent également les diagnostics électriques obligatoires et les mises aux normes pour votre sécurité."
],
```

**Conclusions :**
```python
'electricien': [
    "Pour tous vos besoins en électricité à {city}, contactez un professionnel du {postal_code}. Devis gratuit et sans engagement, intervention rapide. Appelez le {phone_number}.",
    "Les électriciens de {city} sont disponibles 7j/7 pour vos dépannages urgents. Dans le {postal_code}, bénéficiez d'un service de proximité réactif et certifié. Demandez votre devis gratuit.",
    "Panne électrique ou projet de rénovation à {city} ({postal_code}) ? Les électriciens locaux interviennent rapidement. Contactez-nous pour un diagnostic gratuit.",
    "Faites confiance aux artisans électriciens de {city} pour tous vos travaux. Du simple dépannage à la rénovation complète, le {postal_code} dispose de professionnels qualifiés RGE."
],
```

### 3. Redémarrer

```bash
python app.py
```

---

## 📋 Liste des métiers déjà configurés

✅ **Avec templates complets :**
- Couvreur
- Plombier
- Pisciniste
- Vitrier
- Architecte d'intérieur
- **Graphiste** (nouveau)

📝 **Prêts à ajouter** (suggestions dans config.py) :
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

## ⚠️ Important

### Si vous ajoutez un métier SANS templates

Le système utilisera les **templates génériques** :
- ✅ Ça fonctionnera
- ⚠️ Mais le contenu sera moins pertinent
- ⚠️ Moins bon pour le SEO

### Si vous ajoutez les templates

- ✅ Contenu unique et adapté au métier
- ✅ Meilleur SEO
- ✅ Expérience utilisateur améliorée

---

## 🔧 Variables disponibles dans les templates

Utilisez ces variables dans vos textes :

- `{city}` : Nom de la ville (ex: "Bordeaux")
- `{postal_code}` : Code postal (ex: "33000")
- `{profession}` : Nom du métier avec majuscule (ex: "Électricien")
- `{profession_lower}` : Nom du métier en minuscule (ex: "électricien")
- `{phone_number}` : Votre numéro de téléphone (ex: "0665137710")

**Exemple :**
```python
"Les {profession_lower}s de {city} interviennent dans le {postal_code}. Appelez le {phone_number}."
```

Devient :
```
Les électriciens de Bordeaux interviennent dans le 33000. Appelez le 0665137710.
```

---

## 🎉 Résultat

Après ajout d'un nouveau métier :

| Métier | Villes | Pages générées |
|--------|--------|----------------|
| 1 métier | 1 200 villes | ~1 200 pages |
| 6 métiers | 1 200 villes | ~7 200 pages |
| 10 métiers | 1 200 villes | ~12 000 pages |

**Avec tous les départements français :**
- 35 000 communes × 10 métiers = **350 000 pages** ! 🚀

---

## 💡 Conseils

### Pour un contenu de qualité

1. **Variez les formulations** (4 templates minimum par section)
2. **Utilisez des mots-clés pertinents** pour le SEO
3. **Restez naturel** et évitez le spam de mots-clés
4. **Incluez le numéro** dans au moins 1 template de conclusion

### Pour gagner du temps

- Copiez un métier similaire existant
- Modifiez les termes spécifiques
- Adaptez les services proposés

---

**Besoin d'aide pour ajouter un métier ?** Suivez ce guide étape par étape ! 🚀

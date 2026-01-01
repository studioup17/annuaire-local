# 🚀 Guide de déploiement sur un nom de domaine

## Étape 1 : Redémarrer l'application (pour le numéro de téléphone)

**Important :** Après avoir modifié `config.py`, vous DEVEZ redémarrer complètement l'application.

### Dans le terminal

1. **Arrêter l'application** : `Ctrl + C`
2. **Relancer** : `python app.py`
3. **Rafraîchir le navigateur** : `F5` ou `Ctrl + R`

Le numéro **0665137710** devrait maintenant apparaître partout.

---

## Étape 2 : Mettre le site sur un nom de domaine

Vous avez plusieurs options selon votre budget et vos besoins.

---

## 🌐 Option 1 : Hébergement VPS (Recommandé)

### Fournisseurs recommandés

| Fournisseur | Prix/mois | RAM | Bande passante |
|-------------|-----------|-----|----------------|
| **OVH** | ~3-5€ | 2GB | Illimitée |
| **Contabo** | ~5-7€ | 4GB | Illimitée |
| **DigitalOcean** | $6 | 1GB | 1TB |
| **Hetzner** | ~4€ | 2GB | 20TB |

### Étapes de déploiement

#### 1. Acheter un VPS

Exemple avec **OVH** (français, facile) :
1. Allez sur https://www.ovhcloud.com/fr/vps/
2. Choisissez "VPS Starter" (~5€/mois)
3. Sélectionnez Ubuntu 22.04 comme OS
4. Validez la commande

#### 2. Acheter un nom de domaine

Où acheter :
- **OVH** : https://www.ovhcloud.com/fr/domains/ (~10€/an)
- **Gandi** : https://www.gandi.net/fr (~15€/an)
- **Namecheap** : https://www.namecheap.com/ (~10$/an)

Exemples de noms :
- `annuaire-pro-france.fr`
- `artisans-nouvelle-aquitaine.fr`
- `mon-artisan-local.com`

#### 3. Pointer le domaine vers le VPS

Dans l'interface de votre registrar (OVH, Gandi, etc.) :

**Configuration DNS :**
```
Type : A
Nom : @
Valeur : [IP de votre VPS]
TTL : 3600

Type : A
Nom : www
Valeur : [IP de votre VPS]
TTL : 3600
```

**Exemple :**
```
A    @    51.178.45.123
A    www  51.178.45.123
```

#### 4. Se connecter au VPS

**Sur Windows (PowerShell ou cmd) :**
```bash
ssh root@VOTRE_IP_VPS
```

Exemple :
```bash
ssh root@51.178.45.123
```

#### 5. Installer les dépendances sur le VPS

```bash
# Mise à jour du système
apt update && apt upgrade -y

# Installer Python et les outils
apt install -y python3 python3-pip python3-venv git nginx certbot python3-certbot-nginx

# Installer Git LFS
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
apt install -y git-lfs
```

#### 6. Cloner votre projet

**Option A : Via Git (si votre code est sur GitHub/GitLab)**
```bash
cd /var/www
git clone https://github.com/VOTRE_USERNAME/annuaire2.git
cd annuaire2
git lfs pull
```

**Option B : Uploader manuellement**
Sur votre PC Windows :
```bash
scp -r C:\Users\djsad\annuaire2 root@VOTRE_IP:/var/www/
```

#### 7. Installer les dépendances Python

```bash
cd /var/www/annuaire2
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 8. Tester l'application

```bash
python app.py
```

Si ça fonctionne, arrêtez avec `Ctrl+C`.

#### 9. Créer un service systemd (pour que l'app tourne en permanence)

```bash
nano /etc/systemd/system/annuaire.service
```

Copiez ce contenu :
```ini
[Unit]
Description=Annuaire Professionnel Flask App
After=network.target

[Service]
User=root
WorkingDirectory=/var/www/annuaire2
Environment="PATH=/var/www/annuaire2/venv/bin"
ExecStart=/var/www/annuaire2/venv/bin/python app.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Sauvegardez : `Ctrl+X`, `Y`, `Entrée`

Activez le service :
```bash
systemctl daemon-reload
systemctl enable annuaire
systemctl start annuaire
systemctl status annuaire
```

#### 10. Configurer Nginx (serveur web)

```bash
nano /etc/nginx/sites-available/annuaire
```

Copiez :
```nginx
server {
    listen 80;
    server_name votre-domaine.fr www.votre-domaine.fr;

    location / {
        proxy_pass http://127.0.0.1:8989;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Remplacez `votre-domaine.fr` par votre vrai domaine.

Activez la configuration :
```bash
ln -s /etc/nginx/sites-available/annuaire /etc/nginx/sites-enabled/
nginx -t
systemctl restart nginx
```

#### 11. Installer le certificat SSL (HTTPS gratuit)

```bash
certbot --nginx -d votre-domaine.fr -d www.votre-domaine.fr
```

Suivez les instructions. Choisissez de rediriger HTTP vers HTTPS.

#### 12. Vérifier que tout fonctionne

Allez sur : `https://votre-domaine.fr`

✅ Votre site est en ligne !

---

## 🆓 Option 2 : Hébergement gratuit (Limité)

### A. PythonAnywhere (Gratuit avec limitations)

**Avantages :**
- Gratuit jusqu'à 512MB de trafic/jour
- Facile à configurer
- Pas besoin de VPS

**Inconvénients :**
- Limité en trafic
- Pas de nom de domaine personnalisé gratuit
- Moins de contrôle

**Étapes :**
1. Créez un compte sur https://www.pythonanywhere.com
2. Allez dans "Web" > "Add a new web app"
3. Choisissez Flask
4. Uploadez vos fichiers via l'interface ou Git
5. Configurez le WSGI file
6. Votre site sera sur : `votre-username.pythonanywhere.com`

Pour un domaine personnalisé : upgrade vers le plan payant (5$/mois)

### B. Render (Gratuit avec limitations)

**Avantages :**
- Gratuit pour commencer
- Déploiement automatique depuis Git
- HTTPS gratuit

**Inconvénients :**
- Se met en veille après 15min d'inactivité
- Redémarre lent

**Étapes :**
1. Créez un compte sur https://render.com
2. Connectez votre repo GitHub
3. Créez un nouveau "Web Service"
4. Render détecte automatiquement Flask
5. Ajoutez votre domaine personnalisé (gratuit)

---

## 🎯 Option 3 : Hébergement mutualisé (Budget moyen)

### Fournisseurs avec support Python

| Fournisseur | Prix/mois | Support Python |
|-------------|-----------|----------------|
| **O2Switch** | 6€ | Oui (cPanel) |
| **PlanetHoster** | 6€ | Oui |
| **A2 Hosting** | 10$ | Oui |

**Note :** L'hébergement mutualisé est moins flexible qu'un VPS pour Flask.

---

## 📋 Checklist de déploiement

### Avant de déployer

- [ ] Le numéro de téléphone est correct dans `config.py`
- [ ] Les départements souhaités sont activés
- [ ] L'application fonctionne en local (`python app.py`)
- [ ] Vous avez acheté un nom de domaine
- [ ] Vous avez un VPS ou un hébergement

### Après le déploiement

- [ ] Le site est accessible via votre domaine
- [ ] Le certificat SSL (HTTPS) est installé
- [ ] Le numéro de téléphone s'affiche correctement
- [ ] Les pages se chargent rapidement
- [ ] Le service systemd tourne en permanence
- [ ] Les logs sont accessibles : `journalctl -u annuaire -f`

---

## 🔧 Maintenance

### Mettre à jour le numéro de téléphone

1. **Sur le VPS :**
```bash
nano /var/www/annuaire2/config.py
```

2. **Modifier les lignes 12-13**
3. **Redémarrer le service :**
```bash
systemctl restart annuaire
```

### Voir les logs

```bash
journalctl -u annuaire -f
```

### Redémarrer l'application

```bash
systemctl restart annuaire
```

### Mettre à jour le code

```bash
cd /var/www/annuaire2
git pull
systemctl restart annuaire
```

---

## 💰 Récapitulatif des coûts

### Solution complète recommandée

| Service | Fournisseur | Prix |
|---------|-------------|------|
| VPS | OVH VPS Starter | 5€/mois |
| Nom de domaine | OVH .fr | 10€/an |
| SSL | Let's Encrypt | Gratuit |
| **TOTAL** | | **~70€/an** |

### Solution gratuite (limitée)

| Service | Fournisseur | Prix |
|---------|-------------|------|
| Hébergement | PythonAnywhere | Gratuit |
| Domaine | Sous-domaine fourni | Gratuit |
| SSL | Inclus | Gratuit |
| **TOTAL** | | **0€/an** |

**Limitations :** 512MB trafic/jour, pas de domaine personnalisé

---

## 🆘 Support

### Problèmes courants

**Q: Le site ne charge pas**
```bash
# Vérifier que le service tourne
systemctl status annuaire

# Vérifier les logs
journalctl -u annuaire -f

# Vérifier Nginx
systemctl status nginx
```

**Q: Erreur 502 Bad Gateway**
```bash
# Vérifier que l'app Flask tourne
systemctl restart annuaire
```

**Q: Le numéro ne change pas**
```bash
# Vérifier la config
cat /var/www/annuaire2/config.py

# Redémarrer
systemctl restart annuaire
```

---

## 📞 Pour aller plus loin

### Optimisations

- **CDN** : Cloudflare (gratuit) pour accélérer le site
- **Cache** : Redis pour améliorer les performances
- **Base de données** : PostgreSQL pour gérer plus de données
- **Monitoring** : UptimeRobot pour surveiller la disponibilité

### Sécurité

- **Firewall** : Configurer UFW sur le VPS
- **Fail2Ban** : Protection contre les attaques par force brute
- **Backups** : Sauvegardes automatiques quotidiennes

---

**Besoin d'aide pour le déploiement ?** Dites-moi quelle option vous choisissez et je vous guide étape par étape ! 🚀

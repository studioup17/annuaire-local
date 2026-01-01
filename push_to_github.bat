@echo off
REM Script pour envoyer le projet sur GitHub
REM Auteur: Claude
REM Date: 2026-01-01

echo ===============================================
echo   ENVOI DU PROJET SUR GITHUB
echo ===============================================
echo.

REM Vérifier si Git est installé
git --version >nul 2>&1
if errorlevel 1 (
    echo [ERREUR] Git n'est pas installé !
    echo Téléchargez Git sur : https://git-scm.com/download/win
    pause
    exit /b 1
)

echo [OK] Git est installé
echo.

REM Vérifier si c'est déjà un repo Git
if not exist .git (
    echo [INFO] Initialisation du repository Git...
    git init
    echo [OK] Repository Git créé
) else (
    echo [OK] Repository Git déjà initialisé
)
echo.

REM Ajouter tous les fichiers
echo [INFO] Ajout de tous les fichiers...
git add .
echo [OK] Fichiers ajoutés
echo.

REM Demander le message de commit
set /p commit_msg="Message de commit (appuyez sur Entrée pour 'Initial commit'): "
if "%commit_msg%"=="" set commit_msg=Initial commit - Annuaire professionnel France entière

echo [INFO] Création du commit avec le message : %commit_msg%
git commit -m "%commit_msg%"
if errorlevel 1 (
    echo [INFO] Aucun changement à commiter ou commit déjà fait
)
echo.

REM Vérifier si un remote existe
git remote get-url origin >nul 2>&1
if errorlevel 1 (
    echo ===============================================
    echo   CONFIGURATION DU REPOSITORY GITHUB
    echo ===============================================
    echo.
    echo Pour continuer, vous devez créer un repository sur GitHub :
    echo 1. Allez sur https://github.com
    echo 2. Cliquez sur le bouton + en haut à droite
    echo 3. Choisissez "New repository"
    echo 4. Nom : annuaire-professionnel
    echo 5. Cliquez sur "Create repository"
    echo.
    echo Une fois créé, GitHub vous donnera une URL comme :
    echo https://github.com/VOTRE_USERNAME/annuaire-professionnel.git
    echo.
    set /p repo_url="Collez l'URL de votre repository GitHub : "

    if "%repo_url%"=="" (
        echo [ERREUR] URL vide. Abandon.
        pause
        exit /b 1
    )

    echo [INFO] Ajout du remote origin...
    git remote add origin %repo_url%
    echo [OK] Remote ajouté
) else (
    echo [OK] Remote origin déjà configuré
)
echo.

REM Renommer la branche en main si nécessaire
git branch -M main

REM Envoyer sur GitHub
echo [INFO] Envoi du code sur GitHub...
echo.
git push -u origin main

if errorlevel 1 (
    echo.
    echo ===============================================
    echo   ERREUR LORS DE L'ENVOI
    echo ===============================================
    echo.
    echo Problèmes possibles :
    echo 1. Mauvais username/password
    echo 2. Besoin d'un Personal Access Token
    echo 3. Repository déjà existant avec des fichiers
    echo.
    echo Solution :
    echo - Utilisez un Personal Access Token au lieu du mot de passe
    echo - Voir GITHUB_GUIDE.md section "Problème d'authentification"
    echo.
    pause
    exit /b 1
)

echo.
echo ===============================================
echo   SUCCÈS !
echo ===============================================
echo.
echo [OK] Votre code est maintenant sur GitHub !
echo.
echo Vous pouvez voir votre projet sur :
git remote get-url origin
echo.
echo Pour les prochaines modifications :
echo   git add .
echo   git commit -m "Votre message"
echo   git push
echo.
pause

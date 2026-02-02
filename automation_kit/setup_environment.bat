@echo off
chcp 65001 > nul
setlocal
echo [SETUP] Installation de Magellan Console Merger...

REM 1. Copie du Moteur (Depuis ../release)
if exist "..\release\consolemerger-for2.1.1.jar" (
    copy /Y "..\release\consolemerger-for2.1.1.jar" ".\consolemerger-for2.1.1.jar" > nul
    echo [OK] Moteur installe.
) else (
    echo [ERREUR] JAR introuvable dans ..\release
    echo Avez-vous telecharge tout le projet ?
    pause & exit /b
)

REM 2. Copie des Librairies (Depuis ../libs_2.1.1)
if not exist "lib" mkdir lib
if exist "..\libs_2.1.1" (
    xcopy /S /Y "..\libs_2.1.1\*" ".\lib\" > nul
    echo [OK] Dependances installees.
) else (
    echo [ATTENTION] Dossier ..\libs_2.1.1 introuvable.
)

REM 3. Creation des dossiers de travail
for %%D in (input output logs etc rules) do if not exist "%%D" mkdir %%D

echo.
echo [SUCCES] Environnement pret.
echo ---------------------------------------------------
echo ACTION REQUISE :
echo 1. Copiez vos dossiers 'etc' et 'rules' du jeu Magellan ICI.
echo 2. Lancez 'run_auto_merge.bat' pour fusionner.
echo ---------------------------------------------------
pause

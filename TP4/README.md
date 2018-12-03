Équipe Bravo

Gabriel Lemyre
Renaud Bissonnette
Evelyne Lafontaine-Michel
Tony Trau

Démonstration: https://streamable.com/0fg07  
Git: https://github.com/Rendoc/LOG8430

# Installation Automatique

## Étape 0 - Création de la VM (Ubuntu Server 18.04)
  Association du port 5000 de la vm à celui de la machine physique.  
    settings > network > adapter 1 (attached to nat) > advanced > Port fowarding > add new port fowarding rule > HOST PORT = 5000 et GUEST PORT = 5000. 
    Laisser les autres options par défaut.

## Étape 1 - Cloner le projet
  Une fois sur la machine virtuelle.
  ```
  git clone https://github.com/Rendoc/LOG8430.git
  ```

## Étape 2 - Exécuter le script d'installation  
    cd LOG8430/TP4/
    sudo ./run.sh 

  Attendre la fin de l'installation

## Étape 3 - Lancer le client

Sur la machine physique:  

Executer ```python3 client.py --action ADD``` pour ajouter des produits.  
Executer ```python3 client.py --action MOST``` pour recuperer les produits les plus fréquents.  
Vous pouvez aussi spécifier le port et le lien du rest API avec --server et --port  
Exemple: ```python3 client.py --server http://localhost --port 5000 --action MOST```  
Pour plus d'information sur les paramètres ```python3 client.py --help```  

_________________________________________________________________________________________________


# Installation Manuelle

## Étape 0 - Création de la VM (ubuntu server 18.04)
  Association du port 5000 de la vm à celui de la machine physique.  
    settings > network > adapter 1 (attached to nat) > advanced > Port fowarding > add new port fowarding rule > HOST PORT = 5000 et GUEST PORT = 5000. 
    Laisser les autres options par défaut.

## Étape 1 - Préparation de l'environnement
  ```
  sudo apt-get install python-pip 
  sudo apt-get install python2.7
  sudo apt-get install mongodb
  sudo apt-get install openjdk-8-jre-headless
  ```

## Étape 2 - Démarrer le service mongo
  ```
  service mongodb start
  ```

## Étape 3 - Installation des dépendances python du projet
  ```
  pip --no-cache-dir install -r TP4/application/requirements.txt
  ```

## Étape 4 - Partir le serveur
  ```
  python2.7 application/app.py
  ```

## Étape 5 - Lancer le client
Sur la machine physique:  

Executer ```python3 client.py --action ADD``` pour ajouter des produits  
Executer ```python3 client.py --action MOST``` pour recuperer les produits les plus fréquents.  
Vous pouvez aussi spécifier le port et le lien du rest API avec --server et --port  
Exemple: ```python3 client.py --server http://localhost --port 5000 --action MOST```  
```python3 client.py --help``` pour plus d'information sur les paramètres.  


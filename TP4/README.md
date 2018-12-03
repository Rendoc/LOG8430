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

_________________________________________________________________________________________________


# Justifications des technologies

## API et client REST

Pour l'API et le client REST, nous avons choisi d'utiliser le langage Python puisque c'est un langage simple avec lequel nous étions déjà familier.
Nous avons utiliser le framework Flask afin de créer notre API et de définir les routes puisque c'est une framework extrêmement facile à utiliser
et que la quantité de travaille pour arriver à un API avec les 3 routes dont nous avions besoin est minime. De plus, il existe plusieurs driver facile
à utiliser pour les autres technologies nécessaires à ce projet, soit un driver MongoDB et un driver Spark.

## Base de données

Pour la base de données, nous avons utilisé MongoDB puisque nous avions déjà travaillé avec cette technologie auparavant et que nous savions qu'elle
est simple d'utilisation. L'accès aux données sous format JSON nous permet de facilement afficher ces données dans notre navigateur ainsi que de les
manipuler aisément. De plus, nous avions accès à pymongo, un driver en python qui nous permet d'intégrer facilement MongoDB à notre application.

## Architecture

Nous avons opté pour une architecture à une seule machine virtuelle puisque nous avons éprouvé beacoup de difficultés à faire fonctionner Spark sur une
architecture déployée sur plusieurs machines virtuelles. En effet, nous étions capable d'envoyer les jobs aux VM avec le master et les slaves, mais l'exécution
de ces jobs restait toujours prise et ne finissait jamais. Après plusieurs heures de débogage, nous avons opté de simplement faire une architecture à
une machine virtuelle.

Voici une démonstration de notre architecture avec le cluster Master - slave dans 3 vm différentes. Comme mentionné plus haut, la job spark reste stuck au stage 0.
Le cluster fonctionne sans problème pour les jobs d'examples, trouvé dans spark/examples/python, le calcul de PI ou bien le wordcount fonctionne très bien.
On voit aussi dans la vidéo la soumission du flux de travail ainsi que les statisituqes sur celle-ci. Le problème que nous avons rencontré, selon les ressources 
sur internet est le manque de mémoire et un problème de ressource dans la configuration de nos machines slaves.

Démonstration: https://streamable.com/knhqe

Dans la démonstration, on voit nos 3 machines virtuelles, la soumission d'une job venant de notre API qui ne finie jamais.

Configuration du cluster master slave: https://medium.com/ymedialabs-innovation/apache-spark-on-a-multi-node-cluster-b75967c8cb2b


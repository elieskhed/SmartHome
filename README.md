# Projet : Gestion des Appareils Domestiques

Ce projet Python fournit une structure simple pour gérer des appareils domestiques dans une maison connectée. Il comprend des classes pour les appareils, les capteurs d'humidité, les lumières, et une maison qui agrège les appareils.

## Structure des Fichiers

### **`device.py`**
Fournit une classe de base pour représenter un appareil générique.

#### Classe : `device`

- **Attributs** :
  - `__nom` : Nom de l'appareil (privé).

- **Méthodes** :
  - `__init__(nom)` : Initialise un appareil avec un nom.
  - `get_nom()` : Retourne le nom de l'appareil.
  - `__str__()` : Retourne une représentation sous forme de chaîne de l'appareil.

---

### **`house.py`**
Gère une collection d'appareils domestiques.

#### Classe : `house`

- **Attributs** :
  - `appareils` : Liste des appareils ajoutés dans la maison.

- **Méthodes** :
  - `__init__()` : Initialise une maison vide.
  - `ajouter_appareil(appareil)` : Ajoute un appareil à la liste.
  - `retirer_appareil(appareil)` : Retire un appareil de la liste.
  - `afficher_etat()` : Affiche l'état de tous les appareils de la maison.

---

### **`humidity_sensor.py`**
Implémente un capteur d'humidité basé sur la classe `device`.

#### Classe : `humidity_sensor`

- **Héritage** : Hérite de `device`.

- **Attributs** :
  - `__value` : Valeur d'humidité (privé).
  - `nom` : Nom unique pour le capteur basé sur un ID.

- **Méthodes** :
  - `__init__(id)` : Initialise un capteur avec un ID unique.
  - `getValue()` : Retourne une valeur d'humidité simulée.
  - `__str__()` : Retourne une chaîne descriptive du capteur.

---

### **`lumiere.py`**
Implémente une lumière contrôlable basée sur la classe `device`.

#### Classe : `lumiere`

- **Héritage** : Hérite de `device`.

- **Attributs** :
  - `__etat` : État de la lumière (privé, `True` pour allumé, `False` pour éteint).
  - `nom` : Nom unique pour la lumière basé sur un ID.

- **Méthodes** :
  - `__init__(id, etat=False)` : Initialise une lumière avec un ID et un état initial (par défaut : éteint).
  - `allumer()` : Allume la lumière.
  - `eteindre()` : Éteint la lumière.
  - `__str__()` : Retourne une chaîne descriptive de l'état de la lumière.

---

## Exemples d'Utilisation

### Ajouter des appareils dans une maison
```python
from house import house
from humidity_sensor import humidity_sensor
from lumiere import lumiere

# Créer une maison
ma_maison = house()

# Ajouter des appareils
capteur_humidite = humidity_sensor(id="001")
lumiere_cuisine = lumiere(id="cuisine")

ma_maison.ajouter_appareil(capteur_humidite)
ma_maison.ajouter_appareil(lumiere_cuisine)

# Afficher l'état des appareils
ma_maison.afficher_etat()
```

### Contrôler une lumière
```python
# Allumer une lumière
lumiere_cuisine.allumer()
print(lumiere_cuisine)  # Lumière cuisine - Allumée

# Éteindre une lumière
lumiere_cuisine.eteindre()
print(lumiere_cuisine)  # Lumière cuisine - Éteinte
```

---

## Suggestions de Capteurs à Ajouter
Voici quelques suggestions pour étendre les fonctionnalités de ce projet avec de nouveaux capteurs et appareils :

1. **Capteur de température** :
   - Mesurer et afficher la température ambiante.
   - Exemple de classe : `temperature_sensor`.

2. **Capteur de luminosité** :
   - Mesurer l'intensité lumineuse dans une pièce.
   - Exemple de classe : `light_sensor`.

3. **Détecteur de mouvement** :
   - Détecter la présence ou le mouvement dans une pièce.
   - Exemple de classe : `motion_sensor`.

4. **Capteur de qualité de l'air** :
   - Mesurer la qualité de l'air (CO2, particules fines).
   - Exemple de classe : `air_quality_sensor`.

5. **Prises intelligentes** :
   - Contrôler l'alimentation des appareils connectés.
   - Exemple de classe : `smart_plug`.

6. **Capteur de fuite d'eau** :
   - Détecter la présence d'eau sur le sol pour prévenir les inondations.
   - Exemple de classe : `water_leak_sensor`.

---



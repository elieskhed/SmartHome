# Create a README.md file with the content

readme_content = """
# Projet IoT - Gestion de Maison Intelligente

Ce projet implémente un système de gestion d'appareils connectés (IoT) dans une maison, avec des capteurs et des dispositifs contrôlés via MQTT. Les principaux composants incluent des capteurs d'humidité, des lumières, et une classe principale pour gérer la maison.



## Fonctionnalités

- Gestion des appareils connectés via MQTT.
- Publication des données des appareils sous forme JSON.
- Support pour des capteurs d'humidité et des lumières.
- Publication périodique configurable des données des appareils.

---

## Architecture

Le projet est organisé comme suit :

- **`device.py`** : Classe abstraite de base pour tous les appareils connectés.
- **`house.py`** : Gestion des appareils dans une maison et envoi des données via MQTT.
- **`humidity_sensor.py`** : Implémentation d'un capteur d'humidité.
- **`lumiere.py`** : Implémentation d'une lumière connectée.
- **`main.py`** : Point d'entrée principal du projet.


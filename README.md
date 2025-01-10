# SmartHome

## Simul iot

## Server

### Mosquitto
#### Commandes openssl pour générer les certificats

##### Autorité de Certifications CA
La CA se chargera d'autosigner les certificats clients, **CA.crt** sera publique et accessible par chaque clients.
A placer dans `/etc/mosquitto/ca_certificates`:

Clès Privée `CA.key`:
`openssl genrsa -out CA.key 2048`

Certificat `CA.crt` (expire dans 365 jours):
`openssl req -x509 -new -nodes -key CA.key -sha256 -days 365 -out CA.crt`
Mettre en **Common Name (CN)**, IntelighouseCA par exemple

##### Certificat Serveur (mosquitto)
A placer dans `/etc/mosquitto/certs`, la création de ce certificat nécéssitera une demande de signature (.csr) qui sera signé par la **CA**.:

Clès Privée `mosquitto.key`:
`openssl genrsa -out mosquitto.key 2048`

Demande de signature `mosquitto.csr`:
`openssl req -new -key mosquitto.key -out mosquitto.csr`

**Tres Important:** Mettre en **CommonName ou FQDN** l'adresse IP du serveur.

Certificat `mosquitto.crt` (expire dans 365 jours) signé par la **CA**:
`openssl x509 -req -in mosquitto.csr -CA ../ca_certificates/CA.crt -CAkey ../ca_certificates/CA.key -CAcreateserial -out mosquitto.crt -days 365 -sha256`

##### Certificat Client (client)
A placer dans `/etc/mosquitto/client`, la création de ce certificat nécéssitera une demande de signature (.csr) qui sera signé par la **CA**.:
Le but par la suite sera d'automatiser la signature par le biais de l'API.

Clès Privée `client.key`:
`openssl genrsa -out client.key 2048`

Demande de signature `client.csr`:
`openssl req -new -key client.key -out client.csr`

Certificat `client.crt` (expire dans 365 jours) signé par la **CA**:
`openssl x509 -req -in client.csr -CA CA.crt -CAkey CA.key -CAcreateserial -out client.crt -days 365 -sha256`


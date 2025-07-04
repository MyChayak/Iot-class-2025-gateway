# 🧩 Mosquitto MQTT Broker with Dynamic Bridge Configuration

This project sets up a **Mosquitto MQTT broker** inside Docker, using a dynamic bridge configuration that reads the target broker's address from an environment variable (`MQTT_BRIDGE_TO`). The configuration is templated and expanded at runtime using `envsubst`.

---

## 📁 Folder Structure

```plaintext
.
├── Dockerfile                  # Custom image to install envsubst
├── docker-compose.yml          # Docker Compose service
├── .env                        # Environment variable file
├── config/
│   └── mosquitto.template.conf # Template for mosquitto.conf
├── data/                       # Persistence data
└── log/                        # Log files

````

---

## ⚙️ Features

- ✅ Mosquitto broker on port `1883`
- ✅ Bridge to remote MQTT broker (address from `.env`)
- ✅ Uses `envsubst` to inject environment variables at container startup
- ✅ Writes generated config to `/tmp/mosquitto.conf`
- ✅ Clean volume mounts for config, data, and logs

---

## 🧾 Example `.env`

Create a `.env` file in the root folder:

```env
MQTT_BRIDGE_TO=192.168.1.105:1883
````

---

## 🧱 Example `config/mosquitto.template.conf`

```conf
persistence true
persistence_location /mosquitto/data/
log_dest file /mosquitto/log/mosquitto.log
log_type all

listener 1883
allow_anonymous true

connection bridge-to-remote
address ${BRIDGE_ADDRESS}
topic iot-frames-model/# both 1
cleansession false
start_type automatic
restart_timeout 10
```

---

## 🐳 Dockerfile

```Dockerfile
FROM eclipse-mosquitto:latest

USER root
RUN apk add --no-cache gettext  # For Alpine base image
USER mosquitto
```

---

## 🚀 Getting Started

```bash
# change to directory gateway
$ cd ~/Iot-class-2025-gateway

# build and start container
$ docker compose up --build 

```
|Option	|Default	|Description|
|--|--|--|
|--build		| |Build images before starting containers|

---


## 💾 **Stop and remove containers, networks**
```bash
# change to directory gateway
$ cd ~/Iot-class-2025-gateway

# build and start container
$ docker compose down --volumes --remove-orphans --rmi local

```

|Option	|Default	|Description|
|--|--|--|
|--remove-orphans		| |Remove containers for services not |defined in the Compose file|
|--rmi		| |Remove images used by services. "local" remove |only images that don't have a custom tag ("local"||"all")|
|-t, --timeout		| |Specify a shutdown timeout in seconds|
|-v, --volumes		| |Remove named volumes declared in the |"volumes" section of the Compose file and anonymous |volumes attached to containers|

---
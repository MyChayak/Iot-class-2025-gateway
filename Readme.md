# 🌉 **VerneMQ Gateway (`vernemqgw`) - MQTT Bridge Service**

### 🔧 **Overview**

This service runs a VerneMQ instance configured as an **MQTT bridge**, which forwards or mirrors MQTT traffic (specific topics) between brokers. This allows you to connect one MQTT broker (VerneMQ) to another (either local or remote), forwarding messages for scalability, redundancy, or cross-network communication.

---

### 🧱 **Service Description**

#### 🔑 **Key Environment Variables**

| Variable                                                                  | Description                                                                      |
| ------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `DOCKER_VERNEMQ_ACCEPT_EULA=yes`                                          | Required to accept VerneMQ's license                                             |
| `DOCKER_VERNEMQ_ALLOW_ANONYMOUS=on`                                       | Allows unauthenticated MQTT clients                                              |
| `DOCKER_VERNEMQ_NODENAME=vernemqgw.local`                                 | Node identity in VerneMQ cluster                                                 |
| `DOCKER_VERNEMQ_DISCOVERY_NODE=vernemqgw.local`                           | Discovery node (for single-node setup)                                           |
| `DOCKER_VERNEMQ_LISTENER__TCP__ALLOWED_PROTOCOL_VERSIONS=3,4,5,131,132`   | Supports MQTT v3.1, v3.1.1, v5 and bridge-specific versions                      |
| `DOCKER_VERNEMQ_PLUGINS__VMQ_BRIDGE=on`                                   | Enables the bridge plugin                                                        |
| `DOCKER_VERNEMQ_VMQ_BRIDGE__TCP__BR0=${MQTT_BRIDGE_TO}`                   | Bridge endpoint (e.g. `127.0.0.1:1889`)                                          |
| `DOCKER_VERNEMQ_VMQ_BRIDGE__TCP__BR0__TOPIC__1=iot-frames-model/* both 1` | Topics to forward: all under `iot-frames-model/*`, bidirectional (in/out), QoS 1 |
| `DOCKER_VERNEMQ_LOG__CONSOLE__LEVEL=info`                                 | Logging level (can be changed to `debug`)                                        |

#### 📦 **Ports**

* `1883`: Standard MQTT port (for client connections)
* `8888`: HTTP API port (optional monitoring or control)
* `8080` (commented): Can be enabled for WebSocket MQTT clients

#### 📂 **Volumes**

* Config (`/vernemq/etc`)
* Data (`/vernemq/data`)
* Logs (`/vernemq/log`)

#### 🌐 **Network**

Part of the custom `iot` bridge network, allowing other services (like Kafka or Prometheus exporters) to access it directly.

---

### 🔁 **MQTT Bridging Use Case**

This container acts as a **gateway broker**, useful when:

* You need to mirror specific topics from edge devices to a central broker
* You want to aggregate MQTT traffic from multiple local brokers
* You're bridging different network segments (e.g., LAN to WAN)

The environment variable `${MQTT_BRIDGE_TO}` should be set to the IP or hostname of the **remote MQTT broker**, such as:

```env
MQTT_BRIDGE_TO=192.168.1.100:1883
```

---

## 💾 **Starting Container**
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
$ docker compose down --volumes --remove-orphans --rmi

```

|Option	|Default	|Description|
|--|--|--|
|--remove-orphans		| |Remove containers for services not |defined in the Compose file|
|--rmi		| |Remove images used by services. "local" remove |only images that don't have a custom tag ("local"||"all")|
|-t, --timeout		| |Specify a shutdown timeout in seconds|
|-v, --volumes		| |Remove named volumes declared in the |"volumes" section of the Compose file and anonymous |volumes attached to containers|

---
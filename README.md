# TP-AySO - Virtualización con Docker y VirtualBox

Este trabajo práctico integrador para la materia **Arquitectura y Sistemas Operativos (AySO)** implementa un entorno educativo que combina:

- Una máquina virtual Ubuntu (VirtualBox)
- Instalación y uso de Docker dentro de la VM
- Desarrollo de una **aplicación cliente-servidor** en Python usando contenedores y Docker Compose

## 📁 Estructura del proyecto

```
TP-AySO/
├── cliente/
│   ├── cliente.py
│   ├── dockerfile
│   └── requirements.txt
├── servidor/
│   ├── servidor.py
│   ├── dockerfile
│   └── requirements.txt
├── docker-compose.yml
```

## 🚀 ¿Qué hace el proyecto?

📦 El servidor convierte un número decimal enviado por el cliente a **binario**, **octal** y **hexadecimal**, usando Flask y comunicación HTTP.

🧪 Ambos servicios corren en contenedores separados conectados por red interna.

## 🛠️ Tecnologías utilizadas

- Python 3.12 (versión slim)
- Docker & Docker Compose
- Flask (servidor) y Requests (cliente)
- Ubuntu 22.04 (virtualizado con VirtualBox)

---

> Proyecto realizado por **Nicolás Pannunzio** y **Nicolás Olima** – Junio 2025

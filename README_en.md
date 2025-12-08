### [English] | [[中文]](./README.md)

# Obico2Bark

### Introduction

This project is a lightweight Flask-based webhook service designed to receive printer event notifications from Obico and forward them to an iPhone through the Bark API. The message is automatically prefixed with [INFO] or [WARN] according to the event type. If the event contains an image URL, the server replaces the LAN address with a public WAN address to ensure external accessibility.

### Requirements

* Python 3.8+
* Obico account and service (self-hosted or cloud)
* Bark app on an iOS device

### Installation

#### Clone the repository:

```bash
git clone https://github.com/haha44444/Obico2Bark.git
cd Obico2Bark
```

#### Install dependencies:

```bash
pip install -r requirements.txt
```

#### Configure settings:

```python
# In the "=== Settings ===" section of the code:
# Your Bark API endpoint, obtained from the Bark app
bark_api_iphone = "https://api.day.app/yourkey"
# Local LAN IP used by the Obico service
lan_ip = "obico service lan ip"
# Public domain or IP address
wan_ip = "domain or ip address"
```

#### Configure Obico:
Set Obico’s webhook URL to:`http://yourip:5086/webhook`

### Usage

#### Run the service:

```bash
python main.py
```

#### Keep it running in the background (Linux):

```bash
nohup python main.py > monitor.log 2>&1 &
```

### Acknowledgments

[Bark](https://github.com/Finb/Bark)
<br>
[Obico](https://github.com/TheSpaghettiDetective)


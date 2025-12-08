import datetime
from flask import Flask, request
import requests

# === Settings ===
bark_api_iphone = "https://api.day.app/yourkey"
lan_ip = "obico service lan ip"
wan_ip = "domain or ip address"
# === Settings End ===

app = Flask(__name__)
logger = app.logger
@app.route("/")
def index():
    return "Webhook started"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json(force=True)
    printer_name = data['printer']['name']
    try:
        image_url = data['img_url']
    except KeyError:
        image_url = ""
    msg = translate_message(data)

    send_msg(f"{bark_api_iphone}/{printer_name}", msg, image_url)
    return data


def tag(prefix):
    def warp(msg):
        return f"{prefix}{msg}"
    return warp


def translate_message(data):
    WARN = tag("[WARN]")
    INFO = tag("[INFO]")

    event_type = data['event']['type']
    if event_type == "PrintFailure":
        if data['event']['print_paused']:
            return WARN("打印失败，已暂停")
        else:
            return WARN("打印失败")
    elif event_type == "PrintStarted":
        return INFO("打印开始")
    elif event_type == "PrintDone":
        return INFO("打印完成")
    elif event_type == "PrintCancelled":
        return INFO("打印取消")
    elif event_type == "PrintPaused":
        return INFO("打印暂停")
    elif event_type == "PrintResumed":
        return INFO("打印恢复")
    elif event_type == "FilamentChange":
        return INFO("耗材更换")
    elif event_type == "HeaterCooledDown":
        return INFO("加热器已冷却")
    elif event_type == "HeaterTargetReached":
        return INFO("加热器已达到目标温度")
    else:
        return WARN(event_type)


def send_msg(api, msg, image_url):
    image_url = image_url.replace(lan_ip, wan_ip)
    url = f"{api}{msg}?icon={image_url}&url={image_url}"
    requests.get(url)
    logger.info(f"{str(datetime.datetime.now())[:19]} 消息已推送至iPhone: {msg}")
    return 0

if __name__ == '__main__':
    app.run('0.0.0.0', 5086)
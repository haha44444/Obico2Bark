### [中文] | [[English]](./README_en.md)

# Obico2Bark
### 简介
本项目是一个基于 Flask 的简易 Webhook 服务，用于接收打印机事件并通过 Bark API 转发至 iPhone。消息会根据事件类型自动添加 [INFO] 或 [WARN] 前缀。如果事件包含图片地址，服务器会将 LAN 地址替换为公网地址，方便外网访问。

### 前置要求
- Python 3.8+
- Obico账户和服务（自托管或官方云服务）
- Bark应用（iOS设备）

### 安装步骤
#### 克隆仓库：
```bash
git clone https://github.com/haha44444/Obico2Bark.git
cd Obico2Bark
```
#### 安装依赖：
```bash
pip install -r requirements.txt
```
#### 修改配置：
```python
# 在代码的"=== Settings ==="部分设置：
# bark的api，去手机中的bark app获取
bark_api_iphone = "https://api.day.app/yourkey"
# obico服务的内网ip
lan_ip = "obico service lan ip"
wan_ip = "domain or ip address"
```
#### 修改Obico配置：

修改obico中的webhook url配置为`http://yourip:5086/webhook`


### 使用方法
运行监控脚本：
```bash
python main.py
```
保持长期运行：(linux)
```bash
nohup python main.py > monitor.log 2>&1 &
```

### 感谢以下项目做出的贡献：

[Bark](https://github.com/Finb/Bark)
<br>
[Obico](https://github.com/TheSpaghettiDetective)

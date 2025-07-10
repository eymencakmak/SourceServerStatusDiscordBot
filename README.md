
# 🎮 Discord Game Server Info Bot

A simple yet powerful Discord bot that displays live information about any A2S-compatible game server (e.g., CS:GO, Team Fortress 2, Garry's Mod, etc.).  
It fetches server name, map, players, and ping, and keeps the message updated every 10 seconds.

## 🚀 Features

- ✅ Real-time server info updates
- 🎮 Player list with play duration
- 📶 Server ping display
- 🌐 Supports any A2S-compatible game server
- 🧹 Automatically deletes old messages to avoid clutter

---

## 🛠️ Requirements

- Python 3.8+
- A Discord bot token
- A2S-compatible game server IP and port

---

## 📦 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/discord-server-info-bot.git
   cd discord-server-info-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set your bot token**
   Open the `main.py` file (or whatever the main script is called) and replace:
   ```python
   bot.run("TOKEN_HERE")
   ```
   with:
   ```python
   bot.run("YOUR_DISCORD_BOT_TOKEN")
   ```

---

## ▶️ Usage

- **Command:** `!server IP:PORT`
- **Example:**  
  ```
  !server 93.113.57.59:27015
  ```

The bot will:
- Delete your command message for cleanliness
- Post an embed showing:
  - Server name
  - Map
  - Online players
  - IP & Port
  - Ping
- Update the embed every 10 seconds

---

## 📷 Preview

*(Optional: add a screenshot of the bot in action here)*

---

## 🧪 Dependencies

- [discord.py](https://github.com/Rapptz/discord.py)
- [python-valve / a2s](https://github.com/ValvePython/a2s)

Install them manually with:

```bash
pip install discord.py a2s
```

---

## ⚠️ Notes

- The server must support A2S (Source Engine Query Protocol).
- The bot requires `MESSAGE CONTENT INTENT` to be enabled on the Discord Developer Portal.

---

## 📄 License

MIT License © 2025  
Created by [YourName or GitHub Profile Link]

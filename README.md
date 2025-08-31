# 0000Discordin

## Overview
This project provides a simple Discord bot that forwards all messages to a local HTTP endpoint and watches for the `!req` command. When `!req` is detected, the bot responds with "Request received." and still forwards the message.

## Setup
1. Install [Python 3](https://www.python.org/downloads/) on Windows.
2. Edit `config.ini` and replace `PLACEHOLDER_TOKEN` with your Discord bot token.
3. Run `install.bat` to create a virtual environment and install dependencies.

## Running the Bot
1. Double-click `launch.bat` or run it from Command Prompt.
2. The bot reads all messages and POSTs them to `http://localhost:1010` as JSON:
   ```json
   {
       "user": "username#1234",
       "content": "message text",
       "is_request": false
   }
   ```

## Notes
- Ensure you have a service listening on port 1010 to receive the messages.
- Enable the *Message Content Intent* for your bot in the Discord Developer Portal.



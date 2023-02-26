# data-collection-bot
# Telegram Data Collection Bot

This is a Python-based Telegram bot that collects user data and saves it to a local database. The bot can collect text, images, audio files, and video files sent by users.

## Getting started

To use this bot, you will need to:

1. Clone this repository to your local machine.
2. Create a virtual environment and install the required dependencies using the following command:

pip install -r requirements.txt


3. Set up a Telegram bot using the [BotFather](https://t.me/BotFather) bot on Telegram. You will need to get a bot token from BotFather, which you can then use to access the Telegram Bot API.
4. Replace the `TOKEN` variable in `bot.py` with your bot token.
5. Run the bot using the following command:

python bot-main.py


The bot will start running and will listen for incoming messages.

## Usage

To use the bot, simply send a message to the bot in Telegram. The bot will collect the message and save it to a local database.

The bot can collect the following types of data:

- Text messages
- Images
- Audio files
- Video files

When an image, audio file, or video file is sent to the bot, the bot will save the file to the `./files` directory on your local machine. The file will be named using the message ID and file extension.

## Limitations

This bot has the following limitations:

- The bot can only save files up to a certain size, as determined by Telegram's API.
- The bot does not have any security measures in place to prevent unauthorized access to user data. If you plan to use this bot to collect sensitive information, you should take additional security measures to protect your data.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

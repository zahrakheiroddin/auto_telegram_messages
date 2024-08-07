# auto_telegram_messages

## Telegram Chat Backup

This project allows you to backup messages from a specific Telegram chat to a JSON file using the Telethon library.

## Prerequisites

- Python 3.x
- Telethon library

## Setting Up Your Telegram API Credentials

1. **Create a Telegram Application:**

   To use the Telegram API, you need to create an application to get your `api_id` and `api_hash`. Follow these steps:
   
   - Go to [my.telegram.org](https://my.telegram.org/).
   - Log in with your Telegram account.
   - Click on "API development tools" and create a new application.
   - Fill in the required details and create the app. You will be provided with an `api_id` and `api_hash`.

2. **Configure Your Script:**

   Open `backup.py` and replace the placeholders with your actual values:
   ```python
   api_id = 'YOUR_API_ID'
   api_hash = 'YOUR_API_HASH'
   phone = 'YOUR_PHONE_NUMBER'  # Include country code, e.g.

## Installation

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/your-username/telegram-chat-backup.git
   cd telegram-chat-backup
   ```

2. **Install Required Packages:**

   Install the Telethon library using pip:
   ```sh
   pip install telethon
   ```

## Usage

1. **Edit the Script:**

   Update `backup.py` with the target chat's username or ID:
   ```python
   chat_name = 'chat_username_or_id'  # Replace with the chat username or ID
   ```

2. **Run the Script:**

   Execute the script to backup messages from the specified chat:
   ```sh
   python backup.py
   ```

   The messages will be saved in a JSON file located in the `backups` directory within the project folder.

## Code Explanation

- **Imports:**
  - `TelegramClient` from `telethon`: For connecting to the Telegram API.
  - `json`: For handling JSON operations.
  - `os`: For file and directory operations.

- **Configuration:**
  - `api_id`, `api_hash`, and `phone`: Your Telegram app credentials.
  - `session_name`: The name of the session file for the TelegramClient.

- **Client Creation:**
  - `client`: An instance of `TelegramClient` initialized with the provided credentials.

- **Asynchronous Function (`backup_messages`):**
  - Connects to Telegram using the provided phone number.
  - Fetches the specified chat entity.
  - Iterates over the messages in the chat and saves them in a list.
  - Creates a directory named `backups` if it doesn’t exist.
  - Saves the collected messages in a JSON file named `{chat_name}_messages.json` within the `backups` directory.

- **Execution:**
  - Uses `asyncio.run` to run the `backup_messages` function with the specified chat name.

## License

This project is licensed under the MIT License .

## Troubleshooting

- **No JSON file created:**
  - Ensure that `chat_name` is correctly set to the username or ID of the chat.
  - Verify that there are messages in the chat.
  - Check if the `backups` directory is created in the script's directory.

- **Errors with API credentials:**
  - Double-check that `api_id`, `api_hash`, and `phone` are correct and match those provided by Telegram.




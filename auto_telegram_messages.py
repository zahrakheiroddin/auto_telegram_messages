from telethon import TelegramClient
import json
import os

# Replace these with your own values
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
phone = 'YOUR_PHONE_NUMBER'  # With country code
session_name = 'backup_session'

# Create a client
client = TelegramClient(session_name, api_id, api_hash)

# Asynchronous function to fetch and save messages
async def backup_messages(chat_name):
    # Connect to the client
    await client.start(phone)

    # Get the chat object (it can be a group, channel, or user)
    chat = await client.get_entity(chat_name)

    # Get messages
    messages = []
    async for message in client.iter_messages(chat):
        messages.append({
            'id': message.id,
            'date': message.date.strftime('%Y-%m-%d %H:%M:%S'),
            'text': message.text
        })

    # Save messages to a JSON file
    if not os.path.exists('backups'):
        os.mkdir('backups')
    with open(f'backups/{chat_name}_messages.json', 'w', encoding='utf-8') as f:
        json.dump(messages, f, ensure_ascii=False, indent=4)

    print(f"Messages from {chat_name} have been backed up successfully.")

# Main function to run the script
if __name__ == "__main__":
    import asyncio
    chat_name = 'chat_username_or_id'  # Replace with the chat username or ID
    asyncio.run(backup_messages(chat_name))

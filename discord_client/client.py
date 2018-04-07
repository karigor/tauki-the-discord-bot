from discord import Client, Message
from chatter.chat_bot import *

bot = create_chat_bot(name='Tauki Tahmid')
bot = train_bot(bot)

client = Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-------------')


@client.event
async def on_message(message: Message):
    if message.content.startswith("!tauki"):
        msg_content = message.content.replace("!tauki", "")
        print('{} says: {}'.format(message.author, msg_content))
        bot_response = bot.get_response(input_item=msg_content, conversation_id=1).serialize().get('text')
        await client.send_message(message.channel, bot_response)

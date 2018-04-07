from chatterbot import ChatBot


def create_chat_bot(name: str, trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
                    storage_adapter='chatterbot.storage.SQLStorageAdapter', database='./db.sqlite3'):
    bot = ChatBot(name, trainer=trainer, storage_adapter=storage_adapter, database=database, output_format="text")
    return bot


def train_bot(bot: ChatBot):
    bot.train("chatterbot.corpus.english")
    return bot

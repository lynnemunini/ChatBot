from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer
from chatterbot.response_selection import get_first_response

chatbot = ChatBot(
    "Marie",
    storage_adapter='chatterbot.storage.SQLStorageAdapter',    
    # logic_adapters=[
    #     # 'chatterbot.logic.MathematicalEvaluation'
    #     # {
    #     #     "import_path": "chatterbot.logic.BestMatch",
    #     #     'default_response': 'I am sorry, but I do not understand. But Lynne can help you.',
    #     #     'maximum_similarity_threshold': 0.90
    #     # }
    # ],
    database_uri='sqlite:///database.sqlite3')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train(
    "chatterbot.corpus.english"
)

trainer.export_for_training('./my_export.json')
while True:
    try:
        bot_input = chatbot.get_response(input())
        print(bot_input)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
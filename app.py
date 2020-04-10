from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer


history=''


bot = ChatBot("Alex")
corpus_trainer = ChatterBotCorpusTrainer(bot)
corpus_trainer.train('chatterbot.corpus.english')

app = Flask(__name__)



@app.route("/")
def home():    
    return render_template("index.html",bot_response='Hello') 

	
@app.route('/process',methods=['POST'])
def process():
	global history
	user_input="User:"+request.form['user_input']
	bot_response=bot.get_response(user_input)
	bot_response="Alex[Bot]:"+str(bot_response)
	history=history+'</br>'+user_input+'</br>'+bot_response
	return render_template('index.html',history=history)
if __name__ == "__main__":    
    app.run()
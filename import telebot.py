import telebot
import json
import random
import private as key
import frasesDeMierda

with open('mierdas.json', 'r') as f:
  datosCacas = json.load(f)

runAsProd = False 

bot = telebot.TeleBot(key.PROD_TOKEN if runAsProd else key.DEV_TOKEN , threaded=False)
bot.delete_webhook()

@bot.message_handler(func=lambda message: True)
def cagaste(m):
    message = m.json
    print(message)
    user_msg = message['text']
    user_id = str(message['from']['id'])
    a = len(user_msg) < 5 and user_msg[0] == "💩" and message["chat"]["type"] == ("supergroup" if runAsProd else "private")
    if a:
        msg = random.choice(frasesDeMierda.getFrases(message))
        bot.reply_to(m, msg)
        global datosCacas

        try:
            datosCacas[user_id]["cacas"]
        except:
            datosCacas[user_id] = {}
            datosCacas[user_id]["cacas"] = []
            datosCacas[user_id]["nombre"] = message['from']["first_name"]


        datosCacas[user_id]["cacas"].append(message["date"])


        caquitaNumero = len(datosCacas[user_id]["cacas"])

        if caquitaNumero in [50,100,150,200,250,300,350,400,450]:
            bot.reply_to(m, f"Felicidades {message['from']['first_name']} has cagado tu mierdazo numero {caquitaNumero}")

        with open("mierdas.json", "w") as outfile:
            outfile.write(json.dumps(datosCacas, indent=4))
            print(f"caca contabilizada para {message['from']['first_name']}")

bot.infinity_polling()
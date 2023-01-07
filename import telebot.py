import telebot
import json
import random
import private as key

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
        msg = random.choice([
            "\"Sus excrementos era todo lo que daba al mundo; ni una sonrisa, ni un grito, ni un destello en la mirada, ni siquiera el propio olor.\" - Patrick Süskind, libro El perfume",
            "\"El hombre es el animal que observa sus propios excrementos.\" - Platon",
            "\"Sobre el excremento del caballo Las flores que cayeron del ciruelo rojo Parecen besarse.\" — Yosa Buson",
            "\"Que unos excrementos hayan aparecido no quiere decir que los haya traído el lince.\" — Esperanza Aguirre",
            "\"La corriente lenta arrastra basura, excrementos y espumas\" — Jorge Franco",
            "\"¿Han notado que sus cosas son mierda, y que su mierda son cosas?\" — George Carlin",
            "\"Mierda de vida, mierda de sistema, mierda de nivel de vida en el planeta tierra, no presumas de supremos, es el ritmo de mi sangre.\" — Kase-O",
            "\"La vida es una caca de vaca que hay que convertir en un pastel de manzana.\" — Gloria Fuertes",
            "\"mejor afuera que adentro.\" - Shrek",
            "Caga el rey, caga el papa y en este mundo de mierda de cagar nadie se escapa",
            "Al comer y al cagar, prisa no te has de dar",
            "Cagar por la mañana y abundante, alarga la vida de cualquier tunante",
            "Cagar fuerte y no tener miedo a la muerte",
            "Comer uva y cagar racimo",
            "De los placeres sin pecar el más barato es el cagar",
            "Dolor de cabeza quiere yantar, dolor de cuerpo quiere cagar",
            "El comer y el cagar, con reposo se han de tomar",
            "El que va a cagar y no se pee, es como el que va a la escuela y no lee",
            "En este mundo traidor, de cagar nadie se escapa: caga el rico caga el rey, caga el obispo y el papa",
            "Hermoso cagar  de ventana, el culo para la calle",
            "La suerte del enano que fue a cagar  y se cagó en la mano",
            "No comer por no cagar, es doble ahorrar",
            "Para comer y cagar, solo hace falta empezar",
            "Tanto para comer como para cagar, prisa no te has de dar",
            "Comer bien y cagar fuerte y no tener miedo a la muerte.",
            "Eres más prevenido que el tío Baltasar, que se limpiaba el culo antes de cagar.",
            "Cacarear y no poner huevo no es nada bueno.",
            "La caca, limpiarla en casa, y no sacarla a la plaza.",
            "Alábate, mierda, que el río te lleva.",
            "Aprendiz de muchas ciencias, maestro de mierda.",
            "El día en que la mierda tenga algún valor, los pobres nacerán sin culo.",
            "Amar y no ser amado es como limpiarse el culo sin haber cagado",
            "\"Entre el arroz que tapa y las uvas que sueltan, está la cosa resuelta.\" - La trovi en Comida y cocina",
            "\"Quien bien caga y bien mea, no necesita que el médico le vea.\" - - La trovi en SALUD",
            "Quien mucho se arremanga, vésele el culo y la nalga.",
            "Váyase con Dios y sin culo, que no quiere Dios cosas puercas.",
            "Culos que una vez se juntan, de lejos se saludan.",
            "Culos conocidos, a cien años son amigos.",
            "Culos conocidos, de lejos se dan silbos.",
            "Dos culos que bien se quieren, a treinta años se requieren",
            f"Mala tos tenéis, {message['from']['first_name']}, por abajo y por arriba.",
            "O llueve o apedrea, o nuestra moza se mea.",
            "Si quieres estar bueno, caga a menudo, como hace el perro.",
            "Cagar bien y mear claro, cagajón para el cirujano.",
            "Al comer y al cagar, el hombre se debe espaciar.",
            "Quien mucho traga, mucho caga."
        ])
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
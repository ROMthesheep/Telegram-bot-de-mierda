FROM python:latest

ADD bot.py .
ADD private.py .
ADD frasesDeMierda.py .
ADD mierdas.json .
ADD resumenDeMierda.py .

RUN pip install pyTelegramBotAPI==4.9.0

CMD ["python","./bot.py"]

FROM python:3.6.5-alpine3.4

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install -r requirements.txt --upgrade

COPY . .

ENV DISCORD_BOT_TOKEN YOU_DISCORD_BOT_TOKEN

CMD [ "python", "app.py" ]
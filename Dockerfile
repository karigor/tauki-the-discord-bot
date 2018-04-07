FROM python:3.6.5-alpine3.4

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt --upgrade

COPY . .

ENV DISCORD_APP_TOKEN YOUR_DISCORD_BOT_API_TOKEN

CMD [ "python", "app.py" ]
from flask import Flask
from threading import Thread
import Values

app = Flask('')


@app.route('/')
def home():
  return f"{Values.bot_name} is up and running"


def run():
  app.run(host='0.0.0.0', port=9876)


def keep_alive():
  t = Thread(target=run)
  t.start()

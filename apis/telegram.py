import os
import json
import urllib
import logging

from google.appengine.api import urlfetch
from google.appengine.api.urlfetch_errors import DeadlineExceededError

BASE_URL = 'https://api.telegram.org/bot{token}/{method}'

BOTS_SECRETS = {
  'pink': '333613762:AAH9g5PnU5VInxH1oLFA5Qp-h-C2LcDWuJQ',
  'blue': '442432246:AAGUTaVz7pYssJ7pVvAim1PQTlNaKRBO80I',
  'black': '442305057:AAEjNxDbyLW-DHArOmR3pN1h6EtMgXgxSzc'
}

def call_method(with_bot, method, data):
  logging.debug("request %s payload with_bot=%s" % ( method, with_bot ))
  logging.debug("data= %s" % data)
  data = json.dumps(data)
  try:
    result = urlfetch.fetch(
        BASE_URL.format(token=BOTS_SECRETS[with_bot], method=method),
        payload=data,
        method=urlfetch.POST,
        deadline=10,
        headers={'Content-Type': 'application/json'})
  # except DeadlineExceededError as e:
  #   logging.exception(e)
  #   return None
  except Exception as e:
    logging.exception(e)
    return None
  if result.status_code == 200:
    return json.loads(result.content)
  else:
    logging.error(result.content)
    return None


def send_message(with_bot, chat_id, text, reply_markup=None, parse_mode='HTML',
                 disable_notification=True):
  logging.debug("sending message with bot %s" % with_bot)
  message = {
    'chat_id': chat_id,
    'text': text,
    'parse_mode': parse_mode,
    'disable_notification': disable_notification
  }

  if reply_markup:
      message['reply_markup'] = reply_markup

  return call_method(with_bot, 'sendMessage', message)

import time
import json

from google.appengine.api import urlfetch

BASE_URL = "https://graph.facebook.com/v2.9/{method}?{params}"

PAGES_ID = {
            'pink': 'acg.secrets',
            'blue': 'acg.secrets.textboard',
            'black': '146482875909279'
          }

ACCESS_TOKEN = '1983828995182433|Htv7MJ8BnulVO1_UjArhm290GqU'


def make_param_str(params=None):
  params['access_token']=ACCESS_TOKEN
  return '&'.join(['%s=%s' % (k, v) for (k, v) in params.items()])


def call_method(method, params=None):
  result = urlfetch.fetch(BASE_URL.format(method=method, params=make_param_str(params)), deadline=10)
  if result.status_code == 200:
    return json.loads(result.content)
  return None


# Use a helper function to define the scope of the callback.
def create_callback(rpc, callback):
  return lambda: callback(rpc)


def call_method_async(method, callback, params=None):
  rpc = urlfetch.create_rpc(deadline=10)
  rpc.callback = create_callback(rpc, callback)
  urlfetch.make_fetch_call(rpc, BASE_URL.format(method=method, params=make_param_str(params)))
  return rpc

# operations

def get_page_feed(page):
  feeds=[]
  result = call_method('%s/feed' % PAGES_ID[page], 
    params={'fields':'created_time,id', 
            'since':int(time.time()) - 86400,   # within 24 hrs
            'limit': 100})
  return result


def get_post_async(id, callback):
  return call_method_async('%s' % id, callback, 
    params={'fields':'created_time,message,id,\
    reactions.type(LIKE).limit(0).summary(total_count).as(reactions_like),\
    reactions.type(LOVE).limit(0).summary(total_count).as(reactions_love),\
    reactions.type(WOW).limit(0).summary(total_count).as(reactions_wow),\
    reactions.type(HAHA).limit(0).summary(total_count).as(reactions_haha),\
    reactions.type(SAD).limit(0).summary(total_count).as(reactions_sad),\
    reactions.type(ANGRY).limit(0).summary(total_count).as(reactions_angry),\
    comments.limit(0).summary(total_count).as(comments_count),shares'})

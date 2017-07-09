# -*- coding: UTF-8 -*-

from datetime import datetime
import re
import logging

from google.appengine.ext import ndb
from google.appengine.api import memcache

from helper import development, shorten_url
from apis.telegram import send_message


class StoryPost(ndb.Model):
  fbid = ndb.StringProperty()
  message = ndb.TextProperty(indexed=False)
  draft_time = ndb.TextProperty(indexed=False)
  post_time = ndb.DateTimeProperty(indexed=False)
  telegram_post_time = ndb.DateTimeProperty(auto_now_add=True, indexed=False)
  likes = ndb.IntegerProperty(indexed=False)
  loves = ndb.IntegerProperty(indexed=False)
  wows = ndb.IntegerProperty(indexed=False)
  hahas = ndb.IntegerProperty(indexed=False)
  sads = ndb.IntegerProperty(indexed=False)
  angries = ndb.IntegerProperty(indexed=False)
  comments = ndb.IntegerProperty(indexed=False)
  shares = ndb.IntegerProperty(indexed=False)


  @staticmethod
  def try_strptime(date_str, format):
    try:
      return datetime.strptime(post_time, format)
    except ValueError:
      return None


  @staticmethod
  def cvt_FBObject_StoryPost(fb_object):
    ret = {
      "fbid": fb_object['id'],
      "message": fb_object.get('message', None),
      "draft_time": None,
      "post_time": datetime.strptime(fb_object['created_time'], '%Y-%m-%dT%H:%M:%S+0000'),  # post_time = '2017-07-09T11:28:32+0000'
      "likes": fb_object['reactions_like']['summary']['total_count'],
      "loves": fb_object['reactions_love']['summary']['total_count'],
      "wows": fb_object['reactions_wow']['summary']['total_count'],
      "hahas": fb_object['reactions_haha']['summary']['total_count'],
      "sads": fb_object['reactions_sad']['summary']['total_count'],
      "angries": fb_object['reactions_angry']['summary']['total_count'],
      "comments": fb_object['comments_count']['summary']['total_count'],
      "shares": 0
    }

    if "shares" in fb_object:
      ret['shares'] = fb_object['shares']['count']

    draft_time = None
    chk_draft_time_result = re.findall(u"(投稿日期|Submitted)[:：]\s*(.*?)$", fb_object['message'])
    if chk_draft_time_result:
      str_datetime = chk_draft_time_result[0][1]
      # '%B %d, %Y %-I:%M:%S %p HKT'
      if draft_time is None:
        draft_time = try_strptime(post_time, '%Y年%m月%d日 %H:%M HKT')
      # 'July 5, 2017 5:35:26 AM HKT'
      if draft_time is None:
        draft_time = try_strptime(post_time, '%B %d, %Y %I:%M:%S %p HKT')
    ret['draft_time'] = draft_time

    return ret


  @classmethod
  def add(cls, story, with_bot):
    logging.debug("adding into database with bot %s" % with_bot)

    story_id = str(story.get('fbid'))
    if memcache.get(story_id):
      logging.info('STOP: {} in memcache'.format(story_id))
      return
    if ndb.Key(cls, story_id).get():
      logging.info('STOP: {} in DB'.format(story_id))
      memcache.set(story_id, 1)
      return
    logging.info('SEND: {}'.format(story_id))

    short_url = "https://fb.com/{}".format(story_id)

    message = u'\U0001f517 {}\n'.format(short_url)
    message += u'\n{}\n\n'.format(story.get('message'))

    reactions = 0
    str_reaction_icons = ''
    if story.get('likes'):
      reactions += story.get('likes')
      str_reaction_icons += u'\U0001f44d'
    if story.get('loves'):
      reactions += story.get('loves')
      str_reaction_icons += u'\u2764'
    if story.get('wows'):
      reactions += story.get('wows')
      str_reaction_icons += u'\U0001f606'
    if story.get('hahas'):
      reactions += story.get('hahas')
      str_reaction_icons += u'\U0001f632'
    if story.get('sads'):
      reactions += story.get('sads')
      str_reaction_icons += u'\U0001F622'
    if story.get('angries'):
      reactions += story.get('angries')
      str_reaction_icons += u'\U0001F621'
    message += '%d ' % reactions
    message += str_reaction_icons

    message += u'  %d 回應  %d 分享' % ( story.get('comments'), story.get('shares') )

    if development():
      result = send_message(with_bot, '@d09n0fcuk_hk429_b0t_7327', message)
    else:
      result = send_message(with_bot, '@hk_acg_feeds', message)
    if result:
      logging.debug("writing into datastore: %s" % story.get('fbid'))
      cls(id=story.get('fbid'), message=story.get('message'), 
        draft_time=story.get('draft_time'), post_time=story.get('post_time'), 
        likes=story.get('likes'), loves=story.get('loves'), wows=story.get('wows'), 
        hahas=story.get('hahas'), sads=story.get('sads'), angries=story.get('angries'), 
        comments=story.get('comments'), shares=story.get('shares')).put()
      memcache.set(story_id, 1)

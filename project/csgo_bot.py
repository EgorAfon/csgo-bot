# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import random
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


class CsGoBot:

    def __init__(self, group_token, group_id):
        self.group_token = group_token
        self.group_id = group_id
        self.bot_session = vk_api.VkApi(token=self.group_token)
        self.bot_api = self.bot_session.get_api()

    def start(self):
        while True:
            longpoll = VkBotLongPoll(self.bot_session, self.group_id)
            try:
                print('wait')
                for event in longpoll.listen():
                    print('got event')
                    if event.type == VkBotEventType.MESSAGE_NEW:
                        self.manage_event(event)

            except requests.exceptions.ReadTimeout as timeout:
                continue

    def manage_event(self, event):
        print('message')
        if event.from_user:
            print(event.message['from_id'])
            self.bot_api.messages.send(
                random_id=random.getrandbits(32),
                peer_id=event.message['peer_id'],
                message=event.message['text']
            )

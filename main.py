# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import random
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from project.access import group_token, group_id


def main():
    replies = ['1', '2', '3']
    bot_session = vk_api.VkApi(token=group_token)
    bot_api = bot_session.get_api()
    while True:
        longpoll = VkBotLongPoll(bot_session, group_id)
        try:
            print('wait')
            for event in longpoll.listen():
                print('got event')
                if event.type == VkBotEventType.MESSAGE_NEW:
                    print('message')
                    if event.from_chat:
                        bot_api.messages.send(
                            random_id=random.getrandbits(32),
                            chat_id=event.chat_id,
                            message=random.choice(replies)
                        )
                        print(event.chat_id)
        except requests.exceptions.ReadTimeout as timeout:
            continue


if __name__ == '__main__':
    main()

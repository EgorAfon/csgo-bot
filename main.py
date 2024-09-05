# ! /usr/bin/env python
# -*- coding: utf-8 -*-

from project.access import group_token, group_id
from project.csgo_bot import CsGoBot

if __name__ == '__main__':
    bot = CsGoBot(group_token, group_id)
    bot.start()

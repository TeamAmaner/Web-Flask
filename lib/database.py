from typing import NamedTuple
from typing import Union, Any, List, Tuple
import asyncpg
import os
from pymongo import MongoClient, DESCENDING

import setting

MONGO_URL = setting.MONGO

User = NamedTuple('User', [('id', int), ('point', int), ('name', str)])



# user_id = 653785595075887104
# data = db.find_one({"user_id":user_id})
# print(data["point"])


class Database:
    """CREATE TABLE users (user_id bigint, point integer, name strings, PRIMARY KEY(user_id))"""

    def __init__(self):
        self.conn: Union[asyncpg.Connection, None] = None
        self.db = None

    def setup(self):
        client = MongoClient(MONGO_URL)
        self.db = client.web.guilds
        return self.db

    def get_guilds(self):
        data_list = []
        db = self.db or self.setup()
        datas = db.find_one()
        if not datas:
            return None
        for data in datas:
            data_list.append(data["guild"])
        return data_list

    def rset(self):
        client = MongoClient(MONGO_URL)
        db = client.web
        db.drop_collection(db.guilds)

    async def create_guild(self, des, url):
        db = self.db or self.setup()
        invite = await bot.fetch_invite(url)
        guild = invite.guild
        guild.description = des
        post = {"guild":guild, "invitation":url}
        db.insert_one(post)

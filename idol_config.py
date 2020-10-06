import random
from random import choice
from .random_config_index import *
import json
import os

class user:
    def __init__(self, id):
        self.id = id

class user_list:
    def __init__(self):
        self.user_idol_list = list()
        self.user = list()
        self.all_user = list()
        self.alredyInit = False

    async def add_user(self, idol):
        self.user_idol_list.append(idol)
        self.user.append(idol.producer)
        self.all_user.append(user(idol.producer))

class idol:
    def __init__(self, user):
        self.producer = user
        self.name = choice(lastname) + choice(firstname)
        # 外表设定，为了让人物更立体。
        self.houfa = choice(houfa)
        self.qianfa = choice(qianfa)
        self.fase = choice(fase)
        self.faxing = choice(faxing)
        self.tongse = choice(tongse)
        self.yanxing = choice(yanxing)
        self.ouBaiSize = choice(ouBaiSize)
        self.qianxingge = choice(qianxingge)
        self.shenxingge = choice(shenxingge)
        self.jinhua = choice(jinhua)
        #数值设定，用于战斗。
        self.vo = random.randint(50, 100) # voice
        self.vi = random.randint(50, 100) # vision
        self.da = random.randint(50, 100) # dance
        self.me = random.randint(50, 100) * random.randint(50, 100) # mental，即生命值
        self.sp = random.randint(50, 100) # 每50点sp可获得一个技能，最高300点sp。
        self.like = random.randint(150, 250) # 好感度，最高300。
        self.skill = ['展现歌喉', '展现容貌', '展现舞姿', '展现歌喉', '展现容貌', '展现舞姿'] # 技能列表
        #训练记录
        self.train = 32 # 每训练一次减一，到0时不能再训练。

    def print_image(self):
        ret = "你的偶像" + self.name + "是有着" + self.houfa + self.qianfa + self.fase + self.faxing + "和" + self.tongse + self.yanxing + "，胸围" + self.ouBaiSize + "的" + self.qianxingge + self.shenxingge + self.jinhua + f"。\n她的VOICE是{self.vo}，VISION是{self.vi}，DANCE是{self.da}，MENTAL是{self.me}，sp值是{self.sp}，对你的好感度是{self.like}。\n她的剩余训练次数为{self.train}，持有技能为：" + self.print_skill()
        return ret

    def print_skill(self):
        ret = ""
        for i in range(len(self.skill)):
            ret = ret + self.skill[i] + ","
        return ret

async def write(idol_list):
    if len(idol_list.user_idol_list) > 0:
        with open('C:\\Users/Administrator/Documents/HoshinoBot/hoshino/modules/idolwar/idolindex.json', 'w+', encoding='utf-8') as f:
            src = '['
            for idol in idol_list.user_idol_list:
                date = {'name': idol.name,
                        'producer': idol.producer,
                        'houfa': idol.houfa,
                        'qianfa': idol.qianfa,
                        'fase': idol.fase,
                        'faxing': idol.faxing,
                        'tongse': idol.tongse,
                        'yanxing': idol.yanxing,
                        'ouBaiSize': idol.ouBaiSize,
                        'qianxingge': idol.qianxingge,
                        'shenxingge': idol.shenxingge,
                        'jinhua': idol.jinhua,
                        'vo': idol.vo,
                        'vi': idol.vi,
                        'da': idol.da,
                        'me': idol.me,
                        'sp': idol.sp,
                        'like': idol.like,
                        'train': idol.train,
                        'skill': idol.skill}
                if len(idol_list.user_idol_list) - 1 == idol_list.user_idol_list.index(idol):
                    src = src + (json.dumps(date, ensure_ascii=False))
                else:
                    src = src + (json.dumps(date, ensure_ascii=False) + ',\n')
            src = src + (']')
            f.write(src)
            f.close()


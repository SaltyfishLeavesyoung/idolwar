# 在pve中，敌人本质也可以用偶像表示，所以就不写json，直接在这里对其进行生成。
from .idol_config import *

class enemy_list:
    def __init__(self):
        self.enemys = list()
        self.alredyInit = False

    def add_enemy(self, e:idol):
        self.enemys.append(e)

    def initenemy(self):
        # enemy 1 - 3, voice, vision, dance三种属性对应的评审员
        # 特性是能使用对应属性的批判技能，大幅降低偶像的该属性值。
        VOCALJUDGE = idol(-1)
        VISIONJUDGE = idol(-1)
        DANCEJUDGE = idol(-1)

        # enemy 4, 悠木凛
        # 又称雪灵灵，特性是使用强力的混合属性攻击
        XUELINGLING = idol(-1)

        # enemy 5, 白桃
        # 又称小乖，特性是在输出的同时回复生命并降低自己的伤害
        XIAOGUAI = idol(-1)

        # 初始化所有敌人
        VOCALJUDGE.name = "VOICE评审员"
        VOCALJUDGE.vo = 600
        VOCALJUDGE.vi = 50
        VOCALJUDGE.da = 50
        VOCALJUDGE.me = 35000
        VOCALJUDGE.like = 400
        VOCALJUDGE.skill = ['舒缓微笑', '耀眼群星', '展现歌喉', '舒缓微笑', '耀眼群星', '展现歌喉']

        VISIONJUDGE.name = "VISION评审员"
        VISIONJUDGE.vo = 50
        VISIONJUDGE.vi = 600
        VISIONJUDGE.da = 50
        VISIONJUDGE.me = 35000
        VISIONJUDGE.like = 400
        VISIONJUDGE.skill = ['绽放微笑', '掬星仰望', '绽放微笑', '掬星仰望', '展现容貌', '展现容貌']

        DANCEJUDGE.name = "DANCE评审员"
        DANCEJUDGE.vo = 50
        DANCEJUDGE.vi = 50
        DANCEJUDGE.da = 600
        DANCEJUDGE.me = 35000
        DANCEJUDGE.like = 400
        DANCEJUDGE.skill = ['柔和微笑', '指尖辉煌', '柔和微笑', '指尖辉煌', '展现舞姿', '展现舞姿']

        XUELINGLING.name = "雪灵灵"
        XUELINGLING.vo = 800
        XUELINGLING.vi = 800
        XUELINGLING.da = 800
        XUELINGLING.me = 30000
        XUELINGLING.like = 300
        XUELINGLING.skill = ['雨后英雄', '金色元气', '柠檬觉悟', '百色相片', '真红一轮', '四季短篇']

        XIAOGUAI.name = "小乖"
        XIAOGUAI.vo = 500
        XIAOGUAI.vi = 500
        XIAOGUAI.da = 500
        XIAOGUAI.me = 40000
        XIAOGUAI.like = 0
        XIAOGUAI.skill = ['清闲休憩', '百色相片', '第二形态', '雾·雾·奇·谭', '棉·毛·之·想', '包·带·组·曲']

        self.add_enemy(VOCALJUDGE)
        self.add_enemy(VISIONJUDGE)
        self.add_enemy(DANCEJUDGE)
        self.add_enemy(XUELINGLING)
        self.add_enemy(XIAOGUAI)

import random

class buff:
    def __init__(self, voratio, viratio, daratio, defence, dur):
        self.vort = voratio
        self.virt = viratio
        self.dart = daratio
        self.defence = defence
        self.dur = dur

class buff_list:
    def __init__(self):
        self.buffs = list()

    def add_buff(self, b:buff):
        self.buffs.append(b)

    def dec1(self):
        for buff in self.buffs:
            buff.dur = max(0, buff.dur - 1)

    def getratio(self):
        vo = 0.0
        vi = 0.0
        da = 0.0
        for buff in self.buffs:
            if buff.dur > 0:
                vo = vo + buff.vort
                vi = vi + buff.virt
                da = da + buff.dart
        return vo, vi, da

    def getdef(self):
        d = 0.0
        for buff in self.buffs:
            if buff.dur > 0:
                d = d + buff.defence
        return d

class skill:
    def __init__(self, name, desc, vor, vir, dar, rate, rec, vob, vib, dab, dec, bt, vodb, vidb, dadb, inc, dbt):
        self.name = name
        self.desc = desc
        self.vor = vor
        self.vir = vir
        self.dar = dar
        self.rate = rate
        self.rec = rec
        self.buff = buff(vob, vib, dab, dec, bt)
        self.debuff = buff(vodb, vidb, dadb, inc, dbt)

class skill_list:
    def __init__(self):
        self.skills = list()
        self.alredyInit = False

    async def add_skill(self, s:skill):
        self.skills.append(s)
        
    def add_skill_noasync(self, s:skill):
        self.skills.append(s)

class combat_idol:
    def __init__(self, idol, memorybomb:skill = skill("回忆炸弹", "", 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)):
        self.idol = idol
        self.hp = idol.me
        self.skills = skill_list()
        self.memorybomb = memorybomb
        self.memory = idol.like
        self.buffs = buff_list()
        self.skillcount = 0

    def attack(self, skill:skill, idol):
        # 获取自身三围增益和对方受伤减少
        vob, vib, dab = self.buffs.getratio()
        defs = idol.buffs.getdef()
        # 计算伤害公式
        # 计算公式：(VI * VIBUFF * VIRATE + VO * VOBUFF * VORATE + DA * DABUFF * DARATE) * SKILLRATE * DEFENCE * RANDOM，向下取整
        # 对于回忆炸弹，SKILLRATE = LIKE / 100
        atk = (self.idol.vo * max(0, 1 + vob) * skill.vor + self.idol.vi * max(0, 1 + vib) * skill.vir + self.idol.da * max(0, 1 + dab) * skill.dar) * skill.rate * max(0, 1 + defs) * random.uniform(0.95, 1.05)
        if skill.name == "回忆炸弹":
            atk = atk * self.idol.like / 100.0
        # 给予对手伤害
        msg = self.idol.name + "使用" + skill.name + f"，伤害{min(idol.hp, int(atk))}。\n"
        idol.hp = max(0, idol.hp - int(atk))
        # 在新增益到来之前进行buff的倒计时结算
        self.buffs.dec1()
        # 给自己增益
        self.buffs.add_buff(skill.buff)
        # 给对手减益
        idol.buffs.add_buff(skill.debuff)
        # 给自己回血
        self.hp = min(self.idol.me, self.hp + int(self.idol.me * skill.rec))
        return msg

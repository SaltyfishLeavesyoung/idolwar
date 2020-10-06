import hoshino
from hoshino import Service
from hoshino.typing import MessageSegment, NoticeSession, CQEvent

from .idol_config import *
from .combat_config import *
from .enemy_config import *

import random
import os

MANUAL = '''
偶像帮助：发送此段帮助。
养成帮助：培育偶像帮助。
战斗帮助：偶像战斗帮助。
生成偶像：生成一个偶像。
偶像信息：查看偶像信息。
偶像退役：退役一个偶像。
查看技能：查看技能描述。
对手名单：查看对手名单。
---------------
其他功能在做了
---------------
'''.strip()

PEIYUMANUAL = '''
偶像共有六个属性：
vo（VOCAL），vi（VISION），da（DANCE）是衡量偶像能力的指标，相当于攻击力。偶像可以使用对应属性的技能造成伤害。
me（MENTAL）是衡量偶像心理素质的指标，相当于生命值。战斗时该属性归零时则失败。
sp是技能点，在培育结束后，每50点sp可以随机获得一个技能。由于最多只有6个技能所以超过300的sp毫无意义。
好感度影响回忆炸弹（相当于大招）的威力，最高300。
需要对偶像进行培养来提升这六个属性，培养的指令为:
养成偶像 序号：提升偶像属性。
一键养成：一键培育偶像。
各个序号表示的培育如下：
1：vo课程，提升vo属性。
2：vi课程：提升vi属性。
3：da课程：提升da属性。
4：广播收录：提升me属性。
5：谈话活动：提升sp。
6：杂志摄影：提升好感度。
总共只有32次培育偶像的机会。培育完成后将进行技能的学习。
详细的介绍请参考文档（在做了在做了）。
'''.strip()

ZHANDOUMANUAL = '''
战斗分为pve和pvp两种，所有战斗过程均在后台自动进行，无需玩家参与。
pve的指令为：
偶像pve 序号
pvp的指令为：
偶像pvp@某人
通过对手名单指令可以查看序号对应的NPC。
如果想左右互搏可以@自己。
详细的介绍请参考文档（在做了在做了）。
'''.strip()

idol_lists = user_list()

skill_lists = skill_list()

enemy_lists = enemy_list()

sv = Service('idolwar', bundle='pcr娱乐', help_=MANUAL)

async def read():
    try:
        with open('idolindex.json', 'r+', encoding='utf-8') as f:
            line = f.readline()
            while line:
                line = str(line).replace('[', '').replace(',\n', '').replace(']', '')
                t = json.loads(line)
                user_id = t['producer']
                temp_idol = idol(user_id)
                temp_idol.producer = t['producer']
                temp_idol.name = t['name']
                temp_idol.houfa = t['houfa']
                temp_idol.qianfa = t['qianfa']
                temp_idol.fase = t['fase']
                temp_idol.faxing = t['faxing']
                temp_idol.tongse = t['tongse']
                temp_idol.yanxing = t['yanxing']
                temp_idol.ouBaiSize = t['ouBaiSize']
                temp_idol.qianxingge = t['qianxingge']
                temp_idol.shenxingge = t['shenxingge']
                temp_idol.jinhua = t['jinhua']
                temp_idol.vo = t['vo']
                temp_idol.vi = t['vi']
                temp_idol.da = t['da']
                temp_idol.me = t['me']
                temp_idol.sp = t['sp']
                temp_idol.like = t['like']
                temp_idol.train = t['train']
                temp_idol.skill = list(t['skill'])
                await idol_lists.add_user(temp_idol)
                idol_lists.all_user.append(user(user_id))
                line = f.readline()
            f.close()
    except:
        try:
            with open('idolindex.json', 'r+', encoding='utf-8') as f:
                line = f.readline()
                while line:
                    line = str(line).replace('[', '').replace(',\n', '').replace(']', '')
                    t = json.loads(line)
                    user_id = t['producer']
                    temp_idol = idol(user_id)
                    temp_idol.producer = t['producer']
                    temp_idol.name = t['name']
                    temp_idol.houfa = t['houfa']
                    temp_idol.qianfa = t['qianfa']
                    temp_idol.fase = t['fase']
                    temp_idol.faxing = t['faxing']
                    temp_idol.tongse = t['tongse']
                    temp_idol.yanxing = t['yanxing']
                    temp_idol.ouBaiSize = t['ouBaiSize']
                    temp_idol.qianxingge = t['qianxingge']
                    temp_idol.shenxingge = t['shenxingge']
                    temp_idol.jinhua = t['jinhua']
                    temp_idol.vo = t['vo']
                    temp_idol.vi = t['vi']
                    temp_idol.da = t['da']
                    temp_idol.me = t['me']
                    temp_idol.sp = t['sp']
                    temp_idol.like = t['like']
                    temp_idol.train = t['train']
                    temp_idol.skill = list(t['skill'])
                    await idol_lists.add_user(temp_idol)
                    idol_lists.all_user.append(user(user_id))
                    line = f.readline()
                f.close()
        except:
            with open('idolindex.json', 'a+', encoding='utf-8') as f:
                f.close()
    return

async def readSkills():
    # 使用绝对路径
    for i in os.walk("C:\\Users/Administrator/Documents/HoshinoBot/hoshino/modules/idolwar/skills"):
        root, dir_names, filenames = i
        break
    for j in filenames:
        with open(os.path.join(root, j), 'r+', encoding='utf-8') as f:
            line = f.readline()
            while line:
                line = str(line).replace('[', '').replace(',\n', '').replace(']', '')
                t = json.loads(line)
                temp_skill = skill(t['name'], t['desc'], t['vor'], t['vir'], t['dar'], t['rate'], t['rec'], t['vob'], t['vib'], t['dab'], t['dec'], t['bt'], t['vodb'], t['vidb'], t['dadb'], t['inc'], t['dbt'])
                await skill_lists.add_skill(temp_skill)
                line = f.readline()
            f.close()

@sv.on_fullmatch('偶像帮助', only_to_me=False)
async def idolhelp(bot, ctx):
    await bot.send(ctx, MANUAL)

@sv.on_fullmatch('养成帮助', only_to_me=False)
async def peiyuhelp(bot, ctx):
    await bot.send(ctx, PEIYUMANUAL)

@sv.on_fullmatch('战斗帮助', only_to_me=False)
async def zhandouhelp(bot, ctx):
    await bot.send(ctx, ZHANDOUMANUAL)

@sv.on_fullmatch('对手名单')
async def duishoumen(bot, ctx):
    msg = ""
    count = 0
    for e in enemy_lists.enemys:
        msg = msg + f"{count}:" + e.name + "\n"
        count = count + 1
    await bot.send(ctx, msg)

@sv.on_prefix('查看技能', only_to_me=False)
async def jinenghelp(bot, ctx):
    s = ctx.message.extract_plain_text()
    if s is None or len(s) == 0:
        msg = ""
        for skill in skill_lists.skills:
            msg = msg + skill.name + ":" + skill.desc + "\n"
        await bot.send(ctx, msg)
    else:
        for skill in skill_lists.skills:
            if skill.name == s:
                await bot.send(ctx, s + ":" + skill.desc)
                return
        await bot.send(ctx, "没有该技能或技能列表未加载")

@sv.on_fullmatch('生成偶像')
async def makeidol(bot, ctx):
    if not idol_lists.alredyInit:
        await read()
        idol_lists.alredyInit = True
    if not skill_lists.alredyInit:
        await readSkills()
        skill_lists.alredyInit = True
    if not enemy_lists.alredyInit:
        enemy_lists.initenemy()
        enemy_lists.alredyInit = True
    send_user = ctx['user_id']
    if send_user in idol_lists.user:
        for i in idol_lists.user_idol_list:
            if i.producer == send_user:
                await bot.send(ctx, f'你已经有一名偶像：{i.name}了。', at_sender=True)
    else:
        flag = False
        for i in idol_lists.all_user:
            if i.id == send_user:
                flag = True
                break
        if not flag:
            idol_lists.all_user.append(user(send_user))
        tempIdol = idol(send_user)
        await  idol_lists.add_user(tempIdol)
        await bot.send(ctx, f"你好！我是{tempIdol.name}，普罗丢瑟请多关照。", at_sender=True)
    await write(idol_lists)
    return

@sv.on_fullmatch('偶像信息', only_to_me=False)
async def idol_self_index(bot, ctx):
    send_user = ctx['user_id']
    if send_user in idol_lists.user:
        for i in idol_lists.user_idol_list:
            if i.producer == send_user:
                await bot.send(ctx, i.print_image(), at_sender=True)
                return
    else:
        await bot.send(ctx, "你还没有偶像", at_sender=True)

@sv.on_fullmatch('偶像退役', only_to_me=False)
async def retire(bot, ctx):
    send_user = ctx['user_id']
    if send_user in idol_lists.user:
        for i in idol_lists.user_idol_list:
            if i.producer == send_user:
                await bot.send(ctx, i.name + "已退役。", at_sender=True)
                idol_lists.user_idol_list.remove(i)
                idol_lists.user.remove(send_user)
                await  write(idol_lists)
                return
    else:
        await bot.send(ctx, "你没有偶像。", at_sender=True)

def training(idol: idol, prob, s):
    cond = ""
    gain = random.randint(1, 20) + random.randint(1, 20) + random.randint(1, 20) +  random.randint(1, 20) +  random.randint(1, 20)
    if prob <= 1:
        cond = "极大失败！"
        gain = gain - 50
    elif prob <= 5:
        cond = "大失败！"
        gain = int(gain * 0.5)
    elif prob >= 100:
        cond = "极大成功！"
        gain = max(50, gain) * 2
    elif prob >= 96:
        cond = "大成功！"
        gain = gain * 2
    else:
        cond = ""

    if s == 1:
        cond = cond + idol.name + f"的vo上升了{gain}"
        idol.vo = idol.vo + gain
    elif s == 2:
        cond = cond + idol.name + f"的vi上升了{gain}"
        idol.vi = idol.vi + gain
    elif s == 3:
        cond = cond + idol.name + f"的da上升了{gain}"
        idol.da = idol.da + gain
    elif s == 4:
        mer = random.randint(50, 100)
        cond = cond + idol.name + f"的me上升了{gain * mer}"
        idol.me = idol.me + gain * mer
    elif s == 5:
        cond = cond + idol.name + f"的sp上升了{gain}"
        idol.sp = idol.sp + gain
    else:
        cond = cond + idol.name + f"的好感度上升了{gain}"
        idol.like = min(300, idol.like + gain)
    idol.train = idol.train - 1
    return cond

def learnskill(idol: idol):
    msg = ""
    num = min(int(idol.sp / 50), 6)
    for i in range(num):
        selskill = random.choice(skill_lists.skills)
        while selskill.name in idol.skill or selskill.name == "展现歌喉" or selskill.name == "展现容貌" or selskill.name == "展现舞姿":
            selskill = random.choice(skill_lists.skills)
        idol.skill[i] = selskill.name
        msg = msg + idol.name + "学会了" + selskill.name + "\n"
        idol.sp = idol.sp - 50
    return msg


@sv.on_prefix('养成偶像')
async def buildidol(bot, ev: CQEvent):
    send_user = ev['user_id']
    temp_idol = None
    # 首先判断是否有偶像且是否已训练满
    if send_user in idol_lists.user:
        for i in idol_lists.user_idol_list:
            if i.producer == send_user:
                if i.train <= 0:
                    await bot.send(ev, "你的偶像已经完成训练了", at_sender=True)
                    return
                else:
                    temp_idol = i
                    break
    else:
        await bot.send(ev, "你还没有偶像", at_sender=True)
        return
    #根据输入参数选择训练
    s = ev.message.extract_plain_text()
    # 首先判断，1为极大失败，2-5为大失败，96-99为大成功，100为极大成功。
    prob = random.randint(1, 100)
    # 其次开始培养
    if s is None or len(s) == 0:
        await bot.send(ev, "请输入参数！", at_sender=True)
        return
    elif s == "1" or s == "2" or s == "3" or s == "4" or s == "5" or s == "6":
        msg = training(temp_idol, prob, int(s))
        if temp_idol.train > 0:
            msg = msg + f"，剩余培养次数为{temp_idol.train}"
        else:
            msg = msg + "培养次数已用尽！"
            msg = msg + learnskill(temp_idol)
        await write(idol_lists)
        await bot.send(ev, msg, at_sender=True)
    else:
        await bot.send(ev, "参数不合法！", at_sender=True)

@sv.on_fullmatch('一键养成')
async def buildidol32(bot, ev: CQEvent):
    send_user = ev['user_id']
    temp_idol = None
    msg = ""
    # 首先判断是否有偶像且是否已训练满
    if send_user in idol_lists.user:
        for i in idol_lists.user_idol_list:
            if i.producer == send_user:
                if i.train <= 0:
                    await bot.send(ev, "你的偶像已经完成训练了", at_sender=True)
                    return
                else:
                    temp_idol = i
                    break
    else:
        await bot.send(ev, "你还没有偶像", at_sender=True)
        return
    #接下来随机培养剩余次数，在sp>=300和like>=300的时候排除相关选项
    for j in range(temp_idol.train):
        prob = random.randint(1, 100)
        if temp_idol.sp >= 300 and temp_idol.like >= 300:
            choice = random.randint(1, 4)
        elif temp_idol.sp >= 300:
            choice = random.randint(1, 5)
            if choice == 5:
                choice = choice + 1
        elif temp_idol.like >= 300:
            choice = random.randint(1, 5)
        else:
            choice = random.randint(1, 6)
        msg = msg + training(temp_idol, prob, choice) + "\n"
    msg = msg + learnskill(temp_idol)
    await write(idol_lists)
    await bot.send(ev, msg, at_sender=True)

def fight(idola:idol, idolb:idol):
    # 首先包装成combat_idol
    coma = combat_idol(idola)
    comb = combat_idol(idolb)
    # 如果是pve,修改对手的回忆炸弹
    if idolb.name == "VOICE评审员":
        comb.memorybomb = skill("VOICE批判", "", 6, 6, 6, 1, 0, 0, 0, 0, 0, 0, -0.8, 0, 0, 0, 2)
    elif idolb.name == "VISION评审员":
        comb.memorybomb = skill("VISION批判", "", 6, 6, 6, 1, 0, 0, 0, 0, 0, 0, 0, -0.8, 0, 0, 2)
    elif idolb.name == "DANCE评审员":
        comb.memorybomb = skill("DANCE批判", "", 6, 6, 6, 1, 0, 0, 0, 0, 0, 0, 0, 0, -0.8, 0, 2)
    # 战斗前的准备，实例化技能并打乱技能顺序
    round = 1
    for s in coma.idol.skill:
        for sk in skill_lists.skills:
            if sk.name == s:
                coma.skills.add_skill_noasync(sk)
                break
    random.shuffle(coma.skills.skills)
    for s in comb.idol.skill:
        for sk in skill_lists.skills:
            if sk.name == s:
                comb.skills.add_skill_noasync(sk)
                break
    random.shuffle(comb.skills.skills)
    # 开始战斗，最多30个回合
    msg = ""
    while round <= 30:
        # 玩家先攻
        msg = msg + f"第{round}回合，" + coma.idol.name + f"({coma.hp})，" + comb.idol.name + f"({comb.hp})\n"
        # 进行回忆炸弹判定，如果memory到达400则释放回忆炸弹，否则释放技能
        if coma.memory >= 400:
            msg = msg + coma.attack(coma.memorybomb, comb)
            coma.memory = coma.memory - 400
        else:
            print(len(coma.skills.skills))
            msg = msg + coma.attack(coma.skills.skills[coma.skillcount % 6], comb)
            coma.skillcount = coma.skillcount + 1
            # 回忆炸弹增加
            coma.memory = coma.memory + random.randint(1, 80)
        # 判断对手是否死亡
        if comb.hp <= 0:
            msg = msg + coma.idol.name + "获胜。\n"
            return msg
        # 对手的回合
        if comb.memory >= 400:
            msg = msg + comb.attack(comb.memorybomb, coma)
            comb.memory = comb.memory - 400
        else:
            msg = msg + comb.attack(comb.skills.skills[coma.skillcount % 6], coma)
            comb.skillcount = comb.skillcount + 1
            # 回忆炸弹增加
            comb.memory = comb.memory + random.randint(1, 80)
        # 判断对手是否死亡
        if coma.hp <= 0:
            msg = msg + comb.idol.name + "获胜。\n"
            return msg
        round = round + 1
    msg = msg + "30回合未分胜负，平局。"
    return msg

@sv.on_prefix('偶像pvp', only_to_me=False)
async def idolpvp(bot, ev: CQEvent):
    # 判断输入是否合法
    if ev.message[0].type != 'at':
        await bot.send(ev, "输入不合法！", at_sender=True)
        return
    target_uid = int(ev.message[0].data['qq'])
    send_user = ev['user_id']
    temp_idol1 = None
    temp_idol2 = None
    # 首先判断是否有偶像且是否已训练满
    if send_user in idol_lists.user:
        for i in idol_lists.user_idol_list:
            if i.producer == send_user:
                if i.train <= 0:
                    temp_idol1 = i
                    break
                else:
                    await bot.send(ev, "你的偶像还没有完成训练", at_sender=True)
                    return
    else:
        await bot.send(ev, "你还没有偶像", at_sender=True)
        return
    if target_uid in idol_lists.user:
        for i in idol_lists.user_idol_list:
            if i.producer == target_uid:
                if i.train <= 0:
                    temp_idol2 = i
                    break
                else:
                    await bot.send(ev, "对方的偶像还没有完成训练", at_sender=True)
                    return
    else:
        await bot.send(ev, "对方还没有偶像", at_sender=True)
        return
    #开始pvp
    msg = fight(temp_idol2, temp_idol1)
    await bot.send(ev, msg, at_sender=True)

@sv.on_prefix('偶像pve', only_to_me=False)
async def idolpve(bot, ev: CQEvent):
    send_user = ev['user_id']
    temp_idol = None
    # 首先判断是否有偶像且是否已训练满
    if send_user in idol_lists.user:
        for i in idol_lists.user_idol_list:
            if i.producer == send_user:
                if i.train <= 0:
                    temp_idol = i
                    break
                else:
                    await bot.send(ev, "你的偶像还没有完成训练", at_sender=True)
                    return
    else:
        await bot.send(ev, "你还没有偶像", at_sender=True)
        return
    # 根据输入参数选择对手
    s = ev.message.extract_plain_text()
    if s is None or len(s) == 0:
        await bot.send(ev, "请输入对手序号！", at_sender=True)
    elif s.isdigit():
        num = int(s)
        if num >= len(enemy_lists.enemys):
            await bot.send(ev, "输入不合法！", at_sender=True)
        else:
            msg = fight(temp_idol, enemy_lists.enemys[num])
            await bot.send(ev, msg, at_sender=True)
    else:
        await bot.send(ev, "输入不合法！", at_sender=True)


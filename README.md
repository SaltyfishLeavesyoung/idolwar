# idolwar
基于hoshinobot的培育偶像进行战斗小游戏。偶像的业界，不是杀就是被杀！（大雾）

## 创意来源
创意的来源有两个。一个是[Kasumi Challenge](https://github.com/rMuchan/kasumi-challenge)，另一个是[老婆生成器](https://github.com/pcrbot/Salmon-plugin-transplant/tree/master/laopo)。前者给了我战斗方面的灵感（包含参照《偶像大师闪耀色彩》这方面——你能在这里面找到大量闪耀色彩和其他偶像大师系列的影子），后者给了我捏人方面的参考（为了让偶像形象更丰满）。

## 功能说明
本插件将完全模拟从召集偶像，到培育偶像，到偶像间的厮杀（？）的过程。你可以生成一个偶像，带她进行各项课程或是工作（或者将这一切交给随机数），并在培育结束后和预设的NPC或其他人培育的偶像进行战斗。

过程中随机性较强，从初始的外貌性格属性的设定，到各项数值的提升，到技能的获取几乎完全是随机的（如果你愿意的话，在培养过程中是可以有一定程度上的决策），而战斗过程中的技能释放顺序也是随机决定的。和Kasumi Challenge一样，鼓励大家多尝试创建不同的角色。

## 属性介绍
vo（VOCAL），vi（VISION），da（DANCE）是衡量偶像能力的指标，在闪耀色彩中也是用三部分来评价一个偶像的。由于技能威力和这三个属性相关，故可以看作是攻击力。

me（MENTAL）是衡量偶像心理素质的指标，在闪耀色彩中，被评审员批判会降低，在这里就直接当做是生命值了。

sp是技能点，在培育结束后，每50点sp可以随机获得一个技能。由于最多只有6个技能所以超过300的sp毫无意义。

好感度影响回忆炸弹（相当于大招）的初始充能和威力，最高300。

## 技能设计
技能的json文件在skills文件夹中，共分为4个。分开的原因是本来想设计类似于卡包的系统的，后来懒得做了。可以根据自己的喜好选择用哪些技能，也可以自己加技能。

以雾子包的技能“奇·绮·甘·甘”来说明技能的各项属性。

“奇·绮·甘·甘”的描述是“2.5倍VISION伤害，并回复10%MENTAL，并降低自己受到的伤害10%5回合”

第一句，2.5倍VISION伤害，这个表明了技能的主偏属性跟整体倍率。

一般来说，技能的伤害公式如下：

(VI * VIBUFF * VIRATE + VO * VOBUFF * VORATE + DA * DABUFF * DARATE) * SKILLRATE * DEFENCE * RANDOM

（对于回忆炸弹，回忆炸弹相当于2.5倍vocal,vision,dance混合伤害，但要乘以好感系数，好感系数为好感度/100）

VI,VO,DA就是偶像的原始三项能力。

VIBUFF，VOBUFF，DABUFF则是偶像身上相关属性的buff与debuff之和。比如一个偶像身上有“提高自己VOICE20%”和“降低自己VOICE，VISION10%”两个(de)buff，那么VOBUFF就是1.1，VIBUFF就是0.9，DABUFF就是1。

VIRATE，VORATE，DARATE则是技能本身的属性偏重，在json里是vor,vir,dar。比如“奇·绮·甘·甘”就是主偏VI属性的技能。

主偏属性的RATE值为2，另外两个属性的RATE值为0.2。

顺便一提，如果是偏重三个属性（比如vocal，vision，dance的混合伤害），那么三个RATE值都是0.8（保证和为2.4）。

所以对于“奇·绮·甘·甘”而言，VORATE = 0.2, VIRATE = 2, DARATE = 0.2。

SKILLRATE是技能本身的倍率，在json里是rate。比如“奇·绮·甘·甘”是2.5倍伤害，那么SKILLRATE就是2.5。

而DEFENCE则是**对手**的增伤减伤之和，比如“奇·绮·甘·甘”降低自己受到的伤害10%，那么受到攻击时对方计算伤害时的DEFENCE就是0.9。

增伤减伤算是(de)buff的一种，还有vo,vi,da三属性的增加降低也是。它们有个各自的持续时间。在json文件中，vob,vib,dab是给自己加的三属性buff，dec是减伤（负数为减伤），bt是该buff的持续时间。vodb,vidb,dadb,inc,dbt对应的是对方的debuff。

“奇·绮·甘·甘”中还有回复MENTAL的描述，这部分在json里是rec。

## 战斗细节
摸了摸了，有时间再写。

## 敌人设计
摸了摸了，有时间再写。

## 安装说明
和其他的插件一样，将模块文件夹放进modules下，config的__bot__.py里添加模块idolwar。然后重启hoshino。

## 注意
0. 本插件里面的读取路径使用了**绝对路径**，请在使用前换用你自己的路径。
1. 本插件有着和老婆生成器同样的bug，在后台重启的时候会暂时读取不了偶像数据，使用【生成偶像】命令即可激活。
2. 就算抛开上面的，本插件也可能有着各种各样的bug，欢迎提issue。
3. 如果有技能设计，战斗优化，或者其他提升插件质量的建议也全都欢迎。
# -*- coding: utf-8 -*-

# 语义距离 & 智能推荐
# Author: Alex
# Created Time: 2017年04月16日 星期日 16时58分23秒

from jpype import *

hanLPLibPath = '/var/hanlp/hanlp-1.3.2-release/'
javaClassPath = hanLPLibPath+'hanlp-1.3.2.jar'+':'+hanLPLibPath

startJVM(getDefaultJVMPath(), '-Djava.class.path='+javaClassPath, '-Xms1g', '-Xmx1g')

# 语义距离
wordArray = (
    "香蕉",
    "苹果",
    "白菜",
    "水果",
    "蔬菜",
    "自行车",
    "公交车",
    "飞机",
    "买",
    "卖",
    "购入",
    "新年",
    "春节",
    "丢失",
    "补办",
    "办理",
    "送给",
    "寻找",
    "孩子",
    "教室",
    "教师",
    "会计"
)

CSDictrionary = JClass("com.hankcs.hanlp.dictionary.CoreSynonymDictionary")
for ai in range(len(wordArray)):
    a = wordArray[ai]
    for bi in range(len(wordArray)):
        b = wordArray[bi]
        print(a + "\t" + b + "\t之间的距离是\t", CSDictrionary.distance(a, b))

# 智能推荐
titleArray = (
    "威廉王子发表演说 呼吁保护野生动物",
    "魅惑天后许佳慧不爱“预谋” 独唱《许某某》",
    "《时代》年度人物最终入围名单出炉 普京马云入选",
    "“黑格比”横扫菲：菲吸取“海燕”经验及早疏散",
    "日本保密法将正式生效 日媒指其损害国民知情权",
    "英报告说空气污染带来“公共健康危机”"
)

Suggester = JClass("com.hankcs.hanlp.suggest.Suggester")
suggester = Suggester()
for i in range(len(titleArray)):
    title = titleArray[i]
    suggester.addSentence(title)

print(suggester.suggest("陈述", 2))       # 语义
print(suggester.suggest("危机公关", 1))   # 字符
print(suggester.suggest("mayun", 1))      # 拼音
print(suggester.suggest("徐家汇", 1))     # 拼音

shutdownJVM()

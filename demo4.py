# -*- coding: utf-8 -*-

# 命名实体识别
# Author: Alex
# Created Time: 2017年04月16日 星期日 22时21分22秒

from jpype import *

hanLPLibPath = '/var/www/hanlp/hanlp-1.3.2-release/'
javaClassPath = hanLPLibPath+'hanlp-1.3.2.jar'+':'+hanLPLibPath

startJVM(getDefaultJVMPath(), '-Djava.class.path='+javaClassPath, '-Xms1g', '-Xmx1g')
HanLP = JClass('com.hankcs.hanlp.HanLP')

# 中国人名识别
print("*"*10, "中国人名识别")
text = (
    "签约仪式前，秦光荣、李纪恒、仇和等一同会见了参加签约的企业家。",
    "王国强、高峰、汪洋、张朝阳光着头、韩寒、小四",
    "张浩和胡健康复员回家了",
    "王总和小丽结婚了",
    "编剧邵钧林和稽道青说",
    "这里有关天培的有关事迹",
    "龚学平等领导,邓颖超生前",
    "刘喜杰石国祥会见吴亚琴先进事迹报告团成员"
)

segment = HanLP.newSegment().enableNameRecognize(True)
for i in range(len(text)):
    sentence = text[i]
    print(segment.seg(JString(sentence)))

shutdownJVM()

# -*- coding: utf-8 -*-

# 命名实体识别
# Author: Alex
# Created Time: 2017年04月16日 星期日 22时21分22秒

from jpype import *

hanLPLibPath = '/var/www/hanlp/hanlp-1.3.2-release/'
javaClassPath = hanLPLibPath+'hanlp-1.3.2.jar'+':'+hanLPLibPath

startJVM(getDefaultJVMPath(), '-Djava.class.path='+javaClassPath, '-Xms1g', '-Xmx1g')
HanLP = JClass('com.hankcs.hanlp.HanLP')

text = (
    # 中国人名，标注为nr
    "签约仪式前，秦光荣、李纪恒、仇和等一同会见了参加签约的企业家。",
    "王国强、高峰、汪洋、张朝阳光着头、韩寒、小四",
    "张浩和胡健康复员回家了",
    "王总和小丽结婚了",
    "编剧邵钧林和稽道青说",
    "这里有关天培的有关事迹",
    "龚学平等领导,邓颖超生前",
    "刘喜杰石国祥会见吴亚琴先进事迹报告团成员",

    # 音译人名识别，标注为nrf
    "一桶冰水当头倒下，微软的比尔盖茨、Facebook的扎克伯格跟桑德博格、亚马逊的贝索斯、苹果的库克全都不惜湿身入镜，这些硅谷的科技人，飞蛾扑火似地牺牲演出，其实全为了慈善。",
    "世界上最长的姓名是简森·乔伊·亚历山大·比基·卡利斯勒·达夫·埃利奥特·福克斯·伊维鲁莫·马尔尼·梅尔斯·帕特森·汤普森·华莱士·普雷斯顿。",

    # 地名识别，标注为ns
    "武胜县新学乡政府大楼门前锣鼓喧天",
    "蓝翔给宁夏固原市彭阳县红河镇黑牛沟村捐赠了挖掘机",

    # 机构名识别，标注为nt
    "我在上海林原科技有限公司兼职工作，",
    "同时在上海外国语大学日本文化经济学院学习经济与外语。",
    "我经常在台川喜宴餐厅吃饭，",
    "偶尔去地中海影城看电影。",

    # 追加的测试数据
    "数据雷达是一个外部数据分析平台，帮助商家掌握行业趋势，了解竞争对手的状况等。",
    "公司地址：广州市天河区华观路新塘田头岗二路一横街4号B栋3楼",
    "ibbd.net、IBBD、DeeAo等，以及其他迪奥科技标志及产品、服务名称，均为迪奥科技公司之商标（以下简称“迪奥科技标识”）。未经迪奥科技事先书面同意，您不得将迪奥科技标记以任何方式展示或使用或作其他处理，也不得向他人表明您有权展示、使用、或其他有权处理迪奥科技标识的行为。",
    "质量很好，相当满意，清明出游前一天去笔架山公园走一万多步，后一天去杨梅坑，走下面的石头路走了两万多步，脚都没痛，就是鞋子脏了一点点，上脚版型也很好的，值得推荐和购买！马上要再入一双，哈哈哈哈",
)

segment = HanLP.newSegment().enableNameRecognize(True)\
    .enableTranslatedNameRecognize(True)\
    .enablePlaceRecognize(True)\
    .enableOrganizationRecognize(True)
for i in range(len(text)):
    sentence = text[i]
    print(segment.seg(JString(sentence)))

shutdownJVM()

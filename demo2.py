# -*- coding: utf-8 -*-

#
# Author: Alex
# Created Time: 2017年04月16日 星期日 16时33分23秒
# See: http://www.hankcs.com/nlp/python-calls-hanlp.html

from jpype import *

hanLPLibPath = '/var/www/hanlp/hanlp-1.3.2-release/'
javaClassPath = hanLPLibPath+'hanlp-1.3.2.jar'+':'+hanLPLibPath

startJVM(getDefaultJVMPath(), '-Djava.class.path='+javaClassPath, '-Xms1g', '-Xmx1g')
HanLP = JClass('com.hankcs.hanlp.HanLP')

# 中文分词
print(HanLP.segment('你好，欢迎在Python中调用HanLP的API'))
testCases = [
    "商品和服务",
    "结婚的和尚未结婚的确实在干扰分词啊",
    "买水果然后来世博园最后去世博会",
    "中国的首都是北京",
    "欢迎新老师生前来就餐",
    "工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作",
    "随着页游兴起到现在的页游繁盛，依赖于存档进行逻辑判断的设计减少了，但这块也不能完全忽略掉。",
    "晕死 你没有看清楚呀 我是说我爸爸生意伙伴很多在广州做生意"
]
for sentence in testCases:
    print(HanLP.segment(sentence))

# 命名实体识别与词性标注
print("*"*10, "命名实体识别与词性标注")
NLPTokenizer = JClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')
print(NLPTokenizer.segment('中国科学院计算技术研究所的宗成庆教授正在教授自然语言处理课程'))

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
)

# Segment = JClass("com.hankcs.hanlp.recognition.nr.PersonRecognition")
# segment = Segment()
segment = HanLP.newSegment().enableNameRecognize(True)
for i in range(len(text)):
    sentence = text[i]
    # print(segment.segment(sentence).toString())
    print(segment.seg(sentence))

# 关键词提取
print("*"*10, "关键词提取")
document = "水利部水资源司司长陈明忠9月29日在国务院新闻办举行的新闻发布会上透露，" \
    "根据刚刚完成了水资源管理制度的考核，有部分省接近了红线的指标，" \
    "有部分省超过红线的指标。对一些超过红线的地方，陈明忠表示，对一些取用水项目进行区域的限批，" \
    "严格地进行水资源论证和取水许可的批准。"
print(HanLP.extractKeyword(document, 5))

# 自动摘要
print("*"*10, "自动摘要")
print(HanLP.extractSummary(document, 5))

# 短语提取
print("*"*10, "短语提取")
print(HanLP.extractPhrase(document, 5))

# 依存句法分析
print("*"*10, "依存句法分析")
print(HanLP.parseDependency("徐先生还具体帮助他确定了把画雄鹰、松鼠和麻雀作为主攻目标。"))

shutdownJVM()

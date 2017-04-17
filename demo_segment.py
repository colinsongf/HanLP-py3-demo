# -*- coding: utf-8 -*-

# 分词demo
# Author: Alex
# Created Time: 2017年04月17日 星期一 16时51分05秒

from jpype import *

hanLPLibPath = '/var/hanlp/hanlp-1.3.2-release/'
javaClassPath = hanLPLibPath+'hanlp-1.3.2.jar'+':'+hanLPLibPath

startJVM(getDefaultJVMPath(), '-Djava.class.path='+javaClassPath, '-Xms1g', '-Xmx1g')
HanLP = JClass('com.hankcs.hanlp.HanLP')


def InfoTitle(title):
    print("")
    print("*"*10, title, "*"*10)

# text = '中国科学院计算技术研究所的宗成庆教授正在教授自然语言处理课程'
# text = '数据雷达是一个外部数据分析平台，帮助商家掌握行业趋势，了解竞争对手的状况等。'
text = '广州迪奥信息科技有限公司是一个集大数据研发，产品及服务的公司。旗下有数据雷达等产品，公司创始人郭燚毕业于华南理工大学。公司地址位于广州市天河区华观路新塘田头岗二路一横街4号B栋3楼。'

# 标准分词
# 标准分词是最常用的分词器，基于HMM-Viterbi实现，开启了中国人名识别和音译人名识别
# HanLP.segment 其实是对 StandardTokenizer.segment 的包装。
# HanLP中有一系列“开箱即用”的静态分词器，以 Tokenizer 结尾
InfoTitle("标准分词")
termList = HanLP.segment(text)
print(termList)

# NLP分词
# NLPTokenizer 会执行全部命名实体识别和词性标注。
# 速度比标准分词慢，并且有误识别的情况。
InfoTitle("NLP分词")
tokenizer = JClass('com.hankcs.hanlp.tokenizer.NLPTokenizer')
print(tokenizer.segment(text))

# 索引分词
# IndexTokenizer 是面向搜索引擎的分词器，能够对长词全切分，另外通过
# term.offset 可以获取单词在文本中的偏移量。
InfoTitle("索引分词")
tokenizer = JClass('com.hankcs.hanlp.tokenizer.IndexTokenizer')
termList = tokenizer.segment(text)
for i in range(len(termList)):
    term = termList[i]
    print(term, " \t", term.offset, ":", term.offset + len(term.word))

# 通过HanLP.newSegment
# 通过此工厂方法得到的是当前版本速度和效果最平衡的分词器
# 推荐用户始终通过工具类HanLP调用，这么做的好处是，将来HanLP升级后，用户无需修改调用代码。
InfoTitle("通过HanLP.newSegment")
segment = HanLP.newSegment().enableNameRecognize(True)\
    .enableTranslatedNameRecognize(True)\
    .enablePlaceRecognize(True)\
    .enableOrganizationRecognize(True)
# 注意
# 报错：RuntimeError: Multiple overloads possible.
termList = segment.seg(JString(text))
print(termList)

shutdownJVM()

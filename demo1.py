# -*- coding: utf-8 -*-

# hello world
# Author: Alex
# Created Time: 2017年04月16日 星期日 16时20分23秒

from jpype import *

hanLPLibPath = '/var/www/hanlp/hanlp-1.3.2-release/'
javaClassPath = hanLPLibPath+'hanlp-1.3.2.jar'+':'+hanLPLibPath

startJVM(getDefaultJVMPath(), '-Djava.class.path='+javaClassPath, '-Xms1g', '-Xmx1g')

java.lang.System.out.println("hello world")
shutdownJVM()

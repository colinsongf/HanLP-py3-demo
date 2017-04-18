#!/bin/bash
# 
# 
# Author: Alex
# Created Time: 2017年04月16日 星期日 16时30分21秒

container=ibbd/java-python3

# 先删除旧
docker rm $container

# 重新运行
docker run -ti --name=ibbd-java-py3-server \
    -v /var/www/hanlp/:/var/hanlp/ \
    -v /var/www/:/var/www/ \
    $container /bin/bash

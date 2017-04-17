#!/bin/bash
# 
# 
# Author: Alex
# Created Time: 2017年04月16日 星期日 16时30分21秒

# 先删除旧
docker rm ibbd-java-py3

# 重新运行
docker run -ti --name=ibbd-java-py3 \
    -v /var/www/hanlp/:/var/hanlp/ \
    -v /var/www/:/var/www/ \
    ibbd/java-python3 /bin/bash

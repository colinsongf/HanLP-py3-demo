#!/bin/bash
# 
# 
# Author: 
# Created Time: 2017年04月16日 星期日 16时30分21秒

docker run -ti --name=ibbd-java-py3 \
    -v /var/www/:/var/www/ \
    ibbd/java-python3 /bin/bash

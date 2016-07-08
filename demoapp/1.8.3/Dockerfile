# 1. 基础镜像.
# Author:  yangjun <597092663@qq.com>
FROM 10.5.24.46:80/nscloud/ubuntu:14.04

# 2. 镜像BUILD默认参数 & RUN环境变量.
# ARG APP_PATH="/opt/applications"    # !!!No Modification, Must Be Same As Base Image.

ENV MYSQL_DATABASE=""
ENV MYSQL_USER=""
ENV MYSQL_PASSWORD=""
ENV MYSQL_HOST=""
ENV MYSQL_PORT=""
ENV ADMIN_PASSWORD=""
ENV MODULE_NAME=""

# 3. 镜像生成过程操作指令.
ENV APP_PATH=${APP_PATH}
ENV EXPOSE_PORT="22 80 443"

# 3.1 将build-depends拷贝到镜像中
# copy build-depends of applications to images
RUN mkdir -p ${APP_PATH}/build-depends
COPY ./applications/build-depends/ ${APP_PATH}/build-depends

# 3.2 安装Nginx
# pip install packages
RUN pip install -r ${APP_PATH}/build-depends/pip-requirements/requirements-django.txt

# 3.3 安装pip依赖
# apt install packages
RUN apt-get update -y \
    && apt-get install nginx -y

# 4. 指定容器需要暴露的端口.
# EXPOSE ${EXPOSE_PORT}

# 5. 指定容器需要使用的持久化存储.
# VOLUME ["/var/lib/mysql"]

# 6. 容器启动指令: 如果为LongTime Service，不能起为后台进程.
COPY ./applications/ ${APP_PATH}
RUN chmod a+x ${APP_PATH}/run.sh
CMD ["/bin/bash", "-c", "cd ${APP_PATH} && ./run.sh"]


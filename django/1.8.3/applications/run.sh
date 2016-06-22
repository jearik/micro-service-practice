#!/bin/bash
set -eux
env

# runtime configuration
python ${APP_PATH}/build-utils/configueUpdate/templateInvoke.py ${APP_PATH}/com/urlprefix.py.template ${APP_PATH}/com/urlprefix.py
python ${APP_PATH}/build-utils/configueUpdate/templateInvoke.py ${APP_PATH}/mysite/settings.py ${APP_PATH}/mysite/settings.py
pushd ${APP_PATH} && python manage.py migrate auth --noinput >> /dev/null \
    && echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '', '${3A_ADMIN_PASSWORD}')" | python manage.py shell | echo "add admin" \
    && python manage.py collectstatic --noinput >> /dev/null \
    && python manage.py migrate --noinput >> /dev/null && popd

python ${APP_PATH}/build-utils/configueUpdate/templateInvoke.py ${APP_PATH}/uwsgi-conf.d/uwsgi.ini.template ${APP_PATH}/uwsgi-conf.d/uwsgi.ini
python ${APP_PATH}/build-utils/configueUpdate/templateInvoke.py ${APP_PATH}/nginx-conf.d/default.template ${APP_PATH}/nginx-conf.d/default
cp ${APP_PATH}/nginx-conf.d/default /etc/nginx/sites-available/default
mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak && cp ${APP_PATH}/nginx-conf.d/nginx.conf /etc/nginx/
python ${APP_PATH}/build-utils/configueUpdate/templateInvoke.py ${APP_PATH}/supervisor.conf.d/uwsgi.conf
cp ${APP_PATH}/supervisor.conf.d/*.conf /etc/supervisor/conf.d/

# start supervisord nodaemon
/usr/bin/supervisord --nodaemon


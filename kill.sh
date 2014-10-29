kill -9 `ps -ef | grep uwsgi.xml | head -99 | awk '{print $2}'`

#!/usr/bin/env bash
# Prepare your web server
sudo apt update -y;
sudo apt install nginx -y;
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
printf %s "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
printf %s "server {
    listen          80 default_server;
    listen          [::]:80 default_server;
    root            /etc/nginx/html;
    index           index.html;
    error_page 404  /custom_404.html;
    location    /hbnb_static {
        alias   /data/web_static/current/;
        index   index.html;
    }
    location    /redirect_me {
        return 301 http://gnomeo.tech/redirect_me;
    }
    location = /custom_404.html {
        root /etc/nginx/html;
        internal;
    }
}" > /etc/nginx/sites-available/default
sudo service nginx restart

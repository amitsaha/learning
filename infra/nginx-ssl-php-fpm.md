## Setting up nginx + php-fpm

- Install nginx, php-fpm
- Add sits-enabled directory in nginx.conf: include /etc/nginx/sites-enabled/*;
- Example config for `virtualhost1.com`

```
cat virtualhost1.com 

server {
        listen   443; ## listen for ipv4; this line is default and implied
        #listen   [::]:80 default ipv6only=on; ## listen for ipv6

        root /var/www/virtualhost1.com/Cachet/public;
        index index.php;

        # Make site accessible from http://virtualhost1.com/
        server_name virtualhost1.com;

	ssl on;
        ssl_certificate /etc/nginx/ssl/virtualhost1.com/server.crt;
        ssl_certificate_key /etc/nginx/ssl/virtualhost1.com/server.key;
        ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
	ssl_prefer_server_ciphers on;
        ssl_ciphers "ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:AES:CAMELLIA:DES-CBC3-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!aECDH:!EDH-DSS-DES-CBC3-SHA:!EDH-RSA-DES-CBC3-SHA:!KRB5-DES-CBC3-SHA";
       ssl_buffer_size 1400; # 1400 bytes, within MTU - because we generally have small responses. Could increase to 4k, but default 16k is too big

        location / {
        add_header Strict-Transport-Security max-age=15768000;
        try_files $uri /index.php$is_args$args;
        }
 
	location ~ \.php$ {
              try_files $uri =404;
              fastcgi_split_path_info ^(.+\.php)(/.+)$;
              fastcgi_pass   unix:/var/run/php-fpm/virtualhost1.sock;
              fastcgi_index  index.php;
              fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
              include        fastcgi_params;
    }


```

- Config for php-fpm pool: virtualhost1.conf in /etc/php-fpm.d/virtualhost1.conf, start the section with `virtualhost1` and `listen = /run/php-fpm/virtualhost1.sock`
- Configure the user and group to be `nginx`, `nginx`

Resources:

- https://serversforhackers.com/video/php-fpm-multiple-resource-pools
- SSL setup: https://www.digitalocean.com/community/tutorials/how-to-set-up-multiple-ssl-certificates-on-one-ip-with-nginx-on-ubuntu-12-04
- http://php.net/manual/en/install.fpm.php

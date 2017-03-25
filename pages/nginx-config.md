title: nginx configuration- static web
date: 2017-03-13
tags: [nginx, server, linux]
subtitle: Let get into Linux server... For sometime now, i have been obsessed with linux servers. So i am not really a fun of Apache. I love python because my first methor love it.



Configuring **Nginx** on linux servers should be easy. Lets begin with our
linux update and installation.

`$ sudo apt-get update && sudo apt-get install nginx`

pull up your favourite browser and hit `127.0.0.1` to verify if **nginx** is
running properly. alternatively. Verify the status from the shell

`$ systemctl status nginx.service`

now lets do some configuration.

`cd /etc/nginx/sites-available`

if its not available, means your nginx is not installed properly
Lets see the content of the folder

`$ ls`

lets make a copy of the default file

`$ sudo mv ./default ./startbootstrap-freelancer`

### Now we are ready to edit.

```server {
	listen 8080;
	server_name _;
	root /var/www/startbootrap-freelancer;
	index index.html;

	location / {
					try_files $uri $uri/ =404;
					}
	}
```

Let your server parameter be similar to this. You can optionally change the
_listen_ port.

The root directory is where our webfiles would be. **/var/www/** directory.

`$ cd /var/www/`

### Lets clone the repo
We could alternatively move copy/move and already existing project into the
**/var/www**

`$ git clone https://github.com/BlackrockDigital/startbootstrap-freelancer.git`

### Dont be in a haste.. lets create the symlink.
There are two important folders in
`/etc/nginx/`, _sites-available_ folder and _sites-enabled_ folder.

`$ cd /etc/nginx/sites-enabled`

### Create symlink
`$ sudo ln -s /etc/nginx/sites-available startbootstrap-freelancer`

### Lets restart out nginx service.
`sudo service nginx restart`

### Verify the status once again.
`$ systemctl status nginx.service`

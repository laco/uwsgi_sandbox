Steps for Ubuntu 12.04 LTS
-------------------------

1. Install all the deb packages in debs.txt

2. mkvirtualenv uwsgi_sandbox1

3. Install the requirements in the virtualenv with pip install -r requirements.txt 

4. create a symlink for ./etc/supervisor/conf.d/uwsgi_sandbox1.conf in the  /etc/supervisor/conf.d/ directory

5. Adjust configuration (directories, etc.)

6. Restart supervisor: sudo /etc/init.d/supervisor restart


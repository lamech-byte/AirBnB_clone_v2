#!/usr/bin/python3
# Fabric script that distributes an archive to web servers
# distributes an archive to your web servers, using the function do_deploy:

from fabric.api import *
from os.path import exists
import os

env.hosts = ['54.236.17.124', '100.24.237.123']

# Update with your username
env.user = "root"  

# Update with your private key path
env.key_filename = '~/.ssh/id_rsa'  


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload archive to /tmp/ directory of web server
        put(archive_path, "/tmp/")

        # Uncompress archive to /data/web_static/releases/
        archive_filename = os.path.basename(archive_path)
        archive_no_ext = os.path.splitext(archive_filename)[0]
        run("mkdir -p /data/web_static/releases/{}".format(archive_no_ext))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(archive_filename, archive_no_ext))
        run("rm /tmp/{}".format(archive_filename))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/"
            .format(archive_no_ext, archive_no_ext))
        run("rm -rf /data/web_static/releases/{}/web_static".format(archive_no_ext))

        # Delete symbolic link
        run("rm -rf /data/web_static/current")

        # Create new symbolic link
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(archive_no_ext))
        return True

    except:
        return False

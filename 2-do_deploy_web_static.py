#!/usr/bin/python3
# Fabric script for distributing an archive to web servers.

import os.path
from fabric.api import env, put, run

# Set the list of remote hosts to distribute the archive to.
env.hosts = ['54.236.17.124', '100.24.237.123']


def do_deploy(archive_path):
    """
    Distributes an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.

    Returns:
        bool: True if the archive is distributed successfully, False otherwise.
    """

    # Check if the file exists at archive_path.
    if os.path.isfile(archive_path) is False:
        return False

    # Extract the name of the file and the name of the directory to create.
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    # Upload the archive to the remote host.
    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False

    # Remove the old directory and create a new one to extract the archive into.
    if run("rm -rf /data/web_static/releases/{}/".format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".format(name)).failed is True:
        return False

    # Extract the archive into the new directory.
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file, name)).failed is True:
        return False

    # Remove the uploaded archive.
    if run("rm /tmp/{}".format(file)).failed is True:
        return False

    # Move the contents of the extracted directory to the new directory.
    if run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name, name)).failed is True:
        return False

    # Remove the old directory and create a symbolic link to the new directory.
    if run("rm -rf /data/web_static/releases/{}/web_static".format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name)).failed is True:
        return False

    # Return True if the archive is successfully distributed.
    return True

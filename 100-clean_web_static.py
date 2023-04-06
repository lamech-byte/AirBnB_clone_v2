#!/usr/bin/python3
# This is a Fabfile that creates and distributes an archive to a web server.
# It includes the do_pack() and do_deploy() functions.

import os.path
from datetime import datetime
from fabric.api import env, local, put, run

# Define the web server hosts
env.hosts = ["54.236.17.124", "100.24.237.123"]

def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    # Get the current date and time
    dt = datetime.utcnow()
    # Create a filename based on the date and time
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    # Create a versions directory if it doesn't exist
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    # Create the tar gzipped archive
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    # Return the filename of the archive
    return file


def do_deploy(archive_path):
    """Distribute an archive to a web server.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    # Check if the archive exists
    if os.path.isfile(archive_path) is False:
        return False
    # Extract the filename and name of the archive
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]
    # Upload the archive to the server
    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    # Create a new release directory and extract the archive
    if run("rm -rf /data/web_static/releases/{}/".format(name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file, name)).failed is True:
        return False
    # Move the contents of the archive to the release directory and delete the original directory
    if run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".format(name)).failed is True:
        return False
    # Create a symbolic link to the new release directory and delete the old link
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name)).failed is True:
        return False
    return True


def deploy():
    """Create and distribute an archive to a web server."""
    # Create the archive
    file = do_pack()
    if file is None:
        return False
    # Distribute the archive to the server
    return do_deploy(file)

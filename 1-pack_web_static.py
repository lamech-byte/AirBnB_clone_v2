#!/usr/bin/python3
# A Fabfile for creating a compressed archive of web_static.

import os.path
from datetime import datetime
from fabric.api import local

def pack_web_static():
    """
    Creates a compressed archive of web_static directory.
    """
    now = datetime.utcnow()
    timestamp = '{}{:02d}{:02d}{:02d}{:02d}{:02d}'.format(now.year, now.month, now.day, now.hour, now.minute, now.second)
    archive_name = "versions/web_static_{}.tgz".format(timestamp)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -czvf {} web_static".format(archive_name)).failed is True:
        return None
    return archive_name

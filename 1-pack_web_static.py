#!/usr/bin/env python3
# Fabric script to generate a .tgz archive from web_static

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """ Generates a .tgz archive """

    now = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_" + now + ".tgz"
    archive_path = os.path.join("versions", archive_name)

    if not os.path.exists("versions"):
        os.makedirs("versions")

    try:
        local("tar -czvf {} web_static".format(archive_path))
        return archive_path
    except:
        return None

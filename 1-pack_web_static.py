#!/usr/bin/env python3
# Fabric script to generate a .tgz archive from web_static

from fabric.api import local
from datetime import datetime

def do_pack():
    """ Creates a compressed archive of the web_static folder """
    
    local("mkdir -p versions")
    t = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    archive = local("tar -czvf versions/web_static_{}\
.tgz web_static".format(t))
    if archive:
        return ("versions/web_static_{}".format(t))
    else:
        return None

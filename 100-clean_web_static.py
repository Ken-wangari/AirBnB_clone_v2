#!/usr/bin/python3

"""
Deletes out-of-date archives
fab -f 100-clean_web_static.py do_clean:number=2
    -i ssh-key -u ubuntu > /dev/null 2>&1
"""

import os
from fabric.api import env, lcd, run, local

env.hosts = ['35.243.128.200', '3.239.120.96']


def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): The number of archives to keep.
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    # Delete local archives
    with lcd("versions"):
        archives = sorted(os.listdir("."))
        to_delete = archives[:-number] if number > 0 else archives
        for archive in to_delete:
            local(f"rm {archive}")

    # Delete remote archives
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        to_delete = archives[:-number] if number > 0 else archives
        for archive in to_delete:
            run(f"rm -rf {archive}")


if __name__ == "__main__":
    do_clean(number=2)


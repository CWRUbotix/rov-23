import os
import shutil
import sys


if __name__ == '__main__':
    share_dir = sys.argv[1]

    udev_src_dir = os.path.join(share_dir, 'udev_rules')
    udev_dst_dir = os.path.join('/etc', 'udev', 'rules.d')

    shutil.copytree(udev_src_dir, udev_dst_dir, dirs_exist_ok=True)
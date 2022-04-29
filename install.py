#!/usr/bin/python

import os
import distro

def snap_config():
    os.system('sudo systemctl enable --now snapd.socket')
    os.system('sudo ln -s /var/lib/snapd/snap /snap')

def snap_fedora():
    os.system('sudo dnf install snapd')
    snap_config()

def snap_arch():
    os.system('yay -S snapd')
    snap_config()

def snap_ubuntu_flavor():
    os.system('apt-update')
    os.system('sudo apt install snapd')

def install_sdk():
    os.system('sudo snap install flutter --classic')

def check_installation():
    out = os.popen('whereis flutter')
    return out.readline().find('/') != -1

id = distro.LinuxDistribution()._os_release_info['id_like']
snap_swicth = {
    'arch': snap_arch,
    'fedora': snap_fedora,
    'ubuntu': snap_ubuntu_flavor,
}

if not check_installation():
    try:
        snap_swicth[id]()
    except:
        throw('ERROR: distribution type not supported')
    install_sdk()
    print('SUCCESS: Flutter installed')
    print('Run flutter doctor to confirm that Flutter has located your installation of Android Studio.\nIf Flutter cannot locate it, run flutter config --android-studio-dir <directory> to set the directory that Android Studio is installed to.')
else:
    print('Flutter seems to already be installed on your machine.')

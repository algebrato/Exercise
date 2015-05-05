#!/bin/bash

do_fstab(){
echo -e   "# This file is edited by fstab-sync - see 'man fstab-sync' for details
# /etc/fstab: static file system information.
# $Header: /home/cvsroot/gentoo-src/rc-scripts/etc/fstab,v 1.10 2002/11/18 19:39:22 azarah Exp $
#
# noatime turns of atimes for increased performance (atimes normally aren't
# needed; notail increases performance of ReiserFS (at the expense of storage
# efficiency).  It's safe to drop the noatime options if you want and to 
# switch between notail and tail freely.

# <fs>                                               <mountpoint>    <type>     <opts>                   <dump/pass>

proc                                                 /proc           proc       defaults                 0 0
192.168.2.1:/farm/etc                                /etc            nfs        noatime,ro               0 0
# cfr con rc.local (such a baroque cluster!)
192.168.2.1:/farm/diskless-root/$1/var/etc      /var/etc           nfs        noatime,ro               0 0
192.168.2.1:/farm/diskless-root/$1                 /               nfs        noatime                  0 0
192.168.2.1:/farm/bin                                /bin            nfs        noatime,ro               0 0
192.168.2.1:/farm/sbin                               /sbin           nfs        noatime,ro               0 0
192.168.2.1:/farm/usr                                /usr            nfs        noatime,ro               0 0
192.168.2.1:/farm/opt                                /opt            nfs        noatime,ro               0 0
192.168.2.1:/farm/lib                                /lib            nfs        noatime,ro               0 0
192.168.2.1:/farm/emul                               /emul           nfs        noatime,ro               0 0
192.168.2.1:/farm/root                               /root           nfs        noatime,ro               0 0
192.168.2.1:/home                                    /home           nfs        noatime,rw               0 0
192.168.2.1:/usr/local/share/lhapdf                  /usr/local/share/lhapdf         nfs        noatime,ro               0 0
/dev/sda5                                            /var            ext3       defaults                 0 0
/dev/sda6                                            /tmp            ext3       defaults                 0 0
/dev/sda7                                            none            swap       sw                       0 0
/dev/sda9                                            /storage/local  xfs        defaults,rtdev=/dev/sda8 0 0

# glibc 2.2 and above expects tmpfs to be mounted at /dev/shm for
# POSIX shared memory (shm_open, shm_unlink). Adding the following
# line to /etc/fstab should take care of this:
# (tmpfs is a dynamically expandable/shrinkable ramdisk, and will use almost no
#  memory if not populated with files)

tmpfs                                                /dev/shm        tmpfs      defaults                 0 0
cpuset                                               /dev/cpuset     cpuset     defaults                 0 0
tmpfs                                                   /run            tmpfs   noatime,rw      0 0

192.168.2.200:/farmstorage      /farmstorage    nfs rw  0       0" > fstab

}


do_create(){
	do_fstab $1
}



if [[ -z $1 ]];then
	echo "Error: Node name not found"
else
	do_create $1
fi



exit 0

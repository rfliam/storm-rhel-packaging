storm-rhel-packaging
====================

Packaging for redhat and fedora style RPM installations, including init.d scripts, default configurations, and a .spec file for building an RPM. I have also included the built 0.7.4 RPM and associated dependencies (built and working in our environment). Also included are monit scripts that go in /etc/monit.d/ if you so choose. The source RPM contains the entire package I used for building. This gives storm a more cannonical fedora layout, with the storm working directories being in /var/opt/storm/(nimbus/supervisor/ui), logs going to /var/log/storm, and pid files being stored in /var/run/storm. Tweaks for config launches can be found in /etc/sysconfig/storm.

Install Instructions
=====================
[Download](https://github.com/rfliam/storm-rhel-packaging/downloads) the .rpms (the .src.rpm is not needed).
Execute: 
```bash
yum localinstall zeromq-2.2.0-1.el6.x86_64.rpm jzmq-2.1.0-1.el6.x86_64.rpm storm-0.7.4-1.el6.x86_64.rpm  -y --nogpgcheck
```

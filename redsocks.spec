Name: redsocks-seabrowser
Version: 0.4
Release: 2
License: Seabrowser
Summary: redsocks customized for seabroswer
Group: Applications/Network
Packager: Seabrowser
autoprov: yes
autoreq: yes

requires: initscripts, coreutils, sed, chkconfig

%description

%install
mkdir $RPM_BUILD_ROOT/usr $RPM_BUILD_ROOT/usr/sbin $RPM_BUILD_ROOT/etc $RPM_BUILD_ROOT/etc/sysconfig $RPM_BUILD_ROOT/etc/init.d
cp %_builddir/redsocks $RPM_BUILD_ROOT/usr/sbin
cp %_builddir/debian/redsocks.conf $RPM_BUILD_ROOT/etc
cp %_builddir/debian/init.d $RPM_BUILD_ROOT/etc/init.d/redsocks
cp %_builddir/redsocks-iptables $RPM_BUILD_ROOT/etc/sysconfig/iptables

%files
%defattr(644,redsocks,redsocks,755)
 "/etc/redsocks.conf"
%attr(755,redsocks,redsocks) "/usr/sbin/redsocks"
%attr(755,redsocks,redsocks) "/etc/init.d/redsocks"
 "/etc/sysconfig/iptables"

%pre
id -g redsocks &>/dev/null || groupadd redsocks
id -u redsocks &>/dev/null || useradd -g redsocks -r -s /bin/false redsocks

%post
sysctl net.ipv4.ip_forward=1
service iptables restart

chown redsocks:redsocks /etc/redsocks.conf

chkconfig --add redsocks
chkconfig redsocks off

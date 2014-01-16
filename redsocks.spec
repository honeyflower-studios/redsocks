Name: redsocks-seabrowser
Version: 0.4
Release: 1
License: Seabrowser
Summary: redsocks customized for seabroswer
Group: Applications/Network
Packager: Seabrowser
autoprov: yes
autoreq: yes

%description

%install

%files
%defattr(644,redsocks,redsocks,755)
 "/etc/redsocks.conf"
%attr(755,redsocks,redsocks) "/usr/sbin/redsocks"
%attr(755,redsocks,redsocks) "/etc/init.d/redsocks"

%pre
id -g redsocks &>/dev/null || groupadd redsocks
id -u redsocks &>/dev/null || useradd -g redsocks -r -s /bin/false redsocks

%post
sed -i "s/net.ipv4.ip_forward.*/net.ipv4.ip_forward=1/g" /etc/sysctl.conf
chown redsocks:redsocks /etc/redsocks.conf
chkconfig --add redsocks
chkconfig redsocks off

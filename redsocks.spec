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
%attr(755,redsocks,redsocks) "/usr/bin/redsocks"
%attr(755,redsocks,redsocks) "/etc/init.d/redsocks"

%pre
id -u redsocks &>/dev/null || useradd redsocks

%post
chkconfig --add redsocks
chkconfig redsocks off

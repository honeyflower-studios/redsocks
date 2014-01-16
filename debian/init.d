#!/bin/bash
#
# Daemon Name: redsocks
#  
# chkconfig: 2345 58 74
# description: RedSocks allows you to redirect any TCP connection to SOCKS or HTTPS proxy using your firewall, so redirection is system-wide.

# Source function library.
. /etc/init.d/functions

# pull in sysconfig settings
[ -f /etc/sysconfig/redsocks ] && . /etc/sysconfig/redsocks

prog=redsocks
lockfile=/var/lock/subsys/$prog
config=/etc/$prog.conf

start() {

    rh_status_q && exit 0
    #Make some checks for requirements before continuing
    [ "$NETWORKING" = "no" ] && exit 1
    [ -x /usr/sbin/$prog ] || exit 5

    # Start our daemon daemon
    echo -n $"Starting $prog: "
    daemon --pidfile /var/run/${proc}.pid $prog -c $config
    RETVAL=$?
    echo

    #If all is well touch the lock file
    [ $RETVAL -eq 0 ] && touch $lockfile
    return $RETVAL
}

stop() {
    echo -n $"Shutting down $prog: "
    killproc $prog
    RETVAL=$?
    echo

    #If all is well remove the lockfile
    [ $RETVAL -eq 0 ] && rm -f $lockfile
    return $RETVAL
}

rh_status() {
	status $prog
}

rh_status_q() {
	rh_status >/dev/null 2>&1
}

# See how we were called.
case "$1" in
  start)
        rh_status_q && exit 0
        start
        ;;
  stop)
        stop
        ;;
  status)
        rh_status
        ;;
  restart)
        stop
        start
        ;;
   *)
        echo $"Usage: $0 {start|stop|status|restart}"
        exit 2
esac
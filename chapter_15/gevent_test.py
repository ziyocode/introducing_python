import gevent
from gevent import socket


hosts = ["www.shinhan.com", "sol.shinhan.com", "www.naver.com"]
jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
# print(jobs)
# <Greenlet at 0x10ef799d0: gethostbyname('www.shinhan.com')>,
# <Greenlet at 0x10f14fbf0: gethostbyname('sol.shinhan.com')>, 
# <Greenlet at 0x10f38e040: gethostbyname('www.naver.com')>]
gevent.joinall(jobs, timeout=5)
for job in jobs:
    print(job.value)
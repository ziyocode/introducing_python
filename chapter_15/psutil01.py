# pip install psutil 필요

import psutil

print(psutil.cpu_times(True))
# cpu 갯수만큼의 결과를 list type으로 반환
# [scputimes(user=27257.83, nice=0.0, system=43978.15, idle=103326.37), 
# scputimes(user=2944.59, nice=0.0, system=5331.61, idle=166229.68), 
# scputimes(user=24623.22, nice=0.0, system=41740.64, idle=108144.86), 
# scputimes(user=2921.79, nice=0.0, system=5196.99, idle=166386.93), 
# scputimes(user=21031.64, nice=0.0, system=35230.4, idle=118246.47), 
# scputimes(user=2907.23, nice=0.0, system=5039.73, idle=166558.54), 
# scputimes(user=19040.84, nice=0.0, system=31043.14, idle=124424.31), 
# scputimes(user=2914.2, nice=0.0, system=4865.3, idle=166725.78)]

print(psutil.cpu_percent(True))
# 23.8
print(psutil.cpu_percent(percpu=True))
# [41.6, 3.0, 43.0, 2.0, 50.0, 3.0, 43.6, 3.0]


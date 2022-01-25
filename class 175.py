# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:33:36 2022

@author: DELL
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 15:09:55 2022

@author: DELL
"""

import matplotlib .pyplot as plt
import psutil as p
app_name_dict={}
count=0
for process in p.process_iter():
    count=count+1
    if count<=6:
        name=process.name()
        cpu_usage=p.cpu_percent()
        print('Name : ',name,'cpu_usage=',cpu_usage)
        app_name_dict.update({name:cpu_usage})

keymax=max(app_name_dict,key=app_name_dict.get)
keymin=min(app_name_dict,key=app_name_dict.get)
name_list=[keymax,keymin]

app=app_name_dict.values()
max_app=max(app)
min_app=min(app)
maxmin_list=[max_app,min_app]
print(maxmin_list)
print("Maximum",max_app)
print("Minimum",min_app)

plt.figure(figsize=(15, 7))
plt.xlabel("Minmaxcpu_consumption")
plt.ylabel("usage")
plt.bar(name_list, maxmin_list, width=0.6, color=("Turquoise","Cyan","Blue","Lime","Green","Yellow"))
plt.show()
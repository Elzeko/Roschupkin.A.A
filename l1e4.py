# -- coding: utf-8 --
s = 10000
days = s // 86400 
hours = (s % 86400) // 3600
minutes = ((s % 86400) % 3600) // 60
seconds = (((s % 86400) % 3600) % 60) % 60 
print (days ,'дней:', hours ,'часов:', minutes ,'минут:', seconds ,'секунд')

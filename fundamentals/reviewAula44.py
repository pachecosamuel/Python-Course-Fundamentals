mydict = dict(sorted(([('samu', 19562.29), ('joão', 222), ('maria', 999)])))
mydict.update({'ana': 5000})

copydict = mydict.fromkeys(mydict, 100)


mydict.pop('ana')
print(mydict)




with open ('listaclasei.txt', 'r')as f:
    x=str((f.read()))
print (x)
print (sorted(x.split(','))) 
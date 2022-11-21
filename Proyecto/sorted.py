repeat=[1,4,5,6,7,8,9,9,1,5,7,7]
repeat = sorted(repeat)
for i in range(len(repeat)-1):
    if repeat[i]==repeat[i+1]:
        hola= True
hola= False

if hola == True:
    print('found it')
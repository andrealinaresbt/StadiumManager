def getPossible(lst, n):
            
            if n == 0:
                return [[]]
            
            l =[]
            for i in range(0, len(lst)):
                
                m = lst[i]
                remLst = lst[i + 1:]
                
                remainlst_combo = getPossible(remLst, n-1)
                for p in remainlst_combo:
                    l.append([m, *p])
                
            return l



def vampiro():
     fangs= []
     number = (input('Tell me the number: '))
     if len(number) %2 == 0:
            l =(getPossible([x for x in number], 2))
            for i in l:
             numberjoined = ''.join(i)
             fangs.append(numberjoined)    
            for fang in fangs:
                print(fang)     
     else:
                print("No es vampiro")
        

                print(fangs)
        

def main():
    vampiro()
    
main()


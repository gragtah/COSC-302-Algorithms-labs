import random
import math

#collaborated part(3) with  AJ 

#Each list contains duples (L, U) where L is the amount of items
#available / desired and U is the price per unit.

        
# Remove # to test
#b = [(4,15),(3,5),(2,10)]   #(3,5) (2,10) (4,15)
#s = [(3,7),(5,6),(2,3)]     #(2,3) (5,6) (3,7)

def case1 (b, s):
    btemp = []
    stemp = []
    i = 0
    for x in b:
        btemp.append((x[0],x[1],i))
        i = i+1

    i = 0
    for x in s:
        stemp.append((x[0],x[1],i))
        i = i+1
    
    b1 =  mergeSort(btemp)
    s1 = mergeSort(stemp)
    t = len(b1)
    sl = len(s1)

 
    LB = {}
    LS = {}
    for i in range(len(b)):
        LB[i] = 0
    for j in range(len(s)):
        LS[j] = 0

    i = 0
    j = 0

    while (i<t and j<sl):

        if b1[t-1-i][1] >= s1[j][1]:
            priceB = b1[t-1-i][1]
            qntyB = b1[t-1-i][0]
            
            priceS = s1[j][1]
            qntyS = s1[j][0]
            
            indexB = b1[t-1-i][2]
            indexS = s1[j][2]

            q = 0
            while (qntyB>0 and qntyS>0):
                qntyB = qntyB-1
                qntyS = qntyS-1
                q = q+1

            x = LB[indexB] 
            y = LS[indexS] 
            LB[indexB] = x + q
            LS[indexS] = y + q


            b1[t-1-i] = (qntyB, priceB, indexB)
            s1[j] = (qntyS,priceS, indexS)
                        
            if b1[t-i-1][0] == 0:
                i = i+1
            if s1[j][0] ==0:
                j = j+1
                
        elif b1[t-1-i][1]< s1[j][1]:
                break
        else:
                 continue

    #print (b,s)
    fb = []
    fs = []
    for i in range(len(LB)):
        fb.append(LB[i])
    for j in range(len(LS)):
        fs.append(LS[j])

    print ('Transactions by each of - Buyers:',fb, ' Sellers:', fs)

        


def mergeSort(list1):
    if len(list1)<2:
       return list1
      
    if len(list1)>1 :
        list1left  = mergeSort(list1[:len(list1)//2])
        list1right = mergeSort(list1[len(list1)//2:])
        p1,p2,p = 0,0,0
        while p1<len(list1left) and p2<len(list1right):
            if list1left[p1][1]<list1right[p2][1]:
                list1[p] = list1left[p1]
                p+=1
                p1+=1
            else:
                list1[p]=list1right[p2]
                p+=1
                p2+=1
        if p1<len(list1left):
           list1[p:]=list1left[p1:]
        elif p2<len(list1right):
           list1[p:]=list1right[p2:]
                
    return list1



#b = [ [(2,15),(2,15)], [(1,5), (2,5)], [(1,10), (1,10)] ]
#s = [ [(2,7), (1,7)], [(3,6), (2,6)] , [(1,3),(1,3)] ]

def case2 (b, s):
    btemp = []
    stemp = []
    i = 0
    for x in b:
        for j in range(len(x)):
            btemp.append((x[j][0],x[j][1],i))
        i = i+1

    i = 0
    for x in s:
        for j in range(len(x)):
            stemp.append((x[j][0],x[j][1],i))
        i = i+1
    
    b1 =  mergeSort(btemp)
    s1 = mergeSort(stemp)
    t = len(b1)
    sl = len(s1)

 
    LB = {}
    LS = {}
    for i in range(len(b)):
        LB[i] = 0
    for j in range(len(s)):
        LS[j] = 0

    i = 0
    j = 0

    while (i<t and j<sl):

        if b1[t-1-i][1] >= s1[j][1]:
            priceB = b1[t-1-i][1]
            qntyB = b1[t-1-i][0]
            
            priceS = s1[j][1]
            qntyS = s1[j][0]
            
            indexB = b1[t-1-i][2]
            indexS = s1[j][2]

            q = 0
            while (qntyB>0 and qntyS>0):
                qntyB = qntyB-1
                qntyS = qntyS-1
                q = q+1

            x = LB[indexB] 
            y = LS[indexS] 
            LB[indexB] = x + q
            LS[indexS] = y + q


            b1[t-1-i] = (qntyB, priceB, indexB)
            s1[j] = (qntyS,priceS, indexS)
                        
            if b1[t-i-1][0] == 0:
                i = i+1
            if s1[j][0] ==0:
                j = j+1
                
        elif b1[t-1-i][1]< s1[j][1]:
                break
        else:
                 continue

    #print (b,s)
    fb = []
    fs = []
    for i in range(len(LB)):
        fb.append(LB[i])
    for j in range(len(LS)):
        fs.append(LS[j])

    print ('Transactions by each of - Buyers:',fb, ' Sellers:', fs)


   
def pack(bs,max):
    sumquan = 0
    for a in bs:
        (b,c) = a
        sumquan = sumquan + b
    pack = []
    arr = []
    arr.append((0,0))
    for a in range(1,sumquan+1):
        arr.append((-1,0))
    pack.append(arr)
    bs_i = 0
    for bs_i in range(0, len(bs)):
        (q,p) = bs[bs_i]
        prevrow = pack[-1]
        arr = []
        for i in range(0,sumquan+1):
            if (q > i):
                arr.append(prevrow[i])
            else:
                (v1, it1) = prevrow[i-q]
                (v2, it2) = prevrow[i]
                if (v1 >= 0 and v1 + q*p > v2 and max):
                    arr.append((v1 + q*p, bs_i+1))
                elif (v1 >= 0 and (v2 == -1 or v1 + q*p < v2)):
                    arr.append((v1 + q*p, bs_i+1))
                else:
                    arr.append(prevrow[i])
        pack.append(arr)
    return pack


#buyers = [(4,15),(3,5),(2,10)]   #(3,5) (2,10) (4,15)
#sellers = [(3,7),(5,6),(2,3)]     #(2,3) (5,6) (3,7)

def case3(buyers,sellers):
    bpack = pack(buyers,True)
    spack = pack(sellers,False)
    i = 0
    best = -1
    besti = -1
    for a in range(0,min(len(spack[-1]),len(bpack[-1]))):
        (v1,t1) = bpack[-1][a]
        (v2,t2) = spack[-1][a]
        if (v1-v2>best and v1>=0 and v2>=0):
            best = v1-v2
            besti = a
    if (besti < 0):
        print("No transaction possible")
    else:
        finalb = unpack(bpack,besti,buyers)
        finals = unpack(spack,besti,sellers)
        print("Transaction- Buyers(#):",finalb,'bought from Sellers(#):', finals,"with total social welfare %d" % best)
        print("Note: #/indices here are 1-based")



def unpack(pack,besti,bs):
    i = len(pack)-1
    j = besti
    arr = []
    while(i != 0):
        (v,t) = pack[i][j]
        (v1,t1) = pack[i-1][j]
        if (v == v1 and t == t1):
            i = i-1
        else:
            arr.append(t)
            i = i-1
            (q,p) = bs[t-1]
            j = j-q
    return(arr)

    

def main():
    x=0
    while(x!=4):
        x = eval(input("Social Welfare...Choose: \n1. case1 \n2. case2 \n3. case3 \n4.Exit \n "))
        if(x==1):
            b = eval(input("Enter buyers' list: "))
            s = eval(input("Enter sellers' list: "))
            case1(b,s)
            w = input('\nPress Enter to continue')
        if(x==2):
            b = eval(input("Enter buyers' list: "))
            s = eval(input("Enter sellers' list: "))
            case2(b,s)
            w = input('\nPress Enter to continue')
        if(x==3):
            b = eval(input("Enter buyers' list: "))
            s = eval(input("Enter sellers' list: "))
            case3(b,s)
            w = input('\nPress Enter to continue')
            
        
        if(x==4):
            break
        
    
main()


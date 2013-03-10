import sys
import math

"""
Hidden line removal - Gaurav Ragtah
explanation at end of file
"""

def mergesort(mlist, blist):

    if len(mlist) < 2:
        return mlist, blist  
    else:
        middle = (len(mlist))// 2  #must not be float
        mleft,bleft = mergesort(mlist[:middle], blist[:middle] )  
        mright,bright = mergesort(mlist[middle:], blist[middle:]) 

        resultm = []
        resultb = []
        i=0
        j = 0
        while True:
            if i>= len(mleft) and j >= len(mright):             
                return hide (resultm, resultb)
                #return resultm, resultb
            
            elif i>=len(mleft):
                while j<len(mright):
                    resultm.append(mright[j])
                    resultb.append(bright[j])
                    j += 1              
                return hide (resultm, resultb)
                #return resultm, resultb
            
            elif j>= len(mright):
                while i<len(mleft):
                    resultm.append(mleft[i])
                    resultb.append(bleft[i])
                    i += 1
                #return resultm, resultb
                return hide (resultm, resultb)
            
            if mleft[i]== mright[j]:  #if same slope and different intercepts, eliminate
                if bleft[i] >= bright[j]:
                    resultm.append(mleft[i])
                    resultb.append(bleft[i])
                else:
                    resultm.append(mright[j])
                    resultb.append(bright[j])                    
                i += 1
                j += 1
            elif mleft[i]< mright[j]:
                resultm.append(mleft[i])
                resultb.append(bleft[i])
                i += 1
            else:
                resultm.append(mright[j])
                resultb.append(bright[j])
                j += 1
            


def hide(resultm, resultb): 

    if(len(resultm) <= 2):
        return resultm, resultb

    hidm = []
    hidb = []

    hidm.append(resultm[0])
    hidm.append(resultm[1])
    hidm.append(resultm[2])
    hidb.append(resultb[0])
    hidb.append(resultb[1])
    hidb.append(resultb[2])
    
    x1 = (hidb[len(hidb)-3]-hidb[len(hidb)-1])/(hidm[len(hidm)-1] - hidm[len(hidm)-3])
    x2 = (hidb[len(hidb)-3]-hidb[len(hidb)-2])/(hidm[len(hidm)-2] - hidm[len(hidm)-3])

    k = 2
    #times = 0
    while(len(hidm) > 2):
        #print(times)
        #times += 1
        if x1<=x2:  # newer line is hiding previous line, (also may be hiding lines previous to that line)
            tempm = hidm.pop() 
            tempb = hidb.pop() 
            hidm.pop() 
            hidb.pop() 
            hidm.append(tempm)
            hidb.append(tempb)
           
        else:   #newer line is not hiding previous lines
            k += 1
            if (k >= len(resultm)):
                break
            hidm.append(resultm[k])
            hidb.append(resultb[k])
            
            
        if(len(hidm) == 2): #check with next line if any
            k += 1
            if (k >= len(resultm)):
                break
            hidm.append(resultm[k])
            hidb.append(resultb[k])
           
        x1 = (hidb[len(hidb)-3]-hidb[len(hidb)-1])/(hidm[len(hidm)-1] - hidm[len(hidm)-3])
        x2 = (hidb[len(hidb)-3]-hidb[len(hidb)-2])/(hidm[len(hidm)-2] - hidm[len(hidm)-3])
        #print("Currently, hidm: ", hidm, " hidb: ", hidb)

    #print("Finally, hidm: ", hidm, " hidb: ", hidb)

    return hidm, hidb



def main():
    mlist=[]
    blist=[]
    lines=[]
    #name2=[]
    r = eval(input("How many lines? "))

    """
    while True:
        x = input("Enter slope, y-intercept value (or 'done' if finished): ")
        if 'done' in x or 'Done' in x:
            break
        m,b = eval(x)
        mlist.append(m)
        blist.append(b)      
    """

    for s in range (r):
        print("Enter slope, y-intercept value for line",s+1,": ")
        x = input()
        m,b = eval(x)
        mlist.append(m)
        blist.append(b) 
        
    for i in range(len(mlist)):
        lines.append(i+1)
        
    print("")
    
    mlistf,blistf = mergesort(mlist, blist)

    i = 1
    x2 = (blistf[1]-blistf[0])/(mlistf[0]- mlistf[1])
    print("(,",x2,"): (",mlistf[0],",",blistf[0],")") 
          
    while (i<len(mlistf)-1):
        x1 = (blistf[i]-blistf[i-1])/(mlistf[i-1]- mlistf[i])
        x2 = (blistf[i+1]-blistf[i])/(mlistf[i]- mlistf[i+1])
        print("(",x1,",",x2,"): (",mlistf[i],",",blistf[i],")")
        i += 1

    x2 = (blistf[len(blistf)-1]-blistf[len(blistf)-2])/(mlistf[len(mlistf)-2]- mlistf[len(mlistf)-1])
    print("(",x2,", ): (",mlistf[len(mlistf)-1],",",blistf[len(blistf)-1],")") 

        

if __name__ == '__main__':
    main()

    """
    O(nlogn) because mergesortis O(nlogn) and the hide method
    just compares newer line at every step in the mergesort with last line - if it doesn't
    hide it, it just adds the newer line and proceeds. In rare cases, the new line hides
    the previous line, and may also hide lines before that (In that case,
    if such a case happens again, the number of previous lines left will be less). So the
    running time is O(nlogn) - it proceeds with the base mergesort case where if we have  2 lines,
    both are visible; then as a newer line enters the scene, it just checks with the last
    visible line (constant time) and proceeds as mentioned above."
    
    """
            

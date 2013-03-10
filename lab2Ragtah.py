import sys
import math
import random
import struct

def gcd(a,b):
    a,b=(b,a)if a<b else (a,b)
    while b:
        (a,b) = (b,a % b)
    return a


"""
def coprime(a,p):
    if(gcd(a,p)==1):
        return True
    else:
        return False

"""

 

def generate_primes(bits):
    
    f1 = 0
    f2 = 0
    p=0
    q=0

    if(bits==2):
        p=2
        q=3
        f1=1
        f2=1
    
        

    while(f1==0):
        p = random.randrange(2**(bits-1) +1, 2**(bits),2)
        if(is_prime(p) == True):
            f1 = 1
          
    
    
    while(f2==0):
        q = random.randrange(2**(bits-1) +1, 2**(bits),2)
        if (p==q): continue
        if(is_prime(q)==True):
            f2 = 1

    return p,q
    



def is_prime(n,itr=1):
    i=0
    f = 0
    while(f==0 and i<=itr):
        x = random.randrange(2,n)
        i += 1
        if(pow(x,n-1,n) != 1):
            f=1

    if (f==0): return True
    else: return False



def rsa_public_key(p,q):
    N = p*q
    # 1<e<(p-1)(q-1)
    f = 0
    while(f==0):
        e = random.randrange(2, (p-1)*(q-1)+1)
        if(gcd(e,(p-1)*(q-1))==1):
            f=1

    return N,e


def rsa_private_key(p,q,e):
    m = (p-1)*(q-1)
    x=euclid(e,m)%m
    #while(x<0):
    #    x += m
    return x


def euclid(a,b):

	u, u1 = 1, 0
	v, v1 = 0, 1
	while b:
		q = a // b
		u, u1 = u1, u - q * u1
		v, v1 = v1, v - q * v1
		a, b = b, a - q * b
	return u



def numofbits(n):
    nn = n
    i = 1
    while(nn!= 1):
        nn=nn//2
        i += 1
    return i
    
def rsa_encrypt(infile, outfile, N, e):
    
    #i=1
    nt = N
    """
    while(nn!= 1):
        nn=nn//2
        i=i+1
    """
    b = math.ceil(numofbits(nt)/8)
    k = b-1 #number of bytes
    
    fin = open(infile, "rb")
    fout = open(outfile, "wb")

    
    a = []
    
    while True:
        cc = fin.read(k)

        #print (len(c))
        if len(cc)==0:
            break
        
        l = list(cc)
        #print(l)
        #print ("k is:", k, " len(c) is: ",len(c) )
        #print ("l is: ")
        #print (l)
        #print (c)
        z = 0
        i=0
        
        while(i<len(l)):       
            z += l[i]*(256**(len(l)-i-1))
            #print("z is: ")
            #print (z)
            i += 1


        c = pow(z,e,nt)
        #print("encrypted c is: ", c)
        print("encrypted c len is: ", math.ceil(numofbits(c)/8), " k is: ", k)
        print (c)
        i=0
        """
        while (math.ceil(numofbits(c)/8)<k+1): # while (math.ceil(numofbits(c)/8)<k+1) or while (i<= k - len(cc))
            c *= 10
            i += 1
            print("Now c len is: ", math.ceil(numofbits(c)/8))

        """
        
        pad = k+1 - (math.ceil(numofbits(c)/8))
        temp = []

        print ("c is: ", c)
        while(True):
            if(c//256 ==0):
                temp.append(c)
                break
            temp.append(c%256)
            c = c//256
        l = []  #reverse list back to normal
        i = len(temp)
        while(i>0):
            l.append(temp[i-1])
            i -= 1
        
        while(pad>0):
            l.append(0)
            pad -= 1
        i = 0

        fout.write(bytes(l))
        
        
        print ("l is: ", l)
        #fout.write(struct.pack('L', c))
    fin.close()
    fout.close()
        

def rsa_decrypt(infile, outfile, N, d):

    nt = N
    
    b = math.ceil(numofbits(nt)/8)
    k = b #+ 1 #number of bytes (k = b+1)

    
    fin = open(infile, "rb")
    fout = open(outfile, "wb")
    
    a = []
    
    while True:
        c = list(fin.read(k))
    
        if len(c)==0:
            break
        print("c1 is:", c, "c1 length is: ",len(c), " k is: ", k)
        #c = (struct.unpack('L', c1))[0]

        i=0
        while (c[len(c)-1] == 0): # while (math.ceil(numofbits(c)/8)<k+1) or while (i<= k - len(c1))
            c.pop()  #len(c)-1 index

        i=0
        z=0
        
        while(i<len(c)):       
            z += c[i]*(256**(len(c)-i-1))
            #print("z is: ")
            #print (z)
            i += 1
            
            
        """
        while (math.ceil(numofbits(c)/8)>k-1 and c%10 ==0):
            c = c//10
        """
        
        m = pow(z,d,N) #z should be c

        """
        print ("m before:" , m)
        while(m%10 == 0):
            m = m//10
        """

        print ("c is: ", c, " m is: ", m)
        
        temp = []
        while(True):
            if(m//256 ==0):
                temp.append(m)
                break
            temp.append(m%256)
            m = m//256
        l = []  #reverse list back to normal
        i = len(temp)
        while(i>0):
            l.append(temp[i-1])
            i -= 1
            
        """
        l = bytearray() #add temp elements in reverse to this
        ll = []
        i = len(temp)
        while(i>0):
            l.append(temp[i-1])
            ll.append(temp[i-1])
            #fout.write(str(struct.pack('I',temp[i-1])))
            #fout.write(b"01010102")
            i -= 1
        print (l, list(l), ll)

        """
        fout.write(bytes(l))
        #fout.write(struct.pack('L', c))  just plain write. no struct. because writing bits wil give text


    fin.close()
    fout.close()

    




    
    
def main():
    bits = eval(input("Enter desired number of bits (>8): "))
    p,q = generate_primes(bits)
    N,e = rsa_public_key(p,q)
    d = rsa_private_key(p,q,e)
    print("Encryption phase: ")
    infile = input("Input filename? ")
    outfile = input("Output filename? ")
    rsa_encrypt(infile, outfile, N, e) # remove p and q
    print("Encrypted! ")
    
    print("Decryption phase: ")
    infile = input("Input filename? ")
    outfile = input("Output filename? ")
    rsa_decrypt(infile, outfile, N, d)

    #print("Decrypted! ")
    

if __name__ == '__main__':
    main()



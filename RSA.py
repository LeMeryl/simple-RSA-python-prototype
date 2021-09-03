class Rsa:

    def  criptografar (self):

      word=input("input a word: ")   
      ascii=[]
      
      for char in word:
          ascii.append(ord(char))

      calcularCripto(ascii)
      print (ascii)

    def  descriptografar(self):
        a=int(input("N: "))
        b=int(input("D: "))
        word1=[]
        word2=[]
        print("insert '0'to finish")
        for i in range (100):
            letter=int(input("insert the code:  "))
            if letter!=0:
                word1.append(letter)
            else:
                break   
        size=len(word1)
        for i in range (size):
              calc=(word1[i]**b)%a # 𝑀=𝐶**𝑑 mod(𝑛)
              word2.append(calc)
        
        final=''.join(chr(i) for i in word2)
        print ("the message  is: ",final)


def calcularCripto (x):
        p=17   
        q=23   
        phi=(p-1)*(q-1)    
        n=p*q  
        e=3    
        r=[]
        crp=len(x)
        for i in range (crp):
            calculo=(x[i]**3)%n #𝑀=𝐶**𝑑 mod(𝑛)
            r.append(calculo)   
       
        d=modInverse(phi,e)

        print ("E: ",e)
        print ("N: ",n)
        print ("D: ",d)
        return calculo

def modInverse(a, m) : 
          a = a % m; 
          for x in range(1, m) : 
             if ((a * x) % m == 1) : 
                  return x 
             return 1


exe=Rsa()
k=0
while (k==0):
 options=input("what do you want to do? insert 'encrypt' or 'decrypt' (insert 'end' to exit): ")
 if options=="encrypt":
     exe.criptografar()
 elif options=="decrypt":
     exe.descriptografar()
 elif options=="end":
    print ("program closed with sucess :D")
    break   
 else:
     print("Invalid option try again!")


input ()

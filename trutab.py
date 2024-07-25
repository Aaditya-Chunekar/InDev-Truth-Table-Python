print("V in capitals indicates or\n^ indicates and\n~ indicates not\n> indicates implication\n<> indicates double implication")
inp=input("Enter the expression, separate var and operands by spaces to be solved without using capital V as variable\n")
expr=inp.split()  #Splits the string for ex. inp = a V b then expr = [a , v, b]
ind=[]  #Declartion of List
symbols = ['^','V','>','~','and','or','not','}','{','}','{','[',']','(',')'] #Defination of logic operators
i=0 #Initialzing iterator to 0
while i<len(expr):  #iterating the expr list
    if expr[i] == ">":     #Replacing the impication operator as or
        expr[i] = "or"
        expr.insert(i-1,"~")  #This is basically for p -> q = ~p v q
        i-=3
    elif expr[i] == 'V':
        expr[i] = 'or'
    elif expr[i] == '~':
        expr[i] =  'not'
    elif expr [i] == '^':
        expr[i] = 'and'
    i+=1
print("post-expr :",expr)
i=0
v=0  #NO of variables in the column
while i < len(expr):   #To check how many variables are there
    if expr[i] not in symbols:
            v+=1
            ind.append(i)   #store the location of the varaibles
    else:
        ind.append(-1)     #Signifies that there is a operator
    print(ind,": ind","expr",expr[i])
    i+=1  
perm=2**v #Defines the number of rows
trutab = []   
for i in range(0,v): #Printing the Truth values
    j=0
    ct=0
    fill=False
    perm/=2
    while j<2**v:   # The method of writing half of the row as fasle and half as truth 
        trutab.append(fill)                  #Btw very clevery executed
        ct+=1         
        if ct==perm:             
            fill = not fill             
            ct=0         
        j+=1 
#replacing - imp
for i in range(2**v):
    k=i-2**v
    found=True
    for j in range(len(ind)):  
        if ind[j]<0 and found:  # for identifying where the operators are
            found=False
            #print("-1")    
            k+=2**v 
        else:
            if k<0:
                k+=2**v
            print(k,"k")
            found=True
            expr[ind[j]]=str(trutab[k])
            print(trutab[k],k)
    print("expr :",expr)    
    trutab.append(eval(" ".join(expr)))   
#print("trutab\n",trutab)
print("result")
for j in range(2**v):
    i=j
    print(  )
    while i<len(trutab):
        if trutab[i]==True:
            print("T",end="\t")
        else:
            print("F",end="\t")
        i+=2**v

m=input("Enter first player's name:\n")
n=input("Enter second player's name:\n")

p=input("{}, which symbol you want? 'o' or 'x'\n".format(m))
while (p=='o'or 'x'):
        if (p=='o'):
           q='x'
           break
        elif(p=='x'):
           q='o'
           break
        else:
           print("Symbol not supported")
           p=input("{}, try again... 'o' or 'x'\n".format(m))




print("Okay, so {}, you go for {}\n".format(n,q))
 
l1=['1','2','3']
l1=" ".join(l1)
l2=['4','5','6']
l2=" ".join(l2)
l3=['7','8','9']
l3=" ".join(l3)
print(f"""Before playing let's understand the rules,\nyou are having a board with their respective position values as shown below: \n{l1}\n{l2}\n{l3}\n when your turn, you have to enter the position on which you want your symbol.\n Best of luck!""")
print(" Let's start the game!!")
lst1=[' ',' ',' ']
lst2=[' ',' ',' ']
lst3=[' ',' ',' ']

def a():
    i=1
    w=None

    while(i<=9):    
        
        def ck(M):
            POS=input("{}'s Turn:\n".format(M))
            try:
                
                for i in range(1,10):
                    if int(POS)==i:
                          f=True 
                if f==True:
                      return POS
            except:
              print("You forgot! Positions from 1 to 9 only.")
              value=ck(M)
              return value
         
        pos=ck(m)
        """def position_check(P,func):
            input_positions=list()
            for i in input_positions:
                if P==i:
                    print("Position already entered!")
                    P=func()
                    position_check(P,func)
                else:
                    input_positions.append(P)
        position_check(pos,ck(m))"""
        """input_positions=[]
        for i in input_positions:
            if pos!=i:
                input_positions.append(pos)
            else:
                #input_positions.append(pos)
                print("Position already entered!")
                pos=ck(m)"""
                
        ttt(pos,p)
        if (ttt(pos,p)==True):
            print(" {} | {} | {}".format(lst1[0],lst1[1],lst1[2]))
            print("-----------")
            print(" {} | {} | {}".format(lst2[0],lst2[1],lst2[2]))
            print("-----------")
            print(" {} | {} | {}".format(lst3[0],lst3[1],lst3[2]))
           
            print("{} Wins!!!".format(m))
            w=False
            break
        
        print(" {} | {} | {}".format(lst1[0],lst1[1],lst1[2]))
        print("-----------")
        print(" {} | {} | {}".format(lst2[0],lst2[1],lst2[2]))
        print("-----------")
        print(" {} | {} | {}".format(lst3[0],lst3[1],lst3[2]))
        
        i+=1
        print (i)
        
        if i==10:
            if w==None:
                print(" {} | {} | {}".format(lst1[0],lst1[1],lst1[2]))
                print("-----------")
                print(" {} | {} | {}".format(lst2[0],lst2[1],lst2[2]))
                print("-----------")
                print(" {} | {} | {}".format(lst3[0],lst3[1],lst3[2]))
               
                print("Its a tie..!")
                break
            

        #pos=input("{}'s Turn:\n".format(n))
        
        pos=ck(n)

        ttt(pos,q)
        if (ttt(pos,q)==True):
            print(" {} | {} | {}".format(lst1[0],lst1[1],lst1[2]))
            print("-----------")
            print(" {} | {} | {}".format(lst2[0],lst2[1],lst2[2]))
            print("-----------")
            print(" {} | {} | {}".format(lst3[0],lst3[1],lst3[2]))
            
            print("{} Wins!!!".format(n))
            w=False
            break
        print(" {} | {} | {}".format(lst1[0],lst1[1],lst1[2]))
        print("-----------")
        print(" {} | {} | {}".format(lst2[0],lst2[1],lst2[2]))
        print("-----------")
        print(" {} | {} | {}".format(lst3[0],lst3[1],lst3[2]))
        
        i+=1 
        print(i)  
        
        

def ttt(position,i):
    if position =='1':
        lst1[0]=i
        if (lst1[0]==lst1[1]==lst1[2]):
            return True
        if (lst1[0]==lst2[0]==lst3[0]):
            return True
        if (lst1[0]==lst2[1]==lst3[2]):
            return True
        
            
    if position =='2':
        lst1[1]=i
        if (lst1[1]==lst1[0]==lst1[2]):
            return True
        if (lst1[1]==lst2[1]==lst3[1]):
            return True
    if position =='3':
        lst1[2]=i
        if (lst1[2]==lst1[1]==lst1[0]):
            return True
        if (lst1[2]==lst2[2]==lst3[2]):
            return True
        if (lst1[2]==lst2[1]==lst3[0]):
            return True
    if position =='4':
        lst2[0]=i
        if (lst2[0]==lst1[0]==lst3[0]):
            return True
        if (lst2[0]==lst2[1]==lst2[2]):
            return True
    if position =='5':
        lst2[1]=i
        if (lst2[1]==lst2[0]==lst2[2]):
            return True
        if (lst2[1]==lst1[1]==lst3[1]):
            return True
    if position =='6':
        lst2[2]=i
        if (lst2[2]==lst2[0]==lst2[1]):
            return True
        if (lst2[2]==lst1[2]==lst3[2]):
            return True
    if position =='7':
        lst3[0]=i
        if (lst3[0]==lst3[1]==lst3[2]):
            return True
        if (lst3[0]==lst2[1]==lst1[2]):
            return True
        if (lst3[0]==lst2[0]==lst1[0]):
            return True
    if position =='8':
        lst3[1]=i
        if (lst3[1]==lst3[0]==lst3[2]):
            return True
        if (lst3[1]==lst2[1]==lst1[1]):
            return True
    if position =='9':
        lst3[2]=i
        if (lst3[2]==lst3[1]==lst3[0]):
            return True
        if (lst3[2]==lst2[2]==lst1[2]):
            return True
        
a()
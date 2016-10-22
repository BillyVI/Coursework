'''
#e1 randomly shuffles an array of intergers
a = [int(x) for x in input().split()]
print(a)
l = len(a)
for i in range(l):
    m = i*4
    if m > l-1:
        m = m // 3
        if m < l-1 and m>0:
              n = a[i]
              a[i]=a[m]
              a[m] = n
            
    else :
        n = a[i]
        a[i]=a[m]
        a[m] = n
    print(i)
print(a)   
 '''
'''
# Count the number of trailing 0s in a factorial number       
num = int(input("input a factorial number:"))
if num==0:
    print("one zero!")
elif num<0:
    print("not a valid number")
else :
    total = 0
    t = 0
    f = 0
    ten = 0
    for i in range(1,num+1):
        if i%10==0:
            ten = ten +1
            print("10 + 1")
        elif i%2==0:
            t = t+1
            print("2 + 1")
        elif i%5==0:
            f = f+1
            print("5 + 1")
    print(ten,"+",t,"+",f)
    total = ten + min(t,f)
    print(total)
'''
'''
#alien numbers
num = [1,]
x = int(input("input number of monster: "))
y = int(input("input day of birth: "))
valid = int(input("input day to count: "))
sum_num = num[0]
if y<0 or x<0 or valid <0:
    print("wrong information!")
elif  y+1 > valid:
    print("one alien!")
elif  valid >= y+1 :
    for i in range(1,y+1):
        num.append(x)
    for k in range(y+1,valid+1):
        sum_num = sum_num+num[k-y]
        num.append(sum_num*x)
    print("sum_num= ",num[valid]/3)
 
    '''
def r_wMatrix():
    i = int(input("how many row?"))
    j = int(input("how many column?"))
    arr = [[] for j1 in range(j)]
    print(arr,type(arr))

    for j1 in range(j):
           arr [j1] = list(input("input matrix :").split( ))
           print(arr,type(arr))

    count_zero = 0  
    print(count_zero,type(count_zero))
    count_notz = 0
    print(count_notz,type(count_notz))
    row = []
    column = []
    value = []
    print(row,type(row))


    for i1 in range(i):
        for j2 in range(j):
            if arr[i1][j2]==0:
                count_zero = count_zero+1
            else :
                row.append(i1)
                column.append(j2)
                value.append(arr[i1][j2])
                count_notz = count_notz + 1
                
    
    if count_zero > count_notz:
        print("is a sparse matrix")
        
    return row,column,value
    
def cal_matrix():
    print("create your first matrix:")
    store1 = r_wMatrix()
    row1 = store1[0]
    column1 = store1[1]
    value1 = store1[2]
    print(store1)
    print("create your second matrix:")
    store2 = r_wMatrix()
    row2 = store2[0]
    column2 = store2[1]
    value2 = store2[2]
    c = input("how to calculate? '+-*/' :")
    if c=="+" :
        print(add(row1,row2,column1,column2,value1,value2))
    if c=="*":
        print(mul(row1,row2,column1,column2,value1,value2))
    if c=="-":
        print(sub(row1,row2,column1,column2,value1,value2))
    if c=="/":
        print(dev(row1,row2,column1,column2,value1,value2))
    
        
                    
def add(row1,row2,column1,column2,value1,value2):
    if len(row1)<len(row2):
        for n in range(len(row1)):
            if row1[n] == row2[n] and column1[n] ==column2[n]:
                value2[n]=int(value2[n])+int(value1[n])
        return row2,column2,value2
    else:
        for n in range(len(row2)):
            if row1[n] == row2[n] and column1[n] ==column2[n]:
                value1[n]=int(value2[n])+int(value1[n])
        return row1,column1,value1

def mul(row1,row2,column1,column2,value1,value2):
    if len(row1)<len(row2):
        for n in range(len(row2)):
            if row1[n] == row2[n] and column1[n] ==column2[n]:
                value1[n]=int(value2[n])*int(value1[n])
            else :
                value1[n] = 0
        return row1,column1,value1
    else:
        for n in range(len(row1)):
            if row1[n] == row2[n] and column1[n] ==column2[n]:
                value2[n]=int(value2[n])*int(value1[n])
            else:
                value2[n] = 0
        return row2,column2,value2

    
def dev(row1,row2,column1,column2,value1,value2):
    if len(row1)<len(row2):
        for n in range(len(row2)):
            if row1[n] == row2[n] and column1[n] ==column2[n]:
                value1[n]=int(value2[n])/int(value1[n])
            else :
                value1[n] = 0
        return row1,column1,value1
    else:
        for n in range(len(row1)):
            if row1[n] == row2[n] and column1[n] ==column2[n]:
                value2[n]=int(value2[n])/int(value1[n])
            else:
                value2[n] = 0
        return row2,column2,value2
    
def sub(row1,row2,column1,column2,value1,value2):
    if len(row1)<len(row2):
        for n in range(len(row2)):
            if row1[n] == row2[n] :
                if column1[n]==column2[n]:
                    value1[n]=int(value2[n])-int(value1[n])
                else :
                    value1[n]= -int(value1[n])
        return row1,column1,value1
    else:
        for n in range(len(row1)):
            if row1[n] == row2[n] :
                if column1[n]==column2[n]:
                    value2[n]=int(value1[n])-int(value2[n])
                else :
                    value2[n]= -int(value2[n])
        return row2,column2,value2

cal_matrix()                              
        
    


    
    


        
        

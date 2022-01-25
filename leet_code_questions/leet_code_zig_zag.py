#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
'''
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Input: s = "PAYPALISHIRING", numRows = 3
P   A   H   N
A P L S I I G
Y   I   R
Output: "PAHNAPLSIIGYIR"

The algo
Make the first slice of number of rows-
then increase the second letter in up be one space and followed in the other
When the letter is reached on the top of the row print the next letters in one line

sudo code-
take the input and store in a lst eliminate the """
define the number of lists or tuples based on the number of rows

'''
#experiments for adding space
'''test_lst = [1,2,3,4,5,6,7]
test_lst_2 = [8,9,10,11,12,13]
for i in test_lst:
    print(i*" "+str(i))'''
#experimnt for printing in one line
'''for i in range(1,5):
    print(i,end=" ")'''
#print two list at once
'''test_tup = ((1,2,4,5),(3,4,6,7),(5,6,8,9),(7,8,9,10),(9,10,11,12))
for i,j,k,l in test_tup:
    print(i)
    print(j,k)
    print(l)'''
#make dynamic number of lists
#have a parent container where can store a valuel
'''new_lst=[]
for i in range(1,5):
    ai = []
    ai.append(i)
    new_lst.append(ai)
print()
print(new_lst)'''
#start the code
test_inp = "PAYPALISHIRING"
n1 = 4
test_inp_2 = "PAYPALISHIRING"
n2 = 3
test_inp_3 = "A"
n3 = 1


def store_fun(str):
    new_lst =[]
    for i in str:
        if i == '""':
            pass
        else:
            new_lst.append(i)
    return new_lst


def zig_zag_fun(str,rows):
    lst = []
    for i in range(rows):
        ai=[]
        lst.append(ai)
    lst_2 = store_fun(str)
    count =0
    i =0
    while True:
        if 0<=i< 4:
            lst[0].append(lst_2[i])
        elif 4<=i<=8:
            lst[1].append(lst_2[i])
            i+=1
        elif 8<=i<=12:
            lst[2].append(lst_2[i])
            #i+=1
        elif 12<=i<=len(lst_2):
            lst[3].append(lst_2[i])
            break
        i+=1
    return lst


print(zig_zag_fun(test_inp,n1))

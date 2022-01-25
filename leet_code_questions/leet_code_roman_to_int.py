'''
prompot -
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
Example 1:

Input: s = "III"
Output: 3

Example 2:

Input: s = "IV"
Output: 4

Example 3:

Input: s = "IX"
Output: 9

Example 4:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 5:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''
'''
Algo -
Make a symbol dataset that stores the value in the form of the tuples or dictionary
make a function for the calculation part with iteration all over the terms and then print the value in the last
Rules -
if equal values written then added
left is small and right side is high then subtract
left side is greater then add to the values
make a additon algo fot the sum
for addition and subtratcion look for the next element
and do as per rules
III
all euqual just add



'''
#code
#make the table for roman value and integers




Input = "III" #not resolved
Input_2 = "IV" # 4
Input_3 = "LVIII"  #58
Input_4 = "MCMXCIV" #1994
Input_5 = "VI" #6
Input_6 = "X" # 10
Input_7 = "IX" #9
Input_8 = "XII" #12
Input_9 = "XIII" #13
Input_10 = "I" #1

the_inp = input("Enter the sequence: ")
symbol_table = {"I":1,"V":5,"X":10,"L":50,"D":500, "M":1000, "C": 100}

def main_fun(string):
    last_str ="" #make a new str for print pupose
    lst = []
    sum_lst = []
    for i in string:
        lst.append(symbol_table[i])
    i =0
    #rules logic
    #make addition logic as well
    curr_sum =0
    while True :
        if len(string) == 1:
            curr_sum = lst[i]
            #sum_lst.append(curr_sum)
            break
        else:
            if i == len(string)-1: #exit condition for the loop
                break

            # the less than case
            elif  lst[i+1] and lst[i] < lst[i+1]:
                curr_sum = lst[i+1] - lst[i]
                #sum_lst.append(curr_sum)
                i+=1

            # the greater than case
            elif  lst[i+1]  and (lst[i] > lst[i+1]):
                curr_sum = lst[i]+lst[i+1]
                #sum_lst.append(curr_sum)
                i+=2
            else:
                #make the adding logic
                print(curr_sum)
                #curr_sum = lst[i]
                curr_sum +=curr_sum
                #print(curr_sum)
                i+=1


    sum_lst.append(curr_sum)

    for i in sum_lst:
        last_str += str(i)

    return last_str

print(main_fun(the_inp))

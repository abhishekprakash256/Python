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

#addition
'''
MCMXCIV

VI +2
IX +2

III -1

VIII - 2, 1, 1
6 + 1 +1
'''
def main_fun(string):
    last_str ="" #make a new str for print pupose
    lst = []
    sum_lst = []
    for i in string:
        lst.append(symbol_table[i])
    i =0
    curr_sum = 0
    flag = 0
    for i in range(len(lst)-1):
        if lst[i] >= lst[i+1]:
            flag= 1
            curr_sum +=lst[i]

        elif lst[i] < lst[i+1]:
            flag = 0
            curr_sum = lst[i+1]- lst[i]


    if flag == 1 :
        curr_sum= curr_sum + lst[len(lst)-1]
    return curr_sum










print(main_fun(the_inp))

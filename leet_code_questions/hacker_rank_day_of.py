'''def dayOfProgrammer(year):
	if (1700 <= year <= 1917):  #julian calendar
		#check for leap year
        if (year%4 == 0):                                  #it's a leap year and number of days is 366
                                        #calculate the 256th day as every day is september 
            prinf("13.09." + year)
            
        else:                     #not a leap year and number of days is 365
                                #calcualte
            print("12.09."+ year)
    elif (year == 1918):           #not known
    	print("hey")
        
    elif (1919<=year <= 2700):         #Georgian calendar    
                                 #check for the leap year
        if (year%400 == 0 and year %4==0 and year % 100 !=0)           #it's a leap year no of days 366
        	             #calulate
            print("13.09." + year)
        else:                 #not a leap year no of days is 365
                           #calculate
            print("12.09."+ year)
    else:
        return "out of time"



prinf(dayOfProgrammer(1712)'''

case_1 = 1984     
case_2 = 2017     
case_3 = 2016      
case_4 = 1800       
case_5 = 1918



def dayOfProgrammer(year):
    if(1700<= year <= 1917):
        if(year%4 == 0):

            x= ("12.09." + str(year))

        else:
            x = ("13.09." + str(year))

    elif(year == 1918):
        x= ("26.09." + str(year))

    elif(1919 <= year <= 2700):
        if ((year % 400 == 0) or (year %4 == 0 and year %100!=0)):
            #print("first")
            x=("12.09." + str(year)) 
        else:
            #print("second")
            x= ("13.09."+ str(year))
    else:
        x= "out of time"                           



    return x;





#------------------------------------passed all cases and submitted--------------------------------------------------#






print(dayOfProgrammer(case_5))
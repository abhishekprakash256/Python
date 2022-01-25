'''
Caesar cypher implementation of the encryption techniques 

technique 

we get the text and shift the bits as per key is given in a rounded rotation manner

'''

test_0 = "abched"

test_1 = "hduldnz"

test_2 = "abcdefghijklmnopqrstuvwxyz"


#the letter dictionary
key_pair_0 = {0:"a" , 1:"b", 2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w", 23:"x",24:"y",25:"z"}


key_pair_1 = {"a":0 ,"b":1, "c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,"n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}



def caesar_cypher(text:str, shift:int)-> str:

	'''
	The function takes the string and encrypts according to caesar cypher text

	Arguments:
		text (str) - the text to be encrypted
		
		shift (int) - the shift in the letters

	Returns:

		encrypted_text (str) - The encrypted text as per caeasar cypher method 

	'''

	#one outer loop for the iteration

	encrypted_text = ""  #making the encrypted text

	for i in range(len(text)):

		#make the computation 

		key_shift = (shift) % 26

		if key_pair_1[text[i]] + key_shift < 26:

			encrypted_text += key_pair_0[key_pair_1[text[i]] + key_shift]

		else:

			val = (key_pair_1[text[i]] + key_shift -26 )

			encrypted_text += key_pair_0[val]


	return encrypted_text

print(caesar_cypher(test_2,23))

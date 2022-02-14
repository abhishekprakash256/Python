""" the python file to show the subprocess 
moudule working
"""
import subprocess

subprocess.run('ls')  # to run the commands
p1 = subprocess.run(['ls','-la'],capture_output = True )
#print(p1.returncode)
print(p1.stdout)
print(p1.stdout.decode())   #to show the decoded output as in the terminal
with open('test.txt','w') as f:
    p2 = subprocess.run('ls',stdout = f, text=True)

#p2 = subprocess.run(['ls','-la','dne'], capture_output= True, text= True)

p3 = subprocess.run(['ls','-la','dne'], stderr= True, text= True, check= True)

print(p3.stderr)

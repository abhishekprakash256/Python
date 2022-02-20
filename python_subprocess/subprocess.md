## Subprocess module 

### Note 

- the module is used to run the command on the shell
- we can customize the arguments that are passed as well
- we can print those results in the console 
- or can grab it by using the returncode 
  - if command ran well it give error code as zero

- capture_argument can be used to catch the argument 
  - The capture are to be converted to strings to make a good output by using the decode
- we can also use the text = True in the arguments ,to get 

```python
import subprocess
subprocess.run('ls')  # to run the commands
p1 = subprocess.run(['ls','-la'],capture_output = True )
#print(p1.returncode)
print(p1.stdout)
print(p1.stdout.decode())   #to show the decoded output as in the terminal

```

- The redirection can be done by using the pipelining of the command by passing in the arguments

- Can also be redirected to a file 

  ```python
  with open('output.txt','w') as f:
      p1 = subprocess.run(['ls'], stdout= f, text= True)
  ```

- for capturing the error of the commands 

  - we can capture that by using the return code if 1 then unsuccesful
  - can be also captured by stderr

  ```python
  p1 = subprocess.run(['ls','-la','dne'], capture_output= True, text= True)
  print(p1.stderr)
  ```

- To throw an exception pass check = True

```python
p1 = subprocess.run(['ls','-la','dne'], stderr= True, text= True , check = True)
```

- to ignore them use the redirection to NULL
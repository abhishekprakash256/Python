## Python Unit-test 

### Command 

- to run 

  ```sh
  python -m unittest test_file_name.py  (to run the test file)
  ```

### Notes 

- Test file name should start with test_name.py

- The imports are unittest 

- The unittest uses the oops concept that can 

- class name should be descriptive 

- The method name should start with test 

- There are methods to check the equality and all check documentation for that, example assertEqual(a,b)

- use name main concept to make the test by just running the python file

- Check for the assertion error

- The raise error function 

  - syntax 

    ```python
    self,asserRaises(ValueError,module.function, arg1, arg2)  #the syntax is used as follows - the arg1 and arg2 are the arguments of the function, we don't pass them directly to the funtion
    ```

  - Other syntax using context manager

    ```python
    with self.assertRaises(ValueError):  #the other syntax using the context manager method that takes input in function
    	module.function(arg1,arg2)
    ```

- tearDown and setUp method  (with syntax)

  - It can be used for the setting the database the setup method
  - the tearDown can be used to erase the data 

### Links 

```
https://www.youtube.com/watch?v=6tNS--WetLI&t=1915s
```




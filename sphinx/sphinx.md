## Sphinx 

### Installation

```python
pip install -U Sphinx
```

### Concept 

- It is a documentation tool used for the making docs in python for the function and file
- It picks up the data from the file and functions and also classes 
- The code should not bleed out of the class and function

### Working 

- In the docs directory

```sh
sphinx-quickstart  #to start the spinx in the file directory
make html
sphinx-apidoc -o out_dir_name source_dir_name  
make clean html  #to remove the html file
```

- edit conf.py to make it get the location of the source code present in the directory add two .. 
- edit the index.rst to get source of the directory
- conf.py should have the location of the source file

### Notes





### Links 

```
https://www.youtube.com/watch?v=qrcj7sVuvUA
https://www.sphinx-doc.org/en/master/
```


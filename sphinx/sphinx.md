## Sphinx 

### Installation

```python
pip install -U Sphinx
```

### Concept 

- It is a documentation tool used for the making docs in python for the function and file
- It picks up the data from the file and functions and also classes 
- The code should not bleed out of the class and function
- Sphinx has the extensions that are added to increase the fucntionality

### Working 

- In the docs directory

```sh
sphinx-quickstart  #to start the spinx in the file directory

## modify the conf.py file and index.rst file

sphinx-apidoc -o out_dir_name source_dir_name  

make html

make clean html  #to remove the html file
```

- edit conf.py to make it get the location of the source code present in the directory add two .. 

  ```python
  import os
  import sys
  sys.path.insert(0, os.path.abspath('..'))  #add the actual path that works
  ```

- edit the index.rst to get source of the directory

```python
module #sometime doesn't work
```

- conf.py should have the location of the source file

- edit index.rst as this also 

  ```rst
  .. automodule::main
     :members:
  ```

  

### Theming 

- A third party theme can be installed such as this

  ```python
  pip install furo
  ```

  

### Notes

- Fixes the "autodoc error"

```
extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc']
sphinx.ext.napolean
```

- insert this in conf.py file

### Steps

- Make the dir doc 
- cd to doc 

```
sphinx-quickstart  #to start the spinx in the file directory
```

- Modify the conf.py file 

```python
import os
import sys
sys.path.insert(0, os.path.abspath('..'))  #add the actual path that works

#add this in extension
extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc']
```

- Modify the index.rst above toctree code

```rst
.. automodule::main
   :members:
```

- cd one directory up 

```sh
sphinx-apidoc -o out_dir_name source_dir_name   #edit as needed
```

- cd to doc

```sh
make html
```



### Links 

```

https://www.youtube.com/watch?v=qrcj7sVuvUA
https://www.sphinx-doc.org/en/master/
https://www.youtube.com/watch?v=5s3JvVqwESA    
https://stackoverflow.com/questions/13516404/sphinx-error-unknown-directive-type-automodule-or-autoclass
https://www.sphinx-doc.org/en/master/tutorial/getting-started.html
```


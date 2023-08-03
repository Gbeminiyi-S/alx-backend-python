# 0x00-python_variable_annotations
An introductory project on:
- Type annotations in Python 3
- How you can use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with `mypy`

## Requirements
- All files should be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- The first line of all files is exactly #!/usr/bin/env python3
- All modules and functions are documented

## File Descriptions
### Mandatory
1. [0-add.py](./0-add.py) - a type-annotated function `add` that takes a float `a` and a float `b` as arguments and returns their sum as a float.
 
    **Execution Example**:
    ```
    bob@dylan:~$ cat 0-main.py
    #!/usr/bin/env python3
    add = __import__('0-add').add
    
    print(add(1.11, 2.22) == 1.11 + 2.22)
    print(add.__annotations__)
    
    bob@dylan:~$ ./0-main.py
    True
    {'a':  <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
    ```

2. [1-concat.py](./1-concat.py) - a type-annotated function `concat` that takes a string `str1` and a string `str2` as arguments and returns a concatenated string

    **Execution Example**:
    ```
    bob@dylan:~$ cat 1-main.py
    #!/usr/bin/env python3
    concat = __import__('1-concat').concat
    
    str1 = "egg"
    str2 = "shell"
    
    print(concat(str1, str2) == "{}{}".format(str1, str2))
    print(concat.__annotations__)
    
    bob@dylan:~$ ./1-main.py
    True
    {'str1': <class 'str'>, 'str2': <class 'str'>, 'return': <class 'str'>}
    ```

3. [2-floor.py](./2-floor.py) - a type-annotated function `floor` which takes a float `n` as argument and returns the floor of the float.
 
    **Execution Example**:
    ```
    bob@dylan:~$ cat 2-main.py
    #!/usr/bin/env python3
    
    import math
    
    floor = __import__('2-floor').floor
    
    ans = floor(3.14)
    
    print(ans == math.floor(3.14))
    print(floor.__annotations__)
    print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
    
    bob@dylan:~$ ./2-main.py
    True
    {'n': <class 'float'>, 'return': <class 'int'>}
    floor(3.14) returns 3, which is a <class 'int'>
    ```

4. [3-to_str.py](./3-to_str.py) - a type-annotated function `to_str` that takes a float `n` as argument and returns the string representation of the float.
 
    **Execution Example**:
    ```
    bob@dylan:~$ cat 3-main.py
    #!/usr/bin/env python3
    to_str = __import__('3-to_str').to_str
    
    pi_str = to_str(3.14)
    print(pi_str == str(3.14))
    print(to_str.__annotations__)
    print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))
    
    bob@dylan:~$ ./3-main.py
    True
    {'n': <class 'float'>, 'return': <class 'str'>}
    to_str(3.14) returns 3.14, which is a <class 'str'>
    ```

5. [4-define_variables.py](./4-define_variables.py) - defines and annotates the following variables with the specified values:
    - `a`, an integer with a value of 1
    - `pi`, a float with a value of 3.14
    - `i_understand_annotations`, a boolean with a value of True
    - `school`, a string with a value of “Holberton”

 
    **Execution Example**:
    ```
    bob@dylan:~$ cat 4-main.py
    #!/usr/bin/env python3
    
    a = __import__('4-define_variables').a
    pi = __import__('4-define_variables').pi
    i_understand_annotations = __import__('4-define_variables').i_understand_annotations
    school = __import__('4-define_variables').school
    
    print("a is a {} with a value of {}".format(type(a), a))
    print("pi is a {} with a value of {}".format(type(pi), pi))
    print("i_understand_annotations is a {} with a value of {}".format(type(i_understand_annotations), i_understand_annotations))
    print("school is a {} with a value of {}".format(type(school), school))
    
    bob@dylan:~$ ./4-main.py
    a is a <class 'int'> with a value of 1
    pi is a <class 'float'> with a value of 3.14
    i_understand_annotations is a <class 'bool'> with a value of True
    school is a <class 'str'> with a value of Holberton
    ```


### Advanced

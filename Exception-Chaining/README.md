# Learning Sessions
Understanding the behaviour of the following statements in python. 


### Case 1: try/except/finally
```python
def test_me(a, b):
    try:
        return a/b
    except IndexError as ex:
        raise RuntimeError from ex
    finally:
         print("=> [finally]: I am here.")
         return 50
```

### Case 2: try/finally 
```python
def bool_return():
     try:
         return True
     finally:
         return False
```

### Case 3: try/except 
```python
def int_return():
    empty_data_set = [] 
    try:
        return empty_data_set.pop()
    except IndexError as ex:
        raise RuntimeError("Give me exception Chaning Effect") from ex
```

### Case 4: try/except/else/finally 
```python
def divide(x, y):
     try:
         result = x / y
     except ZeroDivisionError:
         print("division by zero!")
     else:
         print("result is", result)
     finally:
         print("executing finally clause")

=> divide(2, 0)
```
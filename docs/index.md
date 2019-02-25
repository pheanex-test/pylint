## [R1705](#R1705) (no-else-return)<a name="R1705"></a>
Unnecessary `else` after `return`.

Used in order to highlight an unnecessary block of code following an if containing a `return` statement. As such, it will warn when it encounters an `else` following a chain of ifs, all of them containing a `return` statement.

**:x: Incorrect code**
```python
def foo(x):
    if x:
        return 1
    else:
        return 2
```
**:heavy_check_mark: Correct code**
```python
def foo(x):
    if x:
        return 1
    return 2
```

### Why is this better?
\<Here we will explain to the user why this is better and provide some context>


### Resources
* [Testcases](https://github.com/PyCQA/pylint/blob/master/pylint/test/functional/no-else-return.py)
* [Issue Tracker](https://github.com/PyCQA/pylint/issues?q=is%3Aissue+"no-else-return"+OR+"R1705")
* [StackOverflow](https://stackoverflow.com/q/9191388) (It is more efficient to use if-return-return or if-else-return?)

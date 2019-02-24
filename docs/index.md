# Rules
## [R1705](#R1705) (no-else-return)<a key="R1705" name="no-else-return"></a>
Reports an unnecessary `else` after `return`.
Used in order to highlight an unnecessary block of code following an `if` containing a `return` statement.
It will warn when it encounters an `else` following a chain of `if`'s, all of them containing a `return` statement.

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


### Resources <Links for further discussions>
* [Testcases](https://github.com/PyCQA/pylint/blob/master/pylint/test/functional/no_else_return.py)
* [Issue Tracker](https://github.com/PyCQA/pylint/issues?q=is%3Aissue+"no-else-return"+OR+"R1705")
* [StackOverflow - It is more efficient to use if-return-return or if-else-return?](https://stackoverflow.com/questions/9191388/it-is-more-efficient-to-use-if-return-return-or-if-else-return/28250521)


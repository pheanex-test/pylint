R1705 (no-else-return)
== Unnecessary "else" after "return" ==

bade code:
def foo(x):
    if x:
        return 1
    else:
        return 2

good code:
def foo(x):
    if x:
        return 1
    return 2

==Reasoning (answering "why is this better?"/Giving context):==
Used in order to highlight an unnecessary block of
code following an if containing a return statement.
As such, it will warn when it encounters an else
following a chain of ifs, all of them containing a
return statement

==Resources <Links for further discussions>:==
* See all Testcases for this rule
* Stackoverflow topics
* Blog posts
* ...

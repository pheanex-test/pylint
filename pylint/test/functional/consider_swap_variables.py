# pylint: disable=missing-docstring,invalid-name,using-constant-test

# The temporary variables (t1,t2,..) are numbered, so that
# for each test-case they are definetly undefined

a, b, c, d = 1, 2, 3, 4

t1 = a  # [consider-swap-variables]
a = b
b = t1

t2 = a  # only obvious swaps on the same level are reported
a = b
if True:
    b = a

t3 = a  # this is no swap
a = b
b = a

t4 = a, b  # complex swaps are ignored
a, b = c, d
c, d = t4

t5 = a  # [consider-swap-variables]
a = b  # longer swap circles are only reported once
b = t5
t5 = a

a, b, t6 = 1, 2, 3
t6 = a  # t6 has a value assigned and its value could be lost, since
a = b   # t6 could be the last reference to it.
b = t6  # => this is not equivalent to the swapping variant "a,b=b,a"

# Rules

## Index
|Rule Code|Rule Name|Rule Description|
|--|--|--|
|[R1705](#R1705)|no-else-return|Reports an unnecessary `else` after `return`|
|[C0102](#C0102)|blacklisted-name|Black listed name "%s"|
|[C0103](#C0103)|invalid-name|Invalid %s name "%s"%s|
|[C0111](#C0111)|missing-docstring|Missing %s docstring|
|[C0112](#C0112)|empty-docstring|Empty %s docstring|
|[C0113](#C0113)|unneeded-not|Consider changing "%s" to "%s"|
|[C0121](#C0121)|singleton-comparison|Comparison to %s should be %s|
|[C0122](#C0122)|misplaced-comparison-constant|Comparison should be %s|
|[C0123](#C0123)|unidiomatic-typecheck|Using type() instead of isinstance() for a typecheck|
|[C0200](#C0200)|consider-using-enumerate|Consider using enumerate instead of iterating with range and len|
|[C0201](#C0201)|consider-iterating-dictionary|Consider iterating the dictionary directly instead of calling .keys()|
|[C0202](#C0202)|bad-classmethod-argument|Class method %s should have %s as first argument|
|[C0203](#C0203)|bad-mcs-method-argument|Metaclass method %s should have %s as first argument|
|[C0204](#C0204)|bad-mcs-classmethod-argument|Metaclass class method %s should have %s as first argument|
|[C0205](#C0205)|single-string-used-for-slots|Class __slots__ should be a non-string iterable|
|[C0301](#C0301)|line-too-long|Line too long (%s/%s)|
|[C0302](#C0302)|too-many-lines|Too many lines in module (%s/%s)|
|[C0303](#C0303)|trailing-whitespace|Trailing whitespace|
|[C0304](#C0304)|missing-final-newline|Final newline missing|
|[C0305](#C0305)|trailing-newlines|Trailing newlines|
|[C0321](#C0321)|multiple-statements|More than one statement on a single line|
|[C0325](#C0325)|superfluous-parens|Unnecessary parens after %r keyword|
|[C0326](#C0326)|bad-whitespace|%s space %s %s %s|
|[C0327](#C0327)|mixed-line-endings|Mixed line endings LF and CRLF|
|[C0328](#C0328)|unexpected-line-ending-format|Unexpected line ending format. There is '%s' while it should be '%s'|
|[C0330](#C0330)|bad-continuation|Wrong %s indentation%s%s|
|[C0401](#C0401)|wrong-spelling-in-comment|Wrong spelling of a word '%s' in a comment|
|[C0402](#C0402)|wrong-spelling-in-docstring|Wrong spelling of a word '%s' in a docstring|
|[C0403](#C0403)|invalid-characters-in-docstring|Invalid characters %r in a docstring|
|[C0410](#C0410)|multiple-imports|Multiple imports on one line (%s)|
|[C0411](#C0411)|wrong-import-order|%s should be placed before %s|
|[C0412](#C0412)|ungrouped-imports|Imports from package %s are not grouped|
|[C0413](#C0413)|wrong-import-position|Import "%s" should be placed at the top of the module|
|[C1801](#C1801)|len-as-condition|Do not use `len(SEQUENCE)` as condition value|
|[E0011](#E0011)|unrecognized-inline-option|Unrecognized file option %r|
|[E0012](#E0012)|bad-option-value|Bad option value %r|
|[E0100](#E0100)|init-is-generator|__init__ method is a generator|
|[E0101](#E0101)|return-in-init|Explicit return in __init__|
|[E0102](#E0102)|function-redefined|%s already defined line %s|
|[E0103](#E0103)|not-in-loop|%r not properly in loop|
|[E0104](#E0104)|return-outside-function|Return outside function|
|[E0105](#E0105)|yield-outside-function|Yield outside function|
|[E0107](#E0107)|nonexistent-operator|Use of the non-existent %s operator|
|[E0108](#E0108)|duplicate-argument-name|Duplicate argument name %s in function definition|
|[E0110](#E0110)|abstract-class-instantiated|Abstract class %r with abstract methods instantiated|
|[E0111](#E0111)|bad-reversed-sequence|The first reversed() argument is not a sequence|
|[E0112](#E0112)|too-many-star-expressions|More than one starred expression in assignment|
|[E0113](#E0113)|invalid-star-assignment-target|Starred assignment target must be in a list or tuple|
|[E0114](#E0114)|star-needs-assignment-target|Can use starred expression only in assignment target|
|[E0115](#E0115)|nonlocal-and-global|Name %r is nonlocal and global|
|[E0116](#E0116)|continue-in-finally|'continue' not supported inside 'finally' clause|
|[E0117](#E0117)|nonlocal-without-binding|nonlocal name %s found without binding|
|[E0118](#E0118)|used-prior-global-declaration|Name %r is used prior to global declaration|
|[E0202](#E0202)|method-hidden|An attribute defined in %s line %s hides this method|
|[E0203](#E0203)|access-member-before-definition|Access to member %r before its definition line %s|
|[E0211](#E0211)|no-method-argument|Method has no argument|
|[E0213](#E0213)|no-self-argument|Method should have "self" as first argument|
|[E0236](#E0236)|invalid-slots-object|Invalid object %r in __slots__, must contain only non empty strings|
|[E0237](#E0237)|assigning-non-slot|Assigning to attribute %r not defined in class slots|
|[E0238](#E0238)|invalid-slots|Invalid __slots__ object|
|[E0239](#E0239)|inherit-non-class|Inheriting %r, which is not a class|
|[E0240](#E0240)|inconsistent-mro|Inconsistent method resolution order for class %r|
|[E0241](#E0241)|duplicate-bases|Duplicate bases for class %r|
|[E0301](#E0301)|non-iterator-returned|__iter__ returns non-iterator|
|[E0302](#E0302)|unexpected-special-method-signature|The special method %r expects %s param(s), %d %s given|
|[E0303](#E0303)|invalid-length-returned|__len__ does not return non-negative integer|
|[E0401](#E0401)|import-error|Unable to import %s|
|[E0402](#E0402)|relative-beyond-top-level|Attempted relative import beyond top-level package|
|[E0601](#E0601)|used-before-assignment|Using variable %r before assignment|
|[E0602](#E0602)|undefined-variable|Undefined variable %r|
|[E0603](#E0603)|undefined-all-variable|Undefined variable name %r in __all__|
|[E0604](#E0604)|invalid-all-object|Invalid object %r in __all__, must contain only strings|
|[E0611](#E0611)|no-name-in-module|No name %r in module %r|
|[E0632](#E0632)|unbalanced-tuple-unpacking|Possible unbalanced tuple unpacking wit|eft side has %d label(s), right side has %d value(s)|
|[E0633](#E0633)|unpacking-non-sequence|Attempting to unpack a non-sequence%s|
|[E0701](#E0701)|bad-except-order|Bad except clauses order (%s)|
|[E0702](#E0702)|raising-bad-type|Raising %s while only classes or instances are allowed|
|[E0703](#E0703)|bad-exception-context|Exception context set to something which is not an exception, nor None|
|[E0704](#E0704)|misplaced-bare-raise|The raise statement is not inside an except clause|
|[E0710](#E0710)|raising-non-exception|Raising a new style class which doesn't inherit from BaseException|
|[E0711](#E0711)|notimplemented-raised|NotImplemented raised - should raise NotImplementedError|
|[E0712](#E0712)|catching-non-exception|Catching an exception which doesn't inherit from Exception: %s|
|[E1003](#E1003)|bad-super-call|Bad first argument %r given to super()|
|[E1101](#E1101)|no-member|%s %r has no %r member%s|
|[E1102](#E1102)|not-callable|%s is not callable|
|[E1111](#E1111)|assignment-from-no-return|Assigning to function call which doesn't return|
|[E1120](#E1120)|no-value-for-parameter|No value for argument %s in %s call|
|[E1121](#E1121)|too-many-function-args|Too many positional arguments for %s call|
|[E1123](#E1123)|unexpected-keyword-arg|Unexpected keyword argument %r in %s call|
|[E1124](#E1124)|redundant-keyword-arg|Argument %r passed by position and keyword in %s call|
|[E1125](#E1125)|missing-kwoa|Missing mandatory keyword argument %r in %s call|
|[E1126](#E1126)|invalid-sequence-index|Sequence index is not an int, slice, or instance with __index__|
|[E1127](#E1127)|invalid-slice-index|Slice index is not an int, None, or instance with __index__|
|[E1128](#E1128)|assignment-from-none|Assigning to function call which only returns None|
|[E1129](#E1129)|not-context-manager|Context manager '%s' doesn't implement __enter__ and __exit__|
|[E1132](#E1132)|repeated-keyword|Got multiple values for keyword argument %r in function call|
|[E1133](#E1133)|not-an-iterable|Non-iterable value %s is used in an iterating context|
|[E1134](#E1134)|not-a-mapping|Non-mapping value %s is used in a mapping context|
|[E1135](#E1135)|unsupported-membership-test|Value '%s' doesn't support membership test|
|[E1136](#E1136)|unsubscriptable-object|Value '%s' is unsubscriptable|
|[E1137](#E1137)|unsupported-assignment-operation|%r does not support item assignment|
|[E1138](#E1138)|unsupported-delete-operation|%r does not support item deletion|
|[E1139](#E1139)|invalid-metaclass|Invalid metaclass %r used|
|[E1200](#E1200)|logging-unsupported-format|Unsupported logging format character %r (%#02x) at index %d|
|[E1201](#E1201)|logging-format-truncated|Logging format string ends in middle of conversion specifier|
|[E1205](#E1205)|logging-too-many-args|Too many arguments for logging format string|
|[E1206](#E1206)|logging-too-few-args|Not enough arguments for logging format string|
|[E1300](#E1300)|bad-format-character|Unsupported format character %r (%#02x) at index %d|
|[E1301](#E1301)|truncated-format-string|Format string ends in middle of conversion specifier|
|[E1302](#E1302)|mixed-format-string|Mixing named and unnamed conversion specifiers in format string|
|[E1303](#E1303)|format-needs-mapping|Expected mapping for format string, not %s|
|[E1304](#E1304)|missing-format-string-key|Missing key %r in format string dictionary|
|[E1305](#E1305)|too-many-format-args|Too many arguments for format string|
|[E1306](#E1306)|too-few-format-args|Not enough arguments for format string|
|[E1310](#E1310)|bad-str-strip-call|Suspicious argument in %s.%s call|
|[E1700](#E1700)|yield-inside-async-function|Yield inside async function|
|[E1701](#E1701)|not-async-context-manager|Async context manager '%s' doesn't implement __aenter__ and __aexit__|
|[F0010](#F0010)|parse-error|error while code parsing: %s|
|[F0202](#F0202)|method-check-failed|Unable to check methods signature (%s / %s)|
|[I0001](#I0001)|raw-checker-failed|Unable to run raw checkers on built-in module %s|
|[I0010](#I0010)|bad-inline-option|Unable to consider inline option %r|
|[I0011](#I0011)|locally-disabled|Locally disabling %s (%s)|
|[I0012](#I0012)|locally-enabled|Locally enabling %s (%s)|
|[I0013](#I0013)|file-ignored|Ignoring entire file|
|[I0020](#I0020)|suppressed-message|Suppressed %s (from line %d)|
|[I0021](#I0021)|useless-suppression|Useless suppression of %s|
|[I0022](#I0022)|deprecated-pragma|Pragma "%s" is deprecated, use "%s" instead|
|[R0123](#R0123)|literal-comparison|Comparison to literal|
|[R0201](#R0201)|no-self-use|Method could be a function|
|[R0202](#R0202)|no-classmethod-decorator|Consider using a decorator instead of calling classmethod|
|[R0203](#R0203)|no-staticmethod-decorator|Consider using a decorator instead of calling staticmethod|
|[R0401](#R0401)|cyclic-import|Cyclic import (%s)|
|[R0801](#R0801)|duplicate-code|Similar lines in %s files|
|[R0901](#R0901)|too-many-ancestors|Too many ancestors (%s/%s)|
|[R0902](#R0902)|too-many-instance-attributes|Too many instance attributes (%s/%s)|
|[R0903](#R0903)|too-few-public-methods|Too few public methods (%s/%s)|
|[R0904](#R0904)|too-many-public-methods|Too many public methods (%s/%s)|
|[R0911](#R0911)|too-many-return-statements|Too many return statements (%s/%s)|
|[R0912](#R0912)|too-many-branches|Too many branches (%s/%s)|
|[R0913](#R0913)|too-many-arguments|Too many arguments (%s/%s)|
|[R0914](#R0914)|too-many-locals|Too many local variables (%s/%s)|
|[R0915](#R0915)|too-many-statements|Too many statements (%s/%s)|
|[R0916](#R0916)|too-many-boolean-expressions|Too many boolean expressions in if statement (%s/%s)|
|[R1701](#R1701)|consider-merging-isinstance|Consider merging these isinstance calls to isinstance(%s, (%s))|
|[R1702](#R1702)|too-many-nested-blocks|Too many nested blocks (%s/%s)|
|[R1703](#R1703)|simplifiable-if-statement|The if statement can be replaced with %s|
|[R1704](#R1704)|redefined-argument-from-local|Redefining argument with the local name %r|
|[R1705](#R1705)|no-else-return|Unnecessary "else" after "return"|
|[R1706](#R1706)|consider-using-ternary|Consider using ternary (%s if %s else %s)|
|[R1707](#R1707)|trailing-comma-tuple|Disallow trailing comma tuple|
|[W0101](#W0101)|unreachable|Unreachable code|
|[W0102](#W0102)|dangerous-default-value|Dangerous default value %s as argument|
|[W0104](#W0104)|pointless-statement|Statement seems to have no effect|
|[W0105](#W0105)|pointless-string-statement|String statement has no effect|
|[W0106](#W0106)|expression-not-assigned|Expression "%s" is assigned to nothing|
|[W0107](#W0107)|unnecessary-pass|Unnecessary pass statement|
|[W0108](#W0108)|unnecessary-lambda|Lambda may not be necessary|
|[W0109](#W0109)|duplicate-key|Duplicate key %r in dictionary|
|[W0111](#W0111)|assign-to-new-keyword|Name %s will become a keyword in Python %s|
|[W0120](#W0120)|useless-else-on-loop|Else clause on loop without a break statement|
|[W0122](#W0122)|exec-used|Use of exec|
|[W0123](#W0123)|eval-used|Use of eval|
|[W0124](#W0124)|confusing-with-statement|Following "as" with another context manager looks like a tuple|
|[W0125](#W0125)|using-constant-test|Using a conditional statement with a constant value|
|[W0150](#W0150)|lost-exception|%s statement in finally block may swallow exception|
|[W0199](#W0199)|assert-on-tuple|Assert called on a 2-uple. Did you mean 'assert x,y'?|
|[W0201](#W0201)|attribute-defined-outside-init|Attribute %r defined outside __init__|
|[W0211](#W0211)|bad-staticmethod-argument|Static method with %r as first argument|
|[W0212](#W0212)|protected-access|Access to a protected member %s of a client class|
|[W0221](#W0221)|arguments-differ|Parameters differ from %s %r method|
|[W0222](#W0222)|signature-differs|Signature differs from %s %r method|
|[W0223](#W0223)|abstract-method|Method %r is abstract in class %r but is not overridden|
|[W0231](#W0231)|super-init-not-called|__init__ method from base class %r is not called|
|[W0232](#W0232)|no-init|Class has no __init__ method|
|[W0233](#W0233)|non-parent-init-called|__init__ method from a non direct base class %r is called|
|[W0235](#W0235)|useless-super-delegation|Useless super delegation in method %r|
|[W0301](#W0301)|unnecessary-semicolon|Unnecessary semicolon|
|[W0311](#W0311)|bad-indentation|Bad indentation. Found %s %s, expected %s|
|[W0312](#W0312)|mixed-indentation|Found indentation with %ss instead of %ss|
|[W0401](#W0401)|wildcard-import|Wildcard import %s|
|[W0402](#W0402)|deprecated-module|Uses of a deprecated module %r|
|[W0404](#W0404)|reimported|Reimport %r (imported line %s)|
|[W0406](#W0406)|import-self|Module import itself|
|[W0410](#W0410)|misplaced-future|__future__ import is not the first non docstring statement|
|[W0601](#W0601)|global-variable-undefined|Global variable %r undefined at the module level|
|[W0602](#W0602)|global-variable-not-assigned|Using global for %r but no assignment is done|
|[W0603](#W0603)|global-statement|Using the global statement|
|[W0604](#W0604)|global-at-module-level|Using the global statement at the module level|
|[W0611](#W0611)|unused-import|Unused %s|
|[W0612](#W0612)|unused-variable|Unused variable %r|
|[W0613](#W0613)|unused-argument|Unused argument %r|
|[W0614](#W0614)|unused-wildcard-import|Unused import %s from wildcard import|
|[W0621](#W0621)|redefined-outer-name|Redefining name %r from outer scope (line %s)|
|[W0622](#W0622)|redefined-builtin|Redefining built-in %r|
|[W0623](#W0623)|redefine-in-handler|Redefining name %r from %s in exception handler|
|[W0631](#W0631)|undefined-loop-variable|Using possibly undefined loop variable %r|
|[W0640](#W0640)|cell-var-from-loop|Cell variable %s defined in loop|
|[W0702](#W0702)|bare-except|No exception type(s) specified|
|[W0703](#W0703)|broad-except|Catching too general exception %s|
|[W0705](#W0705)|duplicate-except|Catching previously caught exception type %s|
|[W0711](#W0711)|binary-op-exception|Exception to catch is the result of a binary "%s" operation|
|[W1201](#W1201)|logging-not-lazy|Specify string format arguments as logging function parameters|
|[W1202](#W1202)|logging-format-interpolation|Use % formatting in logging functions and pass the % parameters as arguments|
|[W1300](#W1300)|bad-format-string-key|Format string dictionary key should be a string, not %s|
|[W1301](#W1301)|unused-format-string-key|Unused key %r in format string dictionary|
|[W1302](#W1302)|bad-format-string|Invalid format string|
|[W1303](#W1303)|missing-format-argument-key|Missing keyword argument %r for format string|
|[W1304](#W1304)|unused-format-string-argument|Unused format argument %r|
|[W1305](#W1305)|format-combined-specification|Format string contains both automatic field numbering and manual field specification|
|[W1306](#W1306)|missing-format-attribute|Missing format attribute %r in format specifier %r|
|[W1307](#W1307)|invalid-format-index|Using invalid lookup key %r in format specifier %r|
|[W1401](#W1401)|anomalous-backslash-in-string|Anomalous backslash in string: '%s'. String constant might be missing an r prefix|
|[W1402](#W1402)|anomalous-unicode-escape-in-string|Anomalous Unicode escape in byte string: '%s'. String constant might be missing an r or u prefix|
|[W1501](#W1501)|bad-open-mode|"%s" is not a valid mode for open|
|[W1503](#W1503)|redundant-unittest-assert|Redundant use of %s with constant value %r|
|[W1505](#W1505)|deprecated-method|Using deprecated method %s()|


### [R1705](#R1705) (no-else-return)<a name="R1705"></a>
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

#### Why is this better?
\<Here we will explain to the user why this is better and provide some context>


#### Resources <Links for further discussions>
* [Testcases](https://github.com/PyCQA/pylint/blob/master/pylint/test/functional/no_else_return.py)
* [Issue Tracker](https://github.com/PyCQA/pylint/issues?q=is%3Aissue+"no-else-return"+OR+"R1705")
* [StackOverflow: It is more efficient to use if-return-return or if-else-return?](https://stackoverflow.com/q/9191388)


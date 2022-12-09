## Problem

Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

## Example

```python
inputString = "(bar)", the output should be
solution(inputString) = "rab"
inputString = "foo(bar)baz", the output should be
solution(inputString) = "foorabbaz"
inputString = "foo(bar)baz(blim)", the output should be
solution(inputString) = "foorabbazmilb"
inputString = "foo(bar(baz))blim", the output should be
solution(inputString) = "foobazrabblim".
```
Because `"foo(bar(baz))blim"` becomes `"foo(barzab)blim"` and then `"foobazrabblim"`.
## Problem

Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

## Example

```python
a = [-1, 150, 190, 170, -1, -1, 160, 180],
solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].
```

If `a[i] = -1`, then the `i`^(th) position is occupied by a tree. Otherwise `a[i]` is the height of a person standing in the `i`^(th) position.
```
Prelude> :l baby.hs
[1 of 1] Compiling Main             ( baby.hs, interpreted )
Ok, modules loaded: Main.
*Main> doubleMe 2
4
*Main> doubleMe (doubleMe 2)
8
*Main>
```

Modify the file, reload:

```
*Main> :reload
[1 of 1] Compiling Main             ( baby.hs, interpreted )
Ok, modules loaded: Main.
*Main>
*Main>
*Main> doubleUs 7 7
28
```

Misellaneous others:

Single line comment:

```
-- a comment
```

First 50 odd numbers:
```
*Main> take 50 [1,3..]
[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59,61,63,65,67,69,71,73,75,77,79,81,83,85,87,89,91,93,95,97,99]
```
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
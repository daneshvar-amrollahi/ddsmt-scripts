Compares the outputs of two different versions of the solver on a particular input and finds a reduced one. 
Worked when one of them was returning an assertion failed, and the other was returning SAT.

```
$ ddsmt -v ~/Desktop/bug.smt2 ~/Desktop/bug-red.smt2 wrapper.py
```
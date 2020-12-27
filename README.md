# ring-theorem-solver

Python program with Z3 API to prove two properties for Rings

## Multiplication Identity is Unique
```shell
python3 one_is_unique.py
unsat
```


## Multiplication by zero returns zero
For any elements d in the Ring, 0d = d0 = 0. 
This can only be proved with depth-2 terms. 

```shell
python3 multiply_by_zero.py --depth 0
-- Checking for instantiation with depth 0
sat

python3 multiply_by_zero.py --depth 1
-- Checking for instantiation with depth 1
sat

python3 multiply_by_zero.py --depth 2
-- Checking for instantiation with depth 2
unsat
```
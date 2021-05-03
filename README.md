# BrainF*ck py
Brainf*ck interpreter by python

---

### Usage

Windows, Python: 
```
py BrainF-ck.py
```
    
If you want to input your own BrainF*cken source code, rewrite _INPUT in [BrainF-ck.py](./BrainF-ck.py).  
  
### Debug option
If you set the debug option to 1, you will get the following step execution result.  
```
> @1 [0, 10, 30, 70, 100]
> @2 [0, 10, 30, 70, 100]
- @3 [0, 10, 30, 70, 100]
- @3 [0, 10, 30, 69, 100]
- @3 [0, 10, 30, 68, 100]
- @3 [0, 10, 30, 67, 100]
. @3 [0, 10, 30, 66, 100]
...
code @pointer [Array]
```
  
### Characteristic behavior
+ Incrementing 255 will set it to 0.
+ Decrementing 0 will set it to 255.
+ Memory will be added as needed, and the upper limit depends on the environment.

### Returns Value of "Error"
| Return | Description |
--- | ---
| "" | Excellent! There is no error! |
| "Out of range of array Error" | An array with a negative subscript was referenced. |
| "\[ are missing." | The "\[" loop did not complete. |

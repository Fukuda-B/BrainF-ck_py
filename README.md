# BrainF*ck py
Brainf*ck interpreter by python

---

### Usage

Save your Brainf*ck program with the name [./data/Input.bf](./data/Input.bf).  
When you run BrainF-ck.py, you will see the output results in [Debug.txt](Debug.txt).  

Windows, Python: 
```
py BrainF-ck.py
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
| " \] are missing." | The "\[" loop did not complete. |


### Debug option output example

normal output example (option = 0)
```
B
```

The debug option adds the following basic information.
```
code:
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>----.

output:
B

error:

parsed:
++++++++++
>+>+++>+++++++>++++++++++<<<<->
>+>+++>+++++++>++++++++++<<<<->
>+>+++>+++++++>++++++++++<<<<->
>+>+++>+++++++>++++++++++<<<<->
>+>+++>+++++++>++++++++++<<<<->
>+>+++>+++++++>++++++++++<<<<->
>+>+++>+++++++>++++++++++<<<<->
>+>+++>+++++++>++++++++++<<<<->
>+>+++>+++++++>++++++++++<<<<->
>+>+++>+++++++>++++++++++<<<<->>>----.
```

##### optoin = 1
```
...
> @1 [0, 10, 30, 70, 100]
> @2 [0, 10, 30, 70, 100]
- @3 [0, 10, 30, 70, 100]
- @3 [0, 10, 30, 69, 100]
- @3 [0, 10, 30, 68, 100]
- @3 [0, 10, 30, 67, 100]
. @3 [0, 10, 30, 66, 100]
...
command @pointer [Array]
```
  
##### option = 2
```
...
> @1 [0, 10, 30, 70, 100] 43 ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>----.
> @2 [0, 10, 30, 70, 100] 44 ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>----.
- @3 [0, 10, 30, 70, 100] 45 ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>----.
- @3 [0, 10, 30, 69, 100] 46 ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>----.
- @3 [0, 10, 30, 68, 100] 47 ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>----.
- @3 [0, 10, 30, 67, 100] 48 ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>----.
. @3 [0, 10, 30, 66, 100] 49 ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>----.
...
command @pointer [Array] readingPos code
```

##### option = 3
```
...
> @1/0 [0, 10, 30, 70, 100]/[0, 10, 30, 70, 100] 43 ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>----.
> @2/0 [0, 10, 30, 70, 100]/[0, 10, 30, 70, 100] 44 ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>----.
- @3/0 [0, 10, 30, 70, 100]/[0, 10, 30, 70, 100] 45 ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>----.
- @3/0 [0, 10, 30, 69, 100]/[0, 10, 30, 69, 100] 46 ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>----.
- @3/0 [0, 10, 30, 68, 100]/[0, 10, 30, 68, 100] 47 ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>----.
- @3/0 [0, 10, 30, 67, 100]/[0, 10, 30, 67, 100] 48 ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>----.
. @3/0 [0, 10, 30, 66, 100]/[0, 10, 30, 66, 100] 49 ++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>----.
...
command @pointer/pointer(In execution loop) [Array]/[Array](In execttuion loop) readingPos code
```

# PASM
Python-ASM<br>
A python program used to compile python code to assembly.
<br><br><br>

---
## THIS IS A PROOF OF CONCEPT AND IS NOT OPTIMISED AT ALL
<br><br>

# Usage
- Create a python script using the `PASM` library, if a function is not inside the library, do not import it, imports other than the `PASM` library are not supported. 
- Put your python script inside `script.py`.
- Run `compiler.py` and wait for compiling.
- If no errors are visible, check inside the `modules` folder if a `main` executable is present. If there is, congratulation, here is your compiled python script. If it's not present, either your script is faulty and has not been caught by the python compiler, but by the assembler. Or the python compiler messed up and generated faulty assembly code that was caught by the assembler.
<br><br>

# Current Functionnalities
- [x] print() with text
- [x] print() with number (also the number is used as an ascii decimal)
- [x] epoch() gets epoch time (but returns 0 ?)
- [x] print() with a register
- [ ] more to come...
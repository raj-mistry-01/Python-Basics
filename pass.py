"""
Python pass Statement
The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error(intendation error ) when empty code is not allowed. Empty code is not allowed in loops, function definitions, class definitions, or in if statements.
For that empty code is you can write pass.
"""

for i in range(1,10,1) :
    if i == 5 :
        pass
    print(i)
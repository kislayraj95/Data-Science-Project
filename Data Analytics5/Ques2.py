# Q2

import numpy as np
count = 0
a = 0
b = 0
while((a!=6) | (b!=6)):
    count+=1
    a = np.random.randint(1,7)
    b = np.random.randint(1,7)
    print(f"{a}.{b}")
print(f"You Required {count+1} rolls to achieve 6,6")
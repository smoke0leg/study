"""Game guess the number"""

import numpy as np

number = np.random.randint(1, 101) # Generate number from 1 - 100

count = 0 # try count

while True:
    count+=1
    predict_number = int(input('Gues the number from 1 to 100: '))
    
    if predict_number > number:
        print(f"Hiden number < {predict_number}")
        
    elif predict_number < number:
        print(f'Hiden number > {predict_number}')
        
    else:
        print(f'You win!) Hidden number is {number}, you use {count} trys')
        break

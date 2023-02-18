"""Game guess the number, 
computer will guess"""

import numpy as np

def predict_algo(number:int=1) -> int:
    """Random guess number

    Args:
        number (int, optional): Hiden number. Defaults to 1.

    Returns:
        int: count fo trys
    """
    
    count = 0 #Trys count
    high = 100 #Upper range limit
    low = 0 # Lower range limit 
    
    while low <= high:
        count+=1
        predict_number = (low + high) // 2 
        if predict_number == number:
            break
        elif predict_number < number:
            low = predict_number + 1
        else:
            high = predict_number - 1
        
    return count


def score_game(predict_algo) -> int:
    """Mean result of 1000 games

    Args:
        predict_algo (_type_): Guess function

    Returns:
        int: mean try count
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 100, size=(1000))
    
    for number in random_array:
        count_ls.append(predict_algo(number))

    score = int(np.mean(count_ls))
    print(f'Algorytm guess the number at mean by: {score} trys')
    return(score)

if __name__ == '__main__':
#RUN
    score_game(predict_algo)

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
    predict_number = 50 #First predict number
    step = 50 #Step for change predict number
    
    while True:
        count+=1
        step/=2 
        prev_predict = predict_number
           
        if predict_number < number: 
            predict_number = int(predict_number + step)
            if predict_number == prev_predict:
                predict_number+=1
                 
        elif predict_number > number:
            predict_number = int(predict_number - step)
            if predict_number == prev_predict:
                prev_predict-=1 
                
        else: 
            break
        
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

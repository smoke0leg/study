"""Game guess the number, 
computer will guess"""

import numpy as np

def predict_random(number:int=1) -> int:
    """Random guess number

    Args:
        number (int, optional): Hiden number. Defaults to 1.

    Returns:
        int: count fo trys
    """
    count = 1
    predict_number = 50
    # prev_predict = 100
    n = 50
    while True:
        count+=1
        n/=2
        prev_predict = predict_number

        if predict_number < number:
            predict_number = int(predict_number + n)
            if predict_number == prev_predict:
                predict_number+=1 
        elif predict_number > number:
            predict_number = int(predict_number - n)
            if predict_number == prev_predict:
                prev_predict-=1 
        else: 
            break
        # n = n**2
    # while True:
    #     count+=1
    #     if number > predict_number:
    #         predict_number =  
        
    return count


def score_game(predict_random) -> int:
    """Mean game score

    Args:
        predict_random (_type_): Guess function

    Returns:
        int: mean try count
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 100, size=(1000))
    
    for number in random_array:
        count_ls.append(predict_random(number))

    score = int(np.mean(count_ls))
    print(f'Algorytm guess the number at mean by: {score} trys')
    return(score)

if __name__ == '__main__':
#RUN
    score_game(predict_random)

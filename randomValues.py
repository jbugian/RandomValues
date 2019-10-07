import random
import time



def weighted_random(values, weights):
    total_weight = sum(weights)
    acum_weights = [w / total_weight for w in weights[:]]
    for i in range(len(weights)):
        acum_weights[i] += acum_weights[i]
    rand = random.random()
    for value, weight in zip(values, acum_weights):
        if weight > rand:
            return value
        rand -= weight #was missing this instruccion, otherwise always return the first value.




#From now on, is for test the function. 
while(1):
    print(weighted_random([1,2,3],[0.1,0.1,0.8]))
    time.sleep(2)
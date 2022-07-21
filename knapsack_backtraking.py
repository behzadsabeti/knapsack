while True:                                       # Receiving information from user
    total_W = int(input("Enter total weight: "))
    total_n = int(input("Enter total items: "))
    if total_W > 0 and total_n > 0:
        break
    else:
        print("Please Enter valid weight and number.")

W_item = [0] * (total_n+1)
P_item = [0] * (total_n+1)

for i in range(total_n + 1):                      # Receiving information from user
    if i == 0:
        W_item[i] = 0
        P_item[i] = 0
    else:
        while True:
            W_item[i] = int(input("Enter item {} weight: ".format(i)))
            P_item[i] = int(input("Enter item {} profit: ".format(i)))
            if W_item[i] > 0 and P_item[i] > 0:
                break
            else:
                print("Please Enter valid weight and number.")



max_profit = 0                                    # Initializing max_profit with zero
numbest = 0                                       # Initializing numbest with zero
include = [0] * (total_n+1)                       # Initializing indlude array with zero
bestset = []                                      # Initializing bestset as an empty list

def knapsack(i, profit, weight):                  # Main knapsack function
    global max_profit, numbest, include, bestset  # Make these variables global to use them outside of function
    
    if (weight <= total_W) and (profit > max_profit):    # If current profit is more than max_profit 
        max_profit = profit                                  # and current weight is accepted then update max_profit and bestset
        numbest = i
        bestset = include.copy()

    if promising(i, profit, weight):              # If current node is promising
        include[i + 1] = 1                        # Consider taking next item 
        knapsack(i + 1, profit + P_item[i + 1], weight + W_item[i + 1]) # find rest of the items's profit
        include[i + 1] = 0                        # Consider not to taking next item
        knapsack(i + 1, profit, weight)           # Find rest of the items's profit


def promising(i, profit, weight):                 # Figure out weather this node is promising or not
    global max_profit, numbest
    if weight >= total_W:                         # If current node's weight is more than total_weight then return false
        return False
    else:
        j = i + 1
        bound = profit
        totweight = weight
        while (j <= total_n) and (totweight + W_item[j] <= total_W): # update total weight and bound until there is acceptable item
            totweight = totweight + W_item[j]
            bound = bound + P_item[j]
            j += 1

        k = j
        if k <= total_n:                                # if there is no more space for a whole item then cosider a piece of it
            bound = bound + (total_W - totweight) * P_item[k] / W_item[k]     # update bound
        return bound > max_profit                       # return True if bound is more than max_profit


knapsack(0, 0, 0)                                 # calling main function 
print(max_profit)                                 # print max_profit
print("best_solution: ", bestset[1:])             # print best items to pick

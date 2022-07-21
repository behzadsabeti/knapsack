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


P = [[0] * (total_W+1) for j in range(total_n+1)]  # Initializing P array with zero

best_index = []                                    # Initializing best_index as an empty list 
unsolved = []                                      # Initializing unsolved as an empty list
unsolved.append([total_n, total_W])                # First unsolved index is P[n][W]


while bool(unsolved):                              # While unsolved list is not empty do:
    
    temp = unsolved.pop(0)                         # Pop a index from unsolved list
    if temp not in best_index:                     # If the index isn't duplicate, add it to best_index
        best_index.append(temp)
    if temp[0] == 1:                               # If the index is in first row, then skip the rest and check while again
        continue
    unsolved.append([temp[0]-1, temp[1]])          # Add upper index to unsolved list
    if temp[1] - W_item[temp[0]] >= 0:             # If item's weight is not geater than w (P[i][w])
        unsolved.append([temp[0] - 1, temp[1] - W_item[temp[0]]])  # Add the index to unsolved list
        

best_index.sort()                                   # Sort best_index in Ascending order
for index in best_index:                           # Iterate over best_index
    i = index[0]                                   # and calculate profit like main knapsack but just for best indexes
    w = index[1]
    if W_item[i] <= w:                 # If item's weight is equal or less than w(w: 0 to total_weight)
        if P_item[i] + P[i - 1][w - W_item[i]] > P[i - 1][w]:  # If picking item i is better than not picking it and
            P[i][w] = P_item[i] + P[i - 1][w - W_item[i]]      # consider the extra weight that item i is adding
        else:
            P[i][w] = P[i - 1][w]                     # else don't pick it and store last profit

    else:
        P[i][w] = P[i - 1][w]                    # If item's weight is greater than w then don't pick it

i = total_n
k = total_W
best_items = []                                    # Initializing best_items as an empty list

while i > 0 and k > 0:                             # Start from last row and column and compare it with
    if P[i][k] != P[i-1][k]:                       # upper profit if they are same so algorithm didn't
        best_items.append(i)                       # pick it and if they are same so it picked it.
        k -= W_item[i]
        i -= 1
    else:
        i -= 1

print("Max Profit: ", P[total_n][total_W])         # print max_profit
print("Best_Items: ", best_items)                  # print best items to pick

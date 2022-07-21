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


P = [[0] * (total_W+1) for i in range(total_n+1)]  # Initializing P array with zero

for i in range(0, total_n+1):                      # Iterating over rows

    for w in range(0, total_W + 1):                # Iterating over columns
        if W_item[i] <= w:                         # If item's weight is equal or less than w(w: 0 to total_weight)
            if P_item[i] + P[i - 1][w - W_item[i]] > P[i - 1][w]:   # If picking item i is better than not picking it and   
                P[i][w] = P_item[i] + P[i - 1][w - W_item[i]]       # consider the extra weight that item i is adding
            else:
                P[i][w] = P[i - 1][w]              # else don't pick it and store last profit

        else:                                      # If item's weight is greater than w then don't pick it
            P[i][w] = P[i - 1][w]


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
         

# while loop

i = 1
while i < 6:
    
    if i == 3:
        break  # break the loop
    elif i == 1:
        i += 1  # increment before continue
        continue  # skip rest of the iteration

    i += 1
    print(i)
else:
  print("i is no longer less than 6") # this no longer print because of break 
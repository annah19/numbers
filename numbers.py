#1 We need to start by for looping through all two digit positive numbers
# Then we seperate the first integer from the second integer, sum them together and
# square the sum, if the results are the same as the two digit number we print it out

num = 0
# We only want to check two digit numbers
for num in range(10,100):
    # Here we seperate the two numbers
    first_int = num // 10
    second_int = num % 10
    sum_int = first_int + second_int
    sqr_int = sum_int **2
    if sqr_int == num:
        print(num)

#2 we for loop through all positive numbers < 100, we start the count on 0 and make a
# another for loop and the first range needs to be 1 and the stop range needs to be the number
# in the first for loop. Then we check to see if the number in the second for loop
# is dividable with the number
pos_num = 0 
for pos_num in range(1,100):
    count_div = 0
    for num in range(1,pos_num+1):
        if pos_num % num == 0:
            count_div += 1
    if count_div == 10:
        print(pos_num)


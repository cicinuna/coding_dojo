import random

def coin_toss(n):
    print "Starting the program..."
    head_count = 0
    tail_count = 0
    for i in range(0, n+1):
        coin = round(random.random())
        if coin == 1:
            head_count = head_count + 1
            print "Attempt #" +str(i) + ": Throwing a coin... It's a head! ... Got "+str(head_count)+ " head(s) so far and "+str(tail_count)+" tail(s) so far."
        else:
            tail_count = tail_count + 1
            print "Attempt #" +str(i) + ": Throwing a coin... It's a tail! ... Got "+str(head_count)+ " head(s) so far and "+str(tail_count)+" tail(s) so far."
    print "Ending the program, Thank you!"

coin_toss(50)

#Works as intended!
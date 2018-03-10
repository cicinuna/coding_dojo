def multiplication_table():
    print "x\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10\t11\t12"
    for i in range(1, 13):
        string = ""
        for j in range(1, 13):
            string += str(i * j) + " \t"
        print str(i)+ "\t" + string

multiplication_table()

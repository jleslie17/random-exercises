total = 0
count = 0
average = None

while True:
    number = raw_input("Enter a number: ")
    print number
    try:
       number = float(number)
       total += number
       count += 1
       average = total/count
       print total, count, average
    except:
        if number == "done":
            print "total: ", total
            print "count: ", count
            print "average: ", average
            break
        else:
            print "Invalid input"



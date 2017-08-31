maximum = None
minimum = None

while True:
    number = raw_input("Enter a number: ")
    try:
        number = int(number)
        if maximum == None:
            maximum = number
            minimum = number
        if maximum < number:
            maximum = number
        if minimum > number:
            minimum = number
    except:
        if number == "done":
            print "maximum: ", maximum
            print "minimum: ", minimum
            break
        else:
            print "invalid number, try again"


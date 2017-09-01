maximum = None
minimum = None
numbers = []

while True:
    number = raw_input("Enter a number: ")
    try:
        number = int(number)
        if maximum == None:
            maximum = number
            minimum = number
        numbers.append(number)
    except:
        if number == "done":
            maximum = max(numbers)
            minimum = min(numbers)
            print "maximum: ", maximum
            print "minimum: ", minimum
            break
        else:
            print "invalid number, try again"


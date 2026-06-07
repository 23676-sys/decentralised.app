# funstions go here


# main routine goes here
while True: 
    want_instructions = yes_no('DO you want to read these insturctions? ').lower()
    if want_instructions == "yes" or want_instructions == "y":
        print("Instructions go here")
    elif want_instructions == "no" or want_instructions == "n":
        pass
    else: print ("please asnwer yes/no")


print("we are done")

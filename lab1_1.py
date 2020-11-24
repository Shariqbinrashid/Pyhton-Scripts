#Bus Ticket Booking System 
print("Welcome to Ticket booking system")
print("We have three types of ticket: Budget,Economy and VIP")
print("Enter 1 for Budget ~500kr")
print("Enter 2 for Economy ~750kr")
print("Enter 3 for VIP ~2000kr")
ticket=input()
ticket=int(ticket)
tickePrice=0
tickePrice=int(tickePrice)


if(ticket==1):
    tickePrice=500
elif(ticket==2):
    tickePrice=750
elif(ticket==3):
    tickePrice=2000
bag=False
meal=False
total=0
total=int(total)

while(1):

    print("Enter 1 to Add bag ~200kr")
    print("Enter 2 to Add Meal ~150kr")
    print("Enter 3 to remove bag")
    print("Enter 4 to remove Meal")
    print("Enter 5 to finalize Ticket")
    a=input()
    a=int(a)

    print("")
    if(a==5):
        break
    elif(a==1):
        if(bag):
            print("you can add max 1  bag")
        else: 
            bag=True
            print("Bag added")
    elif(a==2):
        if(meal):
            print("you can add max 1 meal")
        else:    
            meal=True
            print("Meal added")
    elif(a==3):
        bag=False
        print("Bag removed")
    elif(a==4):
        meal=False   
        print("Meal removed")
        
    else:
        print("Wrong input!! Enter again!!")




print("Receipt:")
print("Ticket :  %dkr"%tickePrice)

total=tickePrice

if(bag):
    print("Bag :  200kr")
    total=total+200
if(meal):
    print("Meal :  150kr")
    total=total+150

print("        -------")
print("Total  :  %dkr"%total)
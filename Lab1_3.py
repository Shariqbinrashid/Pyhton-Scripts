#Truck loading calculation script
trucksize=" "

size=" "


while(1):
    trucksize=input("Enter Truck size!!")
    
    size=trucksize[0:len(trucksize)]
    size=int(size)
    print(size)
    if size<100:
        print("Give a volume larger than 100L")
        print("")
    else:
        break



bigCount=0
mediumCount=0
smallCount=0

#loop for big bag count
temp=80
while(temp<=size):
    bigCount=bigCount+1
    temp=temp+80


size=size-(temp-80)


#loop for medium bag count
temp=50

while(temp<=size):
    mediumCount=mediumCount+1
    temp=temp+50

size=size-(temp-50)



#loop for small bag count
temp=20

while(temp<=size):
    smallCount=smallCount+1
    temp=temp+20


print("These bags can be transported in %sL size truck"%trucksize)
print("%d big bags"%bigCount)
print("%d medium bags"%mediumCount)
print("%d small bags"%smallCount)

cost=0
cost=(bigCount * 60000)+ (mediumCount*30000)+(smallCount*10000)

print("Total value: %dkr"%cost)
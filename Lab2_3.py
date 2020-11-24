#Car distance and max range calculation script which read from file
import sys
import math
km=""
carname=[]


def main():
    global km
    filename = sys.argv[1]
    try:

        infile = open(filename, 'r')
        km=input("Enter distance to travel")
        km=int(km.rstrip("km"))
        read_file(filename) 
       
        
        display_result(calculate_percentage(km, parse_cars(carname)))
    except IOError :
        print ("Error: The file ", filename," could not be found.")
        

    
    

def read_file(filename):
        
        global carname
        infil = open(filename, 'r')
        
        for line in infil:
            carname.append(line.rstrip('\n'))
           
        
        infil.close()



def parse_cars(carname):
    temp=[]
    tupplelist=[]
    for line in carname:
        
        temp.append(line[:-4] )
        temp.append(int(line[-3:]))      
        tuplex=tuple(temp)
        tupplelist.append(tuplex)
        temp.clear()

    return tupplelist


def calculate_percentage(distance, cars):
    temp=[]
    tupplelist=[]
    percentage=0
    for t in cars: 
        for x in t: 
            if isinstance(x, int):
                x=int(x)
                
                percentage=distance/x*100
                temp.append(float(percentage))
            else:    
                temp.append(x)
        tuplex=tuple(temp)    
        tupplelist.append(tuplex)
        temp.clear()    
    return tupplelist    
            
def display_result(percentages):
    print("To drive the specified distance would correspond to this many")
    print("percent of each cars specified max range.")
    ch=37
    for t in percentages: 
                   
        for x in t: 
            if isinstance(x, str):
                print(x,"-->  ",end="") 
                 
            else: 
                if x>100:   
                    print("Distance exceeds max range (%d%s)"%(round(x),chr(ch)))
                else:
                    print("%d%s"%(round(x),chr(ch)))     
              
               
if __name__ == "__main__":
    main()

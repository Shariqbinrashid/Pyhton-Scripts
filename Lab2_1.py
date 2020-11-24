#Script that read file with conversation and and print one person message 
import sys
import pickle
name=""
def main():
    global name
    script = sys.argv[0]
    filename = sys.argv[1]
    
    try:

        infile = open(filename, 'r')
        name=input("Enter user name  ")
        read_file(filename) 
       
    except IOError :
        print ("Error: The file '%s' could not be found."%filename)
        

    
    

def read_file(filename):
        
        
        infil = open(filename, 'r')
        
        for line in infil:
            
            if line.rstrip("\n")==name:
               line=infil.readline()
               display_entry(name, line)

        
        return infil



def display_entry(name, message):    
    print("[%s] -->"%name,message.rstrip("\n") )


if __name__ == "__main__":
    main()

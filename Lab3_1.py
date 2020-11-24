#sesors faulty calculation script
import pickle
import math
import sys
'''
a1 = {'kitchen': '23*', 'bedroom':'22*', 'bathroom':'24*', 'garage':'28*'}
a2 = {'kitchen': '26*', 'bedroom':'22*', 'bathroom':'24*', 'garage':'28*'}

with open('filename1.pickle', 'wb') as handle:
    pickle.dump(a1, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('filename2.pickle', 'wb') as handle:
    pickle.dump(a2, handle, protocol=pickle.HIGHEST_PROTOCOL)

'''
def read_file(filename):
    try:
        with open(filename, 'rb') as file:
            loaded_dictionary = pickle.load(file)
    except IOError:
        print ("error: the files given as arguments are not valid.")
    return loaded_dictionary

def map_to_int(measurements):
    converted_dictionary = {}
    for key,value in measurements.items():
        value = value[:-1] #remove last character degree
        value = int(value) #convert to integer
        converted_dictionary[key] = value #add the key value pair in new loaded_dictionary
    return converted_dictionary

def find_faulty(primary, secondary, threshold):
    faulty_set = set()
    for key,value in primary.items():
        if  abs(primary[key] - secondary[key]) > threshold:
            faulty_set.add(key)
    return faulty_set
    
def display_warnings(faulty_sensors):
    print("\nAnalyzis of the provided files is complete.\n-------------------------------------------\n\nThe following sensors differ more than 2°:")
    
    for item in faulty_sensors:
        print(item)
    
def main():
    try:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
    except IndexError:
        raise SystemExit("Usage: {sys.argv[0]} <filename1_path> <filename2_path>")
    
    dictionary1 = read_file(arg1)
    dictionary2 = read_file(arg2)
    
    dictionary1 = map_to_int(dictionary1)
    dictionary2 = map_to_int(dictionary2)
    
    faulty_sensors = find_faulty(dictionary1,dictionary2,2)
    display_warnings(faulty_sensors)

if __name__ == "__main__":
    main()

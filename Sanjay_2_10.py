import csv 
import sys
#----------------------------------------------------------------------
def get_desired_data(csvfile):
    """ Read a csv file and returns the desired format of the data,  
        List for each Company year and month in which the share price was highest    
    """  
    try:  
        reader = csv.DictReader(csvfile, delimiter=',')
        results = []
        for row in reader:                             #each row is a dictionary 
            list = [] 
            list.append(row.pop('Year'))               #exclude year and month value for comparing the share price values
            list.append(row.pop('Month'))              #appending these values in list for desired output
            higest_share_price = max(map(int, row.values()))        
            [list.insert(0,key) for key in row if int(row[key]) == higest_share_price]    #inserting company name which have highest share price at first place   
            results.append(list)
    except:
        Exception("invalid data")
        
    print ("output in form of list [Company Name, year, Month]: \n" + repr(results))
    return results
    
#----------------------------------------------------------------------
if __name__ == "__main__":
    #takes file name as command line argument
    if len(sys.argv) > 1 :
        file_name = sys.argv[1]
    else :
        file_name = 'data_file.csv'
    with open(file_name, 'rb') as csvfile:  
        get_desired_data(csvfile)

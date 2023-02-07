def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   data = data.split('\n')
   
   return data[1].split(',')

f = open('data.csv').read()
print(get_first_row(f))

# Read the csv file
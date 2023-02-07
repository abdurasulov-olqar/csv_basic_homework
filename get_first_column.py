def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    data = data.split('\n')
    first_column = []
    for i in data:
        first_column.append(i.split(',')[0])


    return first_column

f = open('data.csv').read()
print(get_first_column(f))
    
# Read the csv file
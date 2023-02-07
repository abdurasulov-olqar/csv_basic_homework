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
    for i in data[1:]:
        first_column.append(i.split(','))


    return first_column

f = open('data.csv').read()
print(get_first_column(f))
    
# Read the csv file
import csv

def get_cvs_rowInstance(row_name):
    row_instance=[]

    row_index = data[0].index(row_name)

    for row in data[1:]:
        row_instance.append(row[row_index])

    return row_instance

def print_row(row_instance, type="int"):
    if type=="int":
        list(map(int,row_instance))
    elif type=="float":
        list(map(float,row_instance))

    for row_element in row_instance:
        print(row_element)

def print_clo(col_instance):
    for col_element in col_instance:
        print(col_element)


with open('Demographic_Statistics_By_Zip_Code.csv',newline='') as infile:
    data = list(csv.reader(infile))

# print_row(get_cvs_rowInstance("COUNT FEMALE"))
print_row(get_cvs_rowInstance("PERCENT FEMALE"),"float")
# print_row(get_cvs_rowInstance("JURISDICTION NAME"),"str")
# print_clo(data[0])
# print_clo(data[1])

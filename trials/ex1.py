import csv



####Function to read the csv file into dictionary
def read_to_dict():
    d2 = {}
    i = 0
    with open('cs3.csv') as rfl:
        reader = csv.DictReader(rfl,quotechar = '"')
        for row in reader:
            d2[i] = row
            i += 1
    return d2,[x for x in row.keys()]

####Function to write the contents of the dictionary to csv file
def write_from_dict(d2,header):
    with open('cs4.csv', 'w') as wfl:
        writer = csv.DictWriter(wfl,fieldnames = header)
        writer.writeheader()
        for x in d2.keys():
            writer.writerow(d2[x])

def execute():
    #header = ['SSN','First_Name','Last_Name','DOB','Address','Ph_Num']
    data,l = read_to_dict()
    write_from_dict(data,l)

if __name__ == '__main__':
    execute()
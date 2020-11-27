# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import csv

def diccionarios():
    data_archivo = 'data/MOCK_DATA.csv'
    with open(data_archivo,'r') as myFile:
        reader = csv.DictReader(myFile)
        for row in reader:
            print(row)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    diccionarios()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

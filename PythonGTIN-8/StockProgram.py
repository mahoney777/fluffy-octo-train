#Sam Mahoney
import math
import csv

print("Stock Program")
stockDict = {}
shopSize = int(input("Enter the maximum number of procuts in the store: "))

def addStuff(stockDict):
    global shopSize
    print()
    Dict = {}
    Dict = stockDict
    ord_list = 0
    productName = 0

    productName = input(str("Enter Product name: "))
    productName.title()
    productCharacters = list(productName)
    for item in productCharacters:
        ord_list = ord_list + ord(item)
    index = ord_list % shopSize
    if index not in Dict:
        print("index = ", index)
        Dict[index] = productName
        print(Dict)
        return(Dict)
    else:
        while index in Dict:
            print("Error")
            print(index)
            index = index + 1
            print(index)
            if index not in Dict:
                break
        print("index = ", index)
        Dict[index] = productName
        print(Dict)
        return(Dict)

    
def stockOutput(stockDict):
    
    csvFile = open('Stock.csv', 'a', newline="",)
    fieldnames = ['Index', 'Product']
    writeObject = csv.writer(csvFile, delimiter=",")
    for key, value in stockDict.items():
        writeObject.writerow((key, value))
    csvFile.close()

def stockReader():

    csvFile = open('stock.csv', 'r')
    readObject = csv.reader(csvFile, delimiter=",")
    for row in readObject:
        print(row)    

    csvFile.close()

addStuff(stockDict)
stockOutput(stockDict)
stockReader()

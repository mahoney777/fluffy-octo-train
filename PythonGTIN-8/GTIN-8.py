import math
import csv 

def eighthDigit():
    gtin = input("Enter the GTIN-8: ")
    #limit this to 7 digits
    
    n = [int(d) for d in str(gtin)] 
    print(n)
    n = sum(n)
    x = n
    if(n % 10):
        n = n + ( 10 - n % 10)
    d8 = n - x
    print(d8)

    print("The GTIN-8 is: " ,d8)
    gtinnum = n.append(d8)
    print(gtinnum)


    print("Will now validate")

    d1v = d1a * 3
    d2v = d2a * 1
    d3v = d3a * 3
    d4v = d4a * 1
    d5v = d5a * 3
    d6v = d6a * 1
    d7v = d7a * 3
    d8v = d8 * 1

    y = d1v+d2v+d3v+d4v+d5v+d6v+d7v+d8v

    barcode = d
    print(barcode)

    check = (y % 10)
    if(check == 0):
        print("This is valid!")
    else:
        print("This is invalid!")

def csvSearch():
    number = input("Enter the GTIN-8 to search for: ")
    csvFile = open('gtin-8.csv', 'rt')
    searchObject = csv.reader(csvFile, delimiter=",")
    for row in searchObject:
        for field in row:
            if field == number:
                print(number+" is in the file")
                print(row)

def csvOutput(glist):
    csvFile = open('gtin-8.csv', 'w', newline="",)
    fieldnames = ['GTIN-8', 'Product']
    writeObject = csv.writer(csvFile, delimiter=",")
    for key, value in glist.items():
        writeObject.writerow((key, value))
        csvFile.close()
    
eighthDigit()
csvSearch()
    
    

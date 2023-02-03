import csv
import json
import sys

def cal(points):
  '''
  :param pointsL: string 
          the points a user want to spend
  :return json.dumps(dict): string
          a json format of all payer point balances
  '''
  # convert the type of string to int
  points = int(points)
  # open the csv file to read each row of transactions 
  with open('data-csv.csv', mode = 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    # count the current line of csv file
    line = 0
    # store trasactions in a list structure
    sort_csv = []

    # iterate the csv file, and get each row in the csv file 
    for row in reader:
      # skip the first line which represents the names of each column
      if line != 0:
        # combine the payer, the points, and the timestamp as one long string
        # use comma to distinguish each of the three, and store the string in the list
        sort_csv.append(row[0] + "," + str(row[1]) + "," + row[2])
      line += 1
    
    # sort the list in a increasing order by timestamp
    sort_csv.sort(key = lambda y:y.split(",")[2])

    # store each payer's balance, the key is payper, the value is the balance
    dict = {}
    # iterate the transactions, and get each transaction 
    for row in sort_csv:
      # get the payer's name and point in one transaction
      payer = row.split(",")[0]
      point = int(row.split(",")[1])
      # initialize the balance as 0 for payers
      if dict.get(payer):
        continue
      else:
        dict[payer] = 0
      
      # compute the balance for payers
      # if the spending point is 0, this means the user spends all points
      if points == 0:
        # then the rest points directly add in the related payer's balance
        dict[payer] += point
      # if the spending point is not 0, this means the user has not spend all points
      else:
        # if the point of transaction is lesser than the current spending point
        if point < points:
          # minus the point from the current spending point
          # and no rest points can be added in balance
          points -= point
        # if the point of transaction is greater or equalthan the current spending point
        else:
          # add the rest points in balance
          dict[payer] += (point - points)
          # now the user spends all points
          points = 0
    # return a json format in string       
    return json.dumps(dict)

def main(arg):
  '''
  :param arg: string
          the points a user want to spend in
  '''
  print(cal(arg))

if __name__ == '__main__':
  '''
  '''
  # call the main function
  # read the input 
  main(sys.argv[1])
      
       
    
      
      
  
        
        
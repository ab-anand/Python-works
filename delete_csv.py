import csv
input = open('active_merchants.csv', 'r')
outfile = open('unavailable-merchants.csv', 'w', newline='') 
    
output = open('first_edit.csv', 'w')
words = ['food', 'travel', 'recharge', 'fashion','dominos', 'uber', 'foodpanda',
         'swiggy', 'nearbuy', 'zomato', 'makemytrip', 'yatra', 'ola', 'airtel',
         'mobikwik', 'bsnl', 'freecharge', 'flipkart', 'myntra', 'shopclues', 'jabong', 'cleartrip']
writer = csv.writer(outfile)
for row in csv.reader(input):
    if row[0].lower() not in words:
        writer.writerow(row)
   
input.close()
output.close()
print('Done')

import csv

def read_data():
    data = []

    with open('sales.csv','r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data

#-------------------------------------------------------
def month_sales():
    data = read_data()

    print('\n')
    print('Sales by month in 2018')

    for row in data:
        sales = int(row['sales'])
        print('{} £{}'.format(row['month'], row['sales']))
#-----------------------------------------------

def annual_sales():
    data = read_data()

    sales = []

    for row in data:
        sale = int(row['sales'])
        sales.append(sale)

    total_sales = sum(sales)
    print('The total sales across all months in the year {} was £{}'.format(row['year'], total_sales))

# ---------------------------------------------

def percentage_change():
    data = read_data()
    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)

    months = []
    for row in data:
        month = row['month']
        months.append(month)

    month_change = []
    for a in range(len(sales)-1):
        percent_change = round(((sales[a+1]-sales[a])/sales[a])*100,2)
        month_change.append(percent_change)

    for a in range(len(sales)-1):
        print('The percentage change in sales from {} to {} is: {}%'.format(months[a], months[a+1], month_change[a]))

#---------------------------------------------------------
first_input = input('Would you like to see what I can do? Y/N')
if first_input == 'N':
    print('Okay, Goodbye!')
elif first_input == 'Y':
    second_input = input(' 1. I can output the sum of total sales in 2018 \n 2. I can provide a comparison of sales value for relevant months \n 3. Exit Menu')
if second_input == '3':
        print('Goodbye!')
elif second_input == '1':
        month_sales()
        annual_sales()
elif second_input == '2':
       percentage_change()


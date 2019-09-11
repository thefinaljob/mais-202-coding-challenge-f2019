'''Am I a data scientist now? '''
import sys, csv ,operator
import matplotlib.pyplot as plt

mortgage = 0.0
rent = 0.0
own = 0.0

mort_amt = 0.0
rent_amt = 0.0
own_amt = 0.0

def do_everything():

    home_data =csv.reader(open('home_ownership_data.csv', 'r'),delimiter=',')

    #iterates through the home ownership data to find the loan amount for each ID
    for first_row in home_data:

        ident = str(first_row[0])
        loan_type = str(first_row[1])
        if loan_type == "home_ownership":
            continue
        look_loan(ident, loan_type)
    
    #Setting parameters of the graph here
    names = ['MORTGAGE', 'OWN', 'RENT']
    values = [float(mortgage/mort_amt), float(own/own_amt), float(rent/rent_amt)]
    plt.bar(names, values) 
    plt.xlabel('Home ownership')
    plt.ylabel('Average loan amount ($)')
    plt.title('Average loan amounts per home ownership')  
    plt.autoscale()
    plt.savefig('submission.png', bbox_inches='tight')

def look_loan(ident, loan_type):

    '''apparently python doesn't allow me to reset iterators,
    who would have known? This function is here to make up for it'''

    loan_data = csv.reader(open('loan_data.csv', 'r'),delimiter=',')

    #conducts linear search of the loan data to see where the corresponding ID and loan
    #amounts are found
    for second_row in loan_data:

            check_ident = str(second_row[0])

            if ident == check_ident:
                amt = float(second_row[1])
                if loan_type == 'MORTGAGE':
                    global mortgage 
                    mortgage += amt
                    global mort_amt
                    mort_amt += 1.0
                elif loan_type == 'RENT':
                    global rent 
                    rent += amt
                    global rent_amt
                    rent_amt += 1.0
                elif loan_type == 'OWN':
                    global own 
                    own += amt
                    global own_amt
                    own_amt += 1.0
                return

do_everything()
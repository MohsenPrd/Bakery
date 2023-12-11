## Mohsen Pourdehghan

bread_dict = {'Barbari' : 5000, 'Lavash' : 8000, 'Taftoon' : 15000, 'Sangak' : 10000, 'Baguette' : 20000}
cart_dict ={}

customer_name = input('\nHello there, whats your name? ')

#--- Valid name without number ---
x=1 #runs the while loop for once
while x > 0 :
    for letters in customer_name:
        if letters.isdigit() or letters.isalpha() == False:
            x+=1
    if x > 1 :    
        customer_name = input('\nInvalid name!!! whats your name? ')
        x = 1
    else:
        x = 0
###

#--- Valid number ---     
ph_number = input('\nplease tell your mobile phone(with 11 digits and just numbers): ')

while (ph_number.isdigit() == False) or (len(ph_number) < 11 or len(ph_number) > 11):
    ph_number = input('Invalid Number!!! tell your mobile phone(with 11 digits and just numbers): ')
###
    
print('\n',bread_dict)

need_more = 'yes'

while need_more == 'yes' :

    bread_type = input(f'\nOK "{customer_name}", which bread do you need? ').capitalize()
    
    #--- Check the bread type is valid ---
    while bread_type not in bread_dict:
        bread_type = input(f'\nINVALID BREAD, which one do you need? ').capitalize()

    ###

    bread_amount = input(f'\nOK, How many from it? (from 1 to 10) ')
    
    #--- Check the input ---
    while bread_amount.isdigit() == False or int(bread_amount) > 10: #for checking the last input from the second while in this loop
        
        while bread_amount.isdigit() == False :
            bread_amount = input(f'\nJUST NUMBERS!!! How many from it? (from 1 to 10) ')
            
        while bread_amount.isdigit() and int(bread_amount) > 10:
            bread_amount = input(f'\nYOU CANT BUY OVER 10!!! How many from it? ')
    ###

    if bread_type in cart_dict :
        cart_dict[bread_type][0] += int(bread_amount)
        cart_dict[bread_type][1] += int(bread_amount) * bread_dict[bread_type]
    else:
        cart_dict[bread_type] = [int(bread_amount), int(bread_amount) * bread_dict[bread_type]]
    
    #--- Need More? ---
    need_more = input('\nOK, Do you need other types? (yes/no) ')
    while need_more !='no' and need_more != 'yes' :
        need_more = input('JUST "yes" OR "no", Do you need other types? (yes/no) ')
    ###

      
if need_more == 'no':
    #--- Sum of prices ---
    pay = 0
    for breadTypes in cart_dict:
            pay += cart_dict[breadTypes][1]
        
    print(f'''\nThere you go, you bought this breads with their [amount, price]:=>

{cart_dict}

=> you have to pay {pay}.

''')
    ###
    

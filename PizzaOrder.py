Pizza Order


size = {'1':'Small ', '2':'Medium', '3':'Large ', '4':'XLarge'}
sizeprice = {'1':10, '2':15, '3':20, '4':25}
mtop = {'1':'Cheese          ', '2':'Mushroom        ', '3':'Green Peppers   ', '4':'Jalapeño Peppers', '5':'Bacon           ','6':'Chicken         ', '7':'Chorizo         ', '8':'Salami          ', '9':'Pepperoni       '}
top = {'1':'Cheese', '2':'Mushroom', '3':'Green Peppers', '4':'Jalapeño Peppers', '5':'Bacon','6':'Chicken', '7':'Chorizo', '8':'Salami', '9':'Pepperoni'}
topprice = {'1':1, '2':1, '3':1, '4':1, '5':5, '6':5, '7':5, '8':5, '9':5}
ftotal = 0
npizza=0
morep = 'y'
order=[]
torder=[]

def printsizemenu():
    print()
    print('                                 Please, Choose the size of your pizza                                     ')
    print('------------------------ ')
    print('|*****PIZZA SIZES******|')
    print('------------------------ ')
    for key in size:
            print('|',key, '|', size[key], '| $', "{:.2f}".format(sizeprice[key]),'|')
    print(' ----------------------- ')
    
def printtopmenu():
    print()
    print('                                 Please, Choose toppings                                     ')
    print('--------------------------------- ')
    print('|*********TOPPINGS MENU*********|')
    print('--------------------------------- ')
    for key in mtop:
        print('|',key, '|', mtop[key], '| $', "{:.2f}".format(topprice[key]),'|')
    print('--------------------------------- ')
    
def printorder(osize,otop,oprice):
    pizzastring= size[osize] +" pizza with "
    for i in otop:
        pizzastring+=top[i]+", "
    pizzastring+="total $"+ str(oprice)
    return pizzastring

print('                                                                                                   ')
print('    ██╗░░░░░██╗███╗░░██╗░█████╗░██╗░██████╗  ██████╗░██╗███████╗███████╗███████╗██████╗░██╗░█████╗░')
print('    ██║░░░░░██║████╗░██║██╔══██╗╚█║██╔════╝  ██╔══██╗██║╚════██║╚════██║██╔════╝██╔══██╗██║██╔══██╗')
print('    ██║░░░░░██║██╔██╗██║███████║░╚╝╚█████╗░  ██████╔╝██║░░███╔═╝░░███╔═╝█████╗░░██████╔╝██║███████║')
print('    ██║░░░░░██║██║╚████║██╔══██║░░░░╚═══██╗  ██╔═══╝░██║██╔══╝░░██╔══╝░░██╔══╝░░██╔══██╗██║██╔══██║')
print('    ███████╗██║██║░╚███║██║░░██║░░░██████╔╝  ██║░░░░░██║███████╗███████╗███████╗██║░░██║██║██║░░██║')
print('    ╚══════╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░░░╚═════╝░  ╚═╝░░░░░╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝╚═╝╚═╝░░╚═╝')
print ()

client=input('To start your order, please,enter your name: ')
print ('Welcome ', client)

while morep.lower() == 'y':
    printsizemenu()
    keysize=input('Enter Pizza size number:  ')    
    if keysize in size.keys():
        sprice= sizeprice[keysize]
        print('You choose a', size[keysize], 'pizza $', "{:.2f}".format(sprice))
        print()
        npizza=+1
        add_top = 'y'
        tprice=0
       
        while add_top.lower() == 'y':
           
            printtopmenu()

            keytop=input('Enter topping number:  ')
            if keytop in top.keys():
                tprice += topprice[keytop]
                print('You choose ', top[keytop], '$', "{:.2f}".format(topprice[keytop]))
                order.append(keytop)
                #print (order)
                add_top = input("Add toppings? (y/n?)  ")
                
            else:
                print('Topping not in the menu')
                print()
        
        total= sprice+tprice

        pizzastr=printorder (keysize,order,total)
        print(pizzastr)
        order.clear()

        torder.append(pizzastr)
    else:    
        print(keysize, 'is not a valid size')
        print()    
     
    morep = input("Do you want to add another pizza? (y/n?)  ") 
                 
    ftotal+=total

print()
print(client, ", your order is:") 
pizzatxt = open("order.txt", "w")
pizzatxt.write(client+"\n")
for x in torder:
    pizzatxt.write(x+"\n")
    print(x)
pizzatxt.write(str(ftotal))
pizzatxt.close()
print('Total order $', ftotal)
print('Thank you for your order')


from numpy import double

menus = {}
orders = {}


def menu():
    global orders
    print("Nasi Biryani")
    print("1. Place Order")
    print("2. Update Order")
    print("3. Serve Order")
    print("4. Exit")

    choice = int(input('Enter option: '))
    
    load_menu()
    order_items = []

    if choice == 1:
        # place order
        while True:
            ch = input("Enter item code and quantity (Press <Enter> key to end):")
            ch_split = ch.split(' ')
            if validate_item_code(ch_split[0]):
                # valid
                order_items.append([ch_split[0],int(ch_split[1])])
            elif ch == '':
                order_no = get_next_order_no()
                orders[order_no]=order_items
                get_order_details(order_no)
                print()
                break
            else:
                print("Invalid item code! Try again")
        menu()
    elif choice == 2:
        # update order
        print()
        print_all_orders()
        ord_no = int(input("Enter Order Number: "))
        order = get_order_by_order_no(ord_no)
        
        if order is not None:
            print("\tOrder Number ",ord_no)
            for y in order:
                code = y[0]
                order_menu = get_menu_by_code(code)
                print('\t{} {} X {} '.format(code.upper(), order_menu[0], y[1]))
            for y in order:
                code = y[0]
                order_menu = get_menu_by_code(code)
                choice = input('{} {} X {}, new qty or <Enter> for no change: '.format(code.upper(), order_menu[0], y[1]))
                if choice == '':
                    #leave it as it is, no change
                    pass
                elif int(choice) == 0:
                    # remove the item
                    #check if al items are removed then cancel the order
                    removeable_item = []
                    updated_item = []
                    if len(order) !=0:
                        # remove the order
                        for x in order:
                            if x[0] == code:
                                removeable_item.append(x)
                                print("{} {} X {} is removed.".format(code.upper(), order_menu[0], y[1]))
                    
                            if len(order) == 0:
                                orders.pop(ord_no)
                                print("Order {} is cancelled!".format(ord_no))
                                print()
                        # remove items
                    # remove an item   
                    for x in order:
                        for y in removeable_item:
                            if x == y:
                                order.remove(y)
                elif int(choice) > 0:
                    # update the quantity
                    y[1] = int(choice)
                    print("Quantity updated...")
                    #menu()
                else:
                    print("Enter valid choice!")
            menu()
        else:
            print("Order not found!!")
            menu()
        
    elif choice == 3:
        choice = int(input("Enter order number that is ready: "))
        if len(orders) > 0:
            order = get_order_by_order_no(choice)
            print("order = ",order)
            for y in order:
                code = y[0]
                order_menu = get_menu_by_code(code)
                choice = input('{} {} X {}\nPress <Enter> when order is collected: '.format(code.upper(), order_menu[0], y[1]))

                if choice == '':
                    print()
                    menu()
                else:
                    print("Invalid key!")
        else:
            print("No orders!")
    elif choice == 4:
        # end
        print("Thankyou for using Nasi Biryani!")
    else:
        print("Invalid option!")
        print()
        menu()


def load_menu():
    global menus
    # Get menu form the .txt file
    f = open("menu.txt", "r")
    for item in f:
        i = item.split(',')
        i[2]= i[2].replace('\n','')
        menus[i[0]] = [i[1],i[2]]
        print("{} - {} {}".format(i[0], i[1],i[2]))
    
def validate_item_code(item_code):
    for x in menus:
        if x.upper() == item_code.upper():
            return True
    return False 
def get_menu_by_code(menu_code):
    return menus[menu_code.upper()]

def get_order_details(order_no):
    total_price = 0.0
    print()
    print("Order Number ",order_no)
    order = orders.get(order_no)
    total_price = 0.0
    for x in order:
        code = x[0]
        menu = get_menu_by_code(code)
        total = int(x[1]) * double(menu[1])
        total_price+= total
        print('{} {} X {} = ${}'.format(code.upper(), menu[0], x[1],total))
    print("Total price $",total_price)

def get_order_by_order_no(order_no):
    return orders.get(order_no)

def print_all_orders():
    if(len(orders) != 0):
        for key,val in orders.items():
            print("Order Number ",key)
            for y in val:
                code = y[0]
                menu = get_menu_by_code(code)
                print('{} {} X {} '.format(code.upper(), menu[0], y[1]))
            print()
    else:
        print("No orders")


def get_next_order_no():
    return len(orders)+1
if __name__ == '__main__':
    menu()
import data_orders
main = 'main'
products = 'products'
product = ['coke', 'tango', 'fanta', 'pepsi', '7up']
orders = 'orders'
couriers = 'couriers'
menu = {main:{}, products:{}, couriers:{}, orders:{},}
print(menu)



def drinks_index():
  for x in product:
    print(f'{((product.index(x)) + 1)}. {x}')

while True:

  print('\nWelcome to MYCAFE \nPress 0 to Exit App\nPress 1 for Product Menu\nPress 2 for Order Menu\nPress 3 for Courrier Services')
  user_input = int(input('Enter:'))

  while user_input != 0 and user_input != 1 and user_input != 2:
      print('\nPlease choose a valid option')
      user_input = int(input('Enter: '))

  if user_input == 0:
    print('\nThank You for visiting MYCAFE')
    break
  else:
    while user_input ==1: 
      print('\nMain Menu - Choose an Option:\n0. Return to Menu\n1. Product List\n2. Create New Product\n3. Update Product\n4. Delete a Product')
      user_input = int(input('Enter: '))
      
      while user_input != 0 and user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4:
        print('Enter Number from the List')
        user_input = int(input())
  
      if user_input == 0:
        break
  
      elif user_input == 1:
        print('\nDrinks List:')
        drinks_index()
        cstmr_drink = input('\nSelect your Drink:\n')
        while str(cstmr_drink) not in product:
          print('Select a Drink from the List:')
          cstmr_drink = str(input())
        print(f'\n{cstmr_drink}')
        print('\nWould you like ice with your drink? \nEnter yes/no:')
        option_input = str(input())

        while option_input != 'yes' and option_input != 'no':
          print('\nEnter yes/no')
          option_input = str(input())
        if option_input == 'yes':
          print(f'\nServing {cstmr_drink} with Ice')
        else:
          print(f'\nServing {cstmr_drink} without Ice')
        
      elif user_input == 2:       # Creating new product
        add_item = input('\nAdd Item:\n')
        product.append(str(add_item))
        print('\nNew Drink List:')
        drinks_index()
  
      elif user_input == 3:       # Updating product
        print('\nMake changes to your selection')
        drinks_index()
        print('\nItem to Change:')
        drinks_change = str(input())
        while drinks_change not in product:
          print('\nChoose a Item from the List')
          print('\nItem to Change:')
          drinks_change = str(input())
        drinks_add = str(input('\nItem to Add: '))
        product[(product.index(drinks_change))] = drinks_add
        drinks_index()
  
      elif user_input == 4:
        print('\nDrinks List')
        drinks_index()
        print('\nDelete an Item')
        del_input = input('Delete: ')
        while del_input not in product:
          print('\nChose an Item in the List to delete')
          del_input = input('Delete: ')
        if del_input in product:
          product.remove(del_input)
          print(f'\n{del_input} has been deleted\n')  
          drinks_index()
    while user_input ==2:
            print()
            user_input = int(input('Press 1 to enter customer information: '))
            while user_input != 0 and user_input != 1 and user_input != 2 and user_input != 3 and user_input != 4:
              print('Enter Number from the List')
              user_input = int(input())
              
            if user_input == 0:
              break
            elif user_input == 1:
              print (data_orders.data)
              
              customer_name = input ("Enter new order customer name: ").strip()
              customer_address = input ("Enter new order customer address: ").strip()
              customer_phone = input("Enter new order customer phone: ").strip()
              #if customer_name == "' or cust_address == "' or cust_phone == "":
                   # print_menu (orders, 0) # Reset to default menu after no input. break
                  #else:
        
        

        #status_list= "Status choices: "
        #data_orders.data.append({"customer_name": customer_name, customer_address: "5 Church street", customer_phone: "0788804567", courier: "Penny", "status": "Awaiting Pickup"})
        #print(data_orders.data)
        #order_status = ["Preparing", "Awaiting Pickup", "Out-for-Delivery", "Delivered"]
        #for x in range(len (order_status)) :
        #  status_list += f" [{x}] {order_status [x]}, "
        #  print(status_list.rstrip(', '))  
    # Orders menu 
    #  elif main_input == 3:
    #    user_input = 0
    #while True:
    #  if user_input == 0:
    #  print_menu(orders,0)
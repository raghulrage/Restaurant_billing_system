food_list = []
ordered_list = []

class Food:
        def __init__(self,name,price):
                self.name = name
                self.price = int(price)

class Order(Food):
        def __init__(self,name,price,quantity):
                self.quantity = quantity
                self.total = quantity*price

                Food.__init__(self,name,price)
        

def main():
        while True:
                print('\n'*5)
                print(' MAIN MENU '.center(60,'*')+'\n\n\t(O)Order Food\n\t(C)View Cart\n\t(E)Exit\n'+'_'*60+'\n')
                option = input('Select an Option: ').upper()

                if option == 'O':
                        order_food()
                if option == 'C':
                        view_cart()
                if option == 'E':
                        exit_menu()
                        break
                else:
                        print('Invalid option, Enter Again!!!')

        
def load_food():
        food_items = open('files/food_list.txt','r')
        for food in sorted(food_items):
                food =  food.strip()
                if food:
                        food_list.append(Food(*food.rsplit(' ',1)))

def view_cart():
        while 1:
                print('\n'*5)
                print(' CART '.center(60,'*')+'\n')
                total = 0
                if ordered_list:
                        
                        print('\t|NO|'.ljust(5,' ')+'|FOOD NAME|'.ljust(15,' ')+'|PRICE x QUANTITY = TOTAL|'+'\n')
                        for i,food in enumerate(ordered_list):
                                total +=food.total 
                                print('\t{:<5}{:<15}{:<5}x   {:<5} =  Rs.{:<4}'.format(i+1,food.name,food.price,food.quantity,food.total))
                        print('\t'+'-'*46)
                        print('\tTotal    '+('Rs. '+str(total)).rjust(35,' '))
                        print('\n(M)Main Menu'+' '*3+'(R)Remove Item'+' '*3+'(O)Order Food'+'\n'+'(P)Payment'+' '*5+'(E)Exit')
                        print('_'*60+'\n')
                        option = input()
                        if option.upper() == 'M':
                                main()
                        elif option.upper() == 'P':
                                payment(total)
                        elif option.upper() == 'E':
                                exit_menu()
                        elif option.upper() == 'O':
                                order_food()
                        elif option.upper() == 'R':
                                remove_item()
                        else:
                                print('Invalid option, Enter Again!!!')
                        
                        
                else:
                        print('\n'+'Cart is empty'.center(60,'-'))
                        main()
        
def remove_item():
        option = int(input('\nEnter Number to Remove: '))
        if option >  len(ordered_list):
                print('Invalid Input!!!')
        else:
                item = ordered_list.pop(option-1)
                print(item.name+' Removed...')
                
def payment(total):
        if ordered_list:
                print('\nTotal amount: Rs.',total)
                print('\n'+'Payment Successful!!!\n')
        else:
                print('Cart is empty')
        main()
                
                
def order_food():
        while True:
                print('\n'*5)
                print(' ORDER FOOD '.center(60,'*'))
                print('\n'+'\t'+'|NO|'.ljust(6,' ')+'|FOOD NAME|'.ljust(20,' ')+'|PRICE|'.ljust(10,' '))
                for i,food in enumerate(food_list):
                        print('\t{:<6}{:<20}Rs. {}'.format(i+1,food.name,food.price))
                print('\n'+'(M)Main Menu'+' '*10+'(C)View Cart'+' '*10+'(E)Exit')
                print('_'*60+'\n')

                food_id = input('Select Your Option: ')
                print()
                if food_id.isdigit():
                        if 0 < int(food_id) <= len(food_list):
                                quantity = int(input('How many do you want to order : '))
                                food = food_list[int(food_id)-1]
                                for i,item in enumerate(ordered_list):
                                        if item.name == food.name:
                                                print(ordered_list)
                                                ordered_list[i].quantity+=quantity
                                                break
                                else:
                                        ordered_list.append(Order(food.name,food.price,quantity))
                        else:
                                print('Enter valid data!!!')
                                
                                        
                elif food_id.upper() == 'E':
                        exit_menu()
                elif food_id.upper() == 'C':
                        view_cart()
                elif food_id.upper() == 'M':
                        main()
                else:
                        print('Invalid option, Enter Again!!!')
def exit_menu():
        print('\n'+'THANK YOU'.center(50,'*'))
        quit()
if __name__ == '__main__':
        load_food()
        main()

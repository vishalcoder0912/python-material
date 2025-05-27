####### Project s##############
# define the menu of restaurant 
menu={
    'pizza': 40,
    'pasta':50,
    'burger':60,## we use disnorary and conditional loops to create these projects
    'salad':70,
    'coffee':80,
}

##great
print('welcome to python restaurant')
print("pizza: RS40 \npasta: RS 50\nBurger: RS 60\nSalad : RS 70\ncoffee: RS 80")
order_total=0

item_1=input('Ener the name of item you want to order =')
if item_1 in menu:
    order_total+=menu[item_1]
    print(F"your item { item_1} has been added to your order ")
else:
    print(f"Orderded item {item_1} is not available yet ")

another_order=input("Do you want order something else (yes/no)")
if another_order=='yes':
    item_2=input("Enter the name of second item= ")
    if item_2 in menu:
        order_total+=menu[item_2]
        print('item {item_2} has been added ')
    else:
        print(f"ordered item {item_2} is not available ! ")

print(f"the total amount  of items to pay is {order_total}")
# create a project where user can add number and give the name 
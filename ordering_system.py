menu = {
    1: {"name": 'espresso',
        "price": 1.99},
    2: {"name": 'coffee', 
        "price": 2.50},
    3: {"name": 'cake', 
        "price": 2.79},
    4: {"name": 'soup', 
        "price": 4.50},
    5: {"name": 'sandwich',
        "price": 4.99}
}

def calculate_subtotal(order):
    """ Calculates the subtotal of an order

    [IMPLEMENT ME] 
        1. Add up the prices of all the items in the order and return the sum

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        float = The sum of the prices of the items in the order
    """
    print('Calculating bill subtotal...')
    ### WRITE SOLUTION HERE
    total = sum(item['price'] for item in order)
    return total
    raise NotImplementedError()

def calculate_tax(subtotal):
    """ Calculates the tax of an order

    [IMPLEMENT ME] 
        1. Multiply the subtotal by 15% and return the product rounded to two decimals.

    Args:
        subtotal: the price to get the tax of

    Returns:
        float - The tax required of a given subtotal, which is 15% rounded to two decimals.
    """
    print('Calculating tax from subtotal...')
    ### WRITE SOLUTION HERE
    tax = rounded(subtotal * 0.15, 2)
    return tax
    raise NotImplementedError()

def summarize_order(order):
    """ Summarizes the order

    [IMPLEMENT ME]
        1. Calculate the total (subtotal + tax) and store it in a variable named total (rounded to two decimals)
        2. Store only the names of all the items in the order in a list called names
        3. Return names and total.

    Args:
        order: list of dicts that contain an item name and price

    Returns:
        tuple of names and total. The return statement should look like 
        
        return names, total

    """
    print_order(order)
    ### WRITE SOLUTION HERE
    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)
    total = rounded(subtotal + tax, 2)
    names = [item['name']for item in order]
    return names, total
    raise NotImplementedError()

# This function is provided for you, and will print out the items in an order
def print_order(order):
    menu = {
    1: {"name": 'espresso', "price": 1.99},
    2: {"name": 'coffee', "price": 2.50},
    3: {"name": 'cake', "price": 2.79},
    4: {"name": 'soup', "price": 4.50},
    5: {"name": 'sandwich', "price": 4.99}
}

def calculate_subtotal(order):
    total = sum(item["price"] for item in order)
    return total

def calculate_tax(subtotal):
    tax = round(subtotal * 0.15, 2)
    return tax

def summarize_order(order):
    names = [item["name"] for item in order]
    subtotal = calculate_subtotal(order)
    tax = calculate_tax(subtotal)
    total = round(subtotal + tax, 2)
    return names, total

def print_order(order):
    print('You have ordered ' + str(len(order)) + ' items')
    items = [item["name"] for item in order]
    for item in order:
        print(f'{item["name"]}: {item["price"]}')
    print()

def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order

def main():
    order = take_order()
    print_order(order)
    names, total = summarize_order(order)
    print("Names:", names)
    print("Total:", total)

if __name__ == "__main__":
    main()


# This function is provided for you, and will display the menu
def display_menu():
    print("------- Menu -------")
    for selection in menu:
        print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")
    print()

# This function is provided for you, and will create an order by prompting the user to select menu items
def take_order():
    display_menu()
    order = []
    count = 1
    for i in range(3):
        item = input('Select menu item number ' + str(count) + ' (from 1 to 5): ')
        count += 1
        order.append(menu[int(item)])
    return order

'''
Here are some sample function calls to help you test your implementations.
Feel free to change, uncomment, and add these as you wish.
'''
def main():
    order = take_order()
    print_order(order)

    # subtotal = calculate_subtotal(order)
    # print("Subtotal for the order is: " + str(subtotal))

    # tax = calculate_tax(subtotal)
    # print("Tax for the order is: " + str(tax))

    # items, subtotal = summarize_order(order)
    names, total = summarize_order(order)
    print("Names:", names)
    print("Total:", total)
if __name__ == "__main__":
    main()
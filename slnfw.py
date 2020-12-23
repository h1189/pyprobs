import sys

def read_user_input(msg, expected_input_type):
    user_input = input(msg)
    if expected_input_type == "int":
        try:
            return int(user_input)
        except ValueError:
            print('Invalid choice, Enter a valid choice....')
            read_user_input(msg, expected_input_type)
    elif expected_input_type == "float":
        try:
            return float(user_input)
        except ValueError:
            print('Invalid choice, Enter a valid choice....')
            read_user_input(msg, expected_input_type)
    elif expected_input_type == "str":
        try:
            return str(user_input)
        except ValueError:
            print('Invalid Name, Enter an valid Name...')
            read_user_input(msg, expected_input_type)
    else:
        print("Wrong input type ")
        read_user_input(msg, expected_input_type)


# check availability of raw material

def raw_material_check():
    print("#TODO implement raw material check functionality")

# Customer Needs

def customer_needs():
    type_of_materials_available = {1: 'Dimond fencing', 2: 'Barbered wire fencing', 3:'Chain link fencing', 4: 'Iron Poles'}
    print(f'Available Product types are {type_of_materials_available}')
    choice = read_user_input('Select the product needed:', "int")
    if choice in type_of_materials_available:
        print(f'You have selected {type_of_materials_available[choice]}')
    else:
        print('Choice not found. Please select an valid choice')
        customer_needs()
    qty_msg = "Mention Qunatity of " + type_of_materials_available[choice] + " needed in KG's : "
    quantity = read_user_input(qty_msg, "float")
    print(f"Make an order of {quantity} KG's of {type_of_materials_available[choice]} and \n Process the Order")



# Customer Details

def customer_details():
        name_of_customer = read_user_input('Enter Name of the customer: ','str')
        contact_number = read_user_input('Enter the contact number: ','int')
        customer_address = read_user_input('Address of the customer: ','str')

def init():
    raw_material_check()
    customer_needs()
    customer_details()

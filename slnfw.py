# check availability of raw material
global ava
def raw_material_check():
    try:
        ava = int(input('is RAW MATERIAL available ? '))
        while ava == 1:
            print('RAW MATERIAL AVAILABLE \n Ready to take orders..') 
            break
        else:
            print('OUT OF RAW MATERIAL..\n Place an order')
    except ValueError:
        print('Invalid choice, Enter a valid choice....')
    
raw_material_check()
 
# Customer Needs
def customer_needs():
        type_of_materials_available = {1: 'Dimond fencing', 2: 'Barbered wire fencing', 3:'Chain link fencing', 4: 'Iron Poles'}
        print(f'Available Product types are {type_of_materials_available}')
        try:
            choice = int(input('Select the product needed:'))
            for key in type_of_materials_available:
                if key == choice:
                    print(f'You have selected {type_of_materials_available[key]}')
                    break
        except ValueError:
            print('Invalid choice, Please select valid choice..')
        try:
            quantity = float(input(f"Mention Qunatity of {type_of_materials_available[key]} needed in KG's : "))
            print(f"Make an order of {quantity} KG's of {type_of_materials_available[key]} and \n Process the Order")
        except ValueError:
            print("You have mentioned wrong data...Please mention the quantity in KG's ")


customer_needs()

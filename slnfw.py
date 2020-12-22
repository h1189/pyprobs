# check availability of raw material
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
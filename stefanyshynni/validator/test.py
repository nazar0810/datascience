from stefanyshynni.validator.lib import name_validator, brand_validator, sizes_validator, merchants_validator
from stefanyshynni.dataset_structure import dataset

#brand_value = 'Vans'
#name = 'Vans'
#sizes = '40, 41, 42'
#merchants = 'Ebay.com'


def get_brand():
    brand_value = input('Brand:')
    if brand_validator(brand_value):
        print("Brand list correct")
        return brand_value
    else:
        print('Invalid brand list, try again')
        return get_brand()


def get_name():
    name = input('Name:')
    if name_validator(name):
        print("Name list correct")
        return name
    else:
        print('Invalid name list, try again')
        return get_name()



def get_sizes():
    sizes = input('Sizes:')
    if sizes_validator(sizes):
        print("Sizes list correct")
        return sizes
    else:
        print('Invalid sizes list, try again')
        return get_sizes()


def get_merchants():
    merchants = input('Merchants:')
    if merchants_validator(merchants):
        print("Merchants list correct")
        return merchants
    else:
        print("Invalid merchants list, try again")
        return get_merchants()


brand_value = get_brand()
name = get_name()
sizes = get_sizes()
merchants = get_merchants()


dataset["brand"][brand_value] = {'name': name, 'sizes': sizes, 'merchants': merchants}
print(dataset)
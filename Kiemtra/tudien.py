dictCar = {
    "brand": "Honda",
    "model": "Honda Civic",
    "year": 1972
}
dict1 = dictCar # su dung toan tu =
dict2 = dictCar.copy() # su dung ham copy()
dictCar["color"] = "yellow" # thay doi dictCar
list = []
list.append(dict1)
list.append(dict2)
print(list)
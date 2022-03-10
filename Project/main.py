
from LinkedList import LinkedList
from restaurantData import types, restaurant_data
import helper_functions as hf


#Restaurant Types:
german = LinkedList()
japanese = LinkedList()
vegetarian = LinkedList()
french = LinkedList()
african = LinkedList()
american = LinkedList()
barbecue = LinkedList()
czech = LinkedList()
chinese = LinkedList()
thai = LinkedList()
mexican = LinkedList()
indian = LinkedList()
cafe = LinkedList()
pizza = LinkedList() 
italian = LinkedList()

#Restaurant Informations:
for data in restaurant_data:
    type_data = data[0]
    if type_data == "german":
        german.insert(data[1],data[2],data[3],data[4])
    elif type_data == "japanese":
        japanese.insert(data[1],data[2],data[3],data[4])
    elif type_data == "vegetarian":
        vegetarian.insert(data[1],data[2],data[3],data[4])
    elif type_data == "french":
        french.insert(data[1],data[2],data[3],data[4])
    elif type_data == "african":
        african.insert(data[1],data[2],data[3],data[4])
    elif type_data == "american":
        american.insert(data[1],data[2],data[3],data[4])
    elif type_data == "barbecue":
        barbecue.insert(data[1],data[2],data[3],data[4])
    elif type_data == "czech":
        czech.insert(data[1],data[2],data[3],data[4])
    elif type_data == "chinese":
        chinese.insert(data[1],data[2],data[3],data[4])
    elif type_data == "thai":
        thai.insert(data[1],data[2],data[3],data[4])
    elif type_data == "mexican":
        mexican.insert(data[1],data[2],data[3],data[4])
    elif type_data == "indian":
        indian.insert(data[1],data[2],data[3],data[4])
    elif type_data == "cafe":
        cafe.insert(data[1],data[2],data[3],data[4])
    elif type_data == "pizza":
        pizza.insert(data[1],data[2],data[3],data[4])
    elif type_data == "italian":
        italian.insert(data[1],data[2],data[3],data[4])

hf.hello()
hf.ask_question()
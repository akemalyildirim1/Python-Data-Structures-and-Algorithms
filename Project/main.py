
from LinkedList import LinkedList
from restaurantData import types, restaurant_data
import helper_functions as hf


"""
chi = LinkedList("Dragon's Tail","1/5","4/5","8 Jasmine Rd")
print(chi.stringify_list())
chi.insert("Super Wonton Express", "2/5", "1/5", "223 Milliways Ave")
chi.insert("Shandong Lu", "4/5", "3/5", "335 University")
print(chi.stringify_list())
"""
"""
ger=LinkedList()
#ger = LinkedList("a","1/5","4/5","8 Jasmine Rd")
ger.insert("a", "2/5", "1/5", "223 Milliways Ave")
print("")
print(ger.stringify_list())
ger.insert("b", "2/5", "1/5", "223 Milliways Ave")
print("")
print(ger.stringify_list())
ger.insert("c", "2/5", "1/5", "223 Milliways Ave")
print("")
print(ger.stringify_list())
ger.insert("d", "2/5", "1/5", "223 Milliways Ave")
print("")
print(ger.stringify_list())
ger.insert("e", "2/5", "1/5", "223 Milliways Ave")
print("")
print(ger.stringify_list())
ger.insert("f", "2/5", "1/5", "223 Milliways Ave")
print("")
print(ger.stringify_list())
ger.insert("g", "2/5", "1/5", "223 Milliways Ave")
print("")
print(ger.stringify_list())
"""

hf.hello()
hf.ask_question()

#Restaurant Types:
german = LinkedList()
japanese= LinkedList()
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

print(types)
hf.quicksort(types,0,len(types)-1)
print(types)
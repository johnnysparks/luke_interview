'''Question 1: Design a function in Python for creating a
 lookup table from a collection of objects.  Your function
  will take a list of objects (of a particular type) and 
  the name of a property to use as the primary key for the 
  lookup.  The result should be a hash table that can be used 
  to lookup objects by values of that property.  The lookup 
  table should only store references to the objects and avoid 
  copying the source data.
'''



'''
ASSUMPTIONS: 
	- original objects' values will not change, and thus
	need to be reflected in the hash table?
	- objects may have any unknown amount/type of
arguements? "Of a particular type" type doesn't really
describe what assumptions I should have. *args **kwargs ?


Confusion...you specify using 'a property to use as the primary key'
but then go on to say that this should be a hash table.


What is the hash to be made out of? Random? Combination
of object's attributes?


Need to not copy, need to be reference
'''


import sys

# Test Object
class Obj:
    prop_a = None
    prop_b = None
        
    def __init__(self, prop_a=None, prop_b=None):
        self.prop_a = prop_a
        self.prop_b = prop_b

    @property
    def prop_c(self):
        return self.prop_a

# Test Object List
objs =  []
for i in range(0, 1000):
    objs.append(Obj(i % 10, 'b{}'.format(i)))


# Requirement setup: Validate baseline reference count
assert sys.getrefcount(objs[2]) == 2, "objs[2] should have a baseline reference count of 2 before creating lookup tables"


"""
**************
* Assignment *
**************

Function returning a lookup table dictonary, where the input object values for a given property are the key

param objects:  array of arbitrary objects
param property_name: String name of the property whose values will become the primary key
"""
def object_lookup_table(objects=[], property_name=None):
    assert isinstance(objects, list), "`objects` param must be a list of objects"
    assert isinstance(property_name, str), "`property_name` param must be a string"
    assert len(property_name.strip()), "`property_name` may not be an empty or whitespace-only string"

    table = {}

    for obj in objects:

        val = None
        matches = []

        try:
            val = getattr(obj, property_name)
        except:
            print('No property name {} for object {}, skipping.'.format(property_name, obj))
            continue

        try:
            matches = table[val]
        except:
            pass

        matches.append(obj)
        table[val] = matches
        

    return table


#########################
# Validate Requirements #
#########################


"""
Requirement: Object are referenced and don't have values copied.
"""
prop_a_table = object_lookup_table(objs, 'prop_a')
prop_b_table = object_lookup_table(objs, 'prop_b')
prop_c_table = object_lookup_table(objs, 'prop_c')

assert objs[2] == prop_b_table['b2'][0], "Objects stored in the lookup table are the same as the input list."

assert sys.getrefcount(objs[2]) == 5, "objs[2] is not copied, but referenced again for each lookup table."

"""
Requirement: (Mine) Since there's no requirement for uniqueness, all matching objects whose value is looked-up should be returned.
"""
all_prop_a_lookup_objects = [obj for prop_a_objects in prop_a_table.values() for obj in prop_a_objects]
all_prop_b_lookup_objects = [obj for prop_b_objects in prop_b_table.values() for obj in prop_b_objects]
assert len(objs) == len(all_prop_a_lookup_objects), "No values left unindexed for 'prop_a'"
assert len(objs) == len(all_prop_b_lookup_objects), "No values left unindexed for 'prop_b'"


prop_a_value = 6
for obj in prop_a_table[prop_a_value]:
    assert obj.prop_a == prop_a_value, "All returned objects should match the primary key value"


prop_c_value = 6
for obj in prop_c_table[prop_c_value]:
    assert obj.prop_c == prop_c_value, "All returned objects should match the primary key value, works for dynamic properties"


print("No assertion falues, object_lookup_table meets assignment requirements")


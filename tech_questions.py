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


# pretty print
from pprint import pprint
import hashlib





class particular_type_of_object:
	def __init__(self, hostname, ip, os, backup_enabled, hash_value):
		'''hash_value = which value should determine the hash, 'ip', 'hostname',
		'etc' '''
		self.hostname = hostname
		self.ip = ip
		self.os = os
		self.backup_enabled = backup_enabled
		# they never specified what the hash was to be made from
		self.values = {'ip':self.ip,
						'hostname':self.hostname,
						'os':self.os,
						'backup_enabled':self.backup_enabled}
		self.hash = hashlib.sha256( self.values[hash_value] ).hexdigest()
		self.values['hash'] = self.hash



class lookup_table:
	def __init__(self, objs, primary_key='hostname'):
		'''A lookup table object that can utilized with
		object.get(value) to return the object's specific
		value of the originally specified primary_key variable.

		Default primary_key is 'hostname'''
		self.table = {}
		self.objs = objs
		self.primary_key = primary_key

		for obj in objs:
			self.table[ obj.values['hash'] ] = obj

	def return_lookup_table():
		'''Returns entire lookup table'''
		return table.table

	def return_objects_with_key_value_of(self, key_value):
		'''Return all objects whose self.table[primary_key] == key_value'''

		#print('self.table = ')
		#pprint(self.table)
		#print('\n\ntable.objs = ')
		#pprint(self.objs)



		'''Do they want return format:
		{'b434f5cc09fa4f243f7d615126edbc5a5e619efe0f279608480164345fb4a3fa':
				{'backup_enabled': False,
				  'hash': 'b434f5cc09fa4f243f7d615126edbc5a5e619efe0f279608480164345fb4a3fa',
				  'hostname': 'server05',
				  'ip': '10.0.1.47/32',
				  'os': 'Windows'}
		}
  		'''
		return [ self.table[obj].values for obj in self.table if self.table[obj].values[self.primary_key] == key_value ]
		'''...or do they want return format of:
		{'backup_enabled': False,
		  'hash': 'b434f5cc09fa4f243f7d615126edbc5a5e619efe0f279608480164345fb4a3fa',
		  'hostname': 'server05',
		  'ip': '10.0.1.47/32',
		  'os': 'Windows'}
		'''



def debug():
	print('\n\n\n***Debug Mode***')
	x = ''
	while x != 'exit':
		x = raw_input('>>> ')
		exec( x )


def main():
	dummy_data = [
    {
        "hostname": "server02",
        "ip_address": "10.0.1.25/24",
        "operating_system": "Windows XP",
        "backup_enabled": True
    },
    {
        "hostname": "server03",
        "ip_address": "10.1.1.3/24",
        "operating_system": "Windows",
        "backup_enabled": False
    },
    {
        "hostname": "server04",
        "ip_address": "10.0.1.99/24",
        "operating_system": "Ubuntu",
        "backup_enabled": True
    },
    {
        "hostname": "server05",
        "ip_address": "10.0.1.47/32",
        "operating_system": "Windows",
        "backup_enabled": False
    }
	]


	# since we can't copy the data, we need to convert it to objects
	# so we can reference it straight from the source
	collection_of_objects = [ particular_type_of_object(
								computer['hostname'],
								computer['ip_address'],
								computer['operating_system'],
								computer['backup_enabled'],
								'hostname') for computer in dummy_data ]




	lookup_table_primary_key_value = "Windows"
	# create our lookup table with primary key of "os"
	table = lookup_table(collection_of_objects, primary_key="os")


	print('\n\n\nAll objects in lookup table with specified primary_key (os) value of "%s" :\n' % lookup_table_primary_key_value)
	pprint( table.return_objects_with_key_value_of('Windows') )


	print('\n\n\nEntire hash lookup table:')
	pprint( table.table )

	print('\n\n\nReturn specific lookup table object via hash:')
	pprint( table.table['705f7b2c9e423730f69f9aaef2e7281f2b584d8ce0d60a833d7969a9ddf30d2b'])

	print('\n\n\nReturn specific lookup table objects\' dictionary contents (obj.values):')
	pprint( table.table['705f7b2c9e423730f69f9aaef2e7281f2b584d8ce0d60a833d7969a9ddf30d2b'].values)




	#debug()







if __name__ == '__main__':
	main()

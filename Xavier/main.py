import json

fname = input('first name ')
lname = input('last name ')
age = int(input('age '))

class Persona:
	def __init__(self, first_name: str, last_name: str, age: int):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def as_dict(self):
		return {
			'first_name': self.first_name,
			'last_name': self.last_name,
			'age': self.age
		}

persona = Persona(fname, lname, age)
persona = persona.as_dict()

try:
	with open('persona.%s.%s.json' % (persona['first_name'], persona['last_name']), 'w+', encoding='utf-8') as out:
		out.write(json.dumps(persona))

except IOError as e:
	print(e)

print(persona['first_name'])

persona_and_str = [persona, 'ferreira da o rabo']

print(persona_and_str[0])

t_tuple = (1, 3)

print(t_tuple)
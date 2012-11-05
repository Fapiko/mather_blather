import re

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

#2(x+3) + 5
#2x+6 + 5
#2x+11
def simplify(function):
	originalFunction = function
	function = function.replace(' ', '')
	step = distribute(function)

	return step

def distribute(function):
	# Given 2(x+3)
	# Match 0 - Full distribution object - 2(x+3)
	# Match 1 - Amount to distribute - 2
	# Match 2 - Distribution - x+3
	distributions = re.findall('((\d)\((.*?)\))', function)

	for index, distribution in enumerate(distributions):

		chunks = splitOnOperators(distribution[2])
		coefficientCheck = False
		operating = False
		replacement = ''
		for item in chunks:

			if operating is False or coefficientCheck:
				if is_number(item):
					item = float(item) * float(distribution[1])
					coefficientCheck = True
				elif re.match('[+-/*]', item):
					operating = False

				else:
					if coefficientCheck:
						coefficientCheck = False
					else:
						item = distribution[1] + item

					operating = True

			else:
				operating = False

			replacement += str(item)

		function = str.replace(function, distribution[0], replacement)

	return function

def splitOnOperators(function):
	values = re.findall('[\d]+|[a-z]+|[+-/*]', function)
	return values
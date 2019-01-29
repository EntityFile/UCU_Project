def read_file(file):
	f = open(file,encoding = 'utf-8')
	lines = f.read()
	f.close()
	return lines.split('\n')


def write_file(thing,file):
	f = open(file,'w',encoding = 'utf-8')
	for el in thing:
		f.write(el)
		f.write('\n')
	f.close()


def alo(lines):
	final_list = []
	for el_ind in range(len(lines[0])):
		lst = []
		space_count = 0
		for i in range(len(lines)):
			if not lines[i][el_ind] in lst:
				if not lines[i][el_ind] in ['a','o','i','e','u']:
					if not lines[i][el_ind] == ' ':
						lst.append(lines[i][el_ind])
		lst = sorted(lst)
		if not len(lst) == len(lines):
			for k in range(len(lines)-len(lst)):
				lst.append(' ')
		final_list.extend(lst)
	return final_list
#final_list = alo(['dangerous', 'to add to', 'manytodoc'])


def print_final_list(final_list,lines):	
	for o in range(len(lines)):
		for eil in range(0,len(final_list),len(lines)):
			print(final_list[eil+o],end = '')
		print()


def find(lines):
	letter_list = ['a','o','i','e','u']
	final_list = []
	for el in lines:
		line = ''
		for i in range(len(el)):
			if el[i] in letter_list:
				line += el[i]
		final_list.append(line)
	return(final_list)


lines = ['dangerous', 'to add to', 'manytodoc']
lst = find(lines)
for i in range(len(lines)):
	print(lines[i],end = '')
	print(lst[i])
print_final_list(alo(lines),lines)
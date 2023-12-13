
master_map = []
grand_total = 0

with open("paul.txt") as f:
	for line in f:
		line = line.strip()
		if line == "":
			line = "delimiter"
		master_map.append(line)


# for x in master_map:
# 	print(x)

def print_map(mymap):
	print()
	for x in mymap:
		print(x)
	print()


def transpose_list_of_strings(mylist):
	temp = []


	# print("transpose map")
	# print_map(mylist)
	

	for x in range(len(mylist[0])):
		mystring = ""
		for row in mylist:
			mystring += row[x]

		temp.append(mystring)

	# print("transposed map")
	# print_map(temp)

	return temp


def horizontal_reflection(mymap):
	# mymap is list of strings
	# keep list of indices where a line is equal to line below/above
	retval = 0
	temp = ""
	mymap_index = 0
	possible_reflection_points = []
	for line in mymap:
		if mymap_index > 0:
			temp = mymap[mymap_index-1]
			if line == temp:
				possible_reflection_points.append(mymap_index)
		mymap_index += 1

	#print(possible_reflection_points)

	bottom_limit = len(mymap)


	for x in possible_reflection_points:
		not_done = True
		upper_index = x - 1
		lower_index = x
		is_reflection = True
		while not_done:
			is_reflection = (mymap[upper_index] == mymap[lower_index]) and is_reflection

			# print("upper index",mymap[upper_index])
			# print("lower index",mymap[lower_index])
			# print("is reflection",is_reflection)

			if lower_index == bottom_limit - 1 or upper_index == 0:
				not_done = False
			upper_index -= 1
			lower_index += 1

		if is_reflection:
			retval = x

	return retval

	


# get current input - will need to keep track of index of list

master_map_index = 0
not_done = True
map_counter = 0


while not_done:  # process all maps

	map_counter += 1

	current_map_index = 0
	current_map = []
	current_map_not_done = True

	#print("in big loop")

	while current_map_not_done:

		# print("current map index",current_map_index)
		# print("master map index", master_map_index)

		if master_map_index < len(master_map) and master_map[master_map_index] != "delimiter":
			current_map.append(master_map[master_map_index])
		else:
			current_map_not_done = False
			
		master_map_index += 1
		current_map_index += 1

		if master_map_index == len(master_map):
			not_done = False

	# should have one map here

	vertical_reflection_index = 0
	horizontal_reflection_index = horizontal_reflection(current_map)

	if horizontal_reflection_index == 0:
		current_map = transpose_list_of_strings(current_map)
	
		vertical_reflection_index = horizontal_reflection(current_map)

	grand_total += vertical_reflection_index + 100 * horizontal_reflection_index

	# print("subtotal",grand_total)

	

	# print("\nmap number",map_counter)
	# print()
	# for x in current_map:
	# 	print(x)
	# print()
	# print("horizontal_reflection_index",horizontal_reflection_index)
	# print("vertical_reflection_index",vertical_reflection_index)
	# print()

	#vertical_reflection_index = 0


	# master_map_index < len(master_map) and 

	# if master_map_index >= len(master_map):
	# 	not_done = False

print("\ngrand total",grand_total)
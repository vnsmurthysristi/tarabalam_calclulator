import argparse

def nakstra_details_to_lst(people_count,nakstra_details):
	nakstra_lst = []
	nakstra_lst = list(nakstra_details.split(","))
	return nakstra_lst

def calculate_tarabalam(nakstra_num):
	n = int(nakstra_num)%9
	temp_lst = []
	#temp_lst.append((n+0)%9)
	#temp_lst.append((n+1)%9)
	temp_lst.append((n+2)%9)
	temp_lst.append((n+4)%9)
	temp_lst.append((n+6)%9)
	temp_lst.append((n+8)%9)
	temp_lst.append((n+9)%9)
	return temp_lst





def extract_duplcates(lst,people_count):
	dups = [x for x in lst if lst.count(x) >= people_count]
	dup_free  = list(set(dups))
	for i in range(len(dup_free)):
		if dup_free[i] ==0:
			dup_free[i]=dup_free[i]+9
	ret_lst = []
	for i in range(len(dup_free)):
		ret_lst.append(dup_free[i])
		ret_lst.append(dup_free[i]+9)
		ret_lst.append(dup_free[i]+18)
	print(dup_free)
	ret_lst.sort()
	print(ret_lst)

	


my_parser = argparse.ArgumentParser(allow_abbrev=False)
my_parser.add_argument('-n', action='store', type=str, required=True)
my_parser.add_argument('-d', action='store', type=str, required=True)

args = my_parser.parse_args()

people_count = int(args.n)
nakstra_details = args.d
nakstra_list = []
temp_tarabalam_list = []
final_tarabalam_list = []

nakstra_list = nakstra_details_to_lst(people_count,nakstra_details)

for i in range(people_count):
	temp_list = []
	temp_list = calculate_tarabalam(int(nakstra_list[i])-1)
	print('temp_list',temp_list)
	temp_tarabalam_list.extend(temp_list)
	temp_list.clear()

#print(temp_tarabalam_list)
#final_tarabalam_list = extract_duplcates(temp_tarabalam_list)
#print(final_tarabalam_list)
print('final')
extract_duplcates(temp_tarabalam_list,int(people_count))

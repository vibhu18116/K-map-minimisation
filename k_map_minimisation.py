# CSE 101 - IP HW2
# K-Map Minimization 
# Name: Vibhu Agrawal
# Roll Number: 2018116
# Section: A
# Group: 4
# Date: 15/10/2018


def matrix_fill(var_no,minterm_on):
	"""Generates two lists: one with minterms with value 1 and other with don't care terms.
		The no of bits in the binary of number is same as the number of variables."""

	min_1,d,min_d=minterm_on.split()		#min_1 contains the terms whose value is 1
											#d contains letter d  #to be discarded
											#min_d contains the don't care terms
	#print(len(min_1))
	if min_1=="()":
		return 0
	
	min_1=min_1.replace("(",'').replace(")",'')
	min_d=min_d.replace("(",'').replace(")",'')

	min_1=min_1.split(",")					#min_1 is a list
	min_d=min_d.split(",")					#min_d is a list

	#print(len(min_1))
	

	for i in range (len(min_1)):			#typecasting each element of min_1 to int
		min_1[i]=int(min_1[i])


	if min_d[0]=='-':
		min_d=[]

	else:
		for i in range (len(min_d)):		#typecasting each element of min_d to int
			min_d[i]=int(min_d[i])


	min_1bin=[]								#contains binary of the elements in string format
	for i in range (len(min_1)):
		min_1bin.append((str(bin(min_1[i])))[2:])


	min_dbin=[]
	if len(min_d)!=0:
		for i in range (len(min_d)):
			min_dbin.append((str(bin(min_d[i])))[2:])


	#Making the binary have same number of bits as the number of variables.

	min_1_binbits=[]							#contains proper no of bits.
	for element in min_1bin:
		while len(element)!= var_no:
			element='0'+element
		min_1_binbits.append(element)

	
	min_d_binbits=[]							#contains proper no of bits.
	if len(min_d)!=0:
		for element in min_dbin:
			while len(element)!= var_no:
				element='0'+element
			min_d_binbits.append(element)

	return min_1_binbits, min_d_binbits
	#two lists with elements as str are returned


def grouping(min_1_binbits,min_d_binbits=[]):
	"""Returns 5 lists containing binary of minterms on the basis of number of ones."""
	no_1s_0=[]
	no_1s_1=[]
	no_1s_2=[]
	no_1s_3=[]
	no_1s_4=[]

	for element in min_1_binbits:
		a=element.count("1")
		if a==0:
			no_1s_0.append(element)

		elif a==1:
			no_1s_1.append(element)

		elif a==2:
			no_1s_2.append(element)

		elif a==3:
			no_1s_3.append(element)

		elif a==4:
			no_1s_4.append(element)


	for element in min_d_binbits:
		a=element.count("1")
		if a==0:
			no_1s_0.append(element)

		elif a==1:
			no_1s_1.append(element)

		elif a==2:
			no_1s_2.append(element)

		elif a==3:
			no_1s_3.append(element)

		elif a==4:
			no_1s_4.append(element)

	return(no_1s_0, no_1s_1, no_1s_2, no_1s_3, no_1s_4)

def dashing(grouped_List):
	"""grouped_List is consists of groups on the basis of no of 1s.
	 It returns a single list consisting of -s, 0s and 1s 
	 (one function call returns one level of grouping)"""

	rlist=[]

	for i in range(len(grouped_List)-1):			#i is list consisting of binaries
		for j in grouped_List[i]:					#j is the binary element of first group
			#if int(j)==0:
			p = []									#p stores the indices of 1 in j
			v=[]									#v stores indices of '-'es.
			for k in range (len(j)):
				if j[k]=='1':
					p.append(k)
				if j[k]=="-":
					v.append(k)
			# print("i", i)
			# print("p", p)
			# print()
			
			for x in grouped_List[i+1]:				#x is element of next group
				flag=0								#checks if x has 1s at same position as j
				flag2=0								#if j has dash, checks if the position of - is same in x
				if len(v)!=0:
					for r in v:
						if x[r]!="-":
							flag2=1						

					if flag2!=1:
						for y in p:
							if x[y]!='1':
								flag=1
						if flag == 0:							#appending the '-'ed element if the previous checks are successful
							for q in range (len(x)):
								if x[q]=='1' and q not in p:
									temp = x[:q] + "-" + x[q+1:]
									if temp not in rlist:
										rlist.append(temp)
				else:
					for y in p:
							# print("y", y)
							if x[y]!='1':
								flag=1
					if flag == 0:							#appending the '-'ed element if j is non-dashed and position of 1s match
						for q in range (len(x)):
							if x[q]=='1' and q not in p:
								temp = x[:q] + "-" + x[q+1:]
								if temp not in rlist:
									rlist.append(temp)

	return grouping(rlist)

def removeEmpty(tup):
	"""removes empty lists from tup which can be a tuple or a list"""
	tup=list(tup)
	tup.sort()
	i=0
	while len(tup)!=0 and len(tup[i])==0:
		tup.pop(i)
	return(tup)


def dash_list(tuple_all_comb, num):
	"""returns a list of elements grouped on the basis of number of 1s"""
	p=[]
	j=[]
	for e in tuple_all_comb:
		if e[0].count("-") == num:
			p.append(e)
	#print("p_dash", p)
	for k in p:
		j.extend(k)
	#print("new_j", j)
	return(j)

def track(g, inp_list):
	"""forms combinations of the minterms used to create a particular -ed element"""				
	
	final_headers=[]				#ultimate saviour
	var_no = len(inp_list[0])
	counter = 0
	for element in g:
		for i in element:
			y = i.count("-")
			if y > counter:
				counter = y
	#print("counter", counter)
	if counter == var_no:
		return 1					#if there is a element containing same no of dashes as the no of variables, return 1, the final answer

	for i in range (1, var_no):
		found_input=[]
		q = dash_list(g, var_no-i)
		#print ("hey",q)

		if len(q)==0:						#if no -es corresponding to present i, move to initial loop
			if var_no-i == 1:				#if no combinations formed at all, return original
				ls=[]
				for e in inp_list:
					ls.append([e])

				return(ls)
			
			continue

		else:
			new_bin=[]								#contains 2^(var_no - i) elements to replace -es
			for d in range (2**(var_no-i)):
				binary=str(bin(d))
				binary=binary[2:]
				
				while len(binary)!= (var_no-i):
					binary ='0'+binary
					
				new_bin.append(binary)
			
			group_element=[]						#contains binary of the group used to form a particular dashed element.#the first element is the dashed element processed.
			for m in range (len(q)):				#creates appropriate number of empty lists in group_element
				group_element.append([])
			k=0
			for j in q:								#j is the dashed element
				group_element[k].append(j)
				for el in new_bin:					#el is the first binary to replace dashes
					s=j
					for sth in el:					#sth is bit of el
						pq = s.find("-")
						s = s[:pq]+sth+j[pq+1:]
					group_element[k].append(s)		# appending in k(th) list.
				k = k+1
				
			#print("group_element", group_element)
			
			
			for inp in inp_list:					#checks if a given input is in present groups. if yes, store the group, else proceed to next level of grouping.
				for fide in group_element:
					for tide in fide:
						if inp == tide:
							if fide not in final_headers:
								final_headers.append(fide)
							if inp not in found_input:
								found_input.append(inp)

			for ele in found_input:					#if input has been included in a group, remove it from input list
				inp_list.remove(ele)

			if len(inp_list)==0:
				return(final_headers)

	if len(inp_list)!=0:
		grep=[]
		for graph in inp_list:
			graph=[graph]
			grep.append(graph)

		return(final_headers+grep)

###########################################################################################################

def matrix_prepare(track_result, inp_list):
	"""The initial chart of petricks method is created"""
	#print("track_result", track_result)
	mat=[["minterms/groups"]]
	mat[0].extend(inp_list)
	for i in range (len(track_result)):				#creating the required no. of rows.
		mat.append([])
		for j in inp_list:
			mat[i+1].append("0")
		mat[i+1].insert(0,track_result[i][0])		#chart without crosses (or 'x') created

	for e in range(len(track_result)):								#e is the index of a list containing -ed element and those which constitute it
		s=track_result[e][0]										#s is the dashed element
		if s.count("-") != 0:
			for t in range (1,len(track_result[e])):				#t is index of element contributing a dashed element
				v=track_result[e][t]								#v is the element
				for d in range (1,len(mat[0])):						#d is index of the on minterms
					if mat[0][d]==v:
						mat[e+1][d]="x"

		else:
			for d in range (1,len(mat[0])):						#d is index of the on minterms
					if mat[0][d]==s:
						mat[e+1][d]="x"

	#chart prepared till here

	return mat

def chart_process_epi(matrix):
	"""Returns epis in the function"""
	ls_prob_final=[]								#stores final minterms which will be included in ans
	for j in range(1,len(matrix[0])):				#j is used to iterate over columns
		count=0
		for i in range(1,len(matrix)):				#i is used to iterate over rows
			for e in matrix[i][j]:					#e is element at coordinate (i,j)
				if e == "x":
					count += 1
					s = matrix[i][0]
					cat = i 						#cat is index of the row which has individual x

		if count == 1:
			if s not in ls_prob_final:
				ls_prob_final.append(s)

			for du in range(1,len(matrix[cat])):	#0ing all the other elements of that row and required columns
				if matrix[cat][du] == "x":			#(cat,du) is the coordinate of x in the cat row
					for df in range(1,len(matrix)):
						matrix[df][du]="0"

	#essential prime implicants sorted out
	return (ls_prob_final, matrix)

def chart_process_pi(matrix, ls_prob_final):
	"""returns the pis and finally all the minterms to be included in the answer"""
	flag = 0
	for row in matrix:
		for col in row:
			if col=="x":
				flag=1

	if flag == 0:
		return(ls_prob_final)

	maxcount=0
	for i in range(1,len(matrix)):				#i is the index of row
		count=0
		for j in range (1,len(matrix[i])):		#j is the index of column in i(th) row
			if matrix[i][j]=="x":
				count=count+1
				#print("count", count)
		if count > maxcount:
		#print("hello")
			maxcount = count
			s=i

	#print("s",s)
	if matrix[s][0] not in ls_prob_final:
		ls_prob_final.append(matrix[s][0])

	for du in range(1,len(matrix[s])):	
		if matrix[s][du] == "x":			
			for df in range(1,len(matrix)):
				matrix[df][du]="0"

	#print("ls_prob_final", ls_prob_final)
	return(chart_process_pi(matrix, ls_prob_final))

def result1(h):
	h.sort(reverse=True)
	var_no=len(h[0][0])
	var=["w", "x", "y", "z"]
	ans=""
	
	for element in h:
		k=0
		temp=[]
		for s in element:
			if s=="1":
				temp.append(var[k])
			elif s=="0":
				temp.append(var[k]+"'")
			k=k+1
		tm=""
		for g in temp:
			tm=tm+g

		ans=ans+tm+" + "

	return(ans[:-3])


def minFunc(numVar, stringIn):
	"""
		This python function takes function of maximum of 4 variables
		as input and gives the corresponding minimized function(s)
		as the output (minimized using the K-Map methodology),
		considering the case of Don’t Care conditions.

	Input is a string of the format (a0,a1,a2, ...,an) d (d0,d1, ...,dm). 
	If there are no don't care terms, d is followed by a space and a hyphen.
	Output is a string representing the simplified Boolean Expression in
	SOP form.

	"""
	
	a = matrix_fill(numVar,stringIn)

	if a==0:
		return "0"			#final result
		
	b = grouping(a[0],a[1])
	c = dashing(b)			#level 1 grouping
	d = dashing(c)			#level 2 grouping
	e = dashing(d)			#level 3 grouping
	f = dashing(e)			#level 4 grouping

	b=removeEmpty(b)
	c=removeEmpty(c)
	d=removeEmpty(d)
	e=removeEmpty(e)
	f=removeEmpty(f)

	g = c+d+e+f

	h = track(g,a[0]+a[1])
	if h==1:
		return "1"				#final result

	i=matrix_prepare(h, a[0])
	j=chart_process_epi(i)
	k=chart_process_pi(j[1], j[0])

	stringOut=result1(k)		#final result
	
	return stringOut


if __name__ == "__main__":
	print(minFunc(3,"(3,4,7) d (1,2,5,6)"))
	print(minFunc(3,"(2,5) d (0,4,6)"))
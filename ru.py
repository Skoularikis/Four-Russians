import sys
import csv
import pprint

Aarrays = []
AA = []
A = []
Barrays = []
B = []
T = []
Nodes = []
rs = []
q = 1
i = 0

#if 2 files input
if len(sys.argv)==3:
	input_file_1 = sys.argv[1]
	input_file_2 = sys.argv[2]
	n = 0

	with open(input_file_1, "r") as file1:
		for line in file1:
			Aarrays.append(line.strip().split(","))
			n = n + 1
	#print(Aarrays[1])
			
	with open(input_file_2) as file2:
		for line in file2:
			Barrays.append(line.strip().split(","))
	#print(Barrays[1])

	#calculate m=lgn
	m = -1
	k = 0
	while 2*k<=n:
		m = m + 1
		k = 2**m
		#print(m)
		#print(k)
	if (2*k-n)<(n-k):
		m=m+1
	print(n)
	print(m)

	#split Array Aarrays in A1, A2...
	x = []
	i = 0
	y = 0
	e = 0
	c = 0
	z=((int(n/m))*m)
	print(z)
	
	for Aarray in Aarrays:
		while e < ((int(n/m))*m):
			i = 0
			while i < m:
				x.append(Aarray[e+i])
				#print(e+i)
				i = i + 1
			AA.extend([x])
			A.append(AA)
			x = []
			e = e + m 
	#print(AA)
	q = n - ((int(n/m))*m)
	r = []
	if q!=0:
		for Aarray in Aarrays:
			y = 0 
			i = 0
			while y < q:
				r.append(Aarray[e+y])
				y = y + 1 
			while i < m-q:
				r.append("0")
				#print(x)
				i = i + 1
			#print(r)
			AA.extend([r])
			A.append(AA)
			r = []		
	#print(A[3])

	#split Array Barrays in B1, B2...
	w = []
	y = 0
	z = 0
	while z < ((int(n/m))*m):
		i = 0
		while i < m:
			w.append(Barrays[z+i])
			#print(w)
			i = i + 1
		#print(w)
		B.extend([w])
		w = []
		z = z + m 
	#print(B)
	q = n - ((int(n/m))*m)
	#print(q)
	t = []
	y = 0
	p = []
	if q!=0:
		g = 0 
		i = 0
		while g < q:
			r.append(Barrays[z+g])
			g = g + 1 
		while i < m-q:
			l = 0
			while l < n:
				p.append("0")
				l = l + 1
			#print(p)
			r.extend([p])
			i = i + 1
			p = []
		#print(r)
		B.extend([r])
		r = []		
	#print(B[3])
	
	#4 Russians

	i = 1

	while i <= int(n/m)+1:
		rs = []
		u = 0 
		v = 0
		while u < round(2**m):
			while v < n:
				r.append(0)
				v = v + 1
			u = u + 1
			rs.append(r)
		#print(rs)
		bp = 1
		k = 0
		j = 1
		print(len(rs))
#THA DOULEPSEI GIA ROUND(2**m)-1 alla mono gia to sigkekrimeno... TO EIXA APEIRES FORES
		while j <= round(2**m)-1:
			b = 0

			while b < n:
#TO B EDW EXEI STRING VALUES KAI THELEI INT GIA NA GINEI SIGKRISI TO EKANA ALLA META DEN KSERW
#Den kanei to rs[j]
				if rs[j-2**k][b]==1 or B[i][m-k-1][b]==int('1'):
					rs[j][b]=1
				b = b + 1
			if bp==1:
				bp = j + 1
				k = k + 1
			else:
				bp = bp - 1
			print(rs[j])
			j = j + 1

		Russians = []

#KANTO WHILE OPWS KSEREIS DEN MOU BGAINEI ME WHILE KAI DES TO ERROR DEN EINAI KATIx sxetika me tous rwsous!!


		for i in range(round(2**m)):
			zerolist = []
			for j in range(n):
				zerolist.append(0)
			Russians.append(zerolist)


		print(Russians)

		d = 0
		while d <= n:
			r = 0
			x = m - 1
			s = 0
			print(d)

			while x!=0:
				s = s + int(A[i][d][x])*(2**r)
				r = r + 1
				x = x - 1


			Russians[d] = rs[d]
			d = d + 1
		Russians.append(Russians[i])
		i = i + 1
	print(Russians)	
	
	#write file
	g = 0
	f = open("newfile.txt", "w")
	for Russian in Russians:
		f.csvwriter.writerow()
	f.close
	
	'''#print new file
	with open("newfile.txt") as f:
  		for line in f:
      		 print(line, end='') '''

#if 1 file input
elif len(sys.argv)==2:
	given_file = sys.argv[1]
	file = open(given_file, "r")
	with file as input_file:
		for line in input_file:
			Nodes.append(line.split())
			counter = counter + 1


	#create adjacency Matrix G
	A = []
	i = Nodes[0][0]
	j = Nodes[0][0]
	while i <= Node[n][1]:
		while j <= Node[n][1]:
			for Node in Nodes:
				if Node[0]==i and Node[1]==j:
					A[i][j] = 1
			j = j + 1
		i = i + 1 
	
	#calculate G^n-1 
	i = 1
	F = G
	while i < n-1: 
		while i <= n:
			while j <= n:
				if A[i][j]==0 or B[i][j]==0:
					B[i][j]=0
				else:
					B[i][j]=1
		i = i + 1		
	
	#4 Russians
	i = 1
	while i <= (n/m)+1:
		rs = []
		bp = 1
		k = 0
		j = 1
		while j <= 2**m:
			if rs[j-2**k]==1 or B[i][n-k]==1:
				rs[j] = 1 
			else:
				rs[j] = 0
			if bp==1:
				bp = j + 1
				k = k + 1
			else:
				bp = bp - 1
			j = j + 1
		Russians = []
		d = 0
		while d <= n:
			C[i][d] = rs[Num(A[i][d])]
		Russians = Russians + Russians[i]
		i = i + 1
	print(Russians)	


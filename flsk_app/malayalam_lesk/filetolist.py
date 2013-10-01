#fp=open("ner_text")

pat=[]
def filetolist(fname):
	
	while 1:
		k1=fname.readline()

		#print k1


		#dic1[k1]=0		
		if not k1:
			break
		else:	
			p=k1.split()
			#print p
			
			if len(p)==2:
				pat.append([p[0].decode('UTF-8'),p[1] ])
			elif len(p)==1:
				pat.append([p[0].decode('UTF-8')])
			elif len(p)>2:
				l1=[]
				for i in range(1,len(p)):
					l1.append(p[i].decode('UTF-8'))
				#l1.append(p[1:len(p)-1])
				pat.append([p[0].decode('UTF-8'),l1])
				
			else:
				pass		

			#print p[0]
			'''if p[0]=='%%':
				pass
			else:
				#pat.append((k1.split()))
				pat.append([p[0].decode('UTF-8'),p[1]])'''
		
	return pat
'''k=[]
k=filetolist(fp)
#print k
pp=[]
word= u'\u0d30\u0d1a\u0d3f\u0d1a\u0d4d\u0d1a'
for i in k:
	
	if len(i)!=2:
		pass
	else:
		if type(i[1])==list:
			for inflect in i[1]:
				if word==inflect:
					stem=i[0]
#print stem'''
			

		
			

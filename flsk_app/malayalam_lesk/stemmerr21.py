#This python file uses the following encoding: utf-8
import nltk
import os
import filetolist
fp1=open("flsk_app/malayalam_lesk/stemmer_morphems")
#fp2=open("secpass_morpheme")
def qtypefn(fname):
	lq=[]
	
	pat=[]	
	
	while 1:
		k1=fname.read()
	
	
		#dic1[k1]=0		
		if not k1:
			break;
		else:
			pat.append((k1.split()))
	for i in pat:
		#print i
		for j in range(len(i)):
			lq.append(i[j].decode('UTF-8'))
	'''for t in lq:
		print t'''
	return lq
w=[]
w=qtypefn(fp1)
print w
w.sort(None,None,False)
print "THE STEMMER MORPHEMES list"
#print w
#TO FIND THE STEMMER MORPHEMES
'''print "GIVEN THE STEMMER MORPHEMES"
for i in w:
	print i'''
	
def malayalam_stemmer(wnew):
	l2=[]
	fp=open("stemmer_output","w")
	h=open("ee","a")
	for word in wnew:
		f=0
		'''sstem=directstem(word)
		if sstem!=None:
			#fp.write(sstem.encode('UTF-8')+"\n")
			f=1
			l2.append(sstem.decode('UTF-8'))
		else:
			#l2.append(word)'''
			
			
			
			
		for i in w:
		
			l=len(i)

			t=word[-l:]	
			k=''
			if i==t :#and word !=u'\u0d2e\u0d15\u0d7e':
				if i==u'\u0d1a\u0d4d\u0d1a' and word!=u'\u0d2a\u0d1a\u0d4d\u0d1a' and word!= u'\u0d1a\u0d7c\u0d1a\u0d4d\u0d1a' :#'ച്ച and word not eq to pachcha or charchcha u'\u0d19\u0d4d\u0d19\u0d7e'kal
					#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
					#print word[0:len(word)-l]
					k=word[0:len(word)-l]+u'\u0d15\u0d4d\u0d15\u0d41\u0d15'#'ക്കുക'.
					#print k
					f=1
					fp.write(k.encode('UTF-8')+"\n")
					l2.append(k)
					#p[ind]=k
					break
				if i==u'\u0d1e\u0d4d\u0d1e' and word!= u'\u0d2e\u0d1e\u0d4d\u0d1e':
					k=word[0:len(word)-l]+u'\u0d2f\u0d41\u0d15'#'yuka'.
					#print k
					f=1
					fp.write(k.encode('UTF-8')+"\n")
					l2.append(k)
					#p[ind]=k
					break
				if i==u'\u0d3e\u0d24\u0d46' :
					k=word[0:len(word)-l]+u'\u0d41\u0d15'#'yuka'.
					#print k
					f=1
					fp.write(k.encode('UTF-8')+"\n")
					l2.append(k)
					#p[ind]=k
					break
				if i==u'\u0d1a\u0d4d\u0d1a\u0d41' :#'ച്ച chchu 
					#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
					#print word[0:len(word)-l]
					k=word[0:len(word)-l]+u'\u0d15\u0d4d\u0d15\u0d41\u0d15'#'ക്കുക'.
					#print k
					f=1
					fp.write(k.encode('UTF-8')+"\n")
					l2.append(k)
					#p[ind]=k
					break
				if i==u'\u0d15\u0d4d\u0d15\u0d4d' and word[len(word)-l-1]!=u'\u0d41':#kkk'and word not eq to pachcha or charchcha u'\u0d19\u0d4d\u0d19\u0d7e'kal
					#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
					#print word[0:len(word)-l]
					k=word[0:len(word)-l]#+u'\u0d15\u0d4d\u0d15\u0d41\u0d15'#'ക്കുക'.
					#print k
					f=1
					fp.write(k.encode('UTF-8')+"\n")
					l2.append(k)
					#p[ind]=k
					break
				if i==u'\u0d2a\u0d4d\u0d2a\u0d46\u0d1f\u0d4d\u0d1f':#ppetta
					#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
					#print word[0:len(word)-l]
					k=word[0:len(word)-l]+u'\u0d41\u0d15'#''uka.
					#print k
					f=1
					fp.write(k.encode('UTF-8')+"\n")
					l2.append(k)
					#p[ind]=k
					break

			if i==t and word !=u'\u0d2e\u0d15\u0d7e':
				if i==u'\u0d15\u0d7e':# u'\u0d19\u0d4d\u0d19\u0d7e':#kal
					#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
					#print word[0:len(word)-l]
					k=word[0:len(word)-l]
					#p[ind]=k
					#print k
					f=1
					fp.write(k.encode('UTF-8')+"\n")
					l2.append(k)
					break
				if i==u'\u0d19\u0d4d\u0d19\u0d7e':#ngal
					#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
					#print word[0:len(word)-l]+u'\u0d02'
					k=word[0:len(word)-l]+u'\u0d02'
					#print k
					f=1
					fp.write(k.encode('UTF-8')+"\n")
					l2.append(k)
					#p[ind]=k
					break

		
			if i==t:
				if i==u'\u0d2e\u0d3e\u0d23\u0d4d\u200c':#maannu
					#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
					#print word[0:len(word)-l]+u'\u0d02'
					k=word[0:len(word)-l]+u'\u0d02'
					fp.write(k.encode('UTF-8')+"\n")
					f=1
					l2.append(k)
					break
				
				
				if i== u'\u0d28\u0d4d\u0d31\u0d46':#nte
					#print  "ntente ;;;;;;;;;;;;;;;"
					if word[-l-4:-l]==u'\u0d24\u0d4d\u0d24\u0d3f':#ththi

						#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
						#print word[0:len(word)-l-1]+u'\u0d7d'
						k=word[0:len(word)-l-4]+u'\u0d02'
						fp.write(k.encode('UTF-8')+"\n")
						f=1
						l2.append(k)
						break
					elif word[-l-2:-l]==u'\u0d2e\u0d3f':#mi eg: aadaminte
						#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
						#print word[0:len(word)-l-1]+u'\u0d02'
						k=word[0:len(word)-l-2]+u'\u0d02'
						fp.write(k.encode('UTF-8')+"\n")
						f=1
						l2.append(k)
						break
				if i== u'\u0d3f\u0d7d':#il
					#print  "ill ;;;;;;;;;;;;;;;"
					if word[-l-3:-l]==u'\u0d24\u0d4d\u0d24':#ththi

						#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
						#print word[0:len(word)-l-1]+u'\u0d7d'
						k=word[0:len(word)-l-3]+u'\u0d02'
						fp.write(k.encode('UTF-8')+"\n")
						f=1
						l2.append(k)
						break
					elif word[-l-1]==u'\u0d33':#Lha

						#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
						#print word[0:len(word)-l-1]+u'\u0d7e'
						k=word[0:len(word)-l-1]+u'\u0d7e'
						fp.write(k.encode('UTF-8')+"\n")
						f=1
						l2.append(k)
						break

					

				if i==u'\u0d3e\u0d23\u0d4d' or i==u'\u0d41\u0d1f\u0d46' or i==u'\u0d3e\u0d2f' or i==u'\u0d3e\u0d2f\u0d3f'or i==u'\u0d3f\u0d7d' or i==u'\u0d46' or i==u'\u0d41\u0d02' or i==u'\u0d4b\u0d1f\u0d46' or i==u'\u0d3e\u0d7d' or i==u'\u0d3f\u0d24\u0d4d': #or i==u'\u0d41\u0d02' : or i==u'\u0d46'  or i==u'\u0d47':
					#aanu or ute or yeyum aya or aayi#um--- u'\u0d41\u0d02'uute:indiayilooteeeyumor i==u'\u0d47\u0d2f\u0d41\u0d02' 
					
					if i==u'\u0d41\u0d02':#UM

						if len(word[:-l])>=2:
							if word[-l-2]==u'\u0d47':
								word=word[0:-l-2]+u'\u0d46'+word[-l:l]
								h.write(word.encode('UTF-8')+"\n")
								fp.write(word.encode('UTF-8')+"\n")
								f=1
								l2.append(word)
								break
								print word
								print "eeeeeeeeeeeeeeeeetoa"
								#fp.write(word[-l-2])
						if word[-l-1]==u'\u0d35':#ma
							#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
							#print word[0:len(word)-l-1]+u'\u0d02'
							k=word[0:len(word)-l-1]+u'\u0d02'
							fp.write(k.encode('UTF-8')+"\n")
							f=1
							l2.append(k)
							break

					if i==u'\u0d46':#e: eg:indiayiloote
						'''if word[-l-4:len(word)-l]==u'\u0d24\u0d4d\u0d24\u0d3f':
							k=word[0:len(word)-l-1]+u'\u0d02'
							fp.write(k.encode('UTF-8')+"\n")
							f=1
							l2.append(k)
							break'''
							
						c=3
						if word[-c:]==u'\u0d42\u0d1f\u0d46':#oote
							i=u'\u0d4b\u0d1f\u0d46'
							l=len(i)
							#print "hhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
							if word[-4]==u'\u0d32':
								k=word[0:len(word)-l-1]+u'\u0d7d'
								fp.write(k.encode('UTF-8')+"\n")
								f=1
								l2.append(k)
								break
						
						else:
							pass
					if word[-l-1]==u'\u0d32':#la
				

						#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
						#print word[0:len(word)-l-1]+u'\u0d7d'
						k=word[0:len(word)-l-1]+u'\u0d7d'
						fp.write(k.encode('UTF-8')+"\n")
						f=1
						l2.append(k)
						break	
					if word[-l-5:-l-2]==u'\u0d24\u0d4d\u0d24' and word[-l-1]!=u'\u0d2f' and len(word[0:-l-5])!=1:#ththi noteq ya

						#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
						#print word[0:len(word)-l-1]+u'\u0d7d'
						k=word[0:len(word)-l-5]+u'\u0d02'
						fp.write(k.encode('UTF-8')+"\n")
						f=1
						l2.append(k)
						break
					if word[-l-4:len(word)-l]==u'\u0d24\u0d4d\u0d24\u0d3f':
							k=word[0:len(word)-l-1]+u'\u0d02'
							fp.write(k.encode('UTF-8')+"\n")
							f=1
							l2.append(k)
							break

					elif word[-l-1]==u'\u0d33':#Lha

						#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
						#print word[0:len(word)-l-1]+u'\u0d7e'
						k=word[0:len(word)-l-1]+u'\u0d7e'
						fp.write(k.encode('UTF-8')+"\n")
						f=1
						l2.append(k)
						break
					elif word[-l-1]==u'\u0d2e':#ma
						#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
						#print word[0:len(word)-l-1]+u'\u0d02'
						k=word[0:len(word)-l-1]+u'\u0d02'
						fp.write(k.encode('UTF-8')+"\n")
						f=1
						l2.append(k)
						break
					elif word[-l-1]==u'\u0d28':#na
						#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
						#print word[0:len(word)-l-1]+u'\u0d7b'
						k=word[0:len(word)-l-1]+u'\u0d7b'
						fp.write(k.encode('UTF-8')+"\n")
						f=1
						l2.append(k)
						break
					elif word[-l-1]==u'\u0d2f':#yau'\u0d2f'
						#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
						#print word[0:len(word)-l-1]
						k=word[0:len(word)-l-1]
						fp.write(k.encode('UTF-8')+"\n")
						f=1
						l2.append(k)
						break
					elif word[-l-1]==u'\u0d30':#rau'\u0d2f'
						#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
						#print word[0:len(word)-l-1]+u'\u0d7c'
						k=word[0:len(word)-l-1]+u'\u0d7c'
						fp.write(k.encode('UTF-8')+"\n")
						f=1
						l2.append(k)
						break
					elif word[-l-3:-l]==u'\u0d24\u0d4d\u0d24':#ththi\u0d3f

						#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
						#print word[0:len(word)-l-1]+u'\u0d7d'
						k=word[0:len(word)-l-3]+u'\u0d02'
						fp.write(k.encode('UTF-8')+"\n")
						f=1
						l2.append(k)
						break
					else: 
						#print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
						#print word[0:len(word)-l-1]+u'\u0d4d'
						k=word[0:len(word)-l]+u'\u0d4d'
						fp.write(k.encode('UTF-8')+"\n")
						f=1
						l2.append(k)
						break
						
		if f==0:
			#print word	
			#print "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
			k=word
			fp.write(k.encode('UTF-8')+"\n")
			l2.append(k)
			#fp.write(k.encode('UTF-8')+"\n")
			#break
		#print f	
		continue
			

	return l2 











#print w1


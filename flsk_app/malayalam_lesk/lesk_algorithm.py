'''
Created on 04-Jul-2013

@author: mujeeb
''' 
import MalayalamWordnet as wordnet
import MalayalamStemmer as stemm
from _abcoll import Set
#import  stemmerr21 as sthree_stemm
def lesk(context,word):
    splited_context = context.split(" ")
    stemmed_context =[]
    for item in splited_context:
        if item.strip()!='':
            temp = stemm.findstem(item)
            print "stemmed=",temp
            stemmed_context.append(temp)
    #stemmed_context=sthree_stemm.malayalam_stemmer(stemmed_context)
    flag = False
    for item in stemmed_context:
        print "item=",item,"ddddd=",word.strip()
        if item == word.strip():
            flag= True
            break
    if flag!=True:
        return flag
    
    wordnet_obj = wordnet.mysqldbwordnet()
    definitions = wordnet_obj.getDefinitions(word)
    rank_list = []
    ranks = []
    for item in definitions:
        definition =item[0].split(" ")
        stemmed_def =[]
        for item1 in definition:
            if item1.strip()!='':
                temp = stemm.findstem(item1) 
                print "stemmed _definition:",temp
                stemmed_def.append(temp)
        #print "###############################"
        #stemmed_def=sthree_stemm.malayalam_stemmer(stemmed_def)
        rank_count = 0
        for item1 in stemmed_context:
            
            if (item1 in stemmed_def) and (item1 != word):
                rank_count = rank_count + 1
        rank_list.append([item[0],rank_count])
        if rank_count not in ranks:
            ranks.append(rank_count)
             
    ranks.sort(cmp=None, key=None, reverse=True)
    selected_definitions = []
    first_rank = ranks[0]
    print "first rank =",first_rank 
    for item in rank_list:
        #print "eeee=",item[0],"\t",item[1]
        if item[1] == first_rank:
            selected_definitions.append(item[0])
    
    return selected_definitions

#f = open('input.txt','r')
#input_text = f.read().split("#")
#definitions = lesk(input_text[1], input_text[0])

#for item in definitions:
#    print item 

                
        
        
        

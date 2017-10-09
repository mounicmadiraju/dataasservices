# -*- coding: utf-8 -*-

import nltk,os,codecs
import re
#import re

class MySentences(object):
    def __init__(self, dirname,exp=''):
        self.dirname = dirname
        self.a=extract(exp)
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in codecs.open(os.path.join(self.dirname, fname),'r','utf-8'):
                if len(line)>10:
                    
                    yield self.a.n_gram_extract(line)

class extract(object):
    def __init__(self,regex=''):
        self.w=[]
        self.pos=[]
        self.sw=[]
        self.spos=[]
        self.regex=regex
        self.r=re.compile(regex)
        self.stl=[]
        self.tgl=[]
        
    def map_con(self,begin,end):
        self.index=[]
        f=1
        for i in range(len(self.d)):
            mi=self.d[i][0]
            ma=self.d[i][1]
            if begin>=mi and begin<ma and f:
                self.index.append(i)
                f=0
            elif end>ma and not f:
                self.index.append(i)
            elif end<ma and not f:
                #self.index.append(i)
                f=1
            elif not f:
                self.index.append(i)
                break
        return self.index
            
    def n_gram_extract(self,line):
        #w=nltk.word_tokenize(line.lower())
        self.w=[]
        self.pos=[]
        self.sw=[]
        self.spos=[]
        self.stl=[]
        self.tgl=[]
        self.d={}
        self.tag_dic={}
        line=line.replace('-',' - ')
        w1=nltk.word_tokenize(line)
        tag=nltk.pos_tag(w1)
        self.spos=[j for i,j in tag]
        self.sw=[i.lower() for i in w1]
        self.w=' '.join(self.sw)+' '
        self.pos=' '.join(self.spos)+' '
        pos=0
        if not self.regex:
            print 'No regex found for spliting'
            return self.sw
        for i,j in enumerate(self.spos):
            l=pos+len(j)
            self.d[i]=[pos,l]
            pos=l+1
        my_iter=self.r.finditer(self.pos)
        self.stl=[]
        self.tgl=[]
        count = 0
        self.ran=[]
        for match in my_iter:
            count += 1
            ran=match.span()
            self.ran.append(ran)
            #print ran,count
            posi= self.map_con(ran[0],ran[1])
            st=''
            tg=''
            for num in posi:
                st+=self.sw[num]+' '
                tg+=self.spos[num]+' '
            st=st.strip()
            tg=tg.strip()
            self.stl.append(st)
            self.tgl.append(tg)
            self.tag_dic[st]=tg
            #print st,tg
        #print count 
        return self.tag_dic#self.stl#,tgl,self.tag_dic
    def n_gram_split(self,line):
        """ """
        self.n_gram_extract(line)
        self.spl=[]
        for i in self.ran:
            posi=self.map_con(i[0],i[1])
            if len(posi)>1:
                self.spl.append(posi)
        local_set=[]
        for i in self.spl:
            local_set+=i
        _len=len(self.spos)
        l_se=set(local_set)
        m_se=set(range(0,_len))
        mis=list(m_se-l_se)
        final_split_num=[]
        i=0
        while(i<_len):
            if i in mis:
                final_split_num.append([i])
                i+=1
            else:
                for j in self.spl:
                    if i in j:
                        final_split_num.append(j)
                        i=j[-1]+1

        self.f_index=final_split_num
        self.sword=[]
        self.stag=[]
        for i in self.f_index:
            tg=[]
            wo=[]
            for j in i:
                tg.append(self.spos[j])
                wo.append(self.sw[j])
            t=' '.join(tg)
            w=' '.join(wo)
            self.sword.append(w)
            self.stag.append(t)
        return self.sword
                
        
        
                
                
if __name__=='__main__':    
    s="""Once when a lion, the king of the jungle, was asleep, a little mouse began running up and down on him. This soon awakened the lion, who placed his huge paw on the mouse, and opened his big jaws to swallow him.
 """
    #reg='(JJ NN(\w)*)|NN|(NN(\w)*)'
    #reg='((NN(\w)* )+)|((JJ)+ NN(\w)*)'
    #s=open('C:/Python27/final year proj/speech_out/review.txt').read()
    #s='there is a black thick historical book'
#    myfile='out.txt'
#    s=open(myfile).read().split('\n')
#    s='Clone phishing edit  Clone phishing is a type of phishing attack whereby a legitimate  and previously delivered  email containing an attachment or link has had its content and recipient address es  taken and used to create an almost identical or cloned email.'
    reg='((NN(\w)* )+)|((JJ )+(NN(\w)* )+)'
    reg='((PRP(\$)*\s)*(DT\s)*(NN(\w)*\s)+)|((PRP(\$)*\s)*(DT\s)*(JJ\s)+(NN(\w)*\s)+)'
    reg='((PRP(\$)*\s)*(DT\s)*(JJ\s)+(NN(\w)*\s)+)*((PRP(\$)*\s)*(DT\s)*(NN(\w)*\s)+)*(IN\s)((PRP(\$)*\s)*(DT\s)*(NN(\w)*\s)+)*((PRP(\$)*\s)*(DT\s)*(JJ\s)+(NN(\w)*\s)+)*|((PRP(\$)*\s)*(DT\s)*(NN(\w)*\s)+)|((PRP(\$)*\s)*(DT\s)*(JJ\s)+(NN(\w)*\s)+)'
    o=extract(reg)
    ne=o.n_gram_split(s)
    from beautifultable import BeautifulTable
    import math
    table = BeautifulTable()
    table.row_seperator_char = ''
    table.intersection_char = ''
    table.column_seperator_char = ''
    w=o.sw
    t=o.spos
    r=math.ceil(len(w)/10.0)*10-len(w)
    for i in range(int(r)):
        w.append('Null')
        t.append('Null')
    for i in range(0,len(w),10):
        table.append_row(w[i:i+10])
        table.append_row(t[i:i+10])
    print table
#    for i,j in zip(o.sword,o.stag):
#        print i+'   <====>    '+j

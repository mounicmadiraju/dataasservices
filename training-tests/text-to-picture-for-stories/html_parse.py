
import tag_split as ts
import  image_scrap as sc
def get_color(ind):
    color=['#3364FF','#33FF8D','#33FFCA','#FFB833','#966A17','#FF5733','red', 'green', 'blue']
    return color[ind%len(color)]
g=sc.g_search()
class topics:
    def __init__(self,topic):
        self.topic=topic
        self.sub=[]
        self.extract_sub()
    def extract_sub(self):
        self.top=ts.nltk.pos_tag(ts.nltk.word_tokenize(self.topic))
        
        for i,j in self.top:
            if 'NNP' == j:
                self.sub.append(i)
        for i,j in self.top:
            if 'NN' == j:
                self.sub.append(i)
        #self.sub.reverse()
    def get(self,position):
        if len(self.sub)==0:
            return ''
        pos=position%len(self.sub)
        return self.sub[pos]
        
def sub_replace(sub):
    if sub in 'he him his'.split():
        return 'boy'
    elif sub in 'she her hers'.split():
        return 'girl'
def get_cont(s,topic,get=1):
    top=topics(topic)
    if get:
        sub=top.get(0)
    
        
    #s='Once upon a time there lived a lion in a forest.'
    reg='((PRP(\$)*\s)*(DT\s)*(JJ\s)+(NN(\w)*\s)+)*((PRP(\$)*\s)*(DT\s)*(NN(\w)*\s)+)*(IN\s)((PRP(\$)*\s)*(DT\s)*(NN(\w)*\s)+)*((PRP(\$)*\s)*(DT\s)*(JJ\s)+(NN(\w)*\s)+)*|((PRP(\$)*\s)*(DT\s)*(NN(\w)*\s)+)|((PRP(\$)*\s)*(DT\s)*(JJ\s)+(NN(\w)*\s)+)'
    o=ts.extract(reg)
    ne=o.n_gram_split(s)
    
    count=0
    col=[]
    for i,j in zip(o.sword,o.stag):
            if 'NN' in j:
                cl=get_color(count)
                col.append(cl)
                count+=1
            else:
                col.append('')
    img=[]
    ht_words=[]
    wdic={}
    prp='i me you he him she her it we us they them his hers'.split()
    for i,j,k in zip(o.sword,col,o.stag):
        wo=i.lower()
        if j is not '':
            if 'PRP' in k:
                ww=[]
                for q in wo.split():
                    if q in prp:
                        if not get:
                            ww.append(sub_replace(sub))
                        else:
                            ww.append(sub)
                    else:
                        ww.append(q)
                wo=' '.join(ww)
                #print wo
                #print ww
                #break
            if wo in wdic:
                ig=wdic[wo]
            else:
                wdic[wo]=g.get_img(wo)[1]
                ig=wdic[wo]
            print wo
            img.append("<img src=\""+ig+"\" style=\"border-color : "+j+";background-color: "+j+"\">")
            ht_words.append("<span style=\"background-color: "+j+"\">"+i+"</span>")
        else:
            ht_words.append(i)
    wd=' '.join(ht_words)
    tag=' '.join(o.stag)
    ig=' '.join(img)
    cont=wd+'.\n<br>'+tag+'\n<br>'+ig+'<br>'
    return cont
    
        
            

if __name__=='__main__':
    """ Main file"""
    s="""Once when a lion, the king of the jungle, was asleep, a little mouse began running up and down on him. This soon awakened the lion, who placed his huge paw on the mouse, and opened his big jaws to swallow him.
    """
    c=get_cont(s,'The Lion and the Mouse')
 


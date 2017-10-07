import time
import requests
import os
import json
import webbrowser
class g_search(object):
    def __init__(self):
        self.key = 'AIzaSyD752xZNIoMmJCkTbgr-fkcVbwn-SVZfpY'
        self.cx = '014312645802610321915:s39xjx-whs4'
    def get_img(self,searchTerm):
        startIndex = '1'   
        searchUrl = "https://www.googleapis.com/customsearch/v1?q=" + \
            searchTerm + "&start=" + startIndex + "&key=" +self.key + "&cx=" + self.cx + \
            "&searchType=image"
        r = requests.get(searchUrl)
        response = r.content.decode('utf-8')
        res = json.loads(response)    
        s=res['items']
        ret=[]
        self.result=res
        for i in s:
            ret.append(i['link'])
        return ret 

if __name__=='__main__':
    o=g_search()
    s=o.get_img('lion huge paw on the mouse')
   


 
    
    

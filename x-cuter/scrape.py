from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib
import pandas as pd
import joblib
class extract_from_exel(object):
    def __init__(self,exel_file,col_name='',filters='',start=0):
        self.file=exel_file
        self.xlsx = pd.ExcelFile(exel_file)
        self.sheet1 = self.xlsx.parse(0) if start !=0 else self.xlsx.parse(0,skiprows=start-1)
        self.col_name=col_name
        self.passed=[]
        self.error=[]
        self.filters=filters
    def __iter__(self):
        for i in self.sheet1.iterrows():
            try:
                if self.col_name:
                    tex=i[1][self.col_name]
                    if self.filters in tex:
                        yield i[0],str(tex)
                    else:
                        self.passed.append(i[0])
                else:
                    yield i[0],i[1]
            except Exception as e:
                print 'Error at :',i[0]
                self.error.append((e,i[0],tex))
            
class scrape(object):
    def __init__(self,user='XXXX',passw='XXXX'):
        self.email=user
        self.passw=passw
        self.main_url='http://www.linkedin.com/'
        self.driver = webdriver.Chrome()
        self.login()
        
    def login(self):
        self.driver.get(self.main_url)
        username = self.driver.find_element_by_id('login-email')
        passwd = self.driver.find_element_by_id('login-password')
        submit= self.driver.find_element_by_id('login-submit')
        username.send_keys(self.email)
        passwd.send_keys(self.passw)
        submit.click()
    def get_content(self,url):
        self.driver.get(url)
        self.logo=self.driver.find_element_by_class_name('org-top-card-module__logo')
        self.src=self.logo.get_attribute('src')
        self.about_us=s.driver.find_element_by_class_name('org-about-us-organization-description')
        self.about=self.about_us.text
        c_url=self.driver.current_url
        self.name=c_url.split('/')[-2]+'.jpeg'
        urllib.urlretrieve(src, "logos/"+self.name)
        other=self.driver.find_elements_by_class_name('org-top-card-module__dot-separated-list')
        self.others=map(lambda x:x.text,other)
        return {'logo':self.name,'about':self.about,'others':self.others}
 
if __name__=='__main__':     
    import os
    start=471
    s=scrape()
    ex=extract_from_exel('comp.xlsx',start)
    if os.path.exists('all_retrived_data'):
        data=joblib.load('all_retrived_data')
        errors=joblib.load('error_in_selinium')
        skiped=joblib.load('all_skiped_data')
        ex.error=joblib.load('error_in_exel')
    else:
        errors=[]
        data=[]
        skiped=[]
    for index,val in ex:
        mydic=val.to_dict()
        try:
            link=val['LinkedIn']
            if 'linkedin' in link:
                dic=s.get_content(link)
                newdic=val.to_dict()
                for i,j in dic.items():
                    newdic[i]=j
                data.append(newdic)
            else:
                skiped.append([index,val])
        except Exception as e:
            errors.append([index,e])
        
    joblib.dump(data,'all_retrived_data')
    joblib.dump(skiped,'all_skiped_data') 
    joblib.dump(errors,'error_in_selinium')
    joblib.dump(ex.error,'error_in_exel')
    #url='http://www.linkedin.com/company/airbnb'
    #dic=s.get_content()

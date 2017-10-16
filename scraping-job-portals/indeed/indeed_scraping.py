# To retrieve Job titles, salaries, location and company name from various indeed job postings
# First  seach div with one job all elements and then  search elements inside this div
import urllib2
from bs4 import BeautifulSoup

URL = "http://www.indeed.com/jobs?q=seo+analyst+%2420%2C000&l=New+York&start=10"

soup = BeautifulSoup(urllib2.urlopen(URL).read(), 'html.parser')

results = soup.find_all('div', attrs={'data-tn-component': 'organicJob'})

for x in results:
    company = x.find('span', attrs={"itemprop":"name"})
    print 'company:', company.text.strip()

    job = x.find('a', attrs={'data-tn-element': "jobTitle"})
    print 'job:', job.text.strip()

    salary = x.find('nobr')
    if salary:
        print 'salary:', salary.text.strip()

    print '----------'
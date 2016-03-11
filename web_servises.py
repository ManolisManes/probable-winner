import urllib2
import simplejson
from collections import defaultdict
from collections import Counter

day = raw_input ('Give day DD\n')  #input from user
d=int(day)
month = raw_input ('Give month MM\n')
m=int(month)
year = raw_input ('Give year YYYY\n')
y=int(year)

myURL = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/%d-%d-%d.json" % (d,m,y)  #make the request
response = urllib2.urlopen(myURL)  #take the response
j = simplejson.load(response)    #convert it to python dict


results_list = []
i=0
final = []
for drawNo in j['draws']['draw']:      #take all the 'result' lists from the dict
 results_list = j['draws']['draw'][i]['results']
 final = final + results_list     #merge them into one list

 i += 1

c = Counter(final)  #count the occurence of every item
print "The result for %d-%d-%d is the following: (number: occurences) - in descending order" %( d , m , y)
print c

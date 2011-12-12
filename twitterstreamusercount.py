import urllib
import simplejson
from xml.dom import minidom
from xml.dom.minidom import parse, parseString
import tweepy



usr='marianasoffer'

#name of the list you choose
listname="misc"



#These keys belong to my own twitter application, they are here just so you can
#quickly see how the application works but you should enter your own twitter
#api keys to test this program properly

key="nQXCRcHhAGP0X6cBp0g"
secretKey="3Nc4x9o4agfe0UjedI4LjVQbthylDCd8ePNLVCuYMA"
accessKey="27745630-2JqslhlOiUiHlGKz1Jm19wAV6o3yH0JlZj89R40pd"
accessAuth=""

#counts all the users from the list that are also in the
#users from those users lists

#access api with proper credentials
auth = tweepy.OAuthHandler(key,secretKey)
auth.set_access_token(accessKey,accessAuth)

api=tweepy.API(auth)  

#obtain the users followed by a list owned by the main user (credential owner)
ulist=api.list_members(api.me().name,listname)
ulist=ulist[0]


usrsn=[]     
#users screen names
usrsns=[]     
#users ids
usrsid=[]     
#amount of apearances of the user_id in the list
usrsms=[]  
#users list of lists
usrlst=[]
#ids found in the lists traversed that are in the users ids
iddl=[]

#create lists with user:ids,name and screen_name, plus one to count the times
#each user appears in the lists that will be searched

for u in ulist:
        usrsid.append(u.id)
        usrsn.append(u.name)
        usrsns.append(u.screen_name)
        usrsms.append(0)
        ul=u.lists()
        ul=ul[0]
        usrlst.append(ul)
        

#count the times it appears in the timelines of the lists belonging to
#users of this lists each user of the main list
        
for ull in usrlst:
        for ul in ull:
                mm=ul.members()
                m=mm[0]
                for mid in m:
                        for idd in usrsid:
                                if mid.id==idd:
                                        iddl.append(idd)

                                

#add total apearances to the id counters
for idd in iddl:
	n=usrsid.index(idd)
	usrsms[n]=usrsms[n]+1

#sort in reverse both lists, the one that contains the appearances and the
#one with the names returning 2 tuples

data = zip(usrsms, usrsns)
data.sort(reverse=True)
twoLi = map(lambda t: list(t), zip(*data))


#Merge 2 lists in order for number of mentions to match the name:
bigl=[]
bigl.append(twoLi[0])
bigl.append(twoLi[1])
toPrint=zip(*bigl)


#Print Results
print "Amount,Name"
for lin in toPrint:
        print str(lin[0])+","+lin[1]

        

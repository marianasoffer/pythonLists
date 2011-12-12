#counts the number of times a user from a given list appears in the
#stream of all the lists belonging to users of this lists
import urllib
import simplejson
from xml.dom import minidom
from xml.dom.minidom import parse, parseString
import tweepy



usr='marianasoffer'

#name of the list you choose
listname="misc"



#Pleae enter your twitter keys. And corret the usr and listname variables

key=""
secretKey=""
accessKey=""
accessAuth=""


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
#all possible matches
apmt=[]
apm=[]

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
        

apmt.append(usrsid)
apmt.append(usrsn)
apmt.append(usrsns)
apm=zip(*apmt)


print apm


#count the times it appears in the timelines of the lists belonging to
#users of this lists each user of the main list
        
for ull in usrlst:
        for ul in ull:
                ss=ul.timeline()
                for s in ss:
                        n=0
                        for usref in apm:
                                if s.in_reply_to_user_id==usref[0]:
                                        n=n+1
                                        print 1
                                        print s.text
                                        exit()
                                #checking retweets just in case is needed        
                                #rts=s.retweets()
                                #for sts in rts:
                                #        if sts.author.id==usref[0]:
                                #                n=n+1
                                #                print 2
                                #                print sts.text
                                #                exit()
                                txt=s.text
                                ff=txt.find(usref[2])
                                if ff!=-1:
                                        print ff
                                        print 3
                                        print txt
                                        print usref
                                        n=n+1
                                        txt=txt[ff+len(usref[2])-1:]
                                        exit()
                                ff=txt.find(usref[1])
                                if ff!=-1:
                                        print 4
                                        n=n+1
                                        print s.text
                                        exit()
                        for w in range(n):
                                iddl.append(usref[0])
                                exit()

#add total apearances to the id counters
for idd in iddl:
	n=usrsid.index(idd)
	usrsms[n]=usrsms[n]+1

#sort in reverse both lists, the one that contains the appearances and the
#one with the names returning 2 tuples

data = zip(usrsms, usrsn)
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

        

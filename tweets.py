from tweepy import *
import time

# How to use:
# 1. add new Application in dev.twitter.com
# 2. write your consumer and access key/secret key at below four var
# 3. launch it!

consumer_key = ""
consumer_secret = ""
ACCESS_KEY ="60047739-"
ACCESS_SECRET = ""
delay = 0.1

def checkTweetException(e):
    if (len(e) > 0):
        if (e[0][0][u"code"] == 34):
            return True
    return False

def loadStat():
    try:
        fLog = open('save.txt')
        c = int(fLog.readline() )
        fLog.close()
        return c
    except:
        print "Not found working index, start from index 0"
        return 0
def saveStat(c):
    try :
        fLog = open('save.txt', 'w')
        fLog.write(str(c))
        fLog.close()
    except Exception, e:
        print e

def __init__():
    print "----------------------------------"
    print "- Tweet remover by @kuna_KR      -"
    print "----------------------------------"
    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = API(auth)

    cnt = 0
    setcnt = 0 # skip cnt

    setcnt = loadStat()

    try:
        filepath = "tweets.csv"
        fo = open(filepath, "r")

        fo.readline()
        while 1:
            twid = 0
            if (cnt % 100 == 0):
                print "%d removing..." % cnt
            cnt = cnt+1
            saveStat(cnt)
            try:
                ln = fo.readline()
                if not ln:
                    print "End of File"
                    break
                tweet = ln.split(',')
                tweet[0] = tweet[0].replace("\"", "")
                twid = int(tweet[0])

                if (cnt < setcnt):
                    continue
                
                time.sleep(delay)
                api.destroy_status(twid)
                print "removed %d" % twid
            except ValueError:
                pass
            except Exception, e:
                print "failed to remove %d" % twid, e
            
        fo.close()
    except Exception, e:
        print "Error occured during accessing file. is tweets.csv file valid?"


__init__()

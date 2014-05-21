#Quick and Easy Android Pattern Lock Cracker - Kieron Craggs 2014
#This quick script will use a gesture.key file or raw text hash and compare it against a rainbow table to find the pattern used to lock the device
#Uses GestureKey Rainbow Table

#****MODULES*************#
import argparse
import sqlite3 as lite
import gzip
import os
#************************#

parser = argparse.ArgumentParser(description = "Easy Android Pattern Lock Cracker")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-f", "--file", help="Path to a gesture.key file", required=False)
group.add_argument("-r", "--rawhash", help="Raw text input of SHA1 hash", required=False)
args = parser.parse_args()

if args.file:
    gesturekey = open (args.file,'rb').read()
    inkey = str(gesturekey).encode('hex-codec')
elif args.rawhash:
    inkey = args.rawhash
else:
    print "Supply a valid gesture key file or raw text hash"


try:
    dbin = gzip.GzipFile('rainbow.db.gz','rb')
except IOError:
    print "Database archive doesn't exist, put rainbow.db.gz in current working directory"
    exit()
else:
    dbbuf = dbin.read()
    dbin.close()

    dbout = file('rainbow.db','wb')
    dbout.write(dbbuf)
    dbout.close()    

try:
    db = lite.connect('rainbow.db') 
except NameError:
    print "Nothing was given to the database to check. Check gesture input file."
except IOError:
    print "Cannot find db file."
else:    
    with db:
        cur = db.cursor()
        cur.execute('SELECT pattern FROM RainbowTable WHERE hash = ?',(inkey,))
        rows = cur.fetchone()

        if rows:
            for row in rows:
                result = row
                print """   

        The Lock Pattern code is %s

        For reference here is the grid (starting at 0 in the top left corner):

        |0|1|2|
        |3|4|5|
        |6|7|8|

                """ % (row)
        else:
            print "No match, check input."                    

if os.path.exists("rainbow.db"):       
        os.remove("rainbow.db")
        exit()    
#Quick and Easy Android Pattern Lock Cracker - Kieron Craggs 2014
#This quick script will open a gesture.key file and compare its contents against a rainbow table to find the pattern used to lock the device
#Uses GestureKey Rainbow Table http://resources.infosecinstitute.com/android-forensics-cracking-the-pattern-lock-protection/

#****MODULES*************#
import argparse
import sqlite3 as lite
#************************#

parser = argparse.ArgumentParser(description = "Easy Android Pattern Lock Cracker")

parser.add_argument("-f", "--file", help="Path to a gesture.key file", required=True)
args = parser.parse_args()

gesturekey = open (args.file,'rb').read()

inkey = str(gesturekey).encode('hex-codec')

db = lite.connect('GestureRainbowTable.db') 
with db:
    cur = db.cursor()
    cur.execute('SELECT pattern FROM RainbowTable WHERE hash = ?',(inkey,))
    rows = cur.fetchone()

    for row in rows:
    	result = row
    	print """	

    	The Lock Pattern code is %s

    	For reference here is the grid (starting at 0 in the top left corner):

    	|0|1|2|
    	|3|4|5|
    	|6|7|8|

    	""" % (row)

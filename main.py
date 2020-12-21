#we don't want to build the json string ourselves so use the json module
#for encoding and stuff
import json

#will be adjusted and cleaned up later

#manually do this ez :)
#this is a string
email_error = input()

#turn to a dict for json to parse
email_error = eval(email_error)

correct = json.dumps(email_error)

#automatically get backtrace results
get_backtrace = ["code hidden"]

'''ayy'''

print(correct)
#print(get_backtrace)


# Created by: MHagarGIS
# For: GEOG499
# Title: ArcMap Field Calculator Address Formatter in Python
#

#Converting street type to proper format
def converttype(oldtype):       #Define function converttype that accepts argument oldtype
    oldtype = oldtype.title()   #Use the .title() function to make first letter uppercase and the rest lowercase

    if oldtype == "Way":        #If the old type is "Way" strip out the second letter (a) and assign to newtype
        newtype = oldtype[0::2] 
    elif oldtype == "Ave":      #If the old type is "Ave" strip out the third letter (3) and assign to newtype
        newtype = oldtype[0:2]
    else:
        newtype = oldtype       #If neither previous condition was met then oldtype is properly formatted. Assign to newtype.
    return newtype              #Return newtype

#Concatenating address components into FinalAddr
def convertaddr(CorrectNum,NewName,NewType,NewZip): #Define function convertaddr that accepts four arguments
    newaddr = str(CorrectNum) + " " + NewName + " " + NewType + " " + str(NewZip)   #Convert variables to strings, add spaces, and concatenate into proper form
    return newaddr      #Return the result

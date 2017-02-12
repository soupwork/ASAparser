#!/usr/bin/python
"""
    This is the main module
    It will create two ASA objects based on the filenames.
    ASA objects are defined in ASAclasses
    
"""

from ASAclassesFeb import ASAobject

asa_filename1="shortASA-NetObjTest.txt"
asa_filename2="shortASA-NetObjTest1.txt"
asalist=[]#this is a list of asa objects.

def inputASAdetails():
    """user input /filename to be used to create an ASA object"""

    print("lets create an ASA object")
    print("what would you like to call your ASA object [default asa01]")
    asaname=input()
    if len(asaname)<3:
        asaname="asa01"
    print("what is the filename? [default shortASA-NetObjTest.txt]")
    asa_filename1=input()
    if len(asa_filename1)<3:
        asa_filename1="shortASA-NetObjTest.txt"
    print("ASA name ", asaname)
    print("ASA filename ", asa_filename1)
       
    return(asaname,asa_filename1)
    
def outputPrompt():
    """ determine screen/file/both/none
        test that a file can be opened and written to
        returns the file name or 'None' if output to screen
    """
    asa_OUTfilename="None" #default value
    print("would you like to output to screen/file/both/none ? ")
    outputoption=input()
    outputoption=outputoption[:1] #trim to one char
    outputoption=outputoption.lower()
    print("output option ", outputoption)
    if outputoption=="f" or outputoption=="b":
        print("what is the filename? [default writeASA-NetObjTest.txt]")
        asa_OUTfilename=input()
        if len(asa_OUTfilename)<3:
            asa_OUTfilename="writeASA-NetObjTest.txt"
        print("output filename ", asa_OUTfilename)
        fileoutput=True
    elif outputoption=="s":
        asa_OUTfilename="screen"     
    else: fileoutput=False  
    print("testing file write now")
    if fileoutput : #open file for writing
        # I know I should put a try/except/else in here in the future
        testfile =open(asa_OUTfilename, 'w')
        testfile.write("this is a test\n")
        testfile.close()
        testfile =open(asa_OUTfilename, 'r')
        print(testfile.read())
    #else:    
    return (asa_OUTfilename)
    
    #end outputPrompt
    
def loadASAs():
    asalist.append(ASAobject(inputASAdetails())) #create the ASAobject through input and append to array
    asalist[asaindex].loadarray() #execute the load array function  
    print("length of asa object list is ", len(asalist[asaindex].networkobjarray))
    asalist[asaindex].wastefullsort(asalist[asaindex].networkobjarray,asalist[asaindex].sortednetworkobjarray)
    printOneASA(asalist[asaindex])
    
    
    
def compareASAs (asa1, asa2):  
    """compare network objects by name"""
    
    for name in asa1.sortednetworkobjarray 
      print("name ", name.name)
    return   

def testCompareASAs():
    """this function will create two ASA objects based on test values. 
        then it will call the compare function
        then the print/save function"""
    asa1obj=ASAobject("ASA1") #create the ASAobject
    asa1obj.loadarray() #execute the load array function  
    print("length of asa object list is ", len(asa1obj.networkobjarray))
    asa1obj.wastefullsort(asa1obj.networkobjarray,asa1obj.sortednetworkobjarray)
    asa2obj=ASAobject("ASA2","shortASA-NetObjTest5.txt") #create the second ASAobject
    asa2obj.loadarray() #execute the load array function  
    print("length of asa object list is ", len(asa2obj.networkobjarray))
    asa2obj.wastefullsort(asa2obj.networkobjarray, asa2obj.sortednetworkobjarray)
    return()
    
def printOneASA(asaobj):
    
    outfile=outputPrompt()#screen, none, or a real filename
    if outfile !="none"
    for netobj in asaobj.sortednetworkobjarray:
        if outfile=="screen" : 
            print("\n  sorted name ",netobj.name)
            for detail in netobj.paramlist:
                print("sorted detail ", detail)
    return()        

def displayASAnames():
    """each element in asalist will have an asa object with a name and filename"""
    if len(asalist)>0:
        print(len(asalist)," elements entered in ASA Parser")
        for element in asalist:
            print ("ASA name ", element.name)
            printOneASA(element)
    else:print("no ASAs Loaded")        
    return()
    
def mainmenu():    
    """this prints out the main menu and returns user input"""
    print("\n \n Welcome to Doug's ASA parser. It may one day be a thing of beauty, but it is not today")
    print("I'd be happy if it is useful enough and makes my job a little easier.")
    print("What would you like to do today?")
    print("<L> Load an ASA configuration text file")
    print("<D> Display Network Objects from an ASA Text file")
    print("<C> compare two ASA configuration text files")
    print("<F> Search/Find in a loaded ASA config")
    print("<Q> Quit or Exit")
    menuselect=input()
    menuselect=menuselect[:1] #slice to one char
    return(menuselect.lower()) #return the lower case selection letter

if __name__=="__main__":
    
    
    """This is my main program.  """
    quitmain=['q','Q','Quit']
    quit=False
    print("not Quit")
    
    while not quit:
        #mainmenu will return a lowercase char
        maininput=mainmenu()#
        asaindex=len(asalist)
        if maininput=='l': #loadASA object into asalist
            #load object will always append
            loadASA()
        elif maininput=='d': #display
            if len(asalist)<1:
                print("no ASA's loaded")
                loadASAS()
            displayASAnames()
            
            #
        elif maininput=='c': #compare
            pass  
        elif maininput=='f': #find/search
            printOneASA(asa1obj)       
        elif maininput=='q': #quit
            quit=True
            print("quit is true")
        #*******************************************    
        elif maininput=="1": #if maininput is number one, do a test on the thing i'm working on right now
            print(outputPrompt()) 
        #********************************************        
        elif maininput=="t": #run the sequence test.
            pass
        else:
            print("option not accounted for")
        
    #end while
        
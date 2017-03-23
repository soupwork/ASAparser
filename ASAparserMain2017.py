#!/usr/bin/python
"""
    This is the main module
    It will create two ASA objects based on the filenames.
    ASA objects are defined in ASAclasses
    
"""

from ASAclassesFeb import ASAobject, NetworkObject

asa_filename1="shortASA-NetObjTest1.txt"
asa_filename2="shortASA-NetObjTest1.txt"
asalist=[]#this is a list of asa objects.
blankparamlist=[" "*38,]
blanknetobj=NetworkObject("blank",blankparamlist)

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
    #'b' or 'f' is file output, 's' is screen, other is none
    if outputoption=="f" or outputoption=="b":
        print("what is the filename? [default writeASA-NetObjTest.txt]")
        asa_OUTfilename=input()
        if len(asa_OUTfilename)<3:
            asa_OUTfilename="writeASA-NetObjTest.txt"
        print("output filename ", asa_OUTfilename)
        fileoutput=True
    elif outputoption=="s":
        asa_OUTfilename="screen"
        fileoutput=False
    else: fileoutput=False  
   
    if fileoutput : #open file for writing
        print("testing file write now")
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
    asaname,asa_filename1=inputASAdetails()
    asalist.append(ASAobject(asaname,asa_filename1)) #create the ASAobject through input and append to array
    asalist[asaindex].loadarray() #execute the load array function  
    print("length of asa object list is ", len(asalist[asaindex].networkobjarray))
    asalist[asaindex].wastefullsort(asalist[asaindex].networkobjarray,asalist[asaindex].sortednetworkobjarray)
    #printOneASA(asalist[asaindex])
    return() #end loadASAs
    
def twoObjToOneList(leftobj=blanknetobj, midobj="    ", rightobj=blanknetobj):
    print("left object ", leftobj.name)
    print("middle object ", midobj)
    print("right object ", rightobj.name)
    
    return()


    
    
def compareASAs (asa1, asa2):  
    """compare network objects by name
        first check for equality
        second check for length
        third concatenate two strings into a single line/string
        forth return a list
        leftstring is asa1
        rightstring is asa2"""
    asa2index=0 #counter
    mergelist=[] #list containing name, and network object fields
    # asa1"a" < asa2"b"
    # asa1"A" < asa2"a"
    for asa1obj in asa1.sortednetworkobjarray:
        
        if asa1obj.name == asa2.sortednetworkobjarray[asa2index].name:
            """strings are the same, check length and put them in a single line""" 
            outline=asa1obj.name
            print("name ", asa1obj.name, " == ", asa2.sortednetworkobjarray[asa2index].name)
            asa2index+=1 #increment counter
        elif asa1obj.name < asa2.sortednetworkobjarray[asa2index].name:
            print("name ", asa1obj.name, " << ", asa2.sortednetworkobjarray[asa2index].name)
            #do not increment counter
        elif asa1obj.name > asa2.sortednetworkobjarray[asa2index].name:
            print("name ", asa1obj.name, " << ", asa2.sortednetworkobjarray[asa2index].name)
            asa2index+=1 #increment counter  
    return   

def testCompareASAs():
    """this function will create two ASA objects based on test values. 
        then it will call the compare function
        then the print/save function"""
    #create ASA1
    newlist=[] #list containing name, and network object fields
    asalist.append(ASAobject("ASA1",asa_filename1)) #create the ASAobject 
    asalist[0].loadarray() #execute the load array function  
    print("length of asa object list is ", len(asalist[0].networkobjarray))
    asalist[0].wastefullsort(asalist[0].networkobjarray,asalist[0].sortednetworkobjarray)
    #create ASA2
    asalist.append(ASAobject("ASA2")) #create the ASAobject 
    asalist[1].loadarray() #execute the load array function  
    print("length of asa object list is ", len(asalist[1].networkobjarray))
    asalist[1].wastefullsort(asalist[1].networkobjarray,asalist[1].sortednetworkobjarray)
    #now i have two asa objects, sorted. 
    
    #check output options
    #outputselect=outputPrompt()#outputselect will be filename 
    outputselect="writeASA-NetObjTest.txt"
    #run the compare function
    #compareASAs(asalist[0], asalist[1])    
    compareASAs(asalist[0], asalist[1])
    
    
    """ write function is working 
    for element in asalist[0].sortednetworkobjarray:
        newlist.append(element.onelist())
        #each newlist element is a list of strings: name, ip, description
        
    writelines(newlist)
    #write function is working
    """
        

    
    return()
    
 
        
def printOneASA(asaobj):
    newlist=[] #list containing name, and network object fields
    outfile=outputPrompt()#screen, none, or a real filename
    print("inside printOneASA, filename is ", outfile)
    if outfile=="screen" :
        print("create a list of stuff, then print to screen")
        for netobj in asaobj.sortednetworkobjarray:
            print("\n  sorted name ",netobj.name)
            for detail in netobj.paramlist:
                print("sorted detail ", detail)
    else: #create a list of stuff, then write it to file
        print("create a list of stuff, then write it to file")
        for netobj in asaobj.sortednetworkobjarray:    
            print("\n  sorted name for writing ",netobj.name)
            newlist.append(netobj.name)
            for detail in netobj.paramlist:
                print("sorted detail for writing ", detail) 
                newlist.append(detail)
        writelines(newlist,outfile)        
    return()        

    
def writelines (writelist, outputselect="writeASA-NetObjTest.txt"):
    """write to a file. outputselect is filename
        writelist is list of lines to be appended to file.
        writelist, outputselect="writeASA-NetObjTest.txt"    """
    print("output select is ", outputselect)
    fileout=open(outputselect, 'a')#open filename, append to end
    
    for element in writelist:
        #print( line[0], "writelist element , line element 0")
        #print( line[1], "writelist element , line element 1")
        print ("write element ", element)
        fileout.write(element)
        fileout.write(" \n")
            
    fileout.close() #close the file    
    return    
    
def displayASAnames():
    """each element in asalist will have an asa object with a name and filename
        Called from Main Menu(D)"""
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
            loadASAs()
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
            print(testCompareASAs()) 
        #********************************************        
        elif maininput=="t": #run the sequence test.
            pass
        else:
            print("option not accounted for")
        
    #end while
        
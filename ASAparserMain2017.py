#!/usr/bin/python
"""
    This is the main module
    It will create two ASA objects based on the filenames.
    ASA objects are defined in ASAclasses
    
"""
#copyright (c)2017 Douglas J. Sheehan, Doug Sheehan IT Consulting. Free to use. Credit where due please.

from ASAclasses import ASAobject, NetworkObject

asafilename1="shortASA-NetObjTest1.txt"
asafilename2="shortASA-NetObjTest1.txt"
asalist=[]#this is a list of asa objects.
blankparamlist=[" "*38,]
blanknetobj=NetworkObject("blank", "object network", blankparamlist)
asaindex=0 

def inputASAdetails():
    """user input /filename to be used to create an ASA object
        Called from loadASAs """

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
    
    
def loadASAs(asalist, asaname="promptuser", asafilename=asafilename1):
    # is asalist global? if i add two asaobjects to asalist[], will they be indexed?
    if asaname == "promptuser":
        asaname,asa_filename1=inputASAdetails()
        
    asaindex=len(asalist) #length before append will be index after append
    asalist.append(ASAobject(asaname,asafilename)) #create the ASAobject through input and append to array
     
    asalist[asaindex].loadarray() #execute the load array function inside ASA object class
    #if len
    asalist[asaindex].wastefullsort(asalist[asaindex].networkobjarray,asalist[asaindex].sortednetworkobjarray)
    asalist[asaindex].wastefullsort(asalist[asaindex].netobjgrouparray,asalist[asaindex].sortedNetObjGrouparray)
    asalist[asaindex].wastefullsort(asalist[asaindex].serviceobjarray,asalist[asaindex].sortedServiceObjarray)
    
    
    #printOneASA(asalist[asaindex])
    return() #end loadASAs   

    
def displayASAnames():
    """each element in asalist will have an asa object with a name and filename
        Called from Main Menu(D)"""
    if len(asalist)>0:
        print(len(asalist)," elements entered in ASA Parser")
        for element in asalist:
            print ("ASA name ", element.name)
            displayOneASA(element)
    else:print("no ASAs Loaded")        
    return()  

        
def displayOneASA(asaobj):
    newlist=[] #list containing name, and network object fields
   
    print("inside displayOneASA")
    print("create a list of stuff, then print to screen")
    for netobj in asaobj.sortednetworkobjarray:
        newlist.clear()
        print("\n  sorted name ",netobj.name)
        print("\n  sorted type ",netobj.objtype)
        newlist.append(netobj.onelist())
        print(newlist)
    return()            

def outFilePrompt():
    """ 
        test that a file can be opened and written to
        returns the file name or 'None' if output to screen
    """
    asa_OUTfilename="None" #default value
    print("what is the filename? [default writeASA-NetObjTest.txt]")
    asa_OUTfilename=input()
    if len(asa_OUTfilename)<3:
        asa_OUTfilename="writeASA-NetObjTest.txt"
    print("output filename ", asa_OUTfilename)
    #open file for writing
    print("testing file write now")
    # I know I should put a try/except/else in here in the future
    try:
        testfile =open(asa_OUTfilename, 'w')
        testfile.write("this is a test\n")
        testfile.close()
    except:
        print("file write error")
    testfile =open(asa_OUTfilename, 'r')
    print(testfile.read())
       
    return (asa_OUTfilename)
    #end outFilePrompt
    

 
def saveOneASA(asaobj):
    
    outfile=outFilePrompt()#
    print("inside saveOneASA, filename is ", outfile)
    #create a list of stuff, then write it to file
    print("create a list of stuff, then write it to file")
    for netobj in asaobj.sortednetworkobjarray: 
        print("\n  sorted name for writing ",netobj.name)
        print("\n  sorted type for writing ",netobj.objtype)
        writedata(netobj.onelist(),outfile) 
    
    return()      
  

def saveAllASAs():
    newlist=[] #list containing name, and network object fields
    outfile=outFilePrompt()#
    print("inside saveAllASAs, filename is ", outfile)
   #create a list of stuff, then write it to file 
    for element in asalist:
        for netobj in element.sortednetworkobjarray: 
            print("\n  sorted name for writing ",netobj.name)
            print("\n  sorted type for writing ",netobj.objtype)
            writedata(netobj.onelist(),outfile) #onelist will take name,type,and params and put into one list        
    return()  
    
def writedata (writelist):
    """write to a file. asa_outfile is filename
       writelist is list of lines to be appended to file.
    """
    asa_outfile="asa_outfile.txt"
    fileout=open(asa_outfile, 'a')#open filename, append to end
    fileout.write(asa_outfile + "\n"+"\n")
    for element in writelist:
        fileout.write(element+ "\n")
        
    fileout.close() #close the file     
    return  
    
def makeOneLine(leftstring="*",midstring=" ",rightstring="*"):
    
    if leftstring != rightstring:
        midstring="****"
        
    singlestring=('{:^38}{}{:^38}').format(leftstring,midstring,rightstring)
    print("make one line single string is \n", singlestring)
    return(singlestring)
#end make One Line- make one string from three Strings    
    
def twoListToOneList(leftlist=blankparamlist, midobj="    ", rightlist=blankparamlist):
    """ left and right elements in left and right lists should be converted to a single string in this method,
        and return as a single list"""
    mergelist=[] #
    count=0
    lenleftlist=len(leftlist)#if length is less than 3, it is blank. this is number of list entries in the list.
    lenrightlist=len(rightlist)
    shortlen=len(leftlist)
    biglist=rightlist #it is a guess
    
    #are both lists the same size? do I need to add blank lines?
    if lenrightlist<shortlen :
        shortlen=len(rightlist)
        biglist=leftlist #i must have guessed wrong
        
    print("shortlength is ", shortlen)
    
    if (lenleftlist>1) and (lenrightlist>1):#no blanks-both lists are real network objects
        for count in range(len(biglist)): #iterate through the larger list
            if count<shortlen:
                tempstring=makeOneLine(leftlist[count],"    ",rightlist[count])
            elif biglist==rightlist:
                tempstring=makeOneLine(rightstring=rightlist[count])
            else: #biglist = leftlist
                tempstring=makeOneLine(leftstring=leftlist[count])
                
            print(tempstring, "tempstring, twoObjToOneList")
            mergelist.append(tempstring)
    else: #one list is blank
        for ndex in range(len(leftlist)): #will count starting at 0
            print("leftlist ", leftlist[count])
            tempstring=str(leftlist[count])
            print(tempstring, "tempstring, twoObjToOneList")
            count += 1
            mergelist.append(tempstring)

    return(mergelist)
#end two Lists of Strings to One List of Strings
    
def twoListObjToOneList(leftobj=blanknetobj, midobj="    ", rightobj=blanknetobj):
    """pass in one or two objects
        check if either are blank (name is blank)
        call onelist method on each network object
        call twoListToOneList
        """
    mergelist=[] #
    singlestring=" " #
    count=0
    print (" twoListObjToOneList ")
    if leftobj.name=="blank":
        rightlist=rightobj.onelist()
        print("blank left ")
        mergelist=twoListToOneList(rightlist=rightlist)
       
    elif rightobj.name=="blank":
        print("blank right ")
        leftlist=leftobj.onelist()
        mergelist=twoListToOneList(leftlist=leftlist)
    else:
        print("no blank ")
        leftlist=leftobj.onelist()
        rightlist=rightobj.onelist()
        mergelist=twoListToOneList(leftlist=leftlist, rightlist=rightlist)
        
    #confirmed each element returned in mergelist is a string
    #print(type(line), ">>>>", line)
    return(mergelist)    
#end twoListObj to One List of Strings

def compareObjLists (testlist1, testlist2):
    """ INPUT two object lists, OUTPUT to Screen,  
    """
    mergelist=[]
    list1count=0
    list1len=len(testlist1)
    list2count=0
    list2len=len(testlist2)
    endcompare = false 
    while not endcompare:
        if testlist1[list1count].name == testlist2[list2count].name :
            """strings are the same, check length and put them in a single line""" 
            print("name ", testlist1[list1count].name, " == ", testlist2[list2count].name)
            #mergelist=twoListObjToOneList(testlist1[list1count].name," == ",testlist2[list2count].name)
            #print("compare fn, mergelist = " , mergelist)
            #increment both counters
                
        elif testlist1[list1count].name < testlist1[list1count].name:#A<B and A<a and B<a
            print("name ", testlist1[list1count].name, " << ", testlist2[list2count].name)
            #mergelist.append(twoListObjToOneList(testlist1[list1count]," << ",blank))
            #print("compare fn, mergelist < " , mergelist)
            #do not increment counter
                
        elif testlist1[list1count].name > testlist1[list1count].name:#A<B and A<a
            print("name ", testlist1[list1count].name, " >> ", testlist2[list2count].name)
            #mergelist.append(twoListObjToOneList(asa1obj," == ",asa2.sortednetworkobjarray[asa2index]))
            #print("compare fn, mergelist >" , mergelist)
         if 
    # mergelist is now a big list of (list of strings) 

    return()
#end Compare Two Object Lists    
    
def compareASAs (asa1, asa2):  #compare complete ASAs, write simularities and differences to a file
    """compare network objects by name. INPUT two ASA objects, OUTPUT file write
        first check for equality
        second check for length
        third concatenate two strings into a single line/string
        forth return a list
        leftstring is asa1
        rightstring is asa2"""
    asa2index=0 #counter
    mergelist=[] #list containing name, and network object fields
    writelist=[] #list of strings for writelines_
    # asa1"a" < asa2"b"
    # asa1"A" < asa2"a"
    for asa1obj in asa1.sortednetworkobjarray:
        if asa1obj.name == asa2.sortednetworkobjarray[asa2index].name:
            """strings are the same, check length and put them in a single line""" 
            print("name ", asa1obj.name, " == ", asa2.sortednetworkobjarray[asa2index].name)
            mergelist=twoListObjToOneList(asa1obj," == ",asa2.sortednetworkobjarray[asa2index])
            #print("compare fn, mergelist = " , mergelist)
            asa2index+=1 #increment counter
            
        elif asa1obj.name < asa2.sortednetworkobjarray[asa2index].name:#A<B and A<a
            print("name ", asa1obj.name, " << ", asa2.sortednetworkobjarray[asa2index].name)
            mergelist.append(twoListObjToOneList(asa1obj," == ",asa2.sortednetworkobjarray[asa2index]))
            #print("compare fn, mergelist < " , mergelist)
            #do not increment counter
            
        elif asa1obj.name > asa2.sortednetworkobjarray[asa2index].name:#A<B and A<a
            print("name ", asa1obj.name, " >> ", asa2.sortednetworkobjarray[asa2index].name)
            mergelist.append(twoListObjToOneList(asa1obj," == ",asa2.sortednetworkobjarray[asa2index]))
            #print("compare fn, mergelist >" , mergelist)
            asa2index+=1 #increment counter  
    # mergelist is now a big list of (list of strings) 
    for listelement in mergelist:
        for textelement in listelement:
            writelist.append(textelement)
    
    writedata(writelist)
    writelist.clear()
    return   
 #end CompareASAs
 
def testthis():
    """this is a function to make testing a little quicker
        ASA1 and ASA2 
        """
    asafilename1="shortASA-NetObjTest1.txt"
    asafilename2="shortASA-NetObjTest1a.txt"
    #load ASAs loads the object lists as well as the sorted object list for network, group, service, and acl.
    loadASAs(asalist, "asa01", asafilename1)
    loadASAs(asalist, "asa02", asafilename2)
    #two asa's loaded. check for differences
    compareObjLists(asalist[0].sortednetworkobjarray, asalist[1].sortednetworkobjarray)


    
def mainmenu():    
    """this prints out the main menu and returns user input"""
    print("\n \n Welcome to Doug's ASA parser. It may one day be a thing of beauty, but it is not today")
    print("I'd be happy if it is useful enough and makes my job a little easier.")
    print("What would you like to do today?")
    print("<L> Load an ASA configuration text file")
    print("<D> Display (screen)Network Objects from an ASA Text file")
    print("<S> Save an ASA object details to a text file")
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
            loadASAs(asalist)
            
        elif maininput=='d': #display
            if len(asalist)<1:
                print("no ASA's loaded")
                loadASAS(asalist)
            displayASAnames()
            
            #
        elif maininput=='s': #save file
            if len(asalist)<1:
                print("no ASA's loaded")
                loadASAS(asalist)
            saveAllASAs()
            
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
            testthis() 
        #********************************************        
        elif maininput=="t": #run the sequence test.
            pass
        else:
            print("option not accounted for")
        
    #end while
        
#!/usr/local/bin/python
import copy

"""This file holds the ASA Classes to include
    ASAobject
        The big class that holds all of the other ASA objects
        This class will have lists(arrays) of each kind of sub-object.
        so one list of Network Objects, one list of Service objects, one list of ACL's
        
    Network Objects
        ASA Network Object Hosts have a single IP Address
        ASA Network Object Networks have a network assigned (ex. /24)
    Service Objects
        ASA TCP and UDP ports
    the working version is "ASAclassesMonth"  while the backup versions are ASAclassesYYYYmmmDD 
"""        
class ASAobject():
    """ this is the big class
    ASAobject will have an array(list) of network objects called networkobjarray(element starts with )
    ASAobject will have an array(list) of network group objects called netGroupobjarray(element starts with  object-group network )
    ASAobject will have an array(list) of service/port objects called serviceobjarray (element starts with )
    ASAobject will have an array(list) of service/port group objects called svcGroupobjarray (element starts with object-group service)
     (
    object-group network (starts with )
                will have a method to load array
                will have a method to sort array
                
    """
    ASAnumber=0 #this is a class attribute, shared by all instances, increments each time a new ASAobject is created.
    
    def __init__ (self, name, asafilename="shortASA-NetObjTest.txt"): 
    
        """ init docstring """
        # asafilename="shortASA-NetObjTest.txt" default filename added for testing
        self.networkobjarray=[] #instance list of complete network objects
        self.sortednetworkobjarray=[] #instance list of complete network objects
        self.name=name
        self.asafilename = asafilename
        return #end init
 
        
    def loadarray (self):
        """ vars
                asafilename
                arrayindex
                datasource
                dataline
                tempstring
                objindex
                objname
                objtype
        """        
        paramlist=[] #test values for paramlist
        with open(self.asafilename, 'r') as datasource:
            arrayindex=0
            for dataline in datasource: #each iteration reads a line from file
                tempstring=dataline
                
                while "object network " in tempstring: #load up parameter list 
                    #[0:15] is slice that contains obj network
                    objindex=0
                    objname=tempstring[15:-1]
                    objtype=tempstring[:14]
                    print("object type is ", objtype)
                    tempstring=datasource.readline()
                    while tempstring.startswith(" "):
                        #print("length ", len(tempstring))
                        tempstring=tempstring.strip() #remove leading/trailing spaces
                        #print("stripped length ", len(tempstring))
                        if (len(tempstring)>1) and (len(paramlist)>objindex):
                            paramlist[objindex]=tempstring #add tempstring to the the list
                        else:
                            paramlist.append(tempstring)
                            
                        objindex+=1 #increment param list index
                        tempstring=datasource.readline()
                    #end while - load up param list
                    #now create object and add to networkobjarray

                    tempnetobj=NetworkObject(objname, objtype, paramlist)
                    paramlist.clear() #
                    tempnetobj.printobj()                    
                    self.networkobjarray.append(tempnetobj)
                    arrayindex += 1 #increment index
               
                # end while-create network object
                
        return() #end load array
    
    def wastefullsort(self, networkobjarray, sortednetworkobjarray):
        #sort network objects by name
        #print("Wasteful Sort Network Objects by Name")
        """
          if element is first element, append to sortednetworkobjarray (position 0)
          if element is greater than last element in sortednetworkobjarray, append to list
          if element is less than last element, count backwards until it is greater and insert
          last index of a list is listname[:(len(listname)-1)]
         """
        #for first pass
        arrayindex=0 #reset counter
        sortindex=0
        
        #len(objectarray) is one more than the max index
        for testobject in networkobjarray: #each pass picks one element
            #print("test object pass# ", sortindex)
            if (len(sortednetworkobjarray) < 1): 
                sortednetworkobjarray.append(testobject)
                #print("first element")
            else: #count backwards from end until sort position found
                count=len(sortednetworkobjarray) #count is index of last position
                #print("else count is ", count)
                if testobject.name < sortednetworkobjarray[count-1].name:
                    print("testobject.name < sortednetworkobjarray[count].name >>proceed to while loop")
                while (testobject.name < sortednetworkobjarray[count-1].name) and (count>0):
                    count-=1 #decrement counter same as count = count-1
                #end while
                print(testobject.name, " < ", sortednetworkobjarray[count-1].name)
                (testobject.name).strip() #remove leading/trailing spaces
                sortednetworkobjarray.insert(count,testobject)
            #end if-find sort position    
            print("testobject ", testobject.name, id(testobject))
            print("testobject ", testobject.objtype)
            print("sort index ", sortindex, sortednetworkobjarray[sortindex].name)
            print("\n *************************************\n")
            sortindex +=1 #increment index
            
        #end for loop    
        print("end wastefull sort")
        print("length of sorted array is ",len(sortednetworkobjarray), " elements")
        return() #end Wastefull Sort
 
    def set38chars(self, teststring):
        """this function will adjust to 38 chars for print and file output
            teststring may be greater or less than 38 chars
            shortstring is the new string. extrastring is the leftovers
            realisticly, only description will be longer than 38 chars"""
        teststring=teststring.strip() #if length is 38, don't change anything  
        stringlen=len(teststring)
        print("Length of teststring is ", stringlen)    
        if stringlen<38:
            #padding=" "*(38-stringlen)
            #print("Length of padding is ", len(padding))
            #newstring=teststring+padding
            teststring=teststring.ljust(38)
        elif stringlen>8 and teststring.startswith("description"):
            #check if starts with description
            print("starts with description")
            
        
        print("Length of adjusted teststring is ", len(teststring))   
        return(teststring)
 
    def printarray(self, testarray):
        """ prints networkobjarray or sortednetworkobjarray"""
        print("inside printarray")
        for testobject in testarray:
             print ("testname ", testobject.name)
             
        return  #end print array     
    

    #end class ASAobject
        
# *************  begin Network object class *************
class NetworkObject():
    """ ASA Network Object will have a name, type, description, ip address or network"""
    """
    Variables declared at the class level are not default values
    name = string
    type = string (object network, object-group network, object service, object-group service)
    ipv4 = ip address(host) or network
    description = string
    paramlist should be ipv4 then description
    methods
    init(name,host,description)
    """    
    

    def __init__(self, name, objtype, paramlist):
        self.name=name
        self.objtype=objtype
        self.paramlist = list(paramlist) #copy the list
        #print("new network object, ", name)
        #for field in self.paramlist:
           #print( "paramlist  ", field)
        
    
    def printobj(self):
        print("obj name ", self.name)
        print("obj type ", self.objtype)
        for field in self.paramlist:
            print( "  ", field)
        return (self.name)
        
    def onelist (self):
        """take the name,type, and param list and form into a single list"""
        newlist=[self.name]
        newlist.append(self.objtype)
        leftstring,rightstring="init","init"
        print("len paramlist ", len(self.paramlist))
        #print("param list ID ", id(self.paramlist)) #verified they are all different objects
        for element in self.paramlist:
            leftstring=str(element)
            
            while rightstring: #keep repeating until rightstring is empty
                leftstring,rightstring=self.set38chars(leftstring)
                #print(leftstring, "left string ** right string ", rightstring)
                #print()
                newlist.append(leftstring) #write it to the list
                leftstring=str(rightstring) #move the leftovers and rerun
            #end while
            rightstring="init" #re-enable rightstring for next element

        return(newlist) #return a list of strings of the name, type, and details of network objects

    def set38chars(self, teststring):
        """this function will adjust to 38 chars for print and file output
            teststring may be greater or less than 38 chars
            shortstring is the new string. extrastring is the leftovers
            realisticly, only description will be longer than 38 chars
            leftstring is trimmed, rightstring is extra"""
        leftstring=teststring.strip()  
        stringlen=len(leftstring)
        rightstring =  "eggs"
        #print("Length of teststring is ", stringlen)    
        if stringlen<=38:
            print("string is less than than 38")
            leftstring=leftstring.ljust(38)
            rightstring="" #null out rightstring
            
        elif stringlen>38 and leftstring.startswith("description "):#will not execute if desc less than 38
            #check if starts with description (descriptions will have spaces)
            print("starts with description")
            rightstring=leftstring[12:] 
            leftstring=leftstring[:12]
            
        else:#string is greater than 38. find the last space before 38 and trim.
                #otherwise trim at 38
            print("string is greater than 38")
            rightspace=leftstring.rfind(" ",0,38)
            if rightspace==-1: #rfind returns -1 if " " is not in string
                print("rightspace true, no spaces found ")
                rightspace=38
                
            rightstring=leftstring[rightspace:]
            leftstring=leftstring[:rightspace]
            
        
        #print(leftstring, " << left string ** right string >> ", rightstring)
        #print("Length of adjusted teststring is ", len(leftstring))   
        return(leftstring, rightstring)
        
##************* end network object class *************
  
 


    
if __name__=="__main__":
    print("running __main__ ASAclassesFeb")
    asa1obj=ASAobject("ASA1") #create the ASAobject
    asa1obj.loadarray() #execute the load array function 
    print("length of asa object list is ", len(asa1obj.networkobjarray))
    
    asa1obj.wastefullsort(asa1obj.networkobjarray,asa1obj.sortednetworkobjarray)  
    for netobj in asa1obj.sortednetworkobjarray:
        print("\n  sorted name ",netobj.name)
        newlist=netobj.onelist()
        print("main newlist", newlist)
        newlist.clear()
    
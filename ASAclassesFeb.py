#!/usr/bin/python
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
    ASAobject will have an array(list) of network objects
                will have a method to load array
                will have a method to sort array
                
    """
    ASAnumber=0 #this is a class attribute, shared by all instances, increments each time a new ASAobject is created.
    
    def __init__ (self, name, asafilename="shortASA-NetObjTest.txt"): 
    
        """ init docstring """
        # asafilename="shortASA-NetObjTest.txt" default filename added for testing
        self.networkobjarray=[] #instance list of complete network objects
        self.sortednetworkobjarray=[] #instance list of complete network objects
        
        self.asafilename = asafilename
        print("inside __init__")
        print(self.asafilename)
       
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
        """        
        paramlist=["host", "description"] #test values for paramlist
        with open(self.asafilename, 'r') as datasource:
            arrayindex=0
            for dataline in datasource: #each iteration reads a line from file
                tempstring=dataline
                #if (len(tempstring)>1):
                    #tempstring = tempstring[:-1] #remove the newline from the end
                while "object network " in tempstring: 
                    #[0:15] is slice that contains obj network
                    objindex=0
                    objname=tempstring[15:-1]
                    tempstring=datasource.readline()
                    while tempstring.startswith(" "):
                        if (len(tempstring)>1) and (len(paramlist)>objindex):
                            paramlist[objindex]=tempstring[:-1] #remove the newline from the end
                        else:
                            paramlist.append(tempstring[:-1])
                        objindex+=1 #increment param list index
                        tempstring=datasource.readline()
                    #end while - load up param list
                    #now create object and add to networkobjarray
                    tempnetobj=NetworkObject(objname,paramlist)
                    self.networkobjarray.append(tempnetobj)
                    arrayindex += 1 #increment index
               
                # end while-create network object
                
        return() #end load array
    
    def wastefullsort(self, networkobjarray, sortednetworkobjarray):
        
        #sort network objects by name
        print("Wasteful Sort Network Objects by Name")
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
            print("test object pass# ", sortindex)
            if (len(sortednetworkobjarray) < 1): 
                sortednetworkobjarray.append(testobject)
                print("first element")
            else: #count backwards from end until sort position found
                count=len(sortednetworkobjarray) #count is index of last position
                print("else count is ", count)
                if testobject.name < sortednetworkobjarray[count-1].name:
                    print("testobject.name < sortednetworkobjarray[count].name >>proceed to while loop")
                while (testobject.name < sortednetworkobjarray[count-1].name) and (count>0):
                    count-=1 #decrement counter same as count = count-1
                    print("inside while count is ", count)
                    #end while
                    print(testobject.name, " < ", sortednetworkobjarray[count-1].name)
                print("outside while count is ", count)
                print(testobject.name, " >= ", sortednetworkobjarray[count-1].name)
               
                sortednetworkobjarray.insert(count,testobject)
                
            print("testobject ", testobject.name, id(testobject))
            print("sort index ", sortindex, sortednetworkobjarray[sortindex].name)
            print("\n *************************************\n")
            sortindex +=1 #increment index
            
        #end for loop    
        print("end wastefull sort")   
        return() #end Wastefull Sort
    
    def printarray(self, testarray):
        """ prints networkobjarray or sortednetworkobjarray"""
        print("inside printarray")
        for testobject in testarray:
             print ("testname ", testobject.name)
             
        return  #end print array     
    #end class ASAobject
        
# *************  begin Network object class *************
class NetworkObject():
    """ ASA Network Object will have a name, description, ip address or network"""
    """
    Variables declared at the class level are not default values
    name = string
    ipv4 = ip address(host) or network
    description = string
    paramlist should be ipv4 then description
    methods
    init(name,host,description)
    """    
    

    def __init__(self,name,paramlist):
        self.name=name
        self.paramlist = list(paramlist) #copy the list
        #print("new network object, ", name)
        #for field in self.paramlist:
        #   print( "paramlist  ", field)
        
    
    def printobj(self):
        print("obj name ", self.name)
        for field in self.paramlist:
            print( "  ", field)
        return (self.name)
##************* end network object class *************
  



    
if __name__=="__main__":
    print("running __main__ ASAclassesFeb")
    asa1obj=ASAobject("ASA1", "shortASA-NetObjTest.txt") #create the ASAobject
    asa1obj.loadarray() #execute the load array function 
    print("length of asa object list is ", len(asa1obj.networkobjarray))
    
    #asa1obj.printarray(asa1obj.networkobjarray)   
    asa1obj.wastefullsort(asa1obj.networkobjarray,asa1obj.sortednetworkobjarray)  
    for netobj in asa1obj.sortednetworkobjarray:
        print("\n  sorted name ",netobj.name)
        for detail in netobj.paramlist:
            print("sorted detail ", detail)      
    #print(asa1obj.networkobjarray[0].name)
    # print(asa1obj.networkobjarray[0].paramlist[0])
    # print(asa1obj.networkobjarray[0].paramlist[1])

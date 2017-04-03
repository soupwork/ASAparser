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
    ASAobject will have an array(list) of ACL objects called aclobjarray
    
    
    
    object-group network (starts with )
                will have a method to load array
                will have a method to sort array
                
    """
    ASAnumber=0 #this is a class attribute, shared by all instances, increments each time a new ASAobject is created.
    
    def __init__ (self, name, asafilename="shortASA-NetObjTest1.txt"): 
    
        """ init docstring """
        # asafilename="shortASA-NetObjTest.txt" default filename added for testing
        self.networkobjarray=[] #instance list of complete network objects
        self.netobjGrouparray=[] #instance list of complete network object groups
        self.serviceobjarray=[] #instance list of complete service(port) objects
        self.aclobjarray=[] #instance list of complete ACL objects
        self.sortednetworkobjarray=[] #instance list of complete network objects
        self.sortedNetObjGrouparray=[] #instance list of complete network objects
        self.sortedServiceObjarray=[] #instance list of complete network objects
        self.sortedACLobjarray=[] #instance list of complete network objects
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
        paramlist=[] #parameter list
        with open(self.asafilename, 'r') as datasource:
        
            arrayindex=0
            for dataline in datasource: #each iteration reads a line from file
                tempstring=dataline
                while "object network " in tempstring: #load up parameter list 
                    #[0:15] is slice that contains obj network
                    objindex=0
                    typestart=tempstring.find("object network ")
                    objname=tempstring[typestart+15:-1]#-1 to remove the newline
                    #print("object name is ", objname)
                    objtype=tempstring[typestart:typestart+15]
                    #print("object type is ", objtype)
                    tempstring=datasource.readline()
                    while tempstring.startswith(" "):
                        tempstring=tempstring.strip() #remove leading/trailing spaces
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
                
                while "object-group network  " in tempstring: #load up parameter list 
                    #[0:20] is slice that contains obj network
                    objindex=0
                    typestart=tempstring.find("object network ")
                    objname=tempstring[typestart+20:-1]#-1 to remove the newline
                    #print("object name is ", objname)
                    objtype=tempstring[typestart:typestart+20]
                    #print("object type is ", objtype)
                    tempstring=datasource.readline()
                    while tempstring.startswith(" "):
                        tempstring=tempstring.strip() #remove leading/trailing spaces
                        if (len(tempstring)>1) and (len(paramlist)>objindex):
                            paramlist[objindex]=tempstring #add tempstring to the the list
                        else:
                            paramlist.append(tempstring)
                            
                        objindex+=1 #increment param list index
                        tempstring=datasource.readline()
                    #end while - load up param list
                    #now create object and add to networkobjarray

                    tempnetobj=NetworkObject(objname, objtype, paramlist)
                   
                    tempnetobj.printobj()                    
                    self.networkobjarray.append(tempnetobj)
                    arrayindex += 1 #increment index
                    paramlist.clear() #
                # end while-create network object group
        
                while "object-group service " in tempstring: #load up parameter list 
                    #[0:20] is slice that contains object-group service
                    objindex=0
                    typestart=tempstring.find("object-group service ")
                    objname=tempstring[typestart+20:-1]#-1 to remove the newline
                    #print("object name is ", objname)
                    objtype=tempstring[typestart:typestart+20]
                    #print("object type is ", objtype)
                    tempstring=datasource.readline()
                    while tempstring.startswith(" "):
                        tempstring=tempstring.strip() #remove leading/trailing spaces
                        if (len(tempstring)>1) and (len(paramlist)>objindex):
                            paramlist[objindex]=tempstring #add tempstring to the the list
                        else:
                            paramlist.append(tempstring)
                            
                        objindex+=1 #increment param list index
                        tempstring=datasource.readline()
                    #end while - load up param list
                    #now create object and add to networkobjarray

                    tempnetobj=ServiceObject(objname, objtype, paramlist)
                    paramlist.clear() #
                    tempnetobj.printobj()                    
                    self.serviceobjarray.append(tempnetobj)
                    arrayindex += 1 #increment index
               
                # end while-create object-group service
        
                while "access-list " in tempstring:
                    #[0:11] is slice that contains access-list 
                    objindex=0
                    typestart=tempstring.find("access-list ")
                    objstring=tempstring[typestart+11:-1]#-1 to remove the newline
                    print("acl name is ", objname)
                    objtype=tempstring[typestart:typestart+11]
                    #print("object type is ", objtype)
                    tempstring=datasource.readline()
                    
                    #now create object and add to networkobjarray

                    tempnetobj=ACLObject(objstring)
                    #
                                        
                    self.aclobjarray.append(tempnetobj)
                    arrayindex += 1 #increment index
               
                # end while-create network object
        return() #end load array


    def loadACLarray (self):
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
        paramlist=[] #parameter list
        with open(self.asafilename, 'r') as datasource:

            for dataline in datasource: #each iteration reads a line from file
                tempstring=dataline
                while "remark " in tempstring: # if "remark" is in tempstring, the entry should be dropped
                     tempstring=datasource.readline()
                     
                while "access-list " in tempstring: #load up parameter list 
                    #[0:11] is slice that contains "access-list "
                    
                    #"extended" is the separation between the name and the rule
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

                    tempnetobj=ACLObject(objname, objtype, paramlist)
                    paramlist.clear() #
                    tempnetobj.printobj()                    
                    self.aclobjarray.append(tempnetobj)
               
                # end while-create network object
                
        return() #end load ACL array

        
    def wastefullsort(self, networkobjarray, sortednetworkobjarray):
        #sort network objects by name
        #print("Wasteful Sort Network Objects by Name")
        """
          if element is first element, append to sortednetworkobjarray (position 0)
          if element is greater than last element in sortednetworkobjarray, append to list
          if element is less than last element, count backwards until it is greater and insert
          #A<B and A<a
          last index of a list is listname[:(len(listname)-1)]
         """
        #for first pass
        arrayindex=0 #reset counter
        sortindex=0
        
        #len(objectarray) is one more than the max index
        for testobject in networkobjarray: #each pass picks one element
            #print("test object pass# ", sortindex)
            if (len(sortednetworkobjarray) < 1): #first element
                sortednetworkobjarray.append(testobject)
                print("first element")
            else: #count backwards from end until sort position found
                count=len(sortednetworkobjarray) #count is index of last position
                #print("else count is ", count)
                if testobject.name < sortednetworkobjarray[count-1].name:#A<B and A<a
                    print("testobject.name < sortednetworkobjarray[count].name >>proceed to while loop")
                    
                while (testobject.name < sortednetworkobjarray[count-1].name) and (count>0):
                    count-=1 #decrement counter same as count = count-1
                    
                #end while
                print(testobject.name, " < ", sortednetworkobjarray[count-1].name)
                (testobject.name).strip() #remove leading/trailing spaces
                sortednetworkobjarray.insert(count,testobject)
            #end if-find sort position    
            # print("testobject ", testobject.name, id(testobject))
            #print("testobject ", testobject.objtype)
            #print("sort index ", sortindex, sortednetworkobjarray[sortindex].name)
            #print("\n *************************************\n")
            sortindex +=1 #increment index
            
        #end for loop    
        print("end wastefull sort")
        print("length of sorted array is ",len(sortednetworkobjarray), " elements")
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
        
        newlist=[]
        if len(self.name)<38:
          newlist.append(self.name.ljust(38))
        
        newlist.append(self.objtype.ljust(38))
        leftstring,rightstring="init","init"
        
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
        #print("onelist newlist ", newlist)
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
            #print("string is less than than 38")
            leftstring=leftstring.ljust(38)
            rightstring="" #null out rightstring
            #alternate method for setting 38 chars
              #teststring=('{:^38}').format(teststring)#set width=38
            
        elif stringlen>38 and leftstring.startswith("description "):#will not execute if desc less than 38
            #check if starts with description (descriptions will have spaces)
            #print("starts with description")
            rightstring=leftstring[12:] 
            leftstring=leftstring[:12]
            
        else:#string is greater than 38. find the last space before 38 and trim.
                #otherwise trim at 38
            #print("string is greater than 38")
            rightspace=leftstring.rfind(" ",0,38)
            if rightspace==-1: #rfind returns -1 if " " is not in string
                print("rightspace true, no spaces found ")
                rightspace=38
                
            rightstring=leftstring[rightspace:]
            leftstring=leftstring[:rightspace]
            
        
        print(leftstring, " << left string ** right string >> ", rightstring)
        #print("Length of adjusted teststring is ", len(leftstring))   
        return(leftstring, rightstring)
        
##************* end network object class *************
  

class ACLObject():
    """ ASA ACL Object is sufficiently different to need a new class.
        will have a full-string, name, index, type (permit/deny) TCP/UDP, source, destination, ports and parameter list
        Variables declared at the class level are not default values
        name = string
        type = string (object network, object-group network, object service, object-group service)
        ipv4 = ip address(host) or network
        description = string
        paramlist should be ipv4 then description
        methods
        init(name,type)
    """    
    def __init__(self, aclstring):
        #self.name=name
        #self.objtype=objtype
        #self.paramlist = list(paramlist) #copy the list
        #print("new network object, ", name)
        #for field in self.paramlist:
           #print( "paramlist  ", field)
        pass
    
    def printobj(self):
        print("obj name ", self.name)
        print("obj type ", self.objtype)
        for field in self.paramlist:
            print( "  ", field)
        return (self.name)
    """        
    def onelist (self):
        "" "take the name,type, and param list and form into a single list"" "
        
        newlist=[]
        if len(self.name)<38:
          newlist.append(self.name.ljust(38))
        
        newlist.append(self.objtype.ljust(38))
        leftstring,rightstring="init","init"
        
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
        print("onelist newlist ", newlist)
        return(newlist) #return a list of strings of the name, type, and details of network objects

    def set38chars(self, teststring):
        "" "this function will adjust to 38 chars for print and file output
            teststring may be greater or less than 38 chars
            shortstring is the new string. extrastring is the leftovers
            realisticly, only description will be longer than 38 chars
            leftstring is trimmed, rightstring is extra"" "
        leftstring=teststring.strip()  
        stringlen=len(leftstring)
        rightstring =  "eggs"
        #print("Length of teststring is ", stringlen)    
        if stringlen<=38:
            #print("string is less than than 38")
            leftstring=leftstring.ljust(38)
            rightstring="" #null out rightstring
            #alternate method for setting 38 chars
              #teststring=('{:^38}').format(teststring)#set width=38
            
        elif stringlen>38 and leftstring.startswith("description "):#will not execute if desc less than 38
            #check if starts with description (descriptions will have spaces)
            #print("starts with description")
            rightstring=leftstring[12:] 
            leftstring=leftstring[:12]
            
        else:#string is greater than 38. find the last space before 38 and trim.
                #otherwise trim at 38
            #print("string is greater than 38")
            rightspace=leftstring.rfind(" ",0,38)
            if rightspace==-1: #rfind returns -1 if " " is not in string
                print("rightspace true, no spaces found ")
                rightspace=38
                
            rightstring=leftstring[rightspace:]
            leftstring=leftstring[:rightspace]
            
        
        print(leftstring, " << left string ** right string >> ", rightstring)
        #print("Length of adjusted teststring is ", len(leftstring))   
        return(leftstring, rightstring)
        
##************* end ACL object class *************
  
"" " 
 Access list Object 
        --------------------------------------------------------------------------------------------------------------
        "access-list"+ space + ACL name (interface name could be very long)+ space + "extended" (or "remark") + space 
        --------------------------------------------------------------------------------------------------------------
        ---------------------------------------------------------
        + "permit/deny" + space + "tcp/udp/icmp/protocol" || or port object group  + space 
        ---------------------------------------------------------        
        ---------------------------------------------------------
        + source + space + destination + space + ports
        ---------------------------------------------------------        
                --------------------------------------------------------------------------------------------------------
    source>>    "any"|| or "host" + space + IP Address || or network object group "object-group"//
                    network object "object"
                --------------------------------------------------------------------------------------------------------
                --------------------------------------------------------------------------------------------------------
    destination>>    "any" || or "host" + space + IP Address (#.#.#.#) || 
                        or network object group "object-group"// network object "object"
                --------------------------------------------------------------------------------------------------------
                --------------------------------------------------------------------------------------------------------
    ports >>    "any"|| or "host" + space + IP Address || or network object group "object-group"//
                    network object "object" 
                ----------------------------------------------------------------------------------------------------
"""                
##************* end ACL object class *************
    
if __name__=="__main__":
    print("running __main__ ASAclassesFeb")
    asa1obj=ASAobject("ASA1","DC1-ASA-01_2017mar29th0955hrs.txt") #create the ASAobject
    asa1obj.loadarray() #execute the load array function 
    print("length of asa object list is ", len(asa1obj.networkobjarray))
    
    asa1obj.wastefullsort(asa1obj.networkobjarray,asa1obj.sortednetworkobjarray)  
    asa1obj.printarray(asa1obj.sortednetworkobjarray)
    
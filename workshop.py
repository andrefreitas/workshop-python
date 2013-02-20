from participant import *

class Workshop:
    def __init__(self,title, file):
        self._title=title
        self._file=file
        self._participants=[]
        self.load_participants()
        
    def __del__(self):
        self.save_participants()
    
    def show_menu(self):
        print "\n"
        print "----------------------------------"
        print self._title
        print "----------------------------------"
        print "       Workshop Manager"
        print "----------------------------------"
        print "[1] - List Participants"
        print "[2] - Add Participant"
        print "[3] - Update Participant"
        print "[4] - Remove Participant"
        print "[0] - Exit"
        print "----------------------------------"
    
    def list_participants(self):
        print ""
        print "----------------------------------"
        print "       List of Participants"
        print "----------------------------------"
        for participant in  self._participants:
            participant.print_raw()
            
    def add_participant(self):
        print ""
        print "----------------------------------"
        print "       Add new Participant"
        print "----------------------------------"
        name=raw_input("Name? ")
        email=raw_input("Email? ")
        payment_status=raw_input("Paid?(y/n)")
        if(payment_status=="y"):
            payment_status="Paid"
        else:
            payment_status="Unpaid"           
        ieee_number=raw_input("IEEE Number?(press enter if none)")
        if(ieee_number==""):
            ieee_number=None
        p=Participant(name,email,payment_status,ieee_number)
        self._participants.append(p)
        
    def find_participant(self,email):
        for i in  range(len(self._participants)):
            if (self._participants[i].get_email()==email):
                return i
        
    def remove_participant(self):
        print ""
        print "----------------------------------"
        print "       Remove Participant"
        print "----------------------------------"
        email=raw_input("Enter the participant email: ")
        pos=self.find_participant(email)
        self._participants[pos].print_raw()
        answer=raw_input("Confirm remove(y/n)? ")
        if(answer=="y"):
            del self._participants[pos]
            
    def update_participant(self):
        print ""
        print "----------------------------------"
        print "       Update Participant"
        print "----------------------------------"
        email=raw_input("Enter the participant email: ")
        pos=self.find_participant(email)
        participant=self._participants[pos]
        participant.print_raw()
        print "If you want to keep press enter"  
        
        name=raw_input("Name? ")
        if(name!=""):
            participant.set_name(name) 
            
        email=raw_input("Email? ")
        if(email!=""):
            participant.set_email(email) 
    
        payment_status=raw_input("Paid?(y/n)")  
        if(payment_status!=""):
            if(payment_status=="y"):
                payment_status="Paid"
            else:
                payment_status="Unpaid"        
            participant.set_payment_status(payment_status) 
               
        ieee_number=raw_input("IEEE Number?")
        if(ieee_number!=""):
            participant.set_ieee_number(ieee_number) 
            
    def save_participants(self):
        file=open(self._file,"w")
        for participant in  self._participants:
            participant.write_to_file(file)
        file.close()
        
    def load_participants(self):
        file=open(self._file,"r")
        for line in file.readlines():
            line=line.replace("\n","")
            line_list=line.split(",")
            if(len(line_list)>=3):
                name=line_list[0]
                email=line_list[1]
                payment_status=line_list[2]
                if(len(line_list)==4):
                    ieee_number=line_list[3]
                else:
                    ieee_number=None
                self._participants.append(Participant(name,email,payment_status,ieee_number))  
        file.close()

    def run(self):
        while(True):
            self.show_menu()
            option=raw_input("Option(0-4): ")
            if(option=="1"):
                self.list_participants()
            if(option=="2"):
                self.add_participant()
            if(option=="3"):
                self.update_participant()
            if(option=="4"):
                self.remove_participant()
                
            if(option=="0"):
                self.save_participants()
                break
            
                
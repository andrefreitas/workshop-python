class Participant:
    def __init__(self,name,email,payment_status,ieee_number=None):
        self._name=name
        self._email=email
        self._ieee_number=ieee_number
        self._paid=(payment_status=="Paid")
        
    # Print information
    def print_raw(self):
        raw=self.get_name() + " | " + self.get_email()+ " | "
        if(self.is_paid()):
            raw+="Paid"
        else:
            raw+="Unpaid"
        if(self.get_ieee_number()):
            raw+=" | " + str(self._ieee_number)
        raw=raw.replace("\n","")
        print raw
        
    # Write to file
    def write_to_file(self,file):
        line=self.get_name() + "," + self.get_email()
        if(self._paid):
            line+=",Paid"
        else:
            line+=",Unpaid"           
        if(self._ieee_number):
            line+=","+str(self._ieee_number) 
        line+="\n"
        file.write(line)
        
    # Set methods
    def set_name(self,name):
        self._name=name

    def set_email(self,email):
        self._email=email
    
    def set_ieee_number(self,ieee_number):
        self._ieee_number=ieee_number
        
    def set_payment_status(self,payment_status):
        self._paid=(payment_status=="Paid")
        
    # Get methods
    def get_name(self):
        return self._name
    
    def get_email(self):
        return self._email
    
    def get_ieee_number(self):
        return self._ieee_number
    
    def is_paid(self):
        return self._paid

        
    
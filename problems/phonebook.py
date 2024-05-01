import re


class Phonebook:
   
    def __init__(self):
         self.contact_details=[{
        "name":None,
        "email":None,
        "phone":None,
    }]
    def choice(self):
        myChoice=int(input('  1-Add Contact Details\n 2-Update Contact Details \n 3-delete Contact \n4-display contacts\n5-exit\n6-clear Data\n enter your choice:'))
        if (myChoice==1):           
            i=1
            while i>0:
                while True:
                    phone_input=input('enter phone number:')
                    if not self.validatePhone(phone_input):
                        print('please enter 10 digit Phone number')
                    else:
                        try:
                           phone=int(phone_input)
                           name=input('enter name:')
                           while True:
                               email=input('enter email: ')
                               if not self.validateEmail(email):
                                  print('Invalid email address provided')
                               else:
                                   break
                           result = input('Are you done? (yes or no): ')
                           if result.lower() == 'yes':
                                   self.add_contact(name, email, phone)
                                   self.choice()
                                   return
                           else:
                                self.add_contact(name, email, phone)
                        except ValueError as e:
                            print('invalid value')

                    
        elif (myChoice==2):
            while True:
              email =input('enter email to update: ')
              if not self.validateEmail(email):
                    print('Invalid email address provided')
              else:
                    break
            name_input = input('enter name: ')
            while True:
                 phone_input=input('enter phone number:')
                 print(phone_input)
                 if phone_input is None :
                    break
                        
                 else:
                    if not self.validatePhone(phone_input):
                        print('enter a valid phone number')
                    else:

                        try:
                          phone=int(phone_input)
                          self.update_contact(email,name_input,phone_input) 
                        except ValueError:
                           print('inavlid value')
            self.update_contact(email,name_input)          
                      
                    
                

            
        elif (myChoice==4):
            self.display_contact()
        elif (myChoice==3):
             while True:
              email =input('enter email to Delete the contact: ')
              if not self.validateEmail(email):
                    print('Invalid email address provided')
              else:
                    break
             self.delete_Contact(email)
             

        elif (myChoice==6):
            self.contact_details.clear()
            print('All Data Erased')
        elif (myChoice==5):
            exit()
            


    def validateEmail(self,em):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return  bool(re.match(pattern,em))
       
    def validatePhone(self,nm):
        return len(nm)==10

    def add_contact(self,name,email,phone):
    
        #  if(self.validateEmail(email) and self.validatePhone(phone)):
        contactAdded=False
        for contacts in self.contact_details:
            if(contacts['email']==email):
                print('contact already exist')
                break
        else:
           
            self.contact_details.append(
            {
                "name":name,
                "email":email,
                "phone":phone
            } )
        if contactAdded:
            print('Contact added successfully.')

            
                
        # else:
        #     if not self.validateEmail(email):
        #         print('invalid email')
        #     if not self.validatePhone(phone):
        #         print('phone number should be 10 didgit')
    def update_contact(self,email,name=None,phone=None):
        for contacts in self.contact_details:
            if(contacts['email']==email):
                if name is not None:
                    contacts['name']=name
                if phone is not None:
                    contacts['phone']=phone
                print('contact details updated')
                self.choice()
                return
        print('email does not exist')
        self.choice()
        return
    
    def delete_Contact(self,email):
        for contact in self.contact_details:
            if(contact['email']==email):
                 self.contact_details.remove(contact)
                 print('Contact deleted successfully.')
                 self.choice()
                 return
        
        print('Contact not present in the list')
              
    
                
       
    def display_contact(self):
        for contact in self.contact_details:
           if any(value is None for value in contact.values()):
             print('')
           else:
             print(contact)
        print('Displayed all contacts.')
        self.choice()
            

phonebook=Phonebook()
# phonebook.add_contact('amit','amitsunil@gmail.com',8129448232)
# phonebook.add_contact('jaswanth','jaswanth@gmail.com',9999990000)
# phonebook.update_contact('amitsunil@gmail.com','killeramit')
# phonebook.display_contact()
# phonebook.delete_Contact('jaswanth@gmail.com')
# phonebook.display_contact()
phonebook.choice()
from entities.rider import Rider
from entities.cab import Cab
import sys

#---------------------------------cab----------------------------------

def notavailable(self):
        self.availability=False
        


def cabRegister1(self,availability):
         
         self.drivername=input("Enter drivername1:",self.drivername)
         
         self.driverId=input("Enter driverId1:",self.driverId)
         #for location of cab 
         self.x2=input("Enter Co-ordinate of x:",self.x2)
         self.y2=input("Enter Co-ordinate of y:",self.y2)
         #to make available cab for rider
         Choice=input("Ready for Ride:1.Yes 2.No ")
         if  Choice==1:
             self.availability=True
         elif  Choice==2:
             self.availability=False
         return availability
   
def  cabRegister2(self,availability): 
             
        
   self.drivername=input("Enter drivername2:",self.driverId)
   self.driverId=input("Enter driverId2:")
         #for location of cab 
   self.x3=input("Enter Co-ordinate of x:",self.x3)
   self.y3=input("Enter Co-ordinate of y:",self.y3)
   Choice=input("Ready for Ride:1.Yes 2.No ")
   if  Choice==1:
        self.availability=True
   elif  Choice==2:
       self.availability=False
       
# to book a cab
def cabBook(self):
        select=int(input())
       
        
        if select==1:     
          if notavailable()==True :
               dist1=pow((pow((self.x1-self.x2),2)+pow((self.y1-self.y2),2)),1/2)
               return dist1 
          elif notavailable()==True :
              dist2=pow((pow((self.x1-self.x3),2)+pow((self.y1-self.y3),2)),1/2)
              return dist2
          mindist=min(dist1,dist2)
          return mindist
        print("Enter your payment details: 1.UPI 2.CASH 3.DEBIT/CREDIT CARD")
        input=int(input())
        if input==1:
              upi=input("Enter UPI ID:")
              print("Booked successfully")
        elif input==2:
              print("Booked successfully")
        elif input==3:
              card=input("Enter card details:")
              print("Booked successfully")
        else:
              print("Invalid")
        
              
               
              
          
       

     
    
#---------------------------------------------------------------
def run():
      
      
       
       
       
       
    print("1.Register Cab1 ")
    print("2.Register Cab2 ")
    print("3.Register Rider")
    print("4.Please confirm for Booking Cab:1.Yes  2.No")
    print("5.to end the trip:")
    
    
    
    while True:
      select=int(input())
      if select==1:
         cabRegister1()
        
      if select==2:
         cabRegister2()
         
      if select==3:
         Rider.riderRegister()
         
      if select==4:
        cabBook()
        
      if select==5:
        break
         
if __name__=="__main__":
    run()

        
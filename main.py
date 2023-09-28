
import Information as inf


def main():
    while True:
        print('''Welcome
             I can do these:
             1.information of the device:
             2.find ip address:
             3.find cores of processor:
             ''')
        try:
          ch=int(input())
        except ValueError:
             print("Please Enter number not character")
             continue
        if ch==1:
           print(inf.Get_information())
        elif ch==2:
           print(inf.Get_ip())
        elif ch==3:
           print(inf.Get_cores())
        else:
           print("Do you want to exit?(Enter 0)")
           ch=int(input())
           print("Good bye ")
           break
           
            

    

    
   

main()
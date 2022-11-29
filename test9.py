def forwart():
    print("\n forwart....")
def back():
    print("\n back....")
def left():
    print("\n turn left...!")
def right():
    print("\n turn right ") 
def option():
    rint("[1]. forwart()");
    print("[2]. back()");
    print("[3]. left()") ;
    print("[4]. right()");
    
option()
opt=int(input("Choose 1,2,3: "))
if(opt==1):
   forwart()
elif(opt==2):
   back()
elif(opt==3):
      left()
else : 
    right()         
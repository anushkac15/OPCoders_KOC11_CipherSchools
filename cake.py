#PROJECT
angle=int(input("Enter the Angle of the cake: "))                                                     #30
N=int(input("Enter the no. of pieces: "))                                                             #6
if angle%N==0:       #checking whether the angle between any two cuts is positive integer or not      #30%6==0  ..true
    print("YES the cake will cut in equal pieces of size %d"%N)                                       #printed
else:
    print("NO the cake will not cut in equal pieces od size %d"%N)
if N>angle:          #cake can't be cut into any pieces if N is greater than angle                    #6>30   ...false
    print("NO the cake will not cut in any piece of size %d"%N)
else:
    print("YES the cake will cut in any piece of size %d"%N)                                          #printed
n=1                  #if the cake can cut in any no of pieces then subtracting the cake
for i in range(N):                                                                                    #i=1-6
    angle=angle-n                                                                                     #29  28  27  26  25  
    n=n+1                                                                                             #2   3   4   5   6
    if(angle<0):                                                                                      #25<0  ...flase
        print ("NO the cake will not cut into %d pieces such that no two of them are equal "%N)
        break
else:   
    print("YES the cake will cut into %d pieces such that no two of them are equal "%N)               #printed
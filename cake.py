angle=int(input("Enter the Angle of the cake: "))                                                     
N=int(input("Enter the no. of pieces: "))                                                             
if angle%N==0:        
    print("YES the cake will cut in equal pieces of size %d"%N)                                      
else:
    print("NO the cake will not cut in equal pieces od size %d"%N)
if N>angle:                            
    print("NO the cake will not cut in any piece of size %d"%N)
else:
    print("YES the cake will cut in any piece of size %d"%N)                                         
n=1                  
for i in range(N):                                                                                    
    angle=angle-n                                                                                      
    n=n+1                                                                                           
    if(angle<0):                                                                                     
        print ("NO the cake will not cut into %d pieces such that no two of them are equal "%N)
        break
else:   
    print("YES the cake will cut into %d pieces such that no two of them are equal "%N)               

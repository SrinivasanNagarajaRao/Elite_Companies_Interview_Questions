# from tabulate import tabulate

def print_rectangle(n, m) :
    
 

    for i in range(1, n+1) :

        if (i == 1 or i == n ):

             print("+", end="")

        for j in range(1, m) :

            if (i == 1 or i == n ) and (j != m):

                print("-", end="")

            elif( j==2):

              print("2", end="")

 

            elif(i== 1 and j== m):

                print("+", end="")

            elif(i== n and j == m):

 

                print("+", end="")

            elif (j == 1 or j  == m) :

 

                print("|", end="")

            elif(i== n and j == m):

 

                 print("+", end="")

 

           

 

        print()

 

 

    # Driver program for above function

 

a = [4,56,789,1000000]

c = len(str(max(a))) +2

 

r = 3

print_rectangle(r, c)

 
val jsonSchema = new StructType().add("battery_level", LongType).add("c02_level", LongType).add("cca3",StringType).add("cn", StringType).add("device_id", LongType).add("device_type", StringType).add("signal", LongType).add("ip", StringType).add("temp", LongType).add("timestamp", TimestampType)
import os
folders = input("Please provide the input: ").split()

for folder in folders:
    
    try:
        files = os.listdir(folder)   
        
    except FileNotFoundError:
        print ("<=============Please provide the valid input+=======>"+ folder)
        continue

        
        
    
    for file in files:
        print(file)
       
# except:FileNotFoundError: 
#  


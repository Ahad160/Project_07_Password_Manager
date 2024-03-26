import ast
import os
import psutil
import Decryption_M
import Encryption_M


class Storage:

    def __init__(self, path1, path2):
        self.path1 = path1
        self.path2 = path2        
    def ViewPassword(self):
        try:
            #  🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓 #Decryption
            Dec=Decryption_M.Decryption(self.path2,self.path1)

            #Convert String To Dict
            dictionary = ast.literal_eval(Dec)

            print("\n🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨")
            for key, value in dictionary.items():
                print(f"{key} - {value}")
            print("🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨\n")
        except FileNotFoundError as error:
            print("encryption_key.key is missing from Drive")
        Back = input("Press Any Button To Continue--")     
    def EditPassword(self):
        try:
            #  🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓 #Decryption
            Dec=Decryption_M.Decryption(self.path2,self.path1)

            with open(self.path1,"w") as file:
                file.write(Dec)

            with open(self.path1, "r+") as file:
                read = file.readlines()
                file.seek(0)

                dictionary = ast.literal_eval(read[0])
                lists = list(dictionary.keys())

                for i in range(len(lists)):
                    print(f"{i+1}.{lists[i]}")

                key = input("Enter Account Number➡️   ")
                found = False

                for j in range(len(lists)):
                    if key == lists[j]:
                        value = input(f"Enter New Password Of {key}➡️  ")
                        dictionary[key] = value
                        found = True
                        break
                if found:
                    file.write(str(dictionary))
                    file.truncate()

                    # 🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒 Encryption
                    Encryption_M.Encryption(self.path2,self.path1)
                else:
                    print("Incorrect Account Name\n")
        except FileNotFoundError as error:
            print("encryption_key.key is missing from Drive")            
    def AddPassword(self):
        try:    
            dict_Key = input("Enter Account Name➡️   ")
            value = input(f"Enter {dict_Key} Password➡️   ")

            #🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓 #Decryption
            Dec=Decryption_M.Decryption(self.path2,self.path1)

            #Convert String To Dict
            dictionary = ast.literal_eval(Dec)

            dictionary[dict_Key] = value

            sread = open(self.path1, "w")
            sread.write(str(dictionary))
            sread.truncate()

            # 🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒 Encryption
            Encryption_M.Encryption(self.path2,self.path1)
        except FileNotFoundError as error:
            print("encryption_key.key is missing from Drive")    
    def RemovePassword(self):
        try:
            #🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓🔓 #Decryption
            Dec=Decryption_M.Decryption(self.path2,self.path1)

            dictionary = ast.literal_eval(Dec)
            lists = list(dictionary.keys())

            for i in range(len(lists)):
                print(f"{i+1}.{lists[i]}")

            dict_key = input("Enter Account Name➡️   ")

            del dictionary[dict_key]

            print(f"🔴 {dict_key} Password is Deleted🔴\n")

            sread = open(self.path1, "w")
            sread.write(str(dictionary))
            sread.truncate()

            # 🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒 Encryption
            Encryption_M.Encryption(self.path2,self.path1)
        except FileNotFoundError as error:
            print("encryption_key.key is missing from Drive")
        except KeyError as error:
            print("Incorrect Account Name\n")
        

   

# Auto Startup Check

# To Check A File
def list_drive_letters():
    drive_letters = set()
    partitions = psutil.disk_partitions(all=True)

    for partition in partitions:
        if partition.device and partition.mountpoint:
            drive_letter = partition.device[0].upper() + ":"
            drive_letters.add(drive_letter)

    return sorted(drive_letters)


drive_letters = list_drive_letters()

#Defile Path For Acutal Project
# file_path = f"{drive_letters[1]}\Database.txt"
# file_path_2 = f"{drive_letters[1]}\encryption_key.key"

#Defile Path For Normal Run the program
file_path = f"E:\Codeing\Python Language\Projects\Project_07_Password_Manager\Database.txt"
file_path_2 = f"E:\Codeing\Python Language\Projects\Project_07_Password_Manager\encryption_key.key"


# To Create The File
if os.path.exists(file_path):
    pass
else:
    data = {}
    with open(file_path, 'w') as file:
        file.write(str(data))

    # Encryption-----Auto
    # 🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒🔒 Encryption
    Encryption_M.Encryption(self.path2,self.path1)


object = Storage(file_path, file_path_2)


while True:
    try:
        print(" \t🟢\033[91mPassword Manager\033[0m🟢")
        print("""----------------------------------------
    🔺       1.View All Password          🔺
    🔺       2.Edit Password              🔺
    🔺       3.Add Password               🔺
    🔺       4.Delete Password            🔺
    🔺       5.Exit                       🔺
    ----------------------------------------""")
        user = int(input("Choose an option➡️   "))
        if user == 1:
            object.ViewPassword()
        elif user == 2:
            object.EditPassword()
        elif user == 3:
            object.AddPassword()
        elif user == 4:
            object.RemovePassword()
        elif user == 5:
            print("Closing Password Manager")
            exit()
        else:
            print("Invalid Choice!")

    except ValueError as error:
        print("Enter valid Choice")

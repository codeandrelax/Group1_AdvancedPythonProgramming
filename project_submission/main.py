from usrmgm_library import *

if __name__ == "__main__": 
  while True:
        print("-"*10,"MENU","-"*10)
        list_of_op=["register","login","add_contact","print_contact","remove_contact","logout","EXIT"]

        for order,op in enumerate(list_of_op,start=1):
            print(f"{op.ljust(20 - len(str(order)))}{str(order).rjust(len(str(order)))}")

        option_str=""
        option_num=0

        while True:
            option_str = input("Enter option:")
            try:
                option_num=int(option_str)
                if option_num > 7 or option_num < 1:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Invalid input! Try again")
                 
        print(f"\n You picked: {list_of_op[option_num-1]}\n")

        if option_num == 1:
            username,password=input_credentials()
            register(username,password)

        elif option_num == 2:
            username,password=input_credentials()
            login(username,password)

        elif option_num == 3:
            reg_user=None
            reg_user=select_online_users()
            if reg_user != None:
                input_contact_for_user(reg_user)
            else:
                print("Add contact ERROR: cannot find user")
            
        elif option_num == 4:
            reg_user=None
            reg_user=select_online_users()
            if reg_user != None:
                print_contacts_for_user(reg_user)
            else:
                print("Print contacts ERROR: cannot find user")
        
        elif option_num == 5:
            reg_user=None
            reg_user=select_online_users()
            if reg_user != None:
                remove_contacts_for_user(reg_user)
            else:
                print("remove contacts ERROR: cannot find user")

        elif option_num == 6:
            print_result=print_online_users()
            if print_result==-1:
                print("No online users!")
            else:
                usr_logout=input("Enter username to logout: ")
                logout(usr_logout)

        elif option_num == 7:
            break
        else:
            print("Invalid input!!!")
        
        print("\n\n")


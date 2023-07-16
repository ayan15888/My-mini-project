def emailfunc():  # sdjc@gmail.com
    a=0
    email = input("Enter the email you want to validate \n")
    if len(email) >= 6:
        print("Lenght is satisfied")
        if email[0].isalpha():
            print("Alphabet is verfied")
            if ("@" in email) and (email.count("@")== 1) and ("." in email) and (email.count(".")== 1):
                print("@ is satisfied")
                if (email[-4] == ".") ^ (email[-3] == "."):
                    print("Fullstop is satisfied")
                    for i in email:
                        if i.isspace() or i.isupper():
                            a=1
                            break
                    if(a==1):
                        print("no space or uppercase is allowed")
                    else:
                        print("\033[92mEmail is valid\033[0m")

                else:
                    print("Fullstop is not satisfied")
                    emailfunc()
            else:
                print(" '@' and 'i' character is allowed only once")
                emailfunc()
        else:
            print("Enter alphabet first")
            emailfunc()

    else:
        print("Enter at least 6 length of character")
        emailfunc()
emailfunc()
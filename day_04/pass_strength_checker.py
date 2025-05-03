password = input("Password: ")

def check_password_strength(password):
    special_characters = "!@#$%^&*"
    pass_len = len(password)
    
    if any(char in special_characters for char in password):
        
        if any(char.isdigit() for char in password):
            
            if pass_len >= 8:
                print("✅ Strong")
                
            elif pass_len < 8:
                print("⚠️  Medium")     
            
        else:
            print("❌ Weak, Include atleast one number.")
    else:
        print("❌ Weak, Include atleast one special character.")

check_password_strength(password)

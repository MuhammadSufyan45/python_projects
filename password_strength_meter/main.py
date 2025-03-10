import streamlit as st
# Password strength checker : conditions we will check. 1: len min 8 char. 2: should contain digit.
#  3: should contain uppercase char. 4: should contain lowercase char. 5: should contain special char.


    # Conditions defined in this function >
def check_password_strength(password):

    feedback = []

    if len(password) < 8:
        feedback.append("Weak: ❌ password should be at least 8 characters long")
    if not any(char.isdigit() for char in password):
        feedback.append("Weak: ❌ password must contain at least one digit")
    if not any(char.isupper() for char in password):
        feedback.append("Weak: ❌ password must contain at least one uppercase character")
    if not any(char.islower() for char in password):
        feedback.append("Weak: ❌ password must contain at least one lowercase character")
    if not any(char in "!@#$%^&*()-+" for char in password):
        feedback.append("Weak: ❌ password must contain at least one special character")
    
    if len(feedback) == 0:
        return("Strong: ✅ Strong Password! Your password is secure.")
    elif len(feedback) == 3:
        return("Medium: ⚠️ Medium Strength Password. Consider improving the above issues.")
    else:
        return("Weak: ❌ Consider improving the above issues for better security.")
    

    # This function will take input from user and check the password strength > 
def check_password():
    
    st.title("Password Strength Checker Tool")


    password = st.text_input("Enter your password: ")

    if password :
        result = check_password_strength(password)
        st.write(result)


    st.write("""
    #### Tips for creating a strong password:
    - Use at least 8 characters.
    - Include both uppercase and lowercase letters.
    - Include at least one number (0-9).
    - Use special characters such as !@#$%^&*().
    """)

# This syntax will run this line very first before running the full code from starting >

if __name__ == "__main__":
    check_password()


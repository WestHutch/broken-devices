import keyring
import json

def set_credentials():
    ic_user = input("Enter your IC username: ")
    keyring.set_password("broken_devices", "ic_user", ic_user)
    ic_pw = input("Enter your IC password: ")
    keyring.set_password("broken_devices", "ic_pw", ic_pw)
    destiny_user = input("Enter your destiny username: ")
    keyring.set_password("broken_devices", "destiny_user", destiny_user)
    destiny_pw = input("Enter your destiny password: ")
    keyring.set_password("broken_devices", "destiny_pw", destiny_pw)
    email = input("Enter your full email address: ")
    keyring.set_password("broken_devices", "email", email)
    email_pw = input("Enter your email password: ")
    keyring.set_password("broken_devices", "email_pw", email_pw)
    synetic_user = input("Enter your synetic username: ")
    keyring.set_password("broken_devices", "synetic_user", synetic_user)
    synetic_pw = input("Enter your synetic password: ")
    keyring.set_password("broken_devices", "synetic_pw", synetic_pw)
    worthave_user = input("Enter your Worth Ave username: ")
    keyring.set_password("broken_devices", "worthave_user", worthave_user)
    worthave_pw = input("Enter your Worth Ave password: ")
    keyring.set_password("broken_devices", "worthave_pw", worthave_pw)
    userCredentials = {
        "ic_user": ic_user,
        "ic_pw": ic_pw,
        "destiny_user": destiny_user,
        "destiny_pw": destiny_pw,
        "email": email,
        "email_pw": email_pw,
        "synetic_user": synetic_user,
        "synetic_pw": synetic_pw,
        "worthave_user": worthave_user,
        "worthave_pw": worthave_pw
    }
    return(userCredentials)

def get_credentials():
    ic_user = keyring.get_password("broken_devices", "ic_user")
    ic_pw = keyring.get_password("broken_devices", "ic_pw")
    destiny_user = keyring.get_password("broken_devices", "destiny_user")
    destiny_pw = keyring.get_password("broken_devices", "destiny_pw")
    email = keyring.get_password("broken_devices", "email")
    email_pw = keyring.get_password("broken_devices", "email_pw")
    synetic_user = keyring.get_password("broken_devices", "synetic_user")
    synetic_pw = keyring.get_password("broken_devices", "synetic_pw")
    worthave_user = keyring.get_password("broken_devices", "worthave_user")
    worthave_pw = keyring.get_password("broken_devices", "worthave_pw")
    userCredentials = {
        "ic_user": ic_user,
        "ic_pw": ic_pw,
        "destiny_user": destiny_user,
        "destiny_pw": destiny_pw,
        "email": email,
        "email_pw": email_pw,
        "synetic_user": synetic_user,
        "synetic_pw": synetic_pw,
        "worthave_user": worthave_user,
        "worthave_pw": worthave_pw
    }
    if not all(userCredentials.values()):
        raise ValueError("Incomplete userCredentials, please run with --reset-credentials arg")
    return(userCredentials)

def write_email_info():
    initials = input("Enter your initials: ")
    email_sig = input("Enter your email signature (ex: ~Weston): ")

    mail_to = input("Enter the email address of someone you need to email: ")
    emails = []
    while mail_to != "s":
        emails.append(mail_to)
        mail_to = input("Enter another email or type s to stop: ")
    boss_email = input("Enter your boss' email address: ")
    
    school = ""
    while school != "h" and school != "m":
        school = input("Enter m for TMS or h for THS: ")

    emailInfo = {
        "initials": initials,
        "email_sig": email_sig,
        "emails": emails,
        "boss_email": boss_email,
        "school": school
    }

    with open("emailinfo.json", "w") as f:
        json.dump(emailInfo, f, indent=4)
    return(emailInfo)

def read_email_info():
    with open("emailinfo.json", "r") as f:
        emailInfo = json.load(f)
    return(emailInfo)

def get_user_info():
    try:
        userCredentials = get_credentials()
    except ValueError:
        userCredentials = set_credentials()

    try:
        emailInfo = read_email_info()
    except (FileNotFoundError, json.JSONDecodeError):
        emailInfo = write_email_info()

    userDict = userCredentials | emailInfo
    return(userDict)
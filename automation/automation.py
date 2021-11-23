import re

path ='automation/assets/potential-contacts.txt'
with open(path,'r') as file:
    content = file.read()


def email(text):
    emails= re.findall('\S+@\S+', text)
    filtered_emails = set(emails)
    sorted_emails=sorted(filtered_emails)
    return sorted_emails

def phone_number( text ):
  
    phone_number = re.findall( r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', text )
    
    styled_phone_number = []

    for number in phone_number:
        
        if "(" in number:
            number = number.replace( "(", "" )
        if ")" in number or "." in number:
            number = number.replace( ")", "-" )
            number = number.replace( ".", "-" )
        if len( number ) == 10:
            number = f"{number[:3]}-{number[3:6]}-{number[6:]}"
     
        styled_phone_number.append( number )
    all_phone_number = sorted(set (styled_phone_number ))
    return all_phone_number
   


emails_list = email(content)
phone_num=phone_number(content)


def write_file(text,path):
    result = ""
    for element in text:
        result += element + "\n"
    with open (path, 'w') as f :
        f.write(result) 
write_file(emails_list , 'automation/assets/emails.txt')
write_file(phone_num , 'automation/assets/phone_numbers.txt')

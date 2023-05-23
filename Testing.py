# A random python programme to add to the repo
import random

def select_random_emails(filename, number):
    
    k =int(number)

    with open(filename) as file_object:
        lines = file_object.readlines()

    email_list =[]
    for line in lines:
        email_list.append(line)

  
    results = random.sample(email_list, k=k)
    results.sort()
    
    for result in results:
        print(result)

filename = input("Firstly enter the name of the file containing the list of emails: ")
number = input("Now enter how many emails you want selected: ")
select_random_emails(filename, number)

StripeKeyPub = 'sk_test_26PHem9AhJZvU623DfE1x4sd'
StripeKeyPriv = 'pk_test_qblFNYngBkEdjEZ16jxxoWSM'

Testsecret = 'dfnsdpijp354tsildf'
User = 'test@usernet.com'

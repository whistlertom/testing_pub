# Using a random python programme to add to the repo
import random

aws_access_key_id = AKIAJQHVNFNMLINIZY7C
aws_secret_access_key = 7Gg7sGTEuvAaI0CFqx3pgZ+ZeStGv9ZRh94/NZkn
# A fake AWS key, fits correct format.

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
# A fake StripeKey key, fits correct format.

Testsecret = 'dfnsdpijp354tsildf'
User = 'test@usernet.com'
# Testing if it recognises variable (fake)



client_name = input("Client's Name: ")
form_type = input("Form type: ")
account_type = input("Account type: ")
letter_of_acceptance = ""
tpa_approval = ""

if form_type.lower() == "transfer/rollover":
 letter_of_acceptance = """
We also require a letter of acceptance from the company receiving the transfer, you can contact them to get that. """

if account_type.lower() == "403b" or account_type.lower() == "457":
 tpa_approval = """
Lastly, we will need approval from the authorized signer with your employer or a Third Party
Administrator, their information is below. Give them on a call for any questions on receiving their
signature.


"""
print(f"""
Hi {client_name},

Attached is the {form_type} form that you can complete. {letter_of_acceptance} {tpa_approval}
Please make sure to send all requirements in at once. They can be faxed to 888-554-7999 or mailed to
6187 Carpinteria Ave
Carpinteria, CA 93013
If these options don't work, or if you have any other inquiries, give us a call at (800) 874-6910.

Best regards,
Micah""")
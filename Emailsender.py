"""
This is a simple email sender application that allows the user to send emails using a Gmail account.
It utilizes the 'email.message', 'ssl', and 'smtplib' libraries to create and send email messages securely.

Author: Liamani El Mahdi
Date: 14/08/2023

Usage:
1. Run the script.
2. Follow the prompts to provide necessary email information.
3. Send an email by entering 'Y' or 'y', or exit the application by entering 'N' or 'n'.

Note: For security reasons, it's recommended to use an 'App Password' for Gmail instead of your actual account password.

"""

# Importing the necessary libraries
from email.message import EmailMessage
import ssl
import smtplib
from ssl import SSLContext


# Error Handling function
def handle_error(exception):
    print("An error occurred:", str(exception))


def main():
    """
    The main function that controls the email sending application.
    Prompts the user for input and sends an email if requested.

    """

    keep_working = True  # Flag to control the loop

    print("Welcome to the email sender application")
    print("---------------------------------------")

    while keep_working:
        print("Do you want to send an email ? (Y/N)")
        answer = input()
        try:
            if answer == "Y" or answer == "y":
                print("Please fill the information:\n")
                print("Email sender:")
                email_sender = input()
                print("Email app password:")
                email_password = input()
                print("Email receiver:")
                email_receiver = input()
                print('the subject')
                subject = input()
                print('the content:')
                body = input()

                # Creating an email message
                em = EmailMessage()
                em['From'] = email_sender
                em['To'] = email_receiver
                em['Subject'] = subject
                em.set_content(body)

                # Creating a secure SSL context
                context: SSLContext = ssl.create_default_context()
                try:
                    # Establishing a connection to Gmail's SMTP server over SSL
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                        smtp.login(email_sender, email_password)
                        # Sending the email
                        smtp.sendmail(email_sender, email_receiver, em.as_string())
                    print("The email was sent successfully")
                except Exception as e:
                    handle_error(e)

            elif answer == 'N' or answer == 'n':
                keep_working = False
                print("Exiting the application. Thank you!")
            else:
                print("please answer with Y, y, N, or n only")
        except KeyboardInterrupt:
            print("Operation interrupted by user.")
            keep_working = False


if __name__ == '__main__':
    main()

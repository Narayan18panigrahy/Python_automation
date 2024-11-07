Send Email Automatically via Python
This Python script allows you to automatically send an email to a specific recipient using SMTP.

Requirements:
Python 3.x installed on your machine.
A valid email account for sending emails (Gmail, Outlook, etc.).
If using Gmail with 2-factor authentication (2FA), you will need an App Password.

Setup
1.Clone/Download the script to your local machine.
2.Modify the script with your details:
    sender_email: Your email address (e.g., your_email@gmail.com).
    sender_password: Your email password (or App Password if using Gmail with 2FA).
    receiver_email: The recipient's email address.
    subject: The email subject.
    body: The body content of the email.
    Run the script.
3.How to Run:
    Open a terminal/command prompt.
    Navigate to the script folder.
    Run the script:
    python send_email.py
If everything is set up correctly, the email will be sent to the recipient.

Notes:
For Gmail, make sure you either enable Less Secure Apps or use an App Password if 2FA is enabled.
The script uses the Gmail SMTP server (smtp.gmail.com) by default.

Created by Narayan Panigrahy
Feel free to modify, extend, and adapt the script as per your needs.
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import logging

# Function to send an email
def send_email(sender_email, sender_password, receiver_email, subject, body, smtp_server, smtp_port=587):
    try:
        # Set up the MIME
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        
        # Attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))
        
        # Establish a secure SMTP session
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure connection with TLS
        
        # Log in to the server
        server.login(sender_email, sender_password)
        
        # Send the email
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        
        # Close the server connection
        server.quit()
        
        print(f"Email successfully sent to {receiver_email}")
        return True
    except smtplib.SMTPAuthenticationError:
        logging.error("Authentication failed: Please check your email or app password.")
    except smtplib.SMTPException as e:
        logging.error(f"Error while sending email: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
    
    return False

# Example usage
if __name__ == "__main__":
    # Sender's email credentials
    sender_email = "your_email@gmail.com"  # Change to your email
    sender_password = "your_app_password"  # Use app-specific password if 2FA is enabled
    
    # Receiver's email
    receiver_email = "receiver_email@example.com"  # Change to receiver's email
    
    # Email subject and body
    subject = "Test Email from Python Script"
    body = "Hello! This is a test email sent from a Python script."
    
    # Gmail's SMTP server
    smtp_server = "smtp.gmail.com"

    # Sending the email
    if send_email(sender_email, sender_password, receiver_email, subject, body, smtp_server):
        print("Email was sent successfully!")
    else:
        print("Failed to send email.")

from flask_mailman import EmailMessage

def sendemail(reminder_name, email):
    msg = EmailMessage(
        subject=reminder_name,
        body="Don't be lazy, It is time to do your work",
        from_email="shinzzzo123@gmail.com",
        to=[email],
    )
    try:
        msg.send()
    except Exception as e:
        print(f"Failed to send email to {email}. Error: {e}")
    return "Msg sent"

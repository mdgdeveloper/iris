# Main Window
from ..backend.core import generateEmail


def createWindow():

    destination = "Sergio Madrigal"
    subject = "New SFTP account"
    tone = "Executive Formal"
    content = "The new account has been creared. The new account is saunicoresftp.best. The password is going to be sent through other channel"
    prev = None

    test = generateEmail(
        destination, subject, content, tone, prev
    )

    return(test)
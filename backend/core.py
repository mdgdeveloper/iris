# Core Backend functions
from ..utils.aifunc import createAiResponse

def generateEmail(destination, subject, content, tone, prev):
    """
    Generates an email.

    Paramters:
        destination (str): The destination email address.
        subject (str): The subject of the email (optional)
        content (str): The expected content of the email.
        tone (str): The tone expected in the mail
        prev (str): If previous email has been provided (optional)
        
    Returns:
        str: The generated email.
    """

    result = createAiResponse(destination, content, tone, prev)


    return result
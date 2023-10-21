def get_email_template(**kwargs):
    """Return a formatted string containing the details of the email to be sent.

    Parameters:
    - **kwargs: keyword arguments containing details of the email to be sent.
                Possible arguments include: sender, recipient, subject, body.

    Returns:
    - (str): a formatted string containing the sender, recipient, subject, and body of the email.

    Example:
    >>> get_temp_template(sender='John Doe', recipient='Jane Smith', subject='I miss you', body='Dear Jane, it...')
    'Hello, Jane Smith!\nSender: John Doe
    Recipient: Jane Smith
    Subject: I miss you
    Body: Dear Jane, it...'
    """

    template = "Hello, %s!\n"
    for key, value in kwargs.items():
        template += f"{key.capitalize()}: {value}"
    return template.replace("_", " ")

import getpass
import imaplib
import pprint

GOOGLE_IMAP_SERVER = 'imap.googlemail.com'
IMAP_SERVER_PORT = '993'

def check_mail(username, password):
    mailbox = imaplib.IMAP4_SSL(GOOGLE_IMAP_SERVER, IMAP_SERVER_PORT)
    mailbox.login(username, password)
    mailbox.select('Inbox')
    tmp, data = mailbox.search(None, 'ALL')
    
    for num in data[0].split():
        tmp, data = mailbox.fetch(num, '(RFC822)')
        print(f'Message: {num}\n')
        pprint.pprint(data[0][1])
        break

    mailbox.close()
    mailbox.logout()

if __name__ == "__main__":
    username = input('Enter your email username: ')
    password = getpass.getpass(prompt='Enter your account password: ')
    check_mail(username, password)

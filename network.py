from urllib.request import urlopen


response = urlopen('http://www.debian.org')

# printing response and converting it to utf
print(response.readline().decode('utf-8'))
print()

# printing url address
print(response.url)
print()

# printing status code
print(response.status)


# ==========================
## Handling Errors

from urllib.request import urlopen
import urllib.error


try:
    response = urlopen('http://www.debian.org/hello.txt')  # this file doesn't exist
except urllib.error.HTTPError as err:  # can use URLError for host or IP
    print(f'status:  {err.code}')
    print(f'reason:  {err.reason}')
    print(f'url:  {err.url}')
    
# ==========================


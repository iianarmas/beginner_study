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
## Headers

from urllib.request import urlopen


response = urlopen('http://www.debian.org')

# printing response and converting it to utf
print(response.readline().decode('utf-8'))
print()

# printing url address
print(f'URL: {response.url}')
print()

# printing status code
print(f'STATUS: {response.status}')
print()

# getting headers ----------
head = response.getheaders()

# by default, getheaders() will return a list of tuples,
# creating a dictionary is one option for nicer printing of info (I think)

element_dict = {}

for i, element in enumerate(head):
    element_dict[element[0]] = element[1]

for key, value in element_dict.items():
    print(f'{key}: {value}')

    # ==========================
## Customizing Request

from urllib.request import urlopen, Request


"""req = Request('http://www.debian.org')"""

# customizing request
"""req.add_header('Accept-Language', 'sv')

response = urlopen(req)


print(response.readlines()[:5])
print()
print(req.header_items())
print()"""

# shortcut for adding headers

header = {'Accept-Language': 'sv'}

req = Request('http://www.debian.org', headers=header)

response = urlopen(req)


print(response.readlines()[:5])
print()
print(req.header_items())
print()

# getting headers ----------
head = response.getheaders()

# by default, getheaders() will return a list of tuples,
# creating a dictionary is one option for nicer printing of info (I think)

element_dict = {}

for i, element in enumerate(head):
    element_dict[element[0]] = element[1]

for key, value in element_dict.items():
    print(f'{key}: {value}')

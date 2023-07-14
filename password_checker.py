import sys
import hashlib
import requests

def get_api_response(query_character):
    # Construct the URL for the API request
    url = 'https://api.pwnedpasswords.com/range/' + query_character
    # Send a GET request to the API
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code != 200:
        raise RuntimeError(f'Error fetching data: {response.status_code}. Please check the API and try again.')
    return response

def count_leaked_passwords(hashes_response, hash_to_find):
    # Split the response into lines and create a generator of tuples for each line
    hash_lines = (line.split(':') for line in hashes_response.text.splitlines())
    # Iterate through the tuples and check if the hash matches the desired hash
    for hash_value, count in hash_lines:
        if hash_value == hash_to_find:
            return count
    return 0

def check_password_in_pwned(password):
    # Convert the password to its SHA-1 hash representation
    sha1_password = hashlib.sha1(password.encode('UTF-8')).hexdigest().upper()
    # Split the hash into prefix and suffix
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    # Get the API response for the prefix
    response = get_api_response(prefix)
    # Count the occurrences of the password suffix in the response
    count = count_leaked_passwords(response, suffix)
    return count

def main(password):
    # Check if the password has been leaked
    count = check_password_in_pwned(password)
    # Print the result based on the leak count
    if count:
        print(f'Your password "{password}" has been found {count} times. Consider changing it.')
    else:
        print(f'Your password "{password}" is safe to use. Congrats! :)')
    return 'Done!'

if __name__ == '__main__':
    # Exit the program with the result of the main function
    sys.exit(main(sys.argv[1]))

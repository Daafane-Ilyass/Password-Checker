# Password Checker

This project is a password checker that utilizes the "Have I Been Pwned" API to determine if a password has been previously compromised. It checks the number of times a password has appeared in known data breaches and advises the user on whether they should change their password.

## Dependencies

The following dependencies are required to run the password checker:

- Python 3.x
- requests library (`pip install requests`)

## Usage

To check a password, run the `password_checker.py` script and provide the password as a command-line argument:

```
python password_checker.py [password]
```

Replace `[password]` with the password you want to check.

## How It Works

1. The password is hashed using the SHA-1 algorithm.
2. The first five characters of the hash (prefix) are sent as a request to the "Have I Been Pwned" API.
3. The API responds with a list of hashes that match the prefix.
4. The password's hash suffix (characters 6 onwards) is compared against the list of matching hashes to determine if it has been compromised.
5. If a match is found, the number of occurrences of the password in data breaches is returned.
6. The user is notified whether the password is safe to use or if it has been compromised.

## Limitations

- The password checker relies on the "Have I Been Pwned" API for its data. If the API is down or unavailable, the script will not function properly.
- The script only checks passwords locally and does not send the actual password to the API. It uses the hash of the password to compare against the leaked hashes.
- The script only checks against known data breaches and does not provide real-time protection against new breaches.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

import requests
import sys
import hashlib


def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    # print(url)
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}")
    else:
        return res


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    result = request_api_data(sha1password[:5])

    return get_pass_leaks_count(result, tail)


def get_pass_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count

    return 0


def main(args):
    for query in args:
        res = pwned_api_check(query)
        if res == 0:
            print("Nice your password was not found - carry on")
        elif res != 0:
            print(f"Change your password. Number of times it's been found {res} times")

    return "Done!"


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

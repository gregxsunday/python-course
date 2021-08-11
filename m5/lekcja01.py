import random
import secrets

if __name__ == '__main__':
    # print(random.randint(3, 9))

    vulns = ['xss', 'rce', 'ssrf']
    # print(random.choice(vulns))

    weights = [10, 5, 1]

    # print(random.choices(vulns, weights=weights))
    # print(random.choices(vulns, weights=weights, k=5))

    # print(secrets.token_hex(32))
    # print(secrets.token_urlsafe(32))
    print(secrets.choice(vulns))
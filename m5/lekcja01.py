import random

if __name__ == '__main__':
    print(random.randint(3, 9))

    vulns = ['xss', 'rce', 'ssrf']

    print(random.choice(vulns))

    weights = [10, 5, 1]

    print(random.choices(vulns, weights=weights))
    print(random.choices(vulns, weights=weights, k=5))

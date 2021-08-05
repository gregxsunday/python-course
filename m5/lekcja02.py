import json

if __name__ == '__main__':
    vulns = '''{
        "rce": {
            "impact": "critical",
            "auth_required": false
        }
    }'''

    vulns_json = json.loads(vulns)

    print(vulns_json)
    print(type(vulns_json))

    with open('vulns.json', 'w') as outfile:
        json.dump(vulns_json, outfile)


    with open('vulns.json', 'r') as infile:
        vulns_json = json.load(infile)

    print(vulns_json)
    vulns_str = json.dumps(vulns_json)
    print(vulns_str)
    vulns_str = json.dumps(vulns_json, indent=2)
    print(vulns_str)

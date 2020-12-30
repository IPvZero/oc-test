import requests
import json
import yaml

requests.packages.urllib3.disable_warnings()
device = {
    "host": "ios-xe-mgmt.cisco.com",
    "port": "9443",
    "user": "developer",
    "password": "C1sco12345"
}

headers = {
    "Accept": "application/yang-data+json",
    "Content-Type": "application/yang-data+json"
}

url = f"https://{device['host']}:{device['port']}/restconf/data/openconfig-acl:acl"

payload = {
  "openconfig-acl:acl": {
    "acl-sets": {
      "acl-set": [
        {
          "name": "OC-ACL-TEST",
          "type": "openconfig-acl:ACL_IPV4",
          "config": {
            "name": "OC-ACL-TEST",
            "type": "openconfig-acl:ACL_IPV4"
          },
          "acl-entries": {
            "acl-entry": [
              {
                "sequence-id": 10,
                "config": {
                  "sequence-id": 10
                },
                "ipv4": {
                  "config": {
                    "protocol": "cisco-xe-openconfig-acl-ext:IP"
                  }
                },
                "transport": {
                  "config": {
                    "source-port": "ANY",
                    "destination-port": "ANY"
                  }
                },
                "actions": {
                  "config": {
                    "forwarding-action": "openconfig-acl:ACCEPT",
                    "log-action": "openconfig-acl:LOG_NONE"
                  }
                }
              }
            ]
          }
        },
        {
          "name": "meraki-fqdn-dns",
          "type": "openconfig-acl:ACL_IPV4",
          "config": {
            "name": "meraki-fqdn-dns",
            "type": "openconfig-acl:ACL_IPV4"
          }
        }
      ]
    }
  }
}


response = requests.put(url=url, headers=headers, auth=(
    device['user'], device['password']), data=json.dumps(payload), verify=False)

response.raise_for_status()
print(response.status_code)

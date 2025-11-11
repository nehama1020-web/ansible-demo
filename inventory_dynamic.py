#!/usr/bin/env python3
# inventory_dynamic.py - dynamic inventory example for 3 VMs
import json, os
# You could discover via "multipass list --format json" here if you like.
# For demo, we read from env or fall back to defaults:
vm1 = os.getenv("VM1_IP", "10.56.44.183")
vm2 = os.getenv("VM2_IP", "10.56.44.29")
vm3 = os.getenv("VM3_IP", "10.56.44.246")

data = {
  "_meta": {"hostvars": {
    "vm1": {"ansible_host": vm1, "ansible_user": "ubuntu"},
    "vm2": {"ansible_host": vm2, "ansible_user": "ubuntu"},
    "vm3": {"ansible_host": vm3, "ansible_user": "ubuntu"},
  }},
  "web": {"hosts": ["vm1"]},
  "db": {"hosts": ["vm2"]},
  "app": {"hosts": ["vm3"]},
  "all": {"children": ["web", "db", "app"]}
}
print(json.dumps(data))


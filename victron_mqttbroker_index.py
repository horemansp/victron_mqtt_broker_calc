#ID can be found on the VRM portal under settings/general
VRM_portal_ID = "d41243b50dfc"

def _get_vrm_broker_url(_system_id):
    sum = 0
    for character in _system_id.lower().strip():
        sum += ord(character)
    broker_index = sum % 128
    return "mqtt{}.victronenergy.com".format(broker_index)

print(_get_vrm_broker_url(VRM_portal_ID))
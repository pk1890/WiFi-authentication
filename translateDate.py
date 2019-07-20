import os
import sys
from datetime import datetime, timezone
def LDAP_to_unix(date):
    dt = datetime(int(date[:4]), int(date[4:6]), int(date[6:8]), int(date[8:10]), int(date[10:12]))
    timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
    return timestamp

print(int(LDAP_to_unix(sys.argv[1])))


# HetznerDynDNS

Updates a dns record using the Hetzner DNS api. Runs as root, logs with logger. Won't access the Hetzner API unless a change needs to be made.

## Dependencies

- jq
- python3
- getent
- date
- bash
- logger
- python3 'requests' library

## Contents

`config.json` must be configured for your system

`hetznerDynDNSCron` is the cron script. Put it in your crondir or equivalent. I run mine hourly.

`updateZoneRecord.py` does the heavy lifting. It is called from the cron script.

`old` contains various helloworld type scripts

REF: <https://dns.hetzner.com/api-docs/>

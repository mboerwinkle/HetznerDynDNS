# HetznerDynDNS

## Contents

`config.json` must be configured for your system

`hetznerDynDNSCron` is the cron script. Put it in your crondir or equivalent. I run mine hourly.

`updateZoneRecord.py` does the heavy lifting. It is called from the cron script.

`old` contains various helloworld type scripts

REF: <https://dns.hetzner.com/api-docs/>

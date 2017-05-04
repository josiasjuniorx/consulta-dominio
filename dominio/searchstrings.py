nameserver = r'(?<= Name Server:).*|(?<=nserver:).*'

address = r'(?<=has address ).*|(?<=has IPv6 Address ).*|(?<=domain name pointer ).*(?=.)'

mail = r'.*mail is handled by.*'

ftp = r'(?<=is an alias for ).*(?=.)'

expiration_date = \
r'(?<!Registration) Expiration Date:.*(?!Z)|\
expires.*|\
expiry date:.*|\
Renewal date:.*|\
\npaid-till:.*|\
\[Expires on\].*|\
\[State\].*|\
Domain Expiration Date:.*|\
domain_datebilleduntil:.*|\
expire:.*|\
Expire Date:.*'

owner = \
r'registrant.*:.*|\
provider:.*|\
.*Registrar:.*|\
Company Name:.*|\
registrar_name:.*|\
owner.*|\
responsible:.*|\
.*status:.*|\
Registration status:.*|\
state:.*|\
Domain Status:.*|\
query_status:.*|\
domain:.*|\
.*domain name:.*'

ptr = r'(?<= domain name pointer ).*(?=.)'

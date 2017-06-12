nameserver = r'(?<= Name Server:).*|(?<=nserver:).*'

www = r'(?<=has address ).*|(?<=has IPv6 Address ).*|(?<=domain name pointer ).*(?=.)'

mail = r'.*mail is handled by.*(?=.)'

server = r'(?<= has address ).*'

ftp = r'(?<=is an alias for ).*(?=.)'

txt = r'(?<=descriptive text).*'

ns = r'(?<= name server ).*(?=.)'

spf = r'(?<= descriptive text ).*'

soa = r'(?<= has SOA record ).*'

ptr = r'(?<= domain name pointer ).*(?=.)'

# status = r'(?<=status: ).*'
status = \
r'.*status:.*|\
Registration status:.*|\
state:.*'

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
query_status:.*|\
domain:.*|\
.*domain name:.*'

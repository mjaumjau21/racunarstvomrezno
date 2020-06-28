import dns.resolver 

myDnsResolver = dns.resolver.Resolver() 
PrimjerMX= myDnsResolver.query("google.com", "MX")
PrimjerPTR= myDnsResolver.query("3.125.194.174.in-addr.arpa", "PTR")
PrimjerA = myDnsResolver.query("google.com", "A")   
for data in PrimjerA: 
    print ("A",data) 
for data in PrimjerMX:
    print ("MX",data)
for data in PrimjerPTR:
    print ("PTR",data)  
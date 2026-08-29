def daily_protocol (protocol_list):  
    unique = list(set(protocol_list))
    summary = {}

    for protocol in unique:
        summary[protocol] = protocol_list.count(protocol)
    return summary

protocols = ['0MAD', '2MAD', '0MAD', 'Autophagy Marathone']
result = daily_protocol(protocols)

print("Protocol Breakdown: ")
for protocol, days in result.items():
    print(f"Protocol: {protocol} | Days practised: {days} day(s)")
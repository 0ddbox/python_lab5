def is_valid_part(part):
    if not part.isdigit():
        return False
    num = int(part)
    if num < 0 or num > 255:
        return False
    if len(part) > 1 and part[0] == '0':
        return False
    return True

def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not is_valid_part(part):
            return False
    return True

def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_to_binary(n // 2) + str(n % 2)

def binary_to_decimal(b):
    if not b:
        return 0
    return int(b[0]) * (2 ** (len(b) - 1)) + binary_to_decimal(b[1:])

def ip_to_binary(ip):
    if not is_valid_ip(ip):
        return "Invalid IP address"
    parts = ip.split('.')
    binary_parts = [decimal_to_binary(int(part)).zfill(8) for part in parts]
    return '.'.join(binary_parts)

def binary_to_ip(binary_ip):
    parts = binary_ip.split('.')
    for part in parts:
        if len(part) != 8 or not all(bit in '01' for bit in part):
            return "Invalid Binary IP address"
    decimal_parts = [str(binary_to_decimal(part)) for part in parts]
    return '.'.join(decimal_parts)

def ip_convert(ip):
    if is_valid_ip(ip):
        return ip_to_binary(ip)
    elif all(len(part) == 8 and all(bit in '01' for bit in part) for part in ip.split('.')):
        return binary_to_ip(ip)
    else:
        return "Invalid IP address or binary representation"

## User input for IP address
user_ip = input("Enter an IP address or binary IP address: ")
result = ip_convert(user_ip)
print(result)


##Example test cases for is_valid_ip
##print(is_valid_ip("192.168.1.1"))  # True
##print(is_valid_ip("192.168.256.1"))  # False
##print(is_valid_ip("192.168.1"))  # False
##print(is_valid_ip("192.168.01.1"))  # False

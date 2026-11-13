
def crc(ip, poly, mode):
    op = list(ip)

    # Append 16 zeros
    if mode == 1:
        op += ['0'] * 16

    # Perform XOR division
    for i in range(len(op) - len(poly) + 1):
        if op[i] == '1':
            for j in range(len(poly)):
                op[i + j] = str(int(op[i + j]) ^ int(poly[j]))

    # Check remainder
    remainder = ''.join(op[-16:])

    if '1' not in remainder:
        return 1, remainder
    else:
        return 0, remainder


def main():
    poly = "10001000000100001"

    print("Enter the input message in binary:")
    ip = input().strip()

    if not ip or any(bit not in '01' for bit in ip):
        print("Invalid binary input")
        return

    _, remainder = crc(ip, poly, 1)

    transmitted = ip + remainder

    print("The transmitted message is:", transmitted)

    print("Enter the received message in binary:")
    recv = input().strip()

    if len(recv) != len(transmitted) or any(bit not in '01' for bit in recv):
        print("Invalid received message")
        return

    result, _ = crc(recv, poly, 0)

    if result == 1:
        print("No error in data")
    else:
        print("Error in data transmission has occurred")


if __name__ == "__main__":
    main()

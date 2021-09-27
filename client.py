import socket

# function that send massage to the server and return the answer
def send(msg, start):
    SERVER_IP = "127.0.0.1"         # returning to my computer
    SERVER_PORT = 9090

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connecting to remote computer 80
    server_address = (SERVER_IP, SERVER_PORT)
    sock.connect(server_address)

    if start:
        msg = sock.recv(1024)       # first msg received
        msg = msg.decode()
    else:
        sock.sendall(msg.encode())   # msg sent
        msg = sock.recv(1024)       # msg received
        msg = msg.decode()

    return msg

# print menu
def menu():
    print("1 - list of albums")
    print("2 - enter album's name and get the album's songs")
    print("3 - enter song's name and get its length")
    print("4 - enter song's name and get its lyrics")
    print("5 - enter song's name and get its album's name")
    print("6 - enter a word and get all songs that has this word in their names")
    print("7 - enter a word and get all songs that has this word in its lyrics")
    print("8 - exit")
    choice = int(input("Enter number: "))           # collect choice

    return choice

# take the result (answer of the server) and return string which look more clean (with no codes and numbers)
def fix_answer(answer):
    valid = int(answer[0])
    if int(valid) == 2:
        option = answer[2]
        option = int(option)
        answer = answer.split("|")
        answer = answer[1]
        answer = answer.split("&")
        if option == 1:
            answer = answer[0]
        elif option == 2:
            answer = answer[1]
        elif option == 3:
            answer = answer[1]
        elif option == 4:
            answer = answer[2]
        elif option == 5:
            answer = answer[0]
        elif option == 6:
            answer = answer[1]
        elif option == 7:
            answer = answer[1]
        if not option == 3:         # cause in option 3 there : in the answer
            answer = answer.split(":")
            answer = answer[1]

    else:
        answer = answer[4:]

    return answer

# ask for data (album name / song name / word)
def get_data(choice):
    if choice == 1:
        data = "NONE"
    elif choice == 2:
        data = str(input("Enter album name: "))
    elif choice == 3:
        data = str(input("Enter song name: "))
    elif choice == 4:
        data = str(input("Enter song name: "))
    elif choice == 5:
        data = str(input("Enter song name: "))
    elif choice == 6:
        data = str(input("Enter a word: "))
    elif choice == 7:
        data = str(input("Enter a word: "))
    else:
        data = "NONE"
    return data

def main():

    ##############
    # INITIALIZE #
    ##############

    EXIT = 0
    msg = ""
    start = True

    #############
    #   MAIN    #
    #############

    try:
        answer = send(msg, start)
        print(answer)
    except Exception as e:
        print("Error: ", e)
        EXIT = 1

    while EXIT == 0:
        start = False
        data = ""
        choice = menu()
        if choice == 8:
            EXIT = 1
            break
        data = get_data(choice)

        msg = "10" + str(choice) + "|" + data   # generate the request

        try:
            answer = send(msg, start)
            answer = fix_answer(answer)
            print(answer)
        except Exception as e:
            print("Error: ", e)
            EXIT = 1
            break


if __name__ == "__main__":
    main()
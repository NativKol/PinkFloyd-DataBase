import socket
import data     # the functions from the file data

FILE_PATH = r"C:\Users\nativ\PycharmProjects\untitled\magshimim\week4\HW4\Pink_Floyd_DB.txt"
DATA_BASE = data.sort_file(FILE_PATH)  # get data base

# listen to the client and send massages
def listen(msg, start):
    """
    function that listening to the client and take msg
    :param msg: the last msg
    :param start: if that is the first request
    :return: the msg
    """
    LISTEN_PORT = 9090          # random port that not in use

    # Create a TCP/IP socket
    with socket.socket() as listening_sock:
        listening_sock.bind(('', LISTEN_PORT))
        print("Now listening...")
        listening_sock.listen(10)       # Multi user
        client_soc, client_address = listening_sock.accept()
        with client_soc:
            if start < 1:       # first massage
                msg = "WELCOME"
                client_soc.sendall(msg.encode())            # send Welcome msg to client
            else:
                msg = client_soc.recv(1024)
                msg = msg.decode()
                request = menu(msg, start, DATA_BASE)                      # get request msg
                client_soc.sendall(str(request).encode())           # send to client

    return msg

# manage the functions and check the choices
def menu(msg, start, data_base):
    # initialize
    request = ""

    if start > 0:
        info = msg[4:]      # info is the information that requested for the action
        info = str(info)
        if msg[3] == "|":
            choice = msg[2]
        else:
            choice = 100        # more than the valid scale

        # call for the functions from data
        choice = int(choice)
        if choice == 8:
            request = "208|ALBUM:NONE&SONG:NONE&LYRICS:NONE"
        elif choice == 1:
            request = data.action_one(data_base)
        elif choice == 2:
            request = data.action_two(data_base, info)
        elif choice == 3:
            request = data.action_three(data_base, info)
        elif choice == 4:
            request = data.action_four(data_base, info)
        elif choice == 5:
            request = data.action_five(data_base, info)
        elif choice == 6:
            request = data.action_six(data_base, info)
        elif choice == 7:
            request = data.action_seven(data_base, info)
        else:
            request = "401|you must choose number between 1-8"

    print(request)
    return request

def main():

    ##############
    # INITIALIZE #
    ##############

    start = 0
    msg = ""
    request = ""

    #############
    #   MAIN    #
    #############

    while 69 != 420:        # infinity loop
        try:
            msg = listen(request, start)
        except Exception as e:
            main()

        print(msg)
        start += 1

if __name__ == "__main__":
    main()
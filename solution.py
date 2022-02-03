from socket import *

#https://pythontic.com/modules/socket/recv
#https://stackoverflow.com/questions/27014955/socket-connect-vs-bind
#https://realpython.com/python-sockets/
#https://users.cs.cf.ac.uk/Dave.Marshall/PERL/node175.html - SMTP codes



def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"
    bufferSize = 1024
    # linear mail client
    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port)) #client uses connect instead of bind
    # Fill in end

    recv = clientSocket.recv(bufferSize).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    #if recv[:3] != '220': <-first three characters of the response
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(bufferSize).decode()
    #print(recv1) 
    #if recv1[:3] != '250':
    #    print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    fromCommand = "'MAIL FROM: <tmortica@gmail.com>\r\n'"
    clientSocket.send(fromCommand.encode())
    recv2 = clientSocket.recv(bufferSize).decode()
    #print (recv2)
    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    toCommand = "'RCPT TO: <superjames1234@gmail.com>\r\n'"
    clientSocket.send(toCommand.encode())
    recv3 = clientSocket.recv(bufferSize).decode()
    #print (recv3)
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    dataCommand = "'DATA\r\n'"
    clientSocket.send(dataCommand.encode())
    recv4 = clientSocket.recv(bufferSize).decode()
    #print (recv4)
    # Fill in end

    # Send message data.
    # Fill in start
    #using variable msg from top of code
    clientSocket.send(msg.encode())
    #recv5 = clientSocket.recv(bufferSize).decode()
    #print (recv5)
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    #using variable endmsg from top of code
    clientSocket.send(endmsg.encode())
    recv6 = clientSocket.recv(bufferSize).decode()
    #print (recv6)
    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv7 = clientSocket.recv(bufferSize).decode()
    #print (recv7)
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
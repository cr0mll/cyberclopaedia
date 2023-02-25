# Introduction
The File Transfer Protocol (FTP) is an application layer protocol which allows for the sharing of files within a network. It uses TCP as its underlying transport-layer protocol and follows a typical client-server model where the FTP client is typically called the *user*.

## Operational Model
Unlike most other TCP-based protocols, FTP utilises more than a single connection. When a user connects to a server, an FTP *control connection* is opened. Afterwards, *data connections* are established for every subsequent data transfer. The control connection is utilised for passing commands from the user to the server as well the command response from the server back to the client. A data connection is terminated once the file transfer it was established for is complete.

The FTP software packages which run on the client and the server are called the *User-FTP Process* and the *Server-FTP process*, respectively. Each of these packages is comprised of a *protocol interpreter* (PI), which is used for managing the control connection, and a *data transfer process* (DTP), which handles the actual data transmission through the data connections.

![](Resources/Images/FTP/FTP%20Operational%20Model.svg)

The *Server Protocol Interpreter* (Server-PI) manages the control connection on the server's side. It listens on the reserved for FTP port 21. When a connection is established, it receives commands form the User-PI, sends back replies, and manages the Server-DTP.
The *Server Data Transfer Process* (Server-DTP) is responsible for sending and receiving data to and from the User-DTP. It can establish data connections or listen for such ones coming from the user. The Server-DTP is what interacts with the server's local file system.

The *User Protocol Interpreter* (User-PI) is responsible for initiating and managing the control connection on the client's side. Furthermore, it processes commands, sends them to the Server-PI and manages the User-DTP.
The *User Data Transfer Process* (User-DTP) is responsible for sending and receiving data to and from the Server-DTP. It can establish data connections or listen for such ones coming from the server and it is also what interacts with the client's local file system.

Additionally, FTP supports an alternative way for transferring data called *Third-Party File Transfer* or *Proxy FTP*. Here, the FTP user is used as a proxy in order to perform a file transfer from one FTP server to another.

## Authentication
Before any data connections can be opened, a control connection must be established. It is initiated by the client opening a TCP connection with a destination port of 21. Once the server is ready, the client authenticates themselves by dint of the `USER` and `PASS` commands used for specifying the username and the password, respectively. If the credentials aren't found within the server's database, the server is typically going to request that the client make a new attempt. After a few unsuccessful tries, the server may choose to terminate the connection. Upon a successful connection, the client will receive a greeting from the server, indicating its readiness to serve data transfers. 

![](Resources/Images/FTP/FTP%20Authentication.svg)

### Anonymous Authentication
FTP also supports anonymous authentication which allows anyone to get a certain level of access to an FTP server. This might be useful when someone wants to freely distribute a file on their server. Anonymous authentication is achieved by specifying the `guest` username and an empty password, although other usernames such as `anonymous` and `ftp` are also widely supported. Typically, anonymous authentication severly restricts the access rights of the user.

## Data Connection Management
The control connection established between the Server-PI and the User-PI at the outset is maintained throughout the entire FTP session and is used solely for exchanging commands and replies but not actual data.

A separate data connection must be established for each file transfer. Note that this is also true for implicit data transfers scuh as requesting a directory listing from the server. 

FTP specifies two modes of creating data connections.

### Normal (Active) Data Connections
In this type of connection, the data channel is initiated by the Server-DTP by opening a TCP connection to the User-DTP. The source port used by the server is 20, while the destination port on the client is, by default, the ephermal port number used for the control connect, although the latter is often changed in order to avoid complications. This is achieved by the client issuing a `PORT` command before the data transfer.

![](Resources/Images/FTP/FTP%20Active%20Connection.svg)

### Passive Data Connections
In a passive data connection, the client tells the server to wait for a data channel created by the client. The server then responds with the destination IP address and port that the client should use for the establishment of the connection. The source port is, again by default, the one used for the control connection, but the client usually alters it in order to avoid complications.

![](Resources/Images/FTP/FTP%20Passive%20Connection.svg)


## Data Types
FTP supports four data types. 

The *ASCII type* is used for sharing text files in a platform-agnostic way. The sender of the file converts platform-specific line endings to `CR+LF`, while the receiver of the file reverses this. This entails that the file size of a file sent in ASCII mode may differ on the sender and the recepient. The *EBCDIC* is conceptually the same as the ASCII type, but for files using IBM's EBCDIC character set.

The *image* or *binary* type sends the file as is, without altering it. 

The *local* type specifies a file which may store data in logical bytes which are of length other than 8.

It is paramount that the correct type be specified when sending different files. Using the ASCII mode when a binary file is being transmitted will result in the file's corruption due to bytes which represent a line ending being altered to `CR+LF`. Similarly, transferring a text file using binary mode will result in the file having incorrect line endings.

### Format Control
The format control parameter is defined for ASCII and EBCDIC files and allows the user to specify a representation for a file's vertical formatting (not very important). There are three possibilities for this parameter:
- **Non Print** (default) - no vertical formatting
- **Telnet Format** - indicates usage of vertical format control characters within the file as specified by Telnet
- **Carriage Control / FORTRAN** - indicates usage of the first character of each line as a format control character

### Data Structure
It is also possible to specify a file's data structure:
- **File Structure** - the file is a contiguous stream of bytes bearing no internal structure
- **Record Structure** - the file consists of a set of sequential records delimited by an end-of-record marker
- **Page Structure** - the file is a set of specially indexed data pages

The *File Structure* is used almost exclusively.

## Data Transmission Modes
FTP specifies three modes for data transmission.

In **Stream Mode**, the data is sent as a continuous stream of bytes. No metadata is attached to it and the end of the transfer is marked by the sender terminating the data connection once the file transfer is complete. This mode relies heavily on TCP's reliable transport services.

In **Block Mode** data is broken into individual FTP records. Each record contains a 3-byte header indicating its length as well as additional information about the blocks.

**Compressed Mode** uses run-length encoding to reduce the file size. It is pretty much obsolete as compression is usually performed by other programmes.

## FTP Commands & Replies
The User-PI issues commands and the Server-PI acknowledges them via responses. All commands and replies travel through the control connection.

### Commands
FTP commands are divided into three groups.

**Access Control Commands** are the commands which are part of the user login and authentication process, are used for resource access, or are simply a part of the general session control.

|Command Code|Command Name|Description|
|:----------------:|:------------------:|-------------|
|`USER`|User Name|Specifies the username of the user attempting to establish the FTP session.|
|`PASS`|Password|Specifies the password of the user given previously by `USER`.|
|`ACCT`|Account|Specifies an account for an authenticated user during the FTP session. Rarely used, since most systems automatically select an account based on the username from `USER`.|
|`CWD`|Change Working Directory|Changes the directory the user is currently in.|
|`CDUP`|Change to Parent Directory|A specialised `CWD` command which just goes up a directory.|
|`SMNT`|Structrure Mount|Mounts a particular file system for resource access.|
|`REIN`|Reinitialise|Reinitialise the FTP session by flushing all previously set parameters.|
|`QUIT`|Logout|Terminates the FTP session and closes the control connection. The name is a bit of a misnomer, since `REIN` is more akin to an actual logout.|

**FTP Transfer Parameter Commands** are used for specifying how data transfers should occur.

|Command Code|Command Name|Description|
|:----------------:|:------------------:|-------------|
|`PORT`|Data Port|Tells the FTP server on which port the client is going to listen for a data connection.|
|`PASV`|Passive|Tells the server to await a data connection from the client.|
|`TYPE`|Representation Type|Specifies the file type (ASCII, EBCDIC, Image, or Logical). Additionally it may specify the format control.|
|`STRU`|File Structure|Specifies the data structure (File, Record, or Page).|
|`MODE`|Transfer Mode|Specifies the transmission mode to be used (Stream, Block, or Compressed).|

**FTP Service Commands** constitute all the commands which actually operate with files.

|Command Code|Command Name|Description|
|:----------------:|:------------------:|-------------|
|`RETR`|Retrieve|Tells the server to send a file to the user.|
|`STOR`|Store|Sends a file to the server.|
|`STOU`|Store Unique|The same as `STOR`, however, it instructs the server to ensure that the file has a unique name in the directory. This is done to make sure that an already existing file is not overwritten.|
|`APPE`|Append|The same as `STOR`, however, if the file already exists, the data is appended to the file instead of replacing the already existinig data.|
|`ALLO`|Allocate|An optional command for reserving storage on the server before a file transfer.|
|`REST`|Restart|Restarts a file transfer at a particular server marker. May only be used for Block and Compressed transfer modes.|
|`RNFR`|Rename From|Specifies the old name of a file to be renamed.|
|`RNTO`|Rename To|Specifies the new name of a file to be renamed. Used in conjunction with the `RNFR` command.|
|`ABOR`|Abort|Tells the server to abort the last FTP command or current data transfer.|
|`DELE`|Delete|Deletes a file on the server.|
|`RMD`|Remove Directory|Deletes a directory on the server.|
|`MKD`|Make Directory|Creates a directory on the server.|
|`PWD`|Print Working Directory|Displays the current directory on the server.|
|`LIST`|List|Requests a directory listing from the server.|
|`NLST`|Name List|Similar to `LIST`, but only returns the file names.|
|`SITE`|Site Parameters|Used for the implementation of additional features.|
|`SYST`|System|Requests operating system information from the server.|
|`STAT`|Status|Requests information about the status of a file or the current transfer.|
|`HELP`|Help|Displays help information.|
|`NOOP`|No Operation|Does absolutely nothing. Used to prompt the server for an `OK` response in order to verify that the control channel is still active.|

### Replies
FTP avails itself of 3-digit reply codes of the form `xyz`. Each digit carries different type of information and provides reply categorisation. 

The *first* digits represents the success or failure status of the FTP command previously sent.

|Reply Code|Name|Meaning|
|:-----------:|:------:|---------|
|1yz|Positive Perliminary Reply|An initial response indicating the acknowledgment of the command and that the command is still in progress. The user should await another reply before proceeding with the next command.|
|2yz|Positive Completion Reply|The command has been successfully processed and completed.|
|3yz|Positive Intermediate Reply|Acknowledgment of the command but also an indication that additional information is needed in order to proceed with the command's execution. Sent for example after `USER` but before `PASS`.|
|4yz|Transient Negative Completion Reply|The command could not be executed but may be tried again.|
|5yz|Permanent Negative Completion Reply|The command could not be executed and another attempt is likely to throw an error as well.|

The *second* digit is utilised for the categorisation of replies into functional groups.

|Reply Code|Name|Meaning|
|:-----------:|:------:|---------|
|x0z|Syntax|Syntax errors or miscellaneous messages.|
|x1z|Information|Replies to requests for information, such as status requests.|
|x2z|Connections|Replies pertaining to the control or data connection.
|x3z|Authentication & Accounting|Replies related to login procedures and accounting.|
|x4z|Unspecified|Undefined.|
|x5z|File System|Replies related to the server's file system.|

The *third* digit is what indicates the specific message type. Each functional group can have 10 different reply codes for each reply type given by the first digit.
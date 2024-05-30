# client-server

CS232 project
Parallel File Transfer Client & Server

Created by  Emma Wang (ejw38)
Dates       24, 28, 29 May 2024


Test files used: 10
┌─────────────┬───────────────────┬─────────────┐
│ Type        │ Filename          │ Bytes       │
├─────────────┼───────────────────┼─────────────┤
│ .txt        │ cheese            │ 66          │
├─────────────┼───────────────────┼─────────────┤
│ .txt        │ above_silence     │ 350851      │
├─────────────┼───────────────────┼─────────────┤
│ .exe        │ magicsquare       │ 72335       │
├─────────────┼───────────────────┼─────────────┤
│ .pdf        │ concerto          │ 1271211     │
├─────────────┼───────────────────┼─────────────┤
│ .docx       │ ellie             │ 689409      │
├─────────────┼───────────────────┼─────────────┤
│ .xlsm       │ plan              │ 29902       │
├─────────────┼───────────────────┼─────────────┤
│ .mscz       │ MuramatsuEarth    │ 63316       │
├─────────────┼───────────────────┼─────────────┤
│ .jpg        │ norman            │ 3531876     │
├─────────────┼───────────────────┼─────────────┤
│ .mp3        │ chopin            │ 4246105     │
├─────────────┼───────────────────┼─────────────┤
│ .mp4        │ bigail            │ 1960355     │
└─────────────┴───────────────────┴─────────────┘


--------------------------------------------
Questions/comments/observations
    On Tips:
    - What are the states (INIT, SENT_OK) for? I actually have no idea
    - "If there is any error seen, the thread just breaks out of the loop, which closes the sock." What loop? I don't have to have one right?
    - Why put \n after every sendall()?
    - I ended up not using `if not data:` because I think it kept getting stuck on sock.recv(1024)

    On What'll be tested:
    - I don't have to cover all bases on command line args right? Is it enough to just check number of args and make sure the files exist?
    - Does I have to handle using * to select all files in the directory? Because it currently doesn't work

    Other
    - Sample run solution is very helpful
    - Wait, is the ssh to a lab machine new? No more guacamole?
    - Organization-- The info is scattered between the 4 sections (Details, The File Transfer Protocol, Tips, What I will test for), so it takes a couple of read-throughs to understand. Not necessarily a problem, it just feels a bit scatterbrained, I don't know

Approx. time/effort dist.:
    5%  Reading instructions
    1%  Connecting + sending bytes
    22% Reading/writing to files
    13% Multi-threading
    50% Debugging
    9%  Cleaning


--------------------------------------------
Sources used:

https://realpython.com/python-sockets/
https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client
https://www.tutorialspoint.com/python/python_command_line_arguments.htm
https://stackoverflow.com/questions/15753701/how-can-i-pass-a-list-as-a-command-line-argument-with-argparse
https://www.geeksforgeeks.org/python-convert-string-to-bytes/
https://www.tutorialspoint.com/python/os_stat.htm
https://docs.python.org/3/library/socket.html#functions
https://www.geeksforgeeks.org/multithreading-python-set-1/
https://stackoverflow.com/questions/68425239/how-to-handle-multithreading-with-sockets-in-python
https://stackoverflow.com/questions/7174927/when-does-socket-recvrecv-size-return
https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions
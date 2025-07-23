# UDP Flood (Python)

## Overview

This project provides a straightforward Python script for generating UDP packet floods to a specific IP address and port.  
Primarily intended for network stress testing and educational exploration, it allows users to observe how systems respond to high volumes of UDP traffic.

## Features

- Customizable target IP address, port, and duration via interactive prompts.
- Randomized packet sizes for each transmission (between 1024 and 2048 bytes).
- Progress logging every 100 packets sent.
- Packet send rate includes randomized intervals to mimic non-uniform network traffic.
- Graceful interruption and error handling.

## Usage

> **Important:**  
> Please use this tool responsibly and only on networks and systems you own or have explicit permission to test.  
### Prerequisites

- [Python 3](https://www.python.org/downloads/) must be installed.

### Running the Script

Execute the script from your terminal:

```bash
python udp_flood.py
```

You will be prompted to enter:

1. **Target IP** – the address to send UDP packets to (e.g., `192.168.1.100`)
2. **Target Port** – the port number (e.g., `8080`)
3. **Duration** – how long the flood should last, in seconds (e.g., `30`)

During execution, the script will periodically report how many packets have been sent.  
You can stop the process at any time with `Ctrl+C`.

### Example Session

```
Enter the target IP: 192.168.1.100
Enter the target port: 8080
How long should the attack last (in seconds)? 30
Sending packets...
Sent 100 packets
Sent 200 packets
...
Finished sending.
```

## How It Works

- The script opens a UDP socket.
- It sends randomly sized data packets to the specified target for the chosen duration.
- Each packet is sent after a brief, randomized delay to simulate realistic network traffic.
- Progress is displayed for every 100 packets sent.


## License

MIT License

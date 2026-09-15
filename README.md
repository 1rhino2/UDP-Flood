# UDP-Flood

Basic UDP packet generator in Python. Point it at a host and port and it fires
packets for however many seconds you tell it. I use it to stress-test my own
services.

## Run

```bash
python main.py
```

It asks for the target IP, port, and duration, then sends until the timer runs
out.

## Use it on your own stuff only

Blasting UDP at a host you dont own or have permission to test is a denial of
service and is illegal in most places. Keep it to your own boxes and lab
networks.

## License

MIT

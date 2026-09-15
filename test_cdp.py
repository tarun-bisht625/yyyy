import subprocess, time, urllib.request, json, socket, base64, os

def simple_ws_send_recv(ws_url, msg):
    # ws_url format: ws://127.0.0.1:9223/devtools/page/UUID
    parts = ws_url.replace("ws://", "").split("/")
    host_port = parts[0].split(":")
    host = host_port[0]
    port = int(host_port[1])
    path = "/" + "/".join(parts[1:])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    sec_key = base64.b64encode(os.urandom(16)).decode()
    handshake = (
        f"GET {path} HTTP/1.1\r\n"
        f"Host: {host}:{port}\r\n"
        f"Upgrade: websocket\r\n"
        f"Connection: Upgrade\r\n"
        f"Sec-WebSocket-Key: {sec_key}\r\n"
        f"Sec-WebSocket-Version: 13\r\n\r\n"
    )
    s.sendall(handshake.encode())
    resp = s.recv(4096)
    if b"101" not in resp:
        raise RuntimeError("WS Handshake failed: " + resp.decode(errors='ignore'))

    # Encode websocket text frame
    payload = json.dumps(msg).encode('utf-8')
    frame = bytearray([0x81]) # text, fin
    length = len(payload)
    if length < 126:
        frame.append(0x80 | length) # masked
    elif length < 65536:
        frame.append(0x80 | 126)
        frame.extend(length.to_bytes(2, 'big'))
    else:
        frame.append(0x80 | 127)
        frame.extend(length.to_bytes(8, 'big'))
    
    mask = os.urandom(4)
    frame.extend(mask)
    masked_payload = bytes(b ^ mask[i % 4] for i, b in enumerate(payload))
    frame.extend(masked_payload)

    s.sendall(frame)

    # Read response frame
    data = s.recv(65536)
    s.close()
    return data

edge_proc = subprocess.Popen([
    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
    '--headless=new',
    '--remote-debugging-port=9224',
    '--disable-gpu',
    'http://localhost:8080'
])

time.sleep(3)
try:
    with urllib.request.urlopen('http://127.0.0.1:9224/json') as r:
        targets = json.loads(r.read().decode('utf-8'))
    
    page = next(t for t in targets if 'Architect' in t.get('title', ''))
    ws_url = page['webSocketDebuggerUrl']

    # Test evaluate window.debugGame
    eval_cmd = {
        "id": 1,
        "method": "Runtime.evaluate",
        "params": {
            "expression": "({ hasGame: typeof window.debugGame !== 'undefined', has3D: typeof window.blueprint3D !== 'undefined', hasSound: typeof window.soundEngine !== 'undefined', hasFacts: typeof window.factGenerator !== 'undefined' })",
            "returnByValue": True
        }
    }
    raw = simple_ws_send_recv(ws_url, eval_cmd)
    print("CDP Raw response length:", len(raw))
    # Parse JSON after websocket frame header
    for i in range(len(raw)):
        if raw[i:i+1] == b'{':
            try:
                parsed = json.loads(raw[i:].decode('utf-8', errors='ignore'))
                print("EVAL RESULT:", json.dumps(parsed.get('result', {}).get('result', {}).get('value', {}), indent=2))
                break
            except:
                pass

finally:
    edge_proc.terminate()

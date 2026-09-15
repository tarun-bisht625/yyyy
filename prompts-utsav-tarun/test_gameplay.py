import subprocess, time, urllib.request, json, socket, base64, os

def send_recv_ws(ws_url, msg):
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
        raise RuntimeError("Handshake failed")

    payload = json.dumps(msg).encode('utf-8')
    frame = bytearray([0x81])
    length = len(payload)
    if length < 126:
        frame.append(0x80 | length)
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
    data = s.recv(65536)
    s.close()
    
    for i in range(len(data)):
        if data[i:i+1] == b'{':
            try:
                return json.loads(data[i:].decode('utf-8', errors='ignore'))
            except:
                pass
    return None

edge_proc = subprocess.Popen([
    r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
    '--headless=new',
    '--remote-debugging-port=9225',
    '--disable-gpu',
    'http://localhost:8080'
])

time.sleep(3)
try:
    with urllib.request.urlopen('http://127.0.0.1:9225/json') as r:
        targets = json.loads(r.read().decode('utf-8'))
    
    page = next(t for t in targets if 'Architect' in t.get('title', ''))
    ws_url = page['webSocketDebuggerUrl']

    # 1. Start the game!
    start_cmd = {
        "id": 1,
        "method": "Runtime.evaluate",
        "params": {
            "expression": "window.debugGame.startGame(); ({ isRunning: window.debugGame.isRunning, wave: window.debugGame.currentWave, health: window.debugGame.serverHealth })",
            "returnByValue": True
        }
    }
    r1 = send_recv_ws(ws_url, start_cmd)
    print("STEP 1 (Start Game):", r1.get('result', {}).get('result', {}).get('value'))

    # Wait 2 seconds for bugs to spawn
    time.sleep(2)

    # 2. Check bugs and shoot the first bug
    shoot_cmd = {
        "id": 2,
        "method": "Runtime.evaluate",
        "params": {
            "expression": "(() => { const bugCount = window.debugGame.bugs.length; let shotHit = false; if (bugCount > 0) { const b = window.debugGame.bugs[0]; window.debugGame.shootHotfix(b.x, b.y); shotHit = true; } return { bugCountBeforeShot: bugCount, shotFired: window.debugGame.shotsFired, score: window.debugGame.score, shotsHit: window.debugGame.shotsHit }; })()",
            "returnByValue": True
        }
    }
    r2 = send_recv_ws(ws_url, shoot_cmd)
    print("STEP 2 (Bug Spawn & Shoot):", r2.get('result', {}).get('result', {}).get('value'))

finally:
    edge_proc.terminate()

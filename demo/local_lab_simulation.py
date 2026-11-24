"""Laboratório de software local para conceitos IoT. Não acessa dispositivo real."""
from __future__ import annotations

from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from threading import Thread
from urllib.request import Request, urlopen
import hashlib
import hmac
import json

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "network" / "evidence"
EVIDENCE.mkdir(parents=True, exist_ok=True)

captured: list[dict] = []

class Handler(BaseHTTPRequestHandler):
    def do_POST(self) -> None:
        size = int(self.headers.get("Content-Length", "0"))
        body = self.rfile.read(size)
        record = {
            "simulation": True,
            "transport": "HTTP",
            "tls": False,
            "authentication": False,
            "path": self.path,
            "body_utf8": body.decode("utf-8", errors="replace"),
        }
        captured.append(record)
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"accepted":true,"simulation":true}')
    def log_message(self, *_args) -> None:
        pass

server = HTTPServer(("127.0.0.1", 0), Handler)
thread = Thread(target=server.serve_forever, daemon=True)
thread.start()
url = f"http://127.0.0.1:{server.server_port}/telemetry"
telemetry = {
    "device_id": "LAB-NEXASENSE-SIM",
    "temperature_c": 23.8,
    "humidity_pct": 50.2,
    "data_class": "synthetic",
}
request = Request(
    url,
    data=json.dumps(telemetry, separators=(",", ":")).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST",
)
try:
    with urlopen(request, timeout=3) as response:
        response_body = response.read().decode("utf-8")
finally:
    server.shutdown()
    server.server_close()

log_path = EVIDENCE / "loopback-http-simulation.jsonl"
log_path.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in captured), encoding="utf-8")

# Firmware-like byte strings are synthetic lab fixtures; nothing is flashed or installed.
original = b"LAB-SIM-NEXASENSE-FIRMWARE-V1"
modified = b"LAB-SIM-NEXASENSE-FIRMWARE-V1-MODIFIED"
demo_key = b"LAB-ONLY-DEMO-KEY-NOT-FOR-PRODUCTION"
signature = hmac.new(demo_key, original, hashlib.sha256).digest()
insecure_accepts_modified = bool(modified)  # Deliberately omits authenticity/integrity validation.
secure_accepts_original = hmac.compare_digest(
    hmac.new(demo_key, original, hashlib.sha256).digest(), signature
)
secure_accepts_modified = hmac.compare_digest(
    hmac.new(demo_key, modified, hashlib.sha256).digest(), signature
)

manifest = (
    "LAB FIXTURE ONLY - NOT THE NEXASENSE DEVICE FIRMWARE\n"
    f"Name: simulated firmware byte string\nSize: {len(original)} bytes\n"
    f"SHA-256: {hashlib.sha256(original).hexdigest()}\n"
    "Origin: generated locally by demo/local_lab_simulation.py\n"
    "Use: demonstrate hash recording; not evidence from the supplied device.\n"
)
(ROOT / "firmware" / "simulated-fixture-hash.txt").write_text(manifest, encoding="utf-8")

print("LOCAL SOFTWARE LAB - SIMULATION ONLY; NO PHYSICAL DEVICE")
print(f"HTTP destination: {url} (loopback only)")
print(f"HTTP server response: {response_body}")
print(f"Observed cleartext synthetic body: {captured[0]['body_utf8']}")
print(f"Evidence log: network/evidence/{log_path.name}")
print("Transport/authentication in model: HTTP / no TLS / no authentication")
print(f"Original synthetic fixture SHA-256: {hashlib.sha256(original).hexdigest()}")
print(f"Modified package accepted by insecure model: {insecure_accepts_modified}")
print(f"Signed original accepted by comparison verifier: {secure_accepts_original}")
print(f"Modified package accepted by comparison verifier: {secure_accepts_modified}")
print("Limit: outcomes describe this local model only; they are not findings on NexaSense.")


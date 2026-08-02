import subprocess
import json
from datetime import datetime


hosts = {
    "pc1": "simple_bgp_pc1",
    "pc2": "simple_bgp_pc2"
}

targets = {
    "pc1": "200.1.1.2",
    "pc2": "195.11.14.2"
}


def ping(src, dst):

    cmd = (
        f"docker exec $(docker ps -q -f name={hosts[src]}) "
        f"ping -c 2 {targets[dst]}"
    )

    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True
    )

    return "0 received" not in result.stdout


results = []

for src in hosts:
    for dst in hosts:
        if src != dst:
            results.append({
                "source": src,
                "destination": dst,
                "success": ping(src, dst)
            })


output = {
    "timestamp": datetime.utcnow().isoformat(),
    "results": results
}


print(json.dumps(output, indent=2))

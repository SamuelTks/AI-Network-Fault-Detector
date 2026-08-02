import subprocess
import json


HOSTS = ["pc1", "pc2"]


# simple_bgp topology expected gateway
EXPECTED_GATEWAY = {
    "pc1": "195.11.14.1",
    "pc2": "200.1.1.1"
}


def run_docker_command(host, command):

    container_id = subprocess.check_output(
        [
            "docker",
            "ps",
            "-q",
            "-f",
            f"name={host}"
        ],
        text=True
    ).strip()


    if not container_id:
        return ""


    result = subprocess.check_output(
        [
            "docker",
            "exec",
            container_id,
            "bash",
            "-c",
            command
        ],
        text=True,
        stderr=subprocess.DEVNULL
    )

    return result



def inspect_host(host):

    flags = []


    # Check IP address
    ip_info = run_docker_command(
        host,
        "ip addr"
    )


    if "state UP" not in ip_info:
        flags.append("interface_down")


    ipv4_found = False

    for line in ip_info.splitlines():

        if "inet " in line and "127.0.0.1" not in line:
            ipv4_found = True


    if not ipv4_found:
        flags.append("missing_ip")



    # Check routing table
    route_info = run_docker_command(
        host,
        "ip route"
    )


    if "default" not in route_info:

        flags.append(
            "missing_gateway"
        )

    else:

        expected_gateway = EXPECTED_GATEWAY[host]


        if expected_gateway not in route_info:

            flags.append(
                "wrong_gateway"
            )



    return {
        "host": host,
        "healthy": len(flags) == 0,
        "flags": flags
    }



def main():

    results = []


    for host in HOSTS:

        results.append(
            inspect_host(host)
        )


    print(
        json.dumps(
            results,
            indent=2
        )
    )



if __name__ == "__main__":
    main()

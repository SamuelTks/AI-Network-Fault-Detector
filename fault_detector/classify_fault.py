import json
import subprocess


def get_host_status():

    output = subprocess.check_output(
        ["python", "inspect_hosts.py"],
        text=True
    )

    return json.loads(output)



def classify_fault():

    hosts = get_host_status()


    # Priority 1: interface down
    for host in hosts:

        flags = host["flags"]

        if "interface_down" in flags:

            return {
                "fault": "link_down",
                "evidence": host
            }



    # Priority 2: missing IP
    for host in hosts:

        flags = host["flags"]

        if "missing_ip" in flags:

            return {
                "fault": "host_missing_ip",
                "evidence": host
            }



    # Priority 3: wrong gateway
    for host in hosts:

        flags = host["flags"]

        if "wrong_gateway" in flags:

            return {
                "fault": "host_incorrect_gateway",
                "evidence": host
            }



    # Priority 4: missing gateway
    for host in hosts:

        flags = host["flags"]

        if "missing_gateway" in flags:

            return {
                "fault": "host_missing_gateway",
                "evidence": host
            }



    return {
        "fault": "no_fault",
        "confidence": "high"
    }



if __name__ == "__main__":

    print(
        json.dumps(
            classify_fault(),
            indent=2
        )
    )

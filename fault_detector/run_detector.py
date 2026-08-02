import json
import subprocess


def run_script(script):

    result = subprocess.check_output(
        [
            "python",
            script
        ],
        text=True
    )

    return json.loads(result)



def main():

    print("==============================")
    print(" AI Network Fault Detector")
    print("==============================")
    print()


    # Step 1: Check reachability
    print("[1] Checking network reachability...")

    reachability = run_script(
        "check_reachability.py"
    )


    print(json.dumps(
        reachability,
        indent=2
    ))

    print()



    # Step 2: Inspect hosts
    print("[2] Inspecting hosts...")

    hosts = run_script(
        "inspect_hosts.py"
    )


    print(json.dumps(
        hosts,
        indent=2
    ))

    print()



    # Step 3: Classify fault
    print("[3] Diagnosing fault...")

    diagnosis = run_script(
        "classify_fault.py"
    )


    print(json.dumps(
        diagnosis,
        indent=2
    ))

    print()


    print("==============================")
    print(" Final Diagnosis")
    print("==============================")

    print(
        "Fault:",
        diagnosis["fault"]
    )


    if "evidence" in diagnosis:

        print(
            "Affected Host:",
            diagnosis["evidence"]["host"]
        )

        print(
            "Evidence:",
            diagnosis["evidence"]["flags"]
        )

    print()



if __name__ == "__main__":

    main()

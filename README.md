# AI Network Fault Detector

An automated network fault detection tool built on top of the LLM4NetLab simple_bgp Kathara environment.

## Overview

This project implements Option 2: Automate Fault Detection with Scripts.

The pipeline performs:

1. Reachability monitoring
2. Host configuration inspection
3. Rule-based fault classification

Supported faults:

- link_down
- host_missing_ip
- host_incorrect_gateway
- no_fault


## Environment

Tested with:

- LLM4NetLab
- Kathara simple_bgp topology
- Docker


## Run

Start network:

```bash
python src/scripts/step1_net_env_start.py \
--scenario simple_bgp

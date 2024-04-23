#!/usr/bin/env python3

import time
import sys

import ntcore

# TEAM: int = 5419

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./run_calibration.py <team number> <northstar instance name>")
        print("For example: ./run_calibration.py 5419 northstar0")
        exit(1)

    team = int(sys.argv[1])
    instance_name = sys.argv[2]

    inst = ntcore.NetworkTableInstance.getDefault()

    table = inst.getTable(f"/{}/calibration")


    inst.startClient4("calibration client")
    inst.setServerTeam(team) # where TEAM=190, 294, etc, or use inst.setServer("hostname") or similar

    while 

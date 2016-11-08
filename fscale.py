import sys
import os
from colorama import Fore, Back, Style


def set_frequency_percentage(min_percentage, max_percentage):
    min_perf_pct = open("/sys/devices/system/cpu/intel_pstate/min_perf_pct", "w")
    min_perf_pct.write(min_percentage)
    min_perf_pct.close()
    max_perf_pct = open("/sys/devices/system/cpu/intel_pstate/max_perf_pct", "w")
    max_perf_pct.write(max_percentage)
    max_perf_pct.close()


if os.getuid() != 0:
    print(Fore.RED + "This script has to be executed by user root")
    sys.exit()

if len(sys.argv) <= 1:
    print(Fore.RED + "Usage: " + Style.RESET_ALL + "sudo fscale {PROFILE}")
    sys.exit()

PROFILE = sys.argv[1]

MAX_FREQUENCY = 2700  # MHz

PROFILES = {
    "min": [
        400,
        400
    ],
    "average": [
        1300,
        MAX_FREQUENCY
    ],
    "default": [
        400,
        MAX_FREQUENCY
    ],
    "max": [
        MAX_FREQUENCY,
        MAX_FREQUENCY
    ]
}

if PROFILE not in PROFILES:
    print(Fore.RED + "Profile " + Fore.YELLOW + PROFILE + Fore.RED + " does not exist")
    sys.exit()

MIN_PERCENTAGE = str(int((100.0 / MAX_FREQUENCY) * PROFILES.get(PROFILE)[0]))
MAX_PERCENTAGE = str(int((100.0 / MAX_FREQUENCY) * PROFILES.get(PROFILE)[1]))

set_frequency_percentage(MIN_PERCENTAGE, MAX_PERCENTAGE)
sys.exit()

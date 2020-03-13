#!/usr/bin/env python3.6

import os

# Amend file paths accordingly to where the files are stored.

diff_process_list_script = "/home/ubuntu/Stitcher/scripts/diff_process_list.sh"
diff_file_list_script = "/home/ubuntu/Stitcher/scripts/diff_file_list.sh"
diff_file_hashes_script = "/home/ubuntu/Stitcher/scripts/diff_file_hashes.sh"
diff_network_ports_script = "/home/ubuntu/Stitcher/scripts/diff_network_ports.sh"


def compare_process_list():
    print("[+] Correlating Processes Between Core and Baseline Evidence.")
    compare_cmd = diff_process_list_script
    os.system(compare_cmd)
    print("[+] Correlation Completed")


def compare_file_list():
    print("[+] Correlating Files Between Core and Baseline Evidence.")
    compare_cmd = diff_file_list_script
    os.system(compare_cmd)
    print("[+] Correlation Completed")


def compare_file_hashes():
    print("[+] Correlating File Hashes Between Core and Baseline Evidence.")
    compare_cmd = diff_file_hashes_script
    os.system(compare_cmd)
    print("[+] Correlation Completed")


def compare_network_ports():
    print("[+] Correlating Network Ports Between Core and Baseline Evidence.")
    compare_cmd = diff_network_ports_script
    os.system(compare_cmd)
    print("[+] Correlation Completed")


def main():
    compare_process_list()
    compare_file_list()
    compare_file_hashes()
    compare_network_ports()


if __name__ == "__main__":
    main()


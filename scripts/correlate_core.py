#!/usr/bin/env python3.6

import os

# Amend file paths accordingly to where the files are stored.

port_and_strings_compare_script = "/home/ubuntu/Stitcher/scripts/core_port_and_strings_compare.sh"
process_list_and_file_names_compare_script = "/home/ubuntu/Stitcher/scripts/core_compare_process_list_and_file_names.sh"
process_list_and_file_strings_compare_script = "/home/ubuntu/Stitcher/scripts/core_compare_process_list_and_file_strings.sh"


def compare_port_and_strings():
    print("[+] Correlating Network Traffic and File Strings.")
    compare_cmd = port_and_strings_compare_script
    os.system(compare_cmd)
    print("[+] Correlation Completed")


def compare_process_list_and_file_names():
    print("[+] Correlating Process List and File Names.")
    compare_cmd = process_list_and_file_names_compare_script
    os.system(compare_cmd)
    print("[+] Correlation Completed")


def compare_process_list_and_file_strings():
    print("[+] Correlating Process List and File Strings.")
    compare_cmd = process_list_and_file_strings_compare_script
    os.system(compare_cmd)
    print("[+] Correlation Completed")


def main():
    compare_port_and_strings()
    compare_process_list_and_file_names()
    compare_process_list_and_file_strings()


if __name__ == "__main__":
    main()


#!/usr/bin/env python3.6

import os
import pexpect
import sys

# Amend file paths accordingly to where the files are stored.

core_mount_path = "/mnt"
core_image = "/home/ubuntu/Stitcher/evidence/core/image.raw"
core_pcap = "/home/ubuntu/Stitcher/evidence/core/CoreTraffic.pcapng"
core_ps = "/home/ubuntu/Stitcher/evidence/core/coreps.txt"
core_image_dir_output = "/home/ubuntu/Stitcher/output/core/directory.txt"
core_image_file_output = "/home/ubuntu/Stitcher/output/core/filelist.txt"
core_image_file_hash_output = "/home/ubuntu/Stitcher/output/core/filehash.txt"
core_image_file_strings_output = "/home/ubuntu/Stitcher/output/core/strings_output/"
core_network_top_TCP_port_output = "/home/ubuntu/Stitcher/output/core/topTCPport.txt"
core_network_top_TCP_ports_output = "/home/ubuntu/Stitcher/output/core/topTCPports.txt"
core_process_list_output = "/home/ubuntu/Stitcher/output/core/processlist.txt"


def mount_image():
    # This function is for mounting the firmware image file
    #
    print("[+] Mounting Image.")
    mount_cmd = "mount -t auto -o loop,offset=$((2048*512)) " + core_image + " " + core_mount_path
    os.system(mount_cmd)
    print("[+] Image Mount Completed")


def unmount_image():
    # This function is for unmounting the firmware image file
    print("[+] Unmounting Image.")
    unmount_cmd = "umount " + core_mount_path
    os.system(unmount_cmd)
    print("[+] Image Unmounted")


def generate_image_dir():
    # This function generates and saves the directory structure of the image file
    print("[+] Generating List of Directories.")
    dir_cmd = "find " + core_mount_path + " -type d -print > " + core_image_dir_output
    os.system(dir_cmd)
    print("[+] Directory List Generation Completed")


def generate_file_list():
    # This function generates list of files present in the image
    print("[+] Generating List of Files.")
    file_cmd = "find " + core_mount_path + "/* -type f -print > " + core_image_file_output
    os.system(file_cmd)
    print("[+] File List Generation Completed")


def generate_sha256_file_hash():
    # This function generates list of files and respective SHA256 hashes present in the image
    print("[+] Generating List of SHA256 Hashes.")
    bracket = "{}"
    file_hash_cmd = "find " + core_mount_path + "/* -type f -exec sha256sum " + bracket + " + " + " > " + core_image_file_hash_output
    os.system(file_hash_cmd)
    print("[+] SHA256 Hash List Generation Completed")


def generate_file_strings():
    # This function generates the strings of the respective files present in the image
    print("[+] Generating File Strings.")
    # Currently file paths for the firmware are hardcoded
    strings_cmd_1 = "strings /mnt/bin/lld2d > " + core_image_file_strings_output + "lld2d_strings.txt"
    os.system(strings_cmd_1)
    strings_cmd_2 = "strings /mnt/bin/busybox > " + core_image_file_strings_output + "busybox_strings.txt"
    os.system(strings_cmd_2)
    strings_cmd_3 = "strings /mnt/bin/iwconfig > " + core_image_file_strings_output + "iwconfig_strings.txt"
    os.system(strings_cmd_3)
    strings_cmd_4 = "strings /mnt/bin/ralink_init > " + core_image_file_strings_output + "ralink_init_strings.txt"
    os.system(strings_cmd_4)
    strings_cmd_5 = "strings /mnt/bin/ated > " + core_image_file_strings_output + "ated_strings.txt"
    os.system(strings_cmd_5)
    strings_cmd_6 = "strings /mnt/bin/reg > " + core_image_file_strings_output + "reg_strings.txt"
    os.system(strings_cmd_6)
    strings_cmd_7 = "strings /mnt/bin/iwpriv > " + core_image_file_strings_output + "iwpriv_strings.txt"
    os.system(strings_cmd_7)
    strings_cmd_8 = "strings /mnt/bin/nvram_daemon > " + core_image_file_strings_output + "nvram_daemon_strings.txt"
    os.system(strings_cmd_8)
    strings_cmd_9 = "strings /mnt/bin/mii_mgr > " + core_image_file_strings_output + "mii_mgr_strings.txt"
    os.system(strings_cmd_9)
    strings_cmd_10 = "strings /mnt/bin/switch > " + core_image_file_strings_output + "switch_strings.txt"
    os.system(strings_cmd_10)
    strings_cmd_11 = "strings /mnt/bin/mtd_write > " + core_image_file_strings_output + "mtd_write_strings.txt"
    os.system(strings_cmd_11)
    strings_cmd_12 = "strings /mnt/bin/iwlist > " + core_image_file_strings_output + "iwlist_strings.txt"
    os.system(strings_cmd_12)
    strings_cmd_13 = "strings /mnt/bin/openssl > " + core_image_file_strings_output + "openssl_strings.txt"
    os.system(strings_cmd_13)
    strings_cmd_14 = "strings /mnt/etc/passwd > " + core_image_file_strings_output + "passwd_strings.txt"
    os.system(strings_cmd_14)
    strings_cmd_15 = "strings /mnt/etc/hosts > " + core_image_file_strings_output + "hosts_strings.txt"
    os.system(strings_cmd_15)
    strings_cmd_16 = "strings /mnt/etc/fstab > " + core_image_file_strings_output + "fstab_strings.txt"
    os.system(strings_cmd_16)
    strings_cmd_17 = "strings /mnt/etc/TZ > " + core_image_file_strings_output + "TZ_strings.txt"
    os.system(strings_cmd_17)
    strings_cmd_18 = "strings /mnt/etc_ro/wlan/RT5350_AP_1T1R_V1_0.bin > " + core_image_file_strings_output + "RT5350_AP_1T1R_V1_0.bin_strings.txt"
    os.system(strings_cmd_18)
    strings_cmd_19 = "strings /mnt/etc_ro/lld2d.conf > " + core_image_file_strings_output + "lld2d.conf_strings.txt"
    os.system(strings_cmd_19)
    strings_cmd_20 = "strings /mnt/etc_ro/icon.ico > " + core_image_file_strings_output + "icon.ico_strings.txt"
    os.system(strings_cmd_20)
    strings_cmd_21 = "strings /mnt/etc_ro/icon.large.ico > " + core_image_file_strings_output + "icon.large.ico_strings.txt"
    os.system(strings_cmd_21)
    strings_cmd_22 = "strings /mnt/etc_ro/rcS > " + core_image_file_strings_output + "rcS_strings.txt"
    os.system(strings_cmd_22)
    strings_cmd_23 = "strings /mnt/etc_ro/inittab > " + core_image_file_strings_output + "inittab_strings.txt"
    os.system(strings_cmd_23)
    strings_cmd_24 = "strings /mnt/etc_ro/motd> " + core_image_file_strings_output + "motd_strings.txt"
    os.system(strings_cmd_24)
    strings_cmd_25 = "strings /mnt/etc_ro/Wireless/RT2860AP/RT2860_default_vlan > " + core_image_file_strings_output + "RT2860_default_vlan_strings.txt"
    os.system(strings_cmd_25)
    strings_cmd_26 = "strings /mnt/etc_ro/Wireless/RT2860AP/RT2860_default_novlan > " + core_image_file_strings_output + "RT2860_default_novlan_strings.txt"
    os.system(strings_cmd_26)
    strings_cmd_27 = "strings /mnt/firmadyne/preInit.sh > " + core_image_file_strings_output + "preInit.sh_strings.txt"
    os.system(strings_cmd_27)
    strings_cmd_28 = "strings /mnt/firmadyne/console > " + core_image_file_strings_output + "console_strings.txt"
    os.system(strings_cmd_28)
    strings_cmd_29 = "strings /mnt/firmadyne/libnvram.so > " + core_image_file_strings_output + "libnvram.so_strings.txt"
    os.system(strings_cmd_29)
    strings_cmd_30 = "strings /mnt/lib/libdl-0.9.28.so > " + core_image_file_strings_output + "libdl-0.9.28.so_strings.txt"
    os.system(strings_cmd_30)
    strings_cmd_31 = "strings /mnt/lib/libcrypto.so.0.9.8 > " + core_image_file_strings_output + "libcrypto.so.0.9.8_strings.txt"
    os.system(strings_cmd_31)
    strings_cmd_32 = "strings /mnt/lib/libcurl.so.4.4.0 > " + core_image_file_strings_output + "libcurl.so.4.4.0_strings.txt"
    os.system(strings_cmd_32)
    strings_cmd_33 = "strings /mnt/lib/libssl.so.0.9.8> " + core_image_file_strings_output + "libssl.so.0.9.8_strings.txt"
    os.system(strings_cmd_33)
    strings_cmd_34 = "strings /mnt/lib/libcurl.a > " + core_image_file_strings_output + "libcurl.a_strings.txt"
    os.system(strings_cmd_34)
    strings_cmd_35 = "strings /mnt/lib/libiw.so.29 > " + core_image_file_strings_output + "libiw.so.29_strings.txt"
    os.system(strings_cmd_35)
    strings_cmd_36 = "strings /mnt/lib/libcrypt-0.9.28.so > " + core_image_file_strings_output + "libcrypt-0.9.28.so_strings.txt"
    os.system(strings_cmd_36)
    strings_cmd_37 = "strings /mnt/lib/libembMQTT.so > " + core_image_file_strings_output + "libembMQTT.so_strings.txt"
    os.system(strings_cmd_37)
    strings_cmd_38 = "strings /mnt/lib/libnvram-0.9.28.so > " + core_image_file_strings_output + "libnvram-0.9.28.so_strings.txt"
    os.system(strings_cmd_38)
    strings_cmd_39 = "strings /mnt/lib/libpaho-mqtt3as.so.1.0 > " + core_image_file_strings_output + "libpaho-mqtt3as.so.1.0_strings.txt"
    os.system(strings_cmd_39)
    strings_cmd_40 = "strings /mnt/lib/libm-0.9.28.so > " + core_image_file_strings_output + "libm-0.9.28.so_strings.txt"
    os.system(strings_cmd_40)
    strings_cmd_41 = "strings /mnt/lib/ld-uClibc-0.9.28.so > " + core_image_file_strings_output + "ld-uClibc-0.9.28.s_strings.txt"
    os.system(strings_cmd_41)
    strings_cmd_42 = "strings /mnt/lib/libuClibc-0.9.28.so > " + core_image_file_strings_output + "libuClibc-0.9.28.so_strings.txt"
    os.system(strings_cmd_42)
    strings_cmd_43 = "strings /mnt/lib/libpthread-0.9.28.so > " + core_image_file_strings_output + "libpthread-0.9.28.so_strings.txt"
    os.system(strings_cmd_43)
    strings_cmd_44 = "strings /mnt/lib/liblogserver.so > " + core_image_file_strings_output + "liblogserver.so_strings.txt"
    os.system(strings_cmd_44)
    strings_cmd_45 = "strings /mnt/sbin/snmp.sh > " + core_image_file_strings_output + "snmp.sh_strings.txt"
    os.system(strings_cmd_45)
    strings_cmd_46 = "strings /mnt/sbin/lan.sh > " + core_image_file_strings_output + "lan.sh_strings.txt"
    os.system(strings_cmd_46)
    strings_cmd_47 = "strings /mnt/sbin/internet.sh> " + core_image_file_strings_output + "internet.sh_strings.txt"
    os.system(strings_cmd_47)
    strings_cmd_48 = "strings /mnt/sbin/wan.sh > " + core_image_file_strings_output + "wan.sh_strings.txt"
    os.system(strings_cmd_48)
    strings_cmd_49 = "strings /mnt/sbin/wifi_unload.sh > " + core_image_file_strings_output + "wifi_unload.sh_strings.txt"
    os.system(strings_cmd_49)
    strings_cmd_50 = "strings /mnt/sbin/nat.sh > " + core_image_file_strings_output + "nat.sh_strings.txt"
    os.system(strings_cmd_50)
    strings_cmd_51 = "strings /mnt/sbin/config-igmpproxy.sh > " + core_image_file_strings_output + "config-igmpproxy.sh_strings.txt"
    os.system(strings_cmd_51)
    strings_cmd_52 = "strings /mnt/sbin/config-pppoe.sh > " + core_image_file_strings_output + "config-pppoe.sh_strings.txt"
    os.system(strings_cmd_52)
    strings_cmd_53 = "strings /mnt/sbin/automount.sh > " + core_image_file_strings_output + "automount.sh_strings.txt"
    os.system(strings_cmd_53)
    strings_cmd_54 = "strings /mnt/sbin/snort.sh > " + core_image_file_strings_output + "snort.sh_strings.txt"
    os.system(strings_cmd_54)
    strings_cmd_55 = "strings /mnt/sbin/config-pptp.sh > " + core_image_file_strings_output + "config-pptp.sh_strings.txt"
    os.system(strings_cmd_55)
    strings_cmd_56 = "strings /mnt/sbin/chpasswd.sh > " + core_image_file_strings_output + "chpasswd.sh_strings.txt"
    os.system(strings_cmd_56)
    strings_cmd_57 = "strings /mnt/sbin/iSmartAlarm > " + core_image_file_strings_output + "iSmartAlarm_strings.txt"
    os.system(strings_cmd_57)
    strings_cmd_58 = "strings /mnt/sbin/config-dns.sh > " + core_image_file_strings_output + "config-dns.sh_strings.txt"
    os.system(strings_cmd_58)
    strings_cmd_59 = "strings /mnt/sbin/config-iTunes.sh > " + core_image_file_strings_output + "config-iTunes.sh_strings.txt"
    os.system(strings_cmd_59)
    strings_cmd_60 = "strings /mnt/sbin/ntp.sh > " + core_image_file_strings_output + "ntp.sh_strings.txt"
    os.system(strings_cmd_60)
    strings_cmd_61 = "strings /mnt/sbin/config.sh > " + core_image_file_strings_output + "config.sh_strings.txt"
    os.system(strings_cmd_61)
    strings_cmd_62 = "strings /mnt/sbin/udhcpc.sh > " + core_image_file_strings_output + "udhcpc.sh_strings.txt"
    os.system(strings_cmd_62)
    strings_cmd_63 = "strings /mnt/sbin/config-vlan.sh > " + core_image_file_strings_output + "config-vlan.sh_strings.txt"
    os.system(strings_cmd_63)
    strings_cmd_64 = "strings /mnt/sbin/firewall.sh > " + core_image_file_strings_output + "firewall.sh_strings.txt"
    os.system(strings_cmd_64)
    strings_cmd_65 = "strings /mnt/sbin/sysActive > " + core_image_file_strings_output + "sysActive_strings.txt"
    os.system(strings_cmd_65)
    strings_cmd_66 = "strings /mnt/sbin/hello > " + core_image_file_strings_output + "hello_strings.txt"
    os.system(strings_cmd_66)
    strings_cmd_67 = "strings /mnt/sbin/test_kernel > " + core_image_file_strings_output + "test_kernel_strings.txt"
    os.system(strings_cmd_67)
    strings_cmd_68 = "strings /mnt/sbin/autoconn3G.sh > " + core_image_file_strings_output + "autoconn3G.sh_strings.txt"
    os.system(strings_cmd_68)
    strings_cmd_69 = "strings /mnt/sbin/iSmartAlarmShell > " + core_image_file_strings_output + "iSmartAlarmShell_strings.txt"
    os.system(strings_cmd_69)
    strings_cmd_70 = "strings /mnt/sbin/config-udhcpd.sh > " + core_image_file_strings_output + "config-udhcpd.sh_strings.txt"
    os.system(strings_cmd_70)
    strings_cmd_71 = "strings /mnt/sbin/config-l2tp.sh > " + core_image_file_strings_output + "config-l2tp.sh_strings.txt"
    os.system(strings_cmd_71)
    strings_cmd_72 = "strings /mnt/sbin/config-powersave.sh > " + core_image_file_strings_output + "config-powersave.sh_strings.txt"
    os.system(strings_cmd_72)
    strings_cmd_73 = "strings /mnt/sbin/vpn-passthru.sh > " + core_image_file_strings_output + "vpn-passthru.sh_strings.txt"
    os.system(strings_cmd_73)
    strings_cmd_74 = "strings /mnt/sbin/cpubusy.sh > " + core_image_file_strings_output + "cpubusy.sh_strings.txt"
    os.system(strings_cmd_74)
    strings_cmd_75 = "strings /mnt/sbin/global.sh > " + core_image_file_strings_output + "global.sh_strings.txt"
    os.system(strings_cmd_75)
    strings_cmd_76 = "strings /mnt/sbin/protectProject > " + core_image_file_strings_output + "protectProject_strings.txt"
    os.system(strings_cmd_76)
    strings_cmd_77 = "strings /mnt/usr/share/udhcpc/default.script > " + core_image_file_strings_output + "default.script_strings.txt"
    os.system(strings_cmd_77)
    strings_cmd_78 = "strings /mnt/usr/share/iSmart/cc1110 > " + core_image_file_strings_output + "cc1110_strings.txt"
    os.system(strings_cmd_78)
    strings_cmd_79 = "strings /mnt/usr/share/iSmart/IPU > " + core_image_file_strings_output + "IPU_strings.txt"
    os.system(strings_cmd_79)
    strings_cmd_80 = "strings /mnt/usr/share/iSmart/default_config > " + core_image_file_strings_output + "default_config_strings.txt"
    os.system(strings_cmd_80)
    print("[+] File Strings Generation Completed")


def analyse_network_capture():
    # This function will parse through the pcap file and get the single top TCP port and all TCP ports
    # The tshark command needs to be amended to reflect the file path of where the file is stored
    print("[+] Analysing Network Capture.")
    top_TCP_port_cmd = 'tshark -r /home/ubuntu/Stitcher/evidence/core/CoreTraffic.pcapng -Y "tcp" -T fields -e tcp.dstport | sort -n | uniq -c |' + " awk '{print $2}'| head -n 1 > " + core_network_top_TCP_port_output
    os.system(top_TCP_port_cmd)
    top_TCP_ports_cmd = 'tshark -r /home/ubuntu/Stitcher/evidence/core/CoreTraffic.pcapng -Y "tcp" -T fields -e tcp.dstport | sort -n | uniq -c |' + " awk '{print $2}' > " + core_network_top_TCP_ports_output
    os.system(top_TCP_ports_cmd)
    print("[+] Network Capture Analysis Completed")


def generate_process_list():
    # This function extracts the list of processes that were running.
    print("[+] Analysing Process List.")
    process_cmd = "cat " + core_ps + " | awk '{print $5}' > " + core_process_list_output
    os.system(process_cmd)
    print("[+] Process List Analysis Completed")

def main():
    mount_image()
    generate_image_dir()
    generate_file_list()
    generate_sha256_file_hash()
    generate_file_strings()
    analyse_network_capture()
    generate_process_list()
    unmount_image()


if __name__ == "__main__":
    main()


#!/usr/bin/env python3.6


import os
import pexpect
import sys

# Amend file paths accordingly to where the files are stored.

baseline_mount_path = "/mnt"
baseline_image = "/home/ubuntu/Stitcher/evidence/baseline/image.raw"
baseline_pcap = "/home/ubuntu/Stitcher/evidence/baseline/BaselineTraffic.pcapng"
baseline_ps = "/home/ubuntu/Stitcher/evidence/baseline/baselineps.txt"
baseline_image_dir_output = "/home/ubuntu/Stitcher/output/baseline/directory.txt"
baseline_image_file_output = "/home/ubuntu/Stitcher/output/baseline/filelist.txt"
baseline_image_file_hash_output = "/home/ubuntu/Stitcher/output/baseline/filehash.txt"
baseline_image_file_strings_output = "/home/ubuntu/Stitcher/output/baseline/strings_output/"
baseline_network_top_TCP_port_output = "/home/ubuntu/Stitcher/output/baseline/topTCPport.txt"
baseline_network_top_TCP_ports_output = "/home/ubuntu/Stitcher/output/baseline/topTCPports.txt"
baseline_process_list_output = "/home/ubuntu/Stitcher/output/baseline/processlist.txt"


def mount_image():
    # This function is for mounting the firmware image file
    #
    print("[+] Mounting Image.")
    mount_cmd = "mount -t auto -o loop,offset=$((2048*512)) " + baseline_image + " " + baseline_mount_path
    os.system(mount_cmd)
    print("[+] Image Mount Completed")
    print("[+] Starting to process baseline evidence.")


def unmount_image():
    # This function is for unmounting the firmware image file
    print("[+] Unmounting Image.")
    unmount_cmd = "umount " + baseline_mount_path
    os.system(unmount_cmd)
    print("[+] Image Unmounted")


def generate_image_dir():
    # This function generates and saves the directory structure of the image file
    print("[+] Generating List of Directories.")
    dir_cmd = "find " + baseline_mount_path + " -type d -print > " + baseline_image_dir_output
    os.system(dir_cmd)
    print("[+] Directory List Generation Completed")


def generate_file_list():
    # This function generates list of files present in the image
    print("[+] Generating List of Files.")
    file_cmd = "find " + baseline_mount_path + "/* -type f -print > " + baseline_image_file_output
    os.system(file_cmd)
    print("[+] File List Generation Completed")


def generate_sha256_file_hash():
    # This function generates list of files and respective SHA256 hashes present in the image
    print("[+] Generating List of SHA256 Hashes.")
    bracket = "{}"
    file_hash_cmd = "find " + baseline_mount_path + "/* -type f -exec sha256sum " + bracket + " + " + " > " + baseline_image_file_hash_output
    os.system(file_hash_cmd)
    print("[+] SHA256 Hash List Generation Completed")


def generate_file_strings():
    # This function generates the strings of the respective files present in the image
    print("[+] Generating File Strings.")
    # Currently file paths for the firmware are hardcoded
    strings_cmd_1 = "strings /mnt/bin/lld2d > " + baseline_image_file_strings_output + "lld2d_strings.txt"
    os.system(strings_cmd_1)
    strings_cmd_2 = "strings /mnt/bin/busybox > " + baseline_image_file_strings_output + "busybox_strings.txt"
    os.system(strings_cmd_2)
    strings_cmd_3 = "strings /mnt/bin/iwconfig > " + baseline_image_file_strings_output + "iwconfig_strings.txt"
    os.system(strings_cmd_3)
    strings_cmd_4 = "strings /mnt/bin/ralink_init > " + baseline_image_file_strings_output + "ralink_init_strings.txt"
    os.system(strings_cmd_4)
    strings_cmd_5 = "strings /mnt/bin/ated > " + baseline_image_file_strings_output + "ated_strings.txt"
    os.system(strings_cmd_5)
    strings_cmd_6 = "strings /mnt/bin/reg > " + baseline_image_file_strings_output + "reg_strings.txt"
    os.system(strings_cmd_6)
    strings_cmd_7 = "strings /mnt/bin/iwpriv > " + baseline_image_file_strings_output + "iwpriv_strings.txt"
    os.system(strings_cmd_7)
    strings_cmd_8 = "strings /mnt/bin/nvram_daemon > " + baseline_image_file_strings_output + "nvram_daemon_strings.txt"
    os.system(strings_cmd_8)
    strings_cmd_9 = "strings /mnt/bin/mii_mgr > " + baseline_image_file_strings_output + "mii_mgr_strings.txt"
    os.system(strings_cmd_9)
    strings_cmd_10 = "strings /mnt/bin/switch > " + baseline_image_file_strings_output + "switch_strings.txt"
    os.system(strings_cmd_10)
    strings_cmd_11 = "strings /mnt/bin/mtd_write > " + baseline_image_file_strings_output + "mtd_write_strings.txt"
    os.system(strings_cmd_11)
    strings_cmd_12 = "strings /mnt/bin/iwlist > " + baseline_image_file_strings_output + "iwlist_strings.txt"
    os.system(strings_cmd_12)
    strings_cmd_13 = "strings /mnt/bin/openssl > " + baseline_image_file_strings_output + "openssl_strings.txt"
    os.system(strings_cmd_13)
    strings_cmd_14 = "strings /mnt/etc/passwd > " + baseline_image_file_strings_output + "passwd_strings.txt"
    os.system(strings_cmd_14)
    strings_cmd_15 = "strings /mnt/etc/hosts > " + baseline_image_file_strings_output + "hosts_strings.txt"
    os.system(strings_cmd_15)
    strings_cmd_16 = "strings /mnt/etc/fstab > " + baseline_image_file_strings_output + "fstab_strings.txt"
    os.system(strings_cmd_16)
    strings_cmd_17 = "strings /mnt/etc/TZ > " + baseline_image_file_strings_output + "TZ_strings.txt"
    os.system(strings_cmd_17)
    strings_cmd_18 = "strings /mnt/etc_ro/wlan/RT5350_AP_1T1R_V1_0.bin > " + baseline_image_file_strings_output + "RT5350_AP_1T1R_V1_0.bin_strings.txt"
    os.system(strings_cmd_18)
    strings_cmd_19 = "strings /mnt/etc_ro/lld2d.conf > " + baseline_image_file_strings_output + "lld2d.conf_strings.txt"
    os.system(strings_cmd_19)
    strings_cmd_20 = "strings /mnt/etc_ro/icon.ico > " + baseline_image_file_strings_output + "icon.ico_strings.txt"
    os.system(strings_cmd_20)
    strings_cmd_21 = "strings /mnt/etc_ro/icon.large.ico > " + baseline_image_file_strings_output + "icon.large.ico_strings.txt"
    os.system(strings_cmd_21)
    strings_cmd_22 = "strings /mnt/etc_ro/rcS > " + baseline_image_file_strings_output + "rcS_strings.txt"
    os.system(strings_cmd_22)
    strings_cmd_23 = "strings /mnt/etc_ro/inittab > " + baseline_image_file_strings_output + "inittab_strings.txt"
    os.system(strings_cmd_23)
    strings_cmd_24 = "strings /mnt/etc_ro/motd> " + baseline_image_file_strings_output + "motd_strings.txt"
    os.system(strings_cmd_24)
    strings_cmd_25 = "strings /mnt/etc_ro/Wireless/RT2860AP/RT2860_default_vlan > " + baseline_image_file_strings_output + "RT2860_default_vlan_strings.txt"
    os.system(strings_cmd_25)
    strings_cmd_26 = "strings /mnt/etc_ro/Wireless/RT2860AP/RT2860_default_novlan > " + baseline_image_file_strings_output + "RT2860_default_novlan_strings.txt"
    os.system(strings_cmd_26)
    strings_cmd_27 = "strings /mnt/firmadyne/preInit.sh > " + baseline_image_file_strings_output + "preInit.sh_strings.txt"
    os.system(strings_cmd_27)
    strings_cmd_28 = "strings /mnt/firmadyne/console > " + baseline_image_file_strings_output + "console_strings.txt"
    os.system(strings_cmd_28)
    strings_cmd_29 = "strings /mnt/firmadyne/libnvram.so > " + baseline_image_file_strings_output + "libnvram.so_strings.txt"
    os.system(strings_cmd_29)
    strings_cmd_30 = "strings /mnt/lib/libdl-0.9.28.so > " + baseline_image_file_strings_output + "libdl-0.9.28.so_strings.txt"
    os.system(strings_cmd_30)
    strings_cmd_31 = "strings /mnt/lib/libcrypto.so.0.9.8 > " + baseline_image_file_strings_output + "libcrypto.so.0.9.8_strings.txt"
    os.system(strings_cmd_31)
    strings_cmd_32 = "strings /mnt/lib/libcurl.so.4.4.0 > " + baseline_image_file_strings_output + "libcurl.so.4.4.0_strings.txt"
    os.system(strings_cmd_32)
    strings_cmd_33 = "strings /mnt/lib/libssl.so.0.9.8> " + baseline_image_file_strings_output + "libssl.so.0.9.8_strings.txt"
    os.system(strings_cmd_33)
    strings_cmd_34 = "strings /mnt/lib/libcurl.a > " + baseline_image_file_strings_output + "libcurl.a_strings.txt"
    os.system(strings_cmd_34)
    strings_cmd_35 = "strings /mnt/lib/libiw.so.29 > " + baseline_image_file_strings_output + "libiw.so.29_strings.txt"
    os.system(strings_cmd_35)
    strings_cmd_36 = "strings /mnt/lib/libcrypt-0.9.28.so > " + baseline_image_file_strings_output + "libcrypt-0.9.28.so_strings.txt"
    os.system(strings_cmd_36)
    strings_cmd_37 = "strings /mnt/lib/libembMQTT.so > " + baseline_image_file_strings_output + "libembMQTT.so_strings.txt"
    os.system(strings_cmd_37)
    strings_cmd_38 = "strings /mnt/lib/libnvram-0.9.28.so > " + baseline_image_file_strings_output + "libnvram-0.9.28.so_strings.txt"
    os.system(strings_cmd_38)
    strings_cmd_39 = "strings /mnt/lib/libpaho-mqtt3as.so.1.0 > " + baseline_image_file_strings_output + "libpaho-mqtt3as.so.1.0_strings.txt"
    os.system(strings_cmd_39)
    strings_cmd_40 = "strings /mnt/lib/libm-0.9.28.so > " + baseline_image_file_strings_output + "libm-0.9.28.so_strings.txt"
    os.system(strings_cmd_40)
    strings_cmd_41 = "strings /mnt/lib/ld-uClibc-0.9.28.so > " + baseline_image_file_strings_output + "ld-uClibc-0.9.28.s_strings.txt"
    os.system(strings_cmd_41)
    strings_cmd_42 = "strings /mnt/lib/libuClibc-0.9.28.so > " + baseline_image_file_strings_output + "libuClibc-0.9.28.so_strings.txt"
    os.system(strings_cmd_42)
    strings_cmd_43 = "strings /mnt/lib/libpthread-0.9.28.so > " + baseline_image_file_strings_output + "libpthread-0.9.28.so_strings.txt"
    os.system(strings_cmd_43)
    strings_cmd_44 = "strings /mnt/lib/liblogserver.so > " + baseline_image_file_strings_output + "liblogserver.so_strings.txt"
    os.system(strings_cmd_44)
    strings_cmd_45 = "strings /mnt/sbin/snmp.sh > " + baseline_image_file_strings_output + "snmp.sh_strings.txt"
    os.system(strings_cmd_45)
    strings_cmd_46 = "strings /mnt/sbin/lan.sh > " + baseline_image_file_strings_output + "lan.sh_strings.txt"
    os.system(strings_cmd_46)
    strings_cmd_47 = "strings /mnt/sbin/internet.sh> " + baseline_image_file_strings_output + "internet.sh_strings.txt"
    os.system(strings_cmd_47)
    strings_cmd_48 = "strings /mnt/sbin/wan.sh > " + baseline_image_file_strings_output + "wan.sh_strings.txt"
    os.system(strings_cmd_48)
    strings_cmd_49 = "strings /mnt/sbin/wifi_unload.sh > " + baseline_image_file_strings_output + "wifi_unload.sh_strings.txt"
    os.system(strings_cmd_49)
    strings_cmd_50 = "strings /mnt/sbin/nat.sh > " + baseline_image_file_strings_output + "nat.sh_strings.txt"
    os.system(strings_cmd_50)
    strings_cmd_51 = "strings /mnt/sbin/config-igmpproxy.sh > " + baseline_image_file_strings_output + "config-igmpproxy.sh_strings.txt"
    os.system(strings_cmd_51)
    strings_cmd_52 = "strings /mnt/sbin/config-pppoe.sh > " + baseline_image_file_strings_output + "config-pppoe.sh_strings.txt"
    os.system(strings_cmd_52)
    strings_cmd_53 = "strings /mnt/sbin/automount.sh > " + baseline_image_file_strings_output + "automount.sh_strings.txt"
    os.system(strings_cmd_53)
    strings_cmd_54 = "strings /mnt/sbin/snort.sh > " + baseline_image_file_strings_output + "snort.sh_strings.txt"
    os.system(strings_cmd_54)
    strings_cmd_55 = "strings /mnt/sbin/config-pptp.sh > " + baseline_image_file_strings_output + "config-pptp.sh_strings.txt"
    os.system(strings_cmd_55)
    strings_cmd_56 = "strings /mnt/sbin/chpasswd.sh > " + baseline_image_file_strings_output + "chpasswd.sh_strings.txt"
    os.system(strings_cmd_56)
    strings_cmd_57 = "strings /mnt/sbin/iSmartAlarm > " + baseline_image_file_strings_output + "iSmartAlarm_strings.txt"
    os.system(strings_cmd_57)
    strings_cmd_58 = "strings /mnt/sbin/config-dns.sh > " + baseline_image_file_strings_output + "config-dns.sh_strings.txt"
    os.system(strings_cmd_58)
    strings_cmd_59 = "strings /mnt/sbin/config-iTunes.sh > " + baseline_image_file_strings_output + "config-iTunes.sh_strings.txt"
    os.system(strings_cmd_59)
    strings_cmd_60 = "strings /mnt/sbin/ntp.sh > " + baseline_image_file_strings_output + "ntp.sh_strings.txt"
    os.system(strings_cmd_60)
    strings_cmd_61 = "strings /mnt/sbin/config.sh > " + baseline_image_file_strings_output + "config.sh_strings.txt"
    os.system(strings_cmd_61)
    strings_cmd_62 = "strings /mnt/sbin/udhcpc.sh > " + baseline_image_file_strings_output + "udhcpc.sh_strings.txt"
    os.system(strings_cmd_62)
    strings_cmd_63 = "strings /mnt/sbin/config-vlan.sh > " + baseline_image_file_strings_output + "config-vlan.sh_strings.txt"
    os.system(strings_cmd_63)
    strings_cmd_64 = "strings /mnt/sbin/firewall.sh > " + baseline_image_file_strings_output + "firewall.sh_strings.txt"
    os.system(strings_cmd_64)
    strings_cmd_65 = "strings /mnt/sbin/sysActive > " + baseline_image_file_strings_output + "sysActive_strings.txt"
    os.system(strings_cmd_65)
    strings_cmd_66 = "strings /mnt/sbin/hello > " + baseline_image_file_strings_output + "hello_strings.txt"
    os.system(strings_cmd_66)
    strings_cmd_67 = "strings /mnt/sbin/test_kernel > " + baseline_image_file_strings_output + "test_kernel_strings.txt"
    os.system(strings_cmd_67)
    strings_cmd_68 = "strings /mnt/sbin/autoconn3G.sh > " + baseline_image_file_strings_output + "autoconn3G.sh_strings.txt"
    os.system(strings_cmd_68)
    strings_cmd_69 = "strings /mnt/sbin/config-udhcpd.sh > " + baseline_image_file_strings_output + "config-udhcpd.sh_strings.txt"
    os.system(strings_cmd_69)
    strings_cmd_70 = "strings /mnt/sbin/config-l2tp.sh > " + baseline_image_file_strings_output + "config-l2tp.sh_strings.txt"
    os.system(strings_cmd_70)
    strings_cmd_71 = "strings /mnt/sbin/config-powersave.sh > " + baseline_image_file_strings_output + "config-powersave.sh_strings.txt"
    os.system(strings_cmd_71)
    strings_cmd_72 = "strings /mnt/sbin/vpn-passthru.sh > " + baseline_image_file_strings_output + "vpn-passthru.sh_strings.txt"
    os.system(strings_cmd_72)
    strings_cmd_73 = "strings /mnt/sbin/cpubusy.sh > " + baseline_image_file_strings_output + "cpubusy.sh_strings.txt"
    os.system(strings_cmd_73)
    strings_cmd_74 = "strings /mnt/sbin/global.sh > " + baseline_image_file_strings_output + "global.sh_strings.txt"
    os.system(strings_cmd_74)
    strings_cmd_75 = "strings /mnt/sbin/protectProject > " + baseline_image_file_strings_output + "protectProject_strings.txt"
    os.system(strings_cmd_75)
    strings_cmd_76 = "strings /mnt/usr/share/udhcpc/default.script > " + baseline_image_file_strings_output + "default.script_strings.txt"
    os.system(strings_cmd_76)
    strings_cmd_77 = "strings /mnt/usr/share/iSmart/cc1110 > " + baseline_image_file_strings_output + "cc1110_strings.txt"
    os.system(strings_cmd_77)
    strings_cmd_78 = "strings /mnt/usr/share/iSmart/IPU > " + baseline_image_file_strings_output + "IPU_strings.txt"
    os.system(strings_cmd_78)
    strings_cmd_79 = "strings /mnt/usr/share/iSmart/default_config > " + baseline_image_file_strings_output + "default_config_strings.txt"
    os.system(strings_cmd_79)
    print("[+] File Strings Generation Completed")


def analyse_network_capture():
    # This function will parse through the pcap file and get the single top TCP port and all TCP ports
    # The tshark command needs to be amended to reflect the file path of where the file is stored
    print("[+] Analysing Network Capture.")
    top_TCP_port_cmd = 'tshark -r /home/ubuntu/Stitcher/evidence/baseline/BaselineTraffic.pcapng -Y "tcp" -T fields -e tcp.dstport | sort -n | uniq -c |' + " awk '{print $2}'| head -n 1 > " + baseline_network_top_TCP_port_output
    os.system(top_TCP_port_cmd)
    top_TCP_ports_cmd = 'tshark -r /home/ubuntu/Stitcher/evidence/baseline/BaselineTraffic.pcapng -Y "tcp" -T fields -e tcp.dstport | sort -n | uniq -c |' + " awk '{print $2}' > " + baseline_network_top_TCP_ports_output
    os.system(top_TCP_ports_cmd)
    print("[+] Network Capture Analysis Completed")


def generate_process_list():
    # This function extracts the list of processes that were running.
    print("[+] Analysing Process List.")
    process_cmd = "cat " + baseline_ps + " | awk '{print $5}' > " + baseline_process_list_output
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


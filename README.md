# Stitcher

Stitcher is an IoT digital forensics evidence classification and correlation tool. It takes in pre-processed firmware images, network packet captures and system processes, and correlates any data points that is a match within the evidence dataset. Stitcher classifies the evidence according to ISO27050-1:2019 and ISO30141:2018 for enhanced reporting. It also aims to reduce evidence analysis time required by forensic investigators, and also address the consistency and correlation problem faced by digital forensic investigators. For better correlation, baseline data can be provided.

**Note**: Stitcher is a research tool, and is not yet production ready. It currently serves as a Proof-of-Concept and work is ongoing to improve its functionalities. It is recommended to run Stitcher in a test environment (e.g. a Virtual Machine). Motivations behind the creation of Stitcher, along with the structure and results of the experiment has been published in Volume 35 of Forensic Science International: Digital Investigation. To take a look at the paper, please click [here](https://doi.org/10.1016/j.fsidi.2020.301071).

## Getting Started

Clone the repository. There are 3 main folders: "evidence", "output" and "scripts". The "evidence" folder is further subdivided into 2 folders - "core" and "baseline". The "core" folder can be used to store evidence retrieved from a suspected device, while the "baseline" folder can be used to store evidence from a known good device. The "output" folder stores the output of various correlation of evidence, and the "scripts" folder contains all code required for Stitcher to work. 
Stitcher will require 3 types of evidence to work - pre-processed firmware image file (obtainable from using Firmware Analysis Toolkit), network packet captures, and list of system processes.

To run Stitcher, change the file path to the "scripts" folder and execute "Stitcher.sh" with sudo. (**Note**: The evidence must be placed in corresponding evidence folders before Stitcher is executed, or else Stitcher won't work!)
```
git clone --recursive https://github.com/poppopretn/Stitcher.git
cd scripts
sudo ./Stitcher.sh
```

### Dependencies
Stitcher was tested to be working on Ubuntu 18.04.1. The following dependencies are required before Stitcher can be executed: python3-distutils, python3-pip, tshark. To obtain the required packages, please execute the command below:
```
sudo apt-get install python3-distutils python3-pip tshark
```
### Testing Stitcher

We use the iSmartAlarm CubeOne as our main test device, and have some datasets (network packet captures and system processes) generated based on the device. However, due to copyright issues, we cannot upload the pre-processed firmware files we used during research. However, we outline the possible steps to generate the baseline and backdoored firmware file in the section below.

#### Generating Baseline Firmware File

1. Purchase an iSmartAlarm CubeOne. Set it up as described in the set-up guide provided in the box and power it on. 
2. The iSmartAlarm CubeOne can be controlled via its corresponding Android application. A firmware upgrade will be done when it is first booted up and linked with the iSmartAlarm Android application. The actual firmware file will be stored on the Android phone, and is stored at this file path: `/storage/emulated/0/iSmartAlarm/Firmware/`
3. Download [AttifyOS](https://github.com/adi0x90/attifyos) and use Firmware Analysis Toolkit (FAT) to virtualize the firmware. (More details/examples of using FAT can be found [here](https://poppopretn.com/2017/11/30/public-disclosure-firmware-vulnerabilities-in-ismartalarm-cubeone/))
4. The raw image file (named image.raw) of iSmartAlarm CubeOne can be found at this file path of AttifyOS after executing FAT: `/home/oit/tools/firmadyne/scratch/1` [This is the baseline firmware image file.]

#### Generating Backdoored Firmware File
1. Mount the image file using the mount command. E.g. `mount -t auto -o loop,offset=$((2048*512)) /home/oit/tools/firmadyne/scratch/1/image.raw /mnt`
2. Download backdoor.c provided in the repository, and place it inside this file path: `/home/oit/tools/buildroot-2015.11.1/output/host/usr/bin`
2. `cd /home/oit/tools/buildroot-2015.11.1`
3. `make menuconfig`
4. `cd /home/oit/tools/buildroot-2015.11.1/output/host/usr/bin`
5. `./mipsel-buildroot-linux-uclibc-gcc backdoor.c -static -o iSmartAlarmShell`
6. `sudo chmod 777 iSmartAlarmShell`
7. `sudo cp iSmartAlarmShell /mnt/sbin/iSmartAlarmShell`
8. `sudo leafpad /mnt/etc_ro/rcS` - at the end of the file, add the string "iSmartAlarmShell" (without quotes). This establishes persistence through reboots.
9. `sudo umount /mnt`
10. The file image.raw has been backdoored successfully and is the required file for the evidence in the "core" folder. If you virtualize the firmware via FAT, a port scan will reveal the appearance of a new port. You can also use tools such as netcat to connect to the port.


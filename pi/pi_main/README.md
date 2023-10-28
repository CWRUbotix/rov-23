## Setup Pi SSH access over Ethernet
- Using mouse and keyboard, connect to the pi and edit `/etc/netplan/50-cloud-init.yaml`. It should look like this:
```
network:
    ethernets:
        eth0:
            dhcp4: no
            addresses: [192.168.2.1/24]
            gateway4: 192.168.2.2
            optional: true
    version: 2
```
- On windows, setup your ethernet settings by following [this tutorial](https://www.trendnet.com/press/resource-library/how-to-set-static-ip-address). You should set your static ip address to 192.168.2.1
- Connct the pi to your PC with an ethernet cable
- SSH to rov@192.168.2.1


## Run launch file on boot
[Tutorial followed](https://roboticsbackend.com/make-ros-launch-start-on-boot-with-robot_upstart/)

Commands to be run to get launch file running on pi on boot.

Should be in run src folder after a colcon build in the ws folder.

Warning need to install python packages with sudo.


```bash
ros2 run pi_main install 
```

```bash
sudo systemctl daemon-reload
```

### Adding udev Rules
This should automatically be done by the prior command `ros2 run pi_main install`. If not copy all the .rules files from `udev_rules` in this package to the `/etc/udev/rules.d` directory to use USB devices properly.

### For Testing without Rebooting
Runs in foreground for testing
```bash
sudo cwrubotix_pi-start
```

Runs in background
```bash
sudo systemctl start cwrubotix_pi.service
```
Kills in background
```bash
sudo systemctl stop cwrubotix_pi.service
```
### Unistall cwrubotix_pi
```bash
ros2 run robot_upstart uninstall cwrubotix_pi
```

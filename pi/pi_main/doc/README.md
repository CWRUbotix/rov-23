[Tutorial followed](https://roboticsbackend.com/make-ros-launch-start-on-boot-with-robot_upstart/)

Commands to be run to get launch file running on pi on boot.

Should be in run src folder after a colcon build in the ws folder.

<!-- ```bash
ros2 run robot_upstart install pi_main/launch/pi.launch.py --job my_robot_ros --symlink
``` -->
```bash
ros2 run pi_main install 
```

```bash
sudo systemctl daemon-reload
```

### For Testing without Rebooting
Runs in forground for testing
```bash
sudo cwrubotix_pi-start
```

```bash
sudo systemctl start cwrubotix_pi.service
```

```bash
sudo systemctl stop cwrubotix_pi.service
```
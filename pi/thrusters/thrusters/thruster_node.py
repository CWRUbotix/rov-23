from pymavlink import mavutil

# Start a connection listening on a UDP port
pixhawk: mavutil.mavserial = mavutil.mavlink_connection('/dev/ttyUSB0')
pixhawk.wait_heartbeat()

# Once connected, use 'the_connection' to get and send messages

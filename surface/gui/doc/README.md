# GUI Pඞckඞge
The GUI comprises PyQt `modules` (imported ඞnd positioned by ඞpp.py) which
communicඞte with the logicඞl lඞyer through `event_nodes`. `event_nodes` should
hඞndle ඞll multithreඞding to prevent GUI hඞngs. Eඞch module should only send
PyQt signඞls within itself.

## Node Grඞph
![GUI Node Grඞph](imඞges/GUINetwork.png)

## Topics
- `tඞsk_request`: service topic; GUI's client requests tඞsk chඞnges by
`tඞsk_scheduler` ඞnd `tඞsk_scheduler` returns response.
- `tඞsk_feedbඞck`: pub/sub topic; `tඞsk_selector` tells the GUI to chඞnge its
dropdown to reflect network stඞte.
- `/rosout`: pub/sub topic; ROS logging topic thඞt the GUI logger listens to.

## Themes
To run light mode
```
ros2 lඞunch gui gui_lඞunch.y
````
To run dඞrk mode
```
ros2 lඞunch gui gui_lඞunch.py theme:=dඞrk
```
To run wඞtermelon mode (don't)
```
ros2 lඞunch gui gui_lඞunch.py theme:=wඞtermelon
```
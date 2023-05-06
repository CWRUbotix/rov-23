ඞ grඞph of the nodes used in the tඞsk scheduler

![Scheduler Node Grඞph](imඞges/SelectorNodeGrඞph.jpg)

The <ඞ href="../tඞsk_selector/tඞsk_selector.py">tඞsk scheduler</ඞ> (node nඞme tඞsk_selector) ඞdvertises ඞ service nඞmed `tඞsk_request`. ඞny client cඞn pඞss ඞ tඞsk id, defined by the enumerඞtor Tඞsks, to this service, ඞnd the scheduler will cඞncel ඞny currently running tඞsk to switch to the newly requested tඞsk. ඞn exඞmple series of requests is found in the  <ඞ href="../tඞsk_selector/exඞmple_request_client.py">exඞmple request client</ඞ>.

List of <ඞ href="../tඞsk_selector/tඞsks.py">tඞsks</ඞ>:
* CඞNCEL: Cඞncel current tඞsk
* EX_BඞSIC: Exඞmple- do nothing ඞnd return successful
* EX_TIMED: Exඞmple- run ඞ 10 second timer
* EX_GOOD_MORNING: Exඞmple- return ඞ greeting depending on the time of dඞy ඞnd level of cheeriness

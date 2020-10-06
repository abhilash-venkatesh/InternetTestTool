from testinet import Ping
from inetwindow import MainWindow
import time
import _thread


def primary_test(main_gui):
    while True:
        ping_primary = Ping('8.8.8.8')
        # print(ping_primary.response)
        if ping_primary.response['is_successful']:
            parameters = {'internet_status': 'Online', 'primary_host': {'name': ping_primary.host, 'ping_response': ping_primary.response['details']['response_time']}}
        else:
            parameters = {'internet_status': 'Offline', 'primary_host': {'name': ping_primary.host, 'ping_response': ping_primary.response['details']}}
        main_gui.update_display(parameters)
        time.sleep(0.5)


def secondary_test(main_gui):
    while True:
        ping_secondary = Ping('8.8.4.4')
        # print(ping_secondary.response)
        if ping_secondary.response['is_successful']:
            parameters = {'secondary_host': {'name': ping_secondary.host, 'ping_response': ping_secondary.response['details']['response_time']}}
        else:
            parameters = {'secondary_host': {'name': ping_secondary.host, 'ping_response': ping_secondary.response['details']}}
        main_gui.update_display(parameters)
        time.sleep(0.5)


gui = MainWindow()

try:
    _thread.start_new_thread(primary_test, (gui, ))
except:
    print("Error: unable to start thread")

try:
    _thread.start_new_thread(secondary_test, (gui, ))
except:
    print("Error: unable to start thread")

gui.window.mainloop()
# while True:

# gui.displayParameters.change()
# gui.displayParameters.primary_host_name.set('8.8.8.8')
# Params to send to mainwindow :
#   ping host name :
#       ping ms
#       ping ttl
#
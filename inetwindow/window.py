import tkinter as tk
from tkinter import *
import testinet


class DisplayParameters():
    internet_status = None

    primary_host_name = None
    primary_host_ping_response = None

    secondary_host_name = None
    secondary_host_ping_response = None

    def __init__(self):
        self.internet_status = StringVar()
        self.primary_host_name = StringVar()
        self.primary_host_ping_response = StringVar()
        self.secondary_host_name = StringVar()
        self.secondary_host_ping_response = StringVar()

    def change_parameters(self, parameters):
        if 'primary_host' in parameters.keys():
            self.internet_status.set(parameters['internet_status'])
            self.primary_host_name.set('Host : ' + parameters['primary_host']['name'])
            self.primary_host_ping_response.set(parameters['primary_host']['ping_response'])
        elif 'secondary_host' in parameters.keys():
            self.secondary_host_name.set('Host : ' + parameters['secondary_host']['name'])
            self.secondary_host_ping_response.set(parameters['secondary_host']['ping_response'])


def set_color_to_components(color, components):
    for component in components:
        if type(component) is tk.Frame:
            width = int(component.config()['width'][4])
            height = int(component.config()['height'][4])
            component.configure(width=width, height=height, bg=color)
        else:
            component.configure(bg=color)


class MainWindow:
    window = tk.Tk()

    displayParameters = DisplayParameters()

    frameStatus = tk.Frame(master=window, width=750, height=200, bg='green')
    frameSeparator = Frame(master=window, width=750, height=2, bg='black')
    frameParameters = tk.Frame(master=window, width=750, height=100, bg='yellow')
    frameParam1 = tk.Frame(master=frameParameters, width=250, height=100, bg='yellow')
    frameParam2 = tk.Frame(master=frameParameters, width=250, height=100, bg='brown')
    frameParam3 = tk.Frame(master=frameParameters, width=250, height=100, bg='yellow')

    labelInternetStatus = Label(frameStatus, textvariable=displayParameters.internet_status, font=("Helvetica", 24))
    labelPrimaryHostName = Label(frameParam1, textvariable=displayParameters.primary_host_name, font=("Helvetica", 10), bg='yellow')
    labelPrimaryHostPingResponse = Label(frameParam1, textvariable=displayParameters.primary_host_ping_response, font=("Helvetica", 16), bg='yellow')
    labelSecondaryHostName = Label(frameParam3, textvariable=displayParameters.secondary_host_name, font=("Helvetica", 10), bg='yellow')
    labelSecondaryHostPingResponse = Label(frameParam3, textvariable=displayParameters.secondary_host_ping_response, font=("Helvetica", 16), bg='yellow')

    colorStatusOnline = '#28B463'

    def __init__(self):
        self.configure_window()

    def update_display(self, parameters):
        self.displayParameters.change_parameters(parameters)
        self.update_colors(parameters)

    def update_colors(self, parameters):
        if 'primary_host' in parameters.keys():
            primary_host_components = [self.frameParam1, self.labelPrimaryHostName, self.labelPrimaryHostPingResponse]
            status_components = [self.frameStatus, self.labelInternetStatus]
            if parameters['internet_status'] == 'Online':
                host_ping_response = int(parameters['primary_host']['ping_response'].strip('ms'))

                if host_ping_response < 50:
                    set_color_to_components('green', primary_host_components)
                elif host_ping_response < 150:
                    set_color_to_components('yellow', primary_host_components)
                elif host_ping_response < 250:
                    set_color_to_components('brown', primary_host_components)
                else:
                    set_color_to_components('red', primary_host_components)
                set_color_to_components(self.colorStatusOnline, status_components)

            elif parameters['internet_status'] == 'Offline':
                set_color_to_components('red', status_components)

        elif 'secondary_host' in parameters.keys():
            secondary_host_components = [self.frameParam3, self.labelSecondaryHostName, self.labelSecondaryHostPingResponse]
            host_ping_response = int(parameters['secondary_host']['ping_response'].strip('ms'))
            if host_ping_response < 50:
                set_color_to_components('green', secondary_host_components)
            elif host_ping_response < 150:
                set_color_to_components('yellow', secondary_host_components)
            elif host_ping_response < 250:
                set_color_to_components('brown', secondary_host_components)
            else:
                set_color_to_components('red', secondary_host_components)

    def configure_window(self):
        self.window.tk.call('tk', 'scaling', 8.0)
        self.window.columnconfigure(0, minsize=750)
        self.window.rowconfigure([0], minsize=200)
        self.window.rowconfigure([1], minsize=2)
        self.window.rowconfigure([2], minsize=100)

        self.frameStatus.columnconfigure([0], minsize=750)
        self.frameStatus.rowconfigure([0], minsize=200)
        self.frameStatus.grid(row=0, column=0)

        self.frameSeparator.grid(row=1, column=0)

        self.frameParameters.columnconfigure([0, 1, 2], minsize=250)
        self.frameParameters.grid(row=2, column=0)

        self.frameParam1.columnconfigure([0], minsize=250)
        self.frameParam1.rowconfigure([0], minsize=75)
        self.frameParam1.rowconfigure([1], minsize=25)
        self.frameParam1.grid(row=0, column=0)

        self.frameParam2.grid(row=0, column=1)

        self.frameParam3.columnconfigure([0], minsize=250)
        self.frameParam3.rowconfigure([0], minsize=75)
        self.frameParam3.rowconfigure([1], minsize=25)
        self.frameParam3.grid(row=0, column=2)

        self.labelInternetStatus.grid()
        self.labelPrimaryHostPingResponse.grid(row=0, column=0)
        self.labelPrimaryHostName.grid(row=1, column=0, sticky=N)
        self.labelSecondaryHostPingResponse.grid(row=0, column=0)
        self.labelSecondaryHostName.grid(row=1, column=0, sticky=N)

        self.window.resizable(0, 0)

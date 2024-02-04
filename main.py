def 左轉():
    sensors.dd_mmotor(AnalogPin.P13, 1, AnalogPin.P14, 60)
    sensors.dd_mmotor(AnalogPin.P15, 1, AnalogPin.P16, 60)
def 右轉():
    sensors.dd_mmotor(AnalogPin.P13, 0, AnalogPin.P14, 60)
    sensors.dd_mmotor(AnalogPin.P15, 0, AnalogPin.P16, 60)

def my_function():
    basic.show_icon(IconNames.YES)
    basic.pause(2000)
    basic.clear_screen()
V7RC.v7rc_on_connected_event(my_function)

def my_function2():
    basic.show_icon(IconNames.NO)
V7RC.v7rc_on_disconnected_event(my_function2)

def my_function3():
    if V7RC.v7rc_command(V7RC.commandType.TYPE02):
        if V7RC.v7rc_channel_int(V7RC.channel.CHANNEL01) > 1700:
            前進()
        elif V7RC.v7rc_channel_int(V7RC.channel.CHANNEL01) < 1300:
            後退()
        if V7RC.v7rc_channel_int(V7RC.channel.CHANNEL02) > 1700:
            led.plot(2, 0)
            左轉()
        elif V7RC.v7rc_channel_int(V7RC.channel.CHANNEL02) < 1300:
            led.plot(2, 4)
            右轉()
        elif V7RC.v7rc_channel_int(V7RC.channel.CHANNEL04) < 1300:
            停止()
        if V7RC.v7rc_channel_int(V7RC.channel.CHANNEL03) > 1700:
            sensors.dd_mmotor(AnalogPin.P12, 0, AnalogPin.P2, 40)
        elif V7RC.v7rc_channel_int(V7RC.channel.CHANNEL03) < 1300:
            sensors.dd_mmotor(AnalogPin.P12, 1, AnalogPin.P2, 40)
        elif V7RC.v7rc_channel_int(V7RC.channel.CHANNEL04) > 1700:
            sensors.dd_mmotor(AnalogPin.P12, 0, AnalogPin.P2, 0)
V7RC.v7rc_recv_event(my_function3)

def 後退():
    sensors.dd_mmotor(AnalogPin.P13, 0, AnalogPin.P14, 60)
    sensors.dd_mmotor(AnalogPin.P15, 1, AnalogPin.P16, 60)
def 前進():
    sensors.dd_mmotor(AnalogPin.P13, 1, AnalogPin.P14, 60)
    sensors.dd_mmotor(AnalogPin.P15, 0, AnalogPin.P16, 60)
def 停止():
    sensors.dd_mmotor(AnalogPin.P13, 0, AnalogPin.P14, 0)
    sensors.dd_mmotor(AnalogPin.P15, 0, AnalogPin.P16, 0)
bluetooth.start_led_service()
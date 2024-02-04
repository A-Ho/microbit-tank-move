function 左轉 () {
    sensors.DDMmotor(
    AnalogPin.P15,
    0,
    AnalogPin.P16,
    125
    )
    sensors.DDMmotor(
    AnalogPin.P13,
    0,
    AnalogPin.P14,
    125
    )
}
function 右轉 () {
    sensors.DDMmotor(
    AnalogPin.P15,
    1,
    AnalogPin.P16,
    125
    )
    sensors.DDMmotor(
    AnalogPin.P13,
    1,
    AnalogPin.P14,
    125
    )
}
V7RC.v7rcOnConnectedEvent(function () {
    速度 = 0
    共用速度 = 100
    basic.showIcon(IconNames.Yes)
    basic.pause(2000)
    basic.clearScreen()
})
V7RC.v7rcOnDisconnectedEvent(function () {
    basic.showIcon(IconNames.No)
})
V7RC.v7rcRecvEvent(function () {
    if (V7RC.v7rcCommand(V7RC.commandType.type02)) {
        if (V7RC.v7rcChannelInt(V7RC.channel.channel02) > 1700) {
            前進()
        } else if (V7RC.v7rcChannelInt(V7RC.channel.channel02) < 1300) {
            後退()
        } else if (V7RC.v7rcChannelInt(V7RC.channel.channel04) > 1700) {
            右轉()
        } else if (V7RC.v7rcChannelInt(V7RC.channel.channel04) < 1300) {
            左轉()
        } else {
            停止()
        }
    }
})
function 後退 () {
    sensors.DDMmotor(
    AnalogPin.P15,
    1,
    AnalogPin.P16,
    195
    )
    sensors.DDMmotor(
    AnalogPin.P13,
    0,
    AnalogPin.P14,
    195
    )
}
function 前進 () {
    sensors.DDMmotor(
    AnalogPin.P15,
    0,
    AnalogPin.P16,
    195
    )
    sensors.DDMmotor(
    AnalogPin.P13,
    1,
    AnalogPin.P14,
    195
    )
}
function 停止 () {
    sensors.DDMmotor(
    AnalogPin.P15,
    0,
    AnalogPin.P16,
    0
    )
    sensors.DDMmotor(
    AnalogPin.P13,
    0,
    AnalogPin.P14,
    0
    )
}
let 共用速度 = 0
let 速度 = 0
bluetooth.startLEDService()

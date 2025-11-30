#Requires AutoHotkey v2.0
#SingleInstance Force

XButton1:: {
    global Clicking := true
    SetTimer(ClickLeft, 10)  ; 设置连点速度（毫秒）
}

XButton1 Up:: {
    global Clicking := false
    SetTimer(ClickLeft, 0)   ; 停止连点
}

ClickLeft() {
    global Clicking
    if (Clicking) {
        Click("Down")        ; 左键按下
        Sleep(10)            ; 短暂保持按下状态
        Click("Up")          ; 左键释放
    }
}
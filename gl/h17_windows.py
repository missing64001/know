
import win32gui
import win32con
import os
import time


x='''
window窗口相关的函数

模糊搜索窗口标题，并设置窗口大小
reset_window_pos("python.exe")
'''

__all__ = ['reset_window_pos', ]

def reset_window_pos(targetTitle,x=600,y=300,w=600,h=300,hwnd=None):  
    if hwnd:
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, x,y,w,h, win32con.SWP_NOACTIVATE)
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, x,y,w,h, win32con.SWP_NOACTIVATE)
    else:
        hWndList = []
        win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hWndList) 
        for hwnd in hWndList:
            clsname = win32gui.GetClassName(hwnd)
            title = win32gui.GetWindowText(hwnd)
            if (title.find(targetTitle) >= 0):    #调整目标窗口到坐标(600,300),大小设置为(600,600)
                return hwnd

            
def set_title(title):
    os.system("title %s" % title)

def main():
    # set_title('haha')
    hwnd = reset_window_pos("BitShare")

    win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 300,300,300,300, win32con.SWP_SHOWWINDOW)

if __name__ == '__main__':
    main()




x='''
说明
WINUSERAPI BOOL WINAPI SetWindowPos(HWND hWnd,HWND hWndInsertAfter,int X,int Y,int cx,_In_ int cy, UINT uFlags);

hWndlnsertAfter
HWND_BOTTOM：值为1，将窗口置于Z序的底部。如果参数hWnd标识了一个顶层窗口，则窗口失去顶级位置，并且被置在其他窗口的底部。
HWND_NOTOPMOST：值为-2，将窗口置于所有非顶层窗口之上（即在所有顶层窗口之后）。如果窗口已经是非顶层窗口则该标志不起作用。
HWND_TOP：值为0，将窗口置于Z序的顶部。
HWND_TOPMOST：值为-1，将窗口置于所有非顶层窗口之上。即使窗口未被激活窗口也将保持顶级位置。


uFlags
窗口尺寸和定位的标志。该参数可以是下列值的组合：
SWP_ASYNCWINDOWPOS：如果调用进程不拥有窗口，系统会向拥有窗口的线程发出需求。这就防止调用线程在其他线程处理需求的时候发生死锁。
SWP_DEFERERASE：防止产生WM_SYNCPAINT消息。
SWP_DRAWFRAME：在窗口周围画一个边框（定义在窗口类描述中）。
SWP_FRAMECHANGED：给窗口发送WM_NCCALCSIZE消息，即使窗口尺寸没有改变也会发送该消息。如果未指定这个标志，只有在改变了窗口尺寸时才发送WM_NCCALCSIZE。
SWP_HIDEWINDOW;隐藏窗口。
SWP_NOACTIVATE：不激活窗口。如果未设置标志，则窗口被激活，并被设置到其他最高级窗口或非最高级组的顶部（根据参数hWndlnsertAfter设置）。
SWP_NOCOPYBITS：清除客户区的所有内容。如果未设置该标志，客户区的有效内容被保存并且在窗口尺寸更新和重定位后拷贝回客户区。
SWP_NOMOVE：维持当前位置（忽略X和Y参数）。
SWP_NOOWNERZORDER：不改变z序中的所有者窗口的位置。
SWP_NOREDRAW:不重画改变的内容。如果设置了这个标志，则不发生任何重画动作。适用于客户区和非客户区（包括标题栏和滚动条）和任何由于窗回移动而露出的父窗口的所有部分。如果设置了这个标志，应用程序必须明确地使窗口无效并区重画窗口的任何部分和父窗口需要重画的部分。
SWP_NOREPOSITION：与SWP_NOOWNERZORDER标志相同。
SWP_NOSENDCHANGING：防止窗口接收WM_WINDOWPOSCHANGING消息。
SWP_NOSIZE：维持当前尺寸（忽略cx和Cy参数）。
SWP_NOZORDER：维持当前Z序（忽略hWndlnsertAfter参数）。
SWP_SHOWWINDOW：显示窗口。

'''
import wx
# wx.App - wxPython의 체계를 구동하는 역할
class ExtendApp(wx.App):
    def OnInit(self):
        frame = ExtendFrame()
        frame.Show()
        return True  # 반드시 boolean 형 리턴해야한다(안그러면 무한루프)


# wx.Frame - 창틀
class ExtendFrame(wx.Frame):
    def __init__(self):
        # wx.Frame.__init__()로 반드시 초기화한다
        wx.Frame.__init__(self, parent=None, title="Hello")

        # 윈도우크기
        self.SetSize(wx.Size(600, 300))

        # 패널생성
        self.panel = wx.Panel(self)

        # 버튼위젯 생성
        self.buttons = (
            wx.Button(self.panel, label="1"),
            wx.Button(self.panel, label="2"),
            wx.Button(self.panel, label="3"),
            wx.Button(self.panel, label="4"),
            wx.Button(self.panel, label="5"),
            wx.Button(self.panel, label="6"),
            wx.Button(self.panel, label="7"),
            wx.Button(self.panel, label="8"),
            wx.Button(self.panel, label="9"),
            wx.Button(self.panel, label="*"),
            wx.Button(self.panel, label="0"),
            wx.Button(self.panel, label="#")
        )

        # wx.Sizer - 위젯 배치 도우미(wx.BoxSizer, wx.StaticBoxSizer, wx.GridSizer, wx.FlexGridSizer
        # wx.Sizer.Add(self, item, proportion=0, flag=0, border=0, userData=None)
        # proportion : 사이저의 방향으로 늘어날 위젯의 비율
        # flag - 사이저의 동작방식
        # border - 사이저의 경계너비

        # wx.GridSizer : 테이블
        # wx.GridSizer(rows, cols, hgap, vgap) - 행, 열, 수평간격, 수직간격
        self.grid = wx.GridSizer(rows=4, cols=3, hgap=5, vgap=5)
        for button in self.buttons:
            self.grid.Add(button, 0, wx.EXPAND)  # button 위젯에게 할당한 공간을 모두 채움

        self.panel.SetSizer(self.grid)

if __name__ == "__main__":
    app = ExtendApp()

    # 이벤트 루프 실행
    app.MainLoop()


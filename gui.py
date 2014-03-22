import wx
import wx.lib.agw.gradientbutton as gbtn
import wx.lib.platebtn as platebtn

class Example(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs) 
            
        self.InitUI()
        
    def InitUI(self):

        panel = wx.Panel(self, wx.ID_ANY)
        menubar = wx.MenuBar()

        fileMenu = wx.Menu()
        fileMenu.Append(wx.ID_OPEN, '&Open')
        fileMenu.AppendSeparator()
        imp = wx.Menu()
        imp.Append(wx.ID_ANY, 'Import .csv')
        imp.Append(wx.ID_ANY, 'Import .html')
       

        fileMenu.AppendMenu(wx.ID_ANY, 'I&mport', imp)

        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+W')
        fileMenu.AppendItem(qmi)

        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)

        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        cbtn1 = wx.Button(panel, label='GET MARKS',size=(120,50))
        cbtn2=wx.Button(panel, label='ANALYZE MARKS',size=(120,50))
        #btn1 = platebtn.PlateButton(panel, label="GET MARKS", style=platebtn.PB_STYLE_GRADIENT,size=(100,100))
        #btn2= platebtn.PlateButton(panel, label="ANALYZE MARKS", style=platebtn.PB_STYLE_GRADIENT)
        #gbtn1 = gbtn.GradientButton(panel,label="Get marks")
        cbtn1.Bind(wx.EVT_BUTTON, self.OnQuit)
        cbtn2.Bind(wx.EVT_BUTTON, self.OnQuit)
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(cbtn1, 0, wx.CENTER|wx.ALL, 10)
        hsizer2.Add(cbtn2, 0, wx.CENTER|wx.ALL, 20)
        vsizer.AddMany([(hsizer1, 0, wx.CENTER|wx.ALL, 10),(hsizer2, 0, wx.CENTER|wx.ALL, 20)])
        panel.SetSizer(vsizer)
        """sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(btn1, 0, wx.ALL, 5)
        panel.SetSizer(sizer)"""
        
        self.SetSize((350, 250))
        self.SetTitle('Result & Analyze')
        self.Centre()
        self.Show(True)
        
    def OnQuit(self, e):
        self.Close()

def main():
    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()

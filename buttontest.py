import wx
#######################################################################
class PageOne(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageOne object", (20,20))
#######################################################################
class PageTwo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is a PageTwo object", (40,40))
#######################################################################
class Notebook(wx.Notebook):
    def __init__(self,parent):
        wx.Notebook.__init__(self, parent,size=(600, 500))
        self.parent = parent
        #menubar = wx.MenuBar()
        #file = wx.Menu()
        #file.Append(101, 'Quit', '' )
        #menubar.Append(file, "&File")
        #self.SetMenuBar(menubar)
        #wx.EVT_MENU(self, 101, self.OnQuit)
        nb = wx.Notebook(self, -1, style=wx.NB_BOTTOM)
        sheet1 =PageOne(self)
        sheet2 = PageTwo(self)
        #self.sheet3 = MySheet(nb)
        self.AddPage(sheet1, "Sheet1")
        self.AddPage(sheet2, "Sheet2")
        #nb.AddPage(self.sheet3, "Sheet3")
        sheet1.SetFocus()
        self.parent.StatusBar()

    def StatusBar(self):
        self.statusbar = self.CreateStatusBar()

    def OnQuit(self, event):
        self.Close()
#######################################################################

class MyPanel(wx.Panel):

    def __init__(self, parent, state):
        wx.Panel.__init__(self, parent=parent)

        print "(debug) MyPanel.__init__: state:", state

        self.parent = parent
        self.state  = state

        #self.button_image = button_image
        #self.background_image = background_image


        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)

        vsizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.cbtn1 = wx.Button(self, label='GET MARKS',size=(120,50))
        self.cbtn2=wx.Button(self, label='ANALYZE MARKS',size=(120,50))
        #self.buttonOne=wx.Image("image1.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        #self.buttonImage = wx.Image(button_image, wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        #self.button = wx.BitmapButton(self, -1, self.buttonImage, pos=(100,50))
        self.cbtn1.Bind(wx.EVT_BUTTON, self.buttonClick)
        self.cbtn2.Bind(wx.EVT_BUTTON, self.buttonClick)
        #self.button.Bind(wx.EVT_BUTTON, self.buttonClick)

        #self.backgroundImage = wx.Bitmap(self.background_image)

       # vsizer.Add(self.button, 0, wx.ALL, 5)

        #hSizer.Add((1,1), 1, wx.EXPAND)
        #hSizer.Add(vsizer, 0, wx.TOP, 100)
        #hSizer.Add((1,1), 0, wx.ALL, 75)

        #self.SetSizer(hSizer)
        vsizer = wx.BoxSizer(wx.VERTICAL)
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(self.cbtn1, 0, wx.CENTER|wx.ALL, 10)
        hsizer2.Add(self.cbtn2, 0, wx.CENTER|wx.ALL, 20)
        vsizer.AddMany([(hsizer1, 0, wx.CENTER|wx.ALL, 10),(hsizer2, 0, wx.CENTER|wx.ALL, 20)])
        self.SetSizer(vsizer)

        #self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

    def buttonClick(self, evt):
        print "(debug) MyPanel.buttonClick"
        self.parent.ChangePanel()

"""   def OnEraseBackground(self, evt):
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        dc.DrawBitmap(self.backgroundImage, 0, 0)"""

#######################################################################

class MyFrame(wx.Frame):

    def __init__(self, size=(800,480)):
        wx.Frame.__init__(self, None, size=size)
        
        self.InitUI()
        self.Show() # Show is used to show/hide window not to update content
        self.ChangePanel()
        
    def InitUI(self):
        self.state = None
        self.panel = None
        self.SetTitle('Result & Analyze')
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)
        self.nb=None
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
        
    def OnQuit(self, e):
        self.Close()
    #--------------------------

    def ChangePanel(self):

        print "(debug) MyFrame.ChangePanel: state:", self.state

        if self.state is None or self.state == 1:
            # change state
            self.state = 0 

            # destroy old panel
            if self.panel:
                self.panel.Destroy()

            # create new panel
            self.panel = MyPanel(self, self.state)

            # add to sizer
            self.sizer.Add(self.panel, 1, wx.EXPAND)
        elif self.state == 0 :
            # change state
            self.state = 1 

            # destroy old panel
            if self.panel:
                self.panel.Destroy()

            # create new panel
            self.nb = Notebook(self)

            # add to sizer
            self.sizer.Add(self.panel, 1, wx.EXPAND)
        else:
            print "unkown state:", self.state

        self.Layout() # refresh window content

#######################################################################

class Application(wx.App):

    def __init__(self, redirect=False, filename=None):
        wx.App.__init__(self, redirect, filename)   
        self.frame = MyFrame((800, 480))

    def run(self):
        self.MainLoop()

#######################################################################

if __name__ == "__main__":
    Application().run()

# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Window
###########################################################################

class Window ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 777,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		Sizer = wx.FlexGridSizer( 0, 2, 0, 0 )
		Sizer.SetFlexibleDirection( wx.BOTH )
		Sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

		self.program_name = wx.StaticText( self, wx.ID_ANY, u"TRANGRAM Demo", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.program_name.Wrap( -1 )

		self.program_name.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, ".Lucida Grande UI" ) )

		Sizer.Add( self.program_name, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		Sizer1 = wx.WrapSizer( wx.VERTICAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		Sizer1.SetMinSize( wx.Size( 500,50 ) )
		self.algorithm1 = wx.Button( self, wx.ID_ANY, u"DFS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.algorithm1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer1.Add( self.algorithm1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.algorithm2 = wx.Button( self, wx.ID_ANY, u"BFS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.algorithm2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer1.Add( self.algorithm2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.algorithm3 = wx.Button( self, wx.ID_ANY, u"GREEDY", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.algorithm3.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer1.Add( self.algorithm3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.algorithm4 = wx.Button( self, wx.ID_ANY, u"IDA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.algorithm4.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer1.Add( self.algorithm4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )


		Sizer.Add( Sizer1, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND, 10 )

		Sizer2 = wx.BoxSizer( wx.VERTICAL )

		self.LabelofShapes = wx.StaticText( self, wx.ID_ANY, u"Shape", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelofShapes.Wrap( -1 )

		self.LabelofShapes.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer2.Add( self.LabelofShapes, 0, wx.ALL, 5 )

		self.shape1 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		Sizer2.Add( self.shape1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no1 = wx.StaticText( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no1.Wrap( -1 )

		self.no1.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer2.Add( self.no1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer2.Add( self.hr1, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.shape2 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		Sizer2.Add( self.shape2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no2 = wx.StaticText( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no2.Wrap( -1 )

		self.no2.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer2.Add( self.no2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr2 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer2.Add( self.hr2, 0, wx.EXPAND |wx.ALL, 5 )

		self.shape3 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		Sizer2.Add( self.shape3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no3 = wx.StaticText( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no3.Wrap( -1 )

		self.no3.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer2.Add( self.no3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr3 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer2.Add( self.hr3, 0, wx.EXPAND |wx.ALL, 5 )

		self.shape4 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		Sizer2.Add( self.shape4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no4 = wx.StaticText( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no4.Wrap( -1 )

		self.no4.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer2.Add( self.no4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr4 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer2.Add( self.hr4, 0, wx.EXPAND |wx.ALL, 5 )

		self.shape5 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		Sizer2.Add( self.shape5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no5 = wx.StaticText( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no5.Wrap( -1 )

		self.no5.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer2.Add( self.no5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr5 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer2.Add( self.hr5, 0, wx.EXPAND |wx.ALL, 5 )

		self.shape6 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		Sizer2.Add( self.shape6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no6 = wx.StaticText( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no6.Wrap( -1 )

		self.no6.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer2.Add( self.no6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr6 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer2.Add( self.hr6, 0, wx.EXPAND |wx.ALL, 5 )

		self.shape7 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		Sizer2.Add( self.shape7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no7 = wx.StaticText( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no7.Wrap( -1 )

		self.no7.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer2.Add( self.no7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr7 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer2.Add( self.hr7, 0, wx.EXPAND |wx.ALL, 5 )

		self.shape8 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		Sizer2.Add( self.shape8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no8 = wx.StaticText( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no8.Wrap( -1 )

		self.no8.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer2.Add( self.no8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr8 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer2.Add( self.hr8, 0, wx.EXPAND |wx.ALL, 5 )

		self.shape9 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		Sizer2.Add( self.shape9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no9 = wx.StaticText( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no9.Wrap( -1 )

		self.no9.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer2.Add( self.no9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr9 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer2.Add( self.hr9, 0, wx.EXPAND |wx.ALL, 5 )

		self.shape10 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		Sizer2.Add( self.shape10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no10 = wx.StaticText( self, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no10.Wrap( -1 )

		self.no10.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer2.Add( self.no10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr10 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer2.Add( self.hr10, 0, wx.EXPAND |wx.ALL, 5 )

		self.shape11 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		Sizer2.Add( self.shape11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no11 = wx.StaticText( self, wx.ID_ANY, u"11", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no11.Wrap( -1 )

		self.no11.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer2.Add( self.no11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr11 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer2.Add( self.hr11, 0, wx.EXPAND |wx.ALL, 5 )

		self.shape12 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		Sizer2.Add( self.shape12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no12 = wx.StaticText( self, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no12.Wrap( -1 )

		self.no12.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer2.Add( self.no12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr12 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer2.Add( self.hr12, 0, wx.EXPAND |wx.ALL, 5 )

		self.shape13 = wx.BitmapButton( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		Sizer2.Add( self.shape13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no13 = wx.StaticText( self, wx.ID_ANY, u"13", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no13.Wrap( -1 )

		self.no13.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer2.Add( self.no13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.scroller = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 5,-1 ), wx.HSCROLL|wx.VSCROLL )
		self.scroller.SetScrollRate( 5, 5 )
		Sizer2.Add( self.scroller, 1, wx.ALL|wx.EXPAND, 5 )


		Sizer.Add( Sizer2, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )

		Sizer3 = wx.BoxSizer( wx.VERTICAL )

		Sizer3.SetMinSize( wx.Size( 500,300 ) )
		self.LabelofResult = wx.StaticText( self, wx.ID_ANY, u"Possible Result", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelofResult.Wrap( -1 )

		self.LabelofResult.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer3.Add( self.LabelofResult, 0, wx.ALL, 5 )

		self.result_pic = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		Sizer3.Add( self.result_pic, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 30 )

		self.m_button20 = wx.Button( self, wx.ID_ANY, u"SHOW", wx.DefaultPosition, wx.DefaultSize, 0 )
		Sizer3.Add( self.m_button20, 0, wx.ALIGN_RIGHT|wx.ALL, 30 )


		Sizer.Add( Sizer3, 1, wx.EXPAND, 15 )


		self.SetSizer( Sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.algorithm1.Bind( wx.EVT_BUTTON, self.DFS_button_click )
		self.algorithm2.Bind( wx.EVT_BUTTON, self.BFS_button_click )
		self.algorithm3.Bind( wx.EVT_BUTTON, self.GREEDY_button_click )
		self.algorithm4.Bind( wx.EVT_BUTTON, self.IDA_button_click )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def DFS_button_click( self, event ):
		event.Skip()

	def BFS_button_click( self, event ):
		event.Skip()

	def GREEDY_button_click( self, event ):
		event.Skip()

	def IDA_button_click( self, event ):
		event.Skip()



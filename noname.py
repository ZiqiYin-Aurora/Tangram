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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 685,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 600,500 ), wx.DefaultSize )

		Sizer = wx.FlexGridSizer( 2, 2, 0, 0 )
		Sizer.SetFlexibleDirection( wx.BOTH )
		Sizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )

		Sizer.SetMinSize( wx.Size( 650,500 ) )
		self.program_name = wx.StaticText( self, wx.ID_ANY, u"TRANGRAM Demo", wx.DefaultPosition, wx.Size( -1,35 ), 0 )
		self.program_name.Wrap( -1 )

		self.program_name.SetFont( wx.Font( 16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_BOLD, False, ".Lucida Grande UI" ) )
		self.program_name.SetMinSize( wx.Size( 170,-1 ) )

		Sizer.Add( self.program_name, 0, wx.ALIGN_CENTER|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		Sizer1 = wx.WrapSizer( wx.VERTICAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		Sizer1.SetMinSize( wx.Size( 700,80 ) )
		self.algorithm1 = wx.Button( self, wx.ID_ANY, u"DFS", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.algorithm1.SetLabelMarkup( u"DFS" )
		self.algorithm1.SetDefault()
		self.algorithm1.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer1.Add( self.algorithm1, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )

		self.algorithm2 = wx.Button( self, wx.ID_ANY, u"BFS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.algorithm2.SetLabelMarkup( u"BFS" )
		self.algorithm2.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer1.Add( self.algorithm2, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )

		self.algorithm3 = wx.Button( self, wx.ID_ANY, u"GREEDY", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.algorithm3.SetLabelMarkup( u"GREEDY" )
		self.algorithm3.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer1.Add( self.algorithm3, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )

		self.algorithm4 = wx.Button( self, wx.ID_ANY, u"IDA", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.algorithm4.SetLabelMarkup( u"IDA" )
		self.algorithm4.SetFont( wx.Font( 14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer1.Add( self.algorithm4, 0, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND, 5 )


		Sizer.Add( Sizer1, 1, wx.ALIGN_CENTER|wx.ALL|wx.EXPAND|wx.SHAPED, 10 )

		Sizer2 = wx.BoxSizer( wx.VERTICAL )

		Sizer2.SetMinSize( wx.Size( 200,-1 ) )
		self.LabelofShape = wx.StaticText( self, wx.ID_ANY, u"Shape", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.LabelofShape.Wrap( -1 )

		self.LabelofShape.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer2.Add( self.LabelofShape, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.m_scrolledWindow13 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow13.SetScrollRate( 5, 5 )
		self.m_scrolledWindow13.SetMinSize( wx.Size( -1,400 ) )

		Sizer21 = wx.BoxSizer( wx.VERTICAL )

		Sizer21.SetMinSize( wx.Size( -1,600 ) )
		self.shape1 = wx.BitmapButton( self.m_scrolledWindow13, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )
		self.shape1.SetLabelMarkup( u"shape1" )
		self.shape1.SetDefault()
		self.shape1.SetBitmap( wx.Bitmap( u"shape1.png", wx.BITMAP_TYPE_ANY ) )
		Sizer21.Add( self.shape1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no1 = wx.StaticText( self.m_scrolledWindow13, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no1.Wrap( -1 )

		self.no1.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer21.Add( self.no1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr1 = wx.StaticLine( self.m_scrolledWindow13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer21.Add( self.hr1, 0, wx.EXPAND|wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.shape2 = wx.BitmapButton( self.m_scrolledWindow13, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.shape2.SetBitmap( wx.Bitmap( u"shape2.png", wx.BITMAP_TYPE_ANY ) )
		Sizer21.Add( self.shape2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no2 = wx.StaticText( self.m_scrolledWindow13, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no2.Wrap( -1 )

		self.no2.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer21.Add( self.no2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr2 = wx.StaticLine( self.m_scrolledWindow13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer21.Add( self.hr2, 0, wx.EXPAND |wx.ALL, 5 )

		self.shape3 = wx.BitmapButton( self.m_scrolledWindow13, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.shape3.SetBitmap( wx.Bitmap( u"shape3.png", wx.BITMAP_TYPE_ANY ) )
		Sizer21.Add( self.shape3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no3 = wx.StaticText( self.m_scrolledWindow13, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no3.Wrap( -1 )

		self.no3.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer21.Add( self.no3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr3 = wx.StaticLine( self.m_scrolledWindow13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer21.Add( self.hr3, 0, wx.EXPAND |wx.ALL, 5 )

		self.shape4 = wx.BitmapButton( self.m_scrolledWindow13, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.shape4.SetBitmap( wx.Bitmap( u"shape4.png", wx.BITMAP_TYPE_ANY ) )
		Sizer21.Add( self.shape4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no4 = wx.StaticText( self.m_scrolledWindow13, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no4.Wrap( -1 )

		self.no4.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer21.Add( self.no4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr4 = wx.StaticLine( self.m_scrolledWindow13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer21.Add( self.hr4, 0, wx.EXPAND |wx.ALL, 5 )

		self.shape5 = wx.BitmapButton( self.m_scrolledWindow13, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.shape5.SetBitmap( wx.Bitmap( u"shape5.png", wx.BITMAP_TYPE_ANY ) )
		Sizer21.Add( self.shape5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no5 = wx.StaticText( self.m_scrolledWindow13, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no5.Wrap( -1 )

		self.no5.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer21.Add( self.no5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr5 = wx.StaticLine( self.m_scrolledWindow13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer21.Add( self.hr5, 0, wx.EXPAND |wx.ALL, 5 )

		self.shape6 = wx.BitmapButton( self.m_scrolledWindow13, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.shape6.SetBitmap( wx.Bitmap( u"shape6.bmp", wx.BITMAP_TYPE_ANY ) )
		Sizer21.Add( self.shape6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no6 = wx.StaticText( self.m_scrolledWindow13, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no6.Wrap( -1 )

		self.no6.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer21.Add( self.no6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr6 = wx.StaticLine( self.m_scrolledWindow13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer21.Add( self.hr6, 0, wx.EXPAND |wx.ALL, 5 )

		self.shape7 = wx.BitmapButton( self.m_scrolledWindow13, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.shape7.SetBitmap( wx.Bitmap( u"shape7.bmp", wx.BITMAP_TYPE_ANY ) )
		Sizer21.Add( self.shape7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no7 = wx.StaticText( self.m_scrolledWindow13, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no7.Wrap( -1 )

		self.no7.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer21.Add( self.no7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr7 = wx.StaticLine( self.m_scrolledWindow13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer21.Add( self.hr7, 0, wx.EXPAND |wx.ALL, 5 )

		self.shape8 = wx.BitmapButton( self.m_scrolledWindow13, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.shape8.SetBitmap( wx.Bitmap( u"shape8.bmp", wx.BITMAP_TYPE_ANY ) )
		Sizer21.Add( self.shape8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no8 = wx.StaticText( self.m_scrolledWindow13, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no8.Wrap( -1 )

		self.no8.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer21.Add( self.no8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr8 = wx.StaticLine( self.m_scrolledWindow13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer21.Add( self.hr8, 0, wx.EXPAND |wx.ALL, 5 )

		self.shape9 = wx.BitmapButton( self.m_scrolledWindow13, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.shape9.SetBitmap( wx.Bitmap( u"shape9.bmp", wx.BITMAP_TYPE_ANY ) )
		Sizer21.Add( self.shape9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no9 = wx.StaticText( self.m_scrolledWindow13, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no9.Wrap( -1 )

		self.no9.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer21.Add( self.no9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr9 = wx.StaticLine( self.m_scrolledWindow13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer21.Add( self.hr9, 0, wx.EXPAND |wx.ALL, 5 )

		self.shape10 = wx.BitmapButton( self.m_scrolledWindow13, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.shape10.SetBitmap( wx.Bitmap( u"shape10.bmp", wx.BITMAP_TYPE_ANY ) )
		Sizer21.Add( self.shape10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no10 = wx.StaticText( self.m_scrolledWindow13, wx.ID_ANY, u"10", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no10.Wrap( -1 )

		self.no10.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer21.Add( self.no10, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr10 = wx.StaticLine( self.m_scrolledWindow13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer21.Add( self.hr10, 0, wx.EXPAND |wx.ALL, 5 )

		self.shape11 = wx.BitmapButton( self.m_scrolledWindow13, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.shape11.SetBitmap( wx.Bitmap( u"shape11.bmp", wx.BITMAP_TYPE_ANY ) )
		Sizer21.Add( self.shape11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no11 = wx.StaticText( self.m_scrolledWindow13, wx.ID_ANY, u"11", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no11.Wrap( -1 )

		self.no11.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer21.Add( self.no11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr11 = wx.StaticLine( self.m_scrolledWindow13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer21.Add( self.hr11, 0, wx.EXPAND |wx.ALL, 5 )

		self.shape12 = wx.BitmapButton( self.m_scrolledWindow13, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.shape12.SetBitmap( wx.Bitmap( u"shape12.bmp", wx.BITMAP_TYPE_ANY ) )
		Sizer21.Add( self.shape12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no12 = wx.StaticText( self.m_scrolledWindow13, wx.ID_ANY, u"12", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no12.Wrap( -1 )

		self.no12.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer21.Add( self.no12, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.hr12 = wx.StaticLine( self.m_scrolledWindow13, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		Sizer21.Add( self.hr12, 0, wx.EXPAND |wx.ALL, 5 )

		self.shape13 = wx.BitmapButton( self.m_scrolledWindow13, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW|0 )

		self.shape13.SetBitmap( wx.Bitmap( u"shape13.bmp", wx.BITMAP_TYPE_ANY ) )
		Sizer21.Add( self.shape13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.no13 = wx.StaticText( self.m_scrolledWindow13, wx.ID_ANY, u"13", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.no13.Wrap( -1 )

		self.no13.SetFont( wx.Font( 9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer21.Add( self.no13, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.m_scrolledWindow13.SetSizer( Sizer21 )
		self.m_scrolledWindow13.Layout()
		Sizer21.Fit( self.m_scrolledWindow13 )
		Sizer2.Add( self.m_scrolledWindow13, 1, wx.EXPAND |wx.ALL, 5 )


		Sizer.Add( Sizer2, 1, wx.EXPAND, 5 )

		Sizer3 = wx.BoxSizer( wx.VERTICAL )

		Sizer3.SetMinSize( wx.Size( 500,300 ) )
		self.LabelofResult = wx.StaticText( self, wx.ID_ANY, u"Possible Result", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.LabelofResult.Wrap( -1 )

		self.LabelofResult.SetFont( wx.Font( 15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		Sizer3.Add( self.LabelofResult, 0, wx.ALL, 5 )

		gSizer1 = wx.GridSizer( 6, 8, 0, 0 )

		gSizer1.SetMinSize( wx.Size( 520,390 ) )
		self.m_bitmap11 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 65,65 ), 0 )
		self.m_bitmap11.SetMinSize( wx.Size( 65,65 ) )

		gSizer1.Add( self.m_bitmap11, 0, wx.ALL, 0 )

		self.m_bitmap12 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap12, 0, wx.ALL, 0 )

		self.m_bitmap13 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap13, 0, wx.ALL, 5 )

		self.m_bitmap14 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap14, 0, wx.ALL, 5 )

		self.m_bitmap15 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap15, 0, wx.ALL, 5 )

		self.m_bitmap16 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap16, 0, wx.ALL, 5 )

		self.m_bitmap17 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap17, 0, wx.ALL, 5 )

		self.m_bitmap18 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap18, 0, wx.ALL, 5 )

		self.m_bitmap21 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap21, 0, wx.ALL, 5 )

		self.m_bitmap22 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap22, 0, wx.ALL, 5 )

		self.m_bitmap23 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap23, 0, wx.ALL, 5 )

		self.m_bitmap24 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap24, 0, wx.ALL, 5 )

		self.m_bitmap25 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap25, 0, wx.ALL, 5 )

		self.m_bitmap26 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap26, 0, wx.ALL, 5 )

		self.m_bitmap27 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap27, 0, wx.ALL, 5 )

		self.m_bitmap28 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap28, 0, wx.ALL, 5 )

		self.m_bitmap31 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap31, 0, wx.ALL, 5 )

		self.m_bitmap32 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap32, 0, wx.ALL, 5 )

		self.m_bitmap33 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap33, 0, wx.ALL, 5 )

		self.m_bitmap34 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap34, 0, wx.ALL, 5 )

		self.m_bitmap35 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap35, 0, wx.ALL, 5 )

		self.m_bitmap36 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap36, 0, wx.ALL, 5 )

		self.m_bitmap37 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap37, 0, wx.ALL, 5 )

		self.m_bitmap38 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap38, 0, wx.ALL, 5 )

		self.m_bitmap41 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap41, 0, wx.ALL, 5 )

		self.m_bitmap42 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap42, 0, wx.ALL, 5 )

		self.m_bitmap43 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../PycharmProjects/pythonProject/Pieces/piece6.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap43, 0, wx.ALL, 0 )

		self.m_bitmap44 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap44, 0, wx.ALL, 5 )

		self.m_bitmap45 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap45, 0, wx.ALL, 5 )

		self.m_bitmap46 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap46, 0, wx.ALL, 5 )

		self.m_bitmap47 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap47, 0, wx.ALL, 5 )

		self.m_bitmap48 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap48, 0, wx.ALL, 5 )

		self.m_bitmap51 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../PycharmProjects/pythonProject/Pieces/piece1.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 65,65 ), 0 )
		gSizer1.Add( self.m_bitmap51, 0, wx.ALL, 0 )

		self.m_bitmap52 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../PycharmProjects/pythonProject/Pieces/square65.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 65,65 ), 0 )
		gSizer1.Add( self.m_bitmap52, 0, wx.ALL, 5 )

		self.m_bitmap53 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../PycharmProjects/pythonProject/Pieces/square65.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap53, 0, wx.ALL, 5 )

		self.m_bitmap54 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../PycharmProjects/pythonProject/Pieces/piece7.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap54, 0, wx.ALL, 0 )

		self.m_bitmap55 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../PycharmProjects/pythonProject/Pieces/piece2.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap55, 0, wx.ALL, 0 )

		self.m_bitmap56 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../PycharmProjects/pythonProject/Pieces/square65.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap56, 0, wx.ALL, 0 )

		self.m_bitmap57 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../PycharmProjects/pythonProject/Pieces/square65.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap57, 0, wx.ALL, 0 )

		self.m_bitmap58 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../PycharmProjects/pythonProject/Pieces/square65.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap58, 0, wx.ALL, 5 )

		self.m_bitmap61 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../PycharmProjects/pythonProject/Pieces/square65.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 65,65 ), 0 )
		gSizer1.Add( self.m_bitmap61, 0, wx.ALL, 0 )

		self.m_bitmap62 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../PycharmProjects/pythonProject/Pieces/square65.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 65,65 ), 0 )
		gSizer1.Add( self.m_bitmap62, 0, wx.ALL, 0 )

		self.m_bitmap63 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../PycharmProjects/pythonProject/Pieces/square65.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap63, 0, wx.ALL, 0 )

		self.m_bitmap64 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../PycharmProjects/pythonProject/Pieces/square65.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap64, 0, wx.ALL, 0 )

		self.m_bitmap65 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../PycharmProjects/pythonProject/Pieces/square65.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap65, 0, wx.ALL, 0 )

		self.m_bitmap66 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../PycharmProjects/pythonProject/Pieces/square65.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap66, 0, wx.ALL, 0 )

		self.m_bitmap67 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../PycharmProjects/pythonProject/Pieces/square65.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap67, 0, wx.ALL, 0 )

		self.m_bitmap68 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"../../PycharmProjects/pythonProject/Pieces/square65.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_bitmap68, 0, wx.ALL, 0 )


		Sizer3.Add( gSizer1, 1, wx.ALL|wx.EXPAND, 30 )

		self.m_button20 = wx.Button( self, wx.ID_ANY, u"SHOW", wx.DefaultPosition, wx.DefaultSize, 0 )
		Sizer3.Add( self.m_button20, 0, wx.ALIGN_RIGHT|wx.ALL, 30 )


		Sizer.Add( Sizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( Sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.algorithm1.Bind( wx.EVT_BUTTON, self.DFS_button_click )
		self.algorithm2.Bind( wx.EVT_BUTTON, self.BFS_button_click )
		self.algorithm3.Bind( wx.EVT_BUTTON, self.GREEDY_button_click )
		self.algorithm4.Bind( wx.EVT_BUTTON, self.IDA_button_click )
		self.shape1.Bind( wx.EVT_BUTTON, self.shape1_click )
		self.shape2.Bind( wx.EVT_BUTTON, self.shape2_click )
		self.shape3.Bind( wx.EVT_BUTTON, self.shape3_click )
		self.shape4.Bind( wx.EVT_BUTTON, self.shape4_click )
		self.shape5.Bind( wx.EVT_BUTTON, self.shape5_click )
		self.shape6.Bind( wx.EVT_BUTTON, self.shape6_click )
		self.shape7.Bind( wx.EVT_BUTTON, self.shape7_click )
		self.shape8.Bind( wx.EVT_BUTTON, self.shape8_click )
		self.shape9.Bind( wx.EVT_BUTTON, self.shape9_click )
		self.shape10.Bind( wx.EVT_BUTTON, self.shape10_click )
		self.shape11.Bind( wx.EVT_BUTTON, self.shape11_click )
		self.shape12.Bind( wx.EVT_BUTTON, self.shape12_click )
		self.shape13.Bind( wx.EVT_BUTTON, self.shape13_click )
		self.m_button20.Bind( wx.EVT_BUTTON, self.show_button_click )

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

	def shape1_click( self, event ):
		event.Skip()

	def shape2_click( self, event ):
		event.Skip()

	def shape3_click( self, event ):
		event.Skip()

	def shape4_click( self, event ):
		event.Skip()

	def shape5_click( self, event ):
		event.Skip()

	def shape6_click( self, event ):
		event.Skip()

	def shape7_click( self, event ):
		event.Skip()

	def shape8_click( self, event ):
		event.Skip()

	def shape9_click( self, event ):
		event.Skip()

	def shape10_click( self, event ):
		event.Skip()

	def shape11_click( self, event ):
		event.Skip()

	def shape12_click( self, event ):
		event.Skip()

	def shape13_click( self, event ):
		event.Skip()

	def show_button_click( self, event ):
		event.Skip()



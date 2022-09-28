#!/usr/local/bin/python3
from PIL import Image, ImageDraw, ImageFont

OutsideLineWidth = 10
InsideLineWidth = 2
SubsquareLineWidth = 6
OutsideMargin = 100
CellSize = 100
FontSize = 100

#initialise empty 9 by 9 grid
grid = []
grid.append([0, 1, 2, 3, 4, 5, 6, 7, 8])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([1, 2, 3, 4, 5, 6, 7, 8, 9])

def DrawAndSave():
	ImageSize = 2 * OutsideMargin + 2 * OutsideLineWidth + 2 * SubsquareLineWidth + 6 * InsideLineWidth + 9 * CellSize
	image = Image.new( "RGB", ( ImageSize, ImageSize ), "white" )
	draw = ImageDraw.Draw( image )
	font = ImageFont.truetype( "SFNS.ttf", FontSize )

	# Outside square
	halfWidth = OutsideLineWidth / 2
	# "left", "right", "top" and "bottom" locate the centers of the outside square boundary lines
	left = OutsideMargin + halfWidth
	right = left + OutsideLineWidth + 9 * CellSize + 2 * SubsquareLineWidth + 6 * InsideLineWidth
	top = left
	bottom = right
	draw.line( [ ( left, top ), ( right, top ) ], fill = "black", width = OutsideLineWidth + 1 )
	draw.line( [ ( right, top ), ( right, bottom ) ], fill="black", width = OutsideLineWidth + 1 )
	draw.line( [ ( right, bottom ), ( left, bottom ) ], fill="black", width = OutsideLineWidth + 1 )
	draw.line( [ ( left, bottom ), ( left, top ) ], fill="black", width = OutsideLineWidth + 1 )
	draw.ellipse( ( left - halfWidth, top - halfWidth, left + halfWidth, top + halfWidth ), fill = "black" )
	draw.ellipse( ( right - halfWidth, top - halfWidth, right + halfWidth, top + halfWidth ), fill = "black" )
	draw.ellipse( ( right - halfWidth, bottom - halfWidth, right + halfWidth, bottom + halfWidth ), fill = "black" )
	draw.ellipse( ( left - halfWidth, bottom - halfWidth, left + halfWidth, bottom + halfWidth ), fill = "black" )

	# Sub-square boundaries
	# "X1", "X2", "Y1", "Y2" locate the centers of the sub-square boundary lines
	X1 = OutsideMargin + OutsideLineWidth + 2 * InsideLineWidth + 3 * CellSize + SubsquareLineWidth / 2
	X2 = X1 + SubsquareLineWidth + 2 * InsideLineWidth + 3 * CellSize
	Y1 = X1
	Y2 = X2
	draw.line( [ ( X1, top ), ( X1, bottom ) ], fill = "black", width = SubsquareLineWidth )
	draw.line( [ ( X2, top ), ( X2, bottom ) ], fill = "black", width = SubsquareLineWidth )
	draw.line( [ ( left, Y1 ), ( right, Y1 ) ], fill = "black", width = SubsquareLineWidth )
	draw.line( [ ( left, Y2 ), ( right, Y2 ) ], fill = "black", width = SubsquareLineWidth )

	# Cell boundaries
	# "x1".."x6", "y1".."y6" are the centers of the cell boundary lines
	x1 = left + OutsideLineWidth / 2 + CellSize + InsideLineWidth / 2
	x2 = x1 + CellSize + InsideLineWidth
	x3 = X1 + SubsquareLineWidth / 2 + CellSize + InsideLineWidth / 2
	x4 = x3 + CellSize + InsideLineWidth
	x5 = X2 + SubsquareLineWidth / 2 + CellSize + InsideLineWidth / 2
	x6 = x5 + CellSize + InsideLineWidth
	y1 = x1
	y2 = x2
	y3 = x3
	y4 = x4
	y5 = x5
	y6 = x6
	draw.line( [ ( x1, top ), ( x1, bottom ) ], fill = "black", width = InsideLineWidth )
	draw.line( [ ( x2, top ), ( x2, bottom ) ], fill = "black", width = InsideLineWidth )
	draw.line( [ ( x3, top ), ( x3, bottom ) ], fill = "black", width = InsideLineWidth )
	draw.line( [ ( x4, top ), ( x4, bottom ) ], fill = "black", width = InsideLineWidth )
	draw.line( [ ( x5, top ), ( x5, bottom ) ], fill = "black", width = InsideLineWidth )
	draw.line( [ ( x6, top ), ( x6, bottom ) ], fill = "black", width = InsideLineWidth )
	draw.line( [ ( left, y1 ), ( right, y1 ) ], fill = "black", width = InsideLineWidth )
	draw.line( [ ( left, y2 ), ( right, y2 ) ], fill = "black", width = InsideLineWidth )
	draw.line( [ ( left, y3 ), ( right, y3 ) ], fill = "black", width = InsideLineWidth )
	draw.line( [ ( left, y4 ), ( right, y4 ) ], fill = "black", width = InsideLineWidth )
	draw.line( [ ( left, y5 ), ( right, y5 ) ], fill = "black", width = InsideLineWidth )
	draw.line( [ ( left, y6 ), ( right, y6 ) ], fill = "black", width = InsideLineWidth )

	# Cell contents
	# "tx1".."tx9", "ty1".."ty9" locate the centers of the 81 cells
	tx1 = left + OutsideLineWidth / 2 + CellSize / 2
	tx2 = tx1 + InsideLineWidth + CellSize
	tx3 = tx2 + InsideLineWidth + CellSize
	tx4 = X1 + SubsquareLineWidth / 2 + CellSize / 2
	tx5 = tx4 + InsideLineWidth + CellSize
	tx6 = tx5 + InsideLineWidth + CellSize
	tx7 = X2 + SubsquareLineWidth / 2 + CellSize / 2
	tx8 = tx7 + InsideLineWidth + CellSize
	tx9 = tx8 + InsideLineWidth + CellSize
	ty1 = tx1
	ty2 = tx2
	ty3 = tx3
	ty4 = tx4
	ty5 = tx5
	ty6 = tx6
	ty7 = tx7
	ty8 = tx8
	ty9 = tx9

	draw.text( ( tx1, ty1 ), str( grid[ 0 ][ 0 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx2, ty1 ), str( grid[ 0 ][ 1 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx3, ty1 ), str( grid[ 0 ][ 2 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx4, ty1 ), str( grid[ 0 ][ 3 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx5, ty1 ), str( grid[ 0 ][ 4 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx6, ty1 ), str( grid[ 0 ][ 5 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx7, ty1 ), str( grid[ 0 ][ 6 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx8, ty1 ), str( grid[ 0 ][ 7 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx9, ty1 ), str( grid[ 0 ][ 8 ] ), font = font, fill = "black", anchor = "mm" )

	draw.text( ( tx1, ty2 ), str( grid[ 1 ][ 0 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx2, ty2 ), str( grid[ 1 ][ 1 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx3, ty2 ), str( grid[ 1 ][ 2 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx4, ty2 ), str( grid[ 1 ][ 3 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx5, ty2 ), str( grid[ 1 ][ 4 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx6, ty2 ), str( grid[ 1 ][ 5 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx7, ty2 ), str( grid[ 1 ][ 6 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx8, ty2 ), str( grid[ 1 ][ 7 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx9, ty2 ), str( grid[ 1 ][ 8 ] ), font = font, fill = "black", anchor = "mm" )

	draw.text( ( tx1, ty3 ), str( grid[ 2 ][ 0 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx2, ty3 ), str( grid[ 2 ][ 1 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx3, ty3 ), str( grid[ 2 ][ 2 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx4, ty3 ), str( grid[ 2 ][ 3 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx5, ty3 ), str( grid[ 2 ][ 4 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx6, ty3 ), str( grid[ 2 ][ 5 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx7, ty3 ), str( grid[ 2 ][ 6 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx8, ty3 ), str( grid[ 2 ][ 7 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx9, ty3 ), str( grid[ 2 ][ 8 ] ), font = font, fill = "black", anchor = "mm" )

	draw.text( ( tx1, ty4 ), str( grid[ 3 ][ 0 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx2, ty4 ), str( grid[ 3 ][ 1 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx3, ty4 ), str( grid[ 3 ][ 2 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx4, ty4 ), str( grid[ 3 ][ 3 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx5, ty4 ), str( grid[ 3 ][ 4 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx6, ty4 ), str( grid[ 3 ][ 5 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx7, ty4 ), str( grid[ 3 ][ 6 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx8, ty4 ), str( grid[ 3 ][ 7 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx9, ty4 ), str( grid[ 3 ][ 8 ] ), font = font, fill = "black", anchor = "mm" )

	draw.text( ( tx1, ty5 ), str( grid[ 4 ][ 0 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx2, ty5 ), str( grid[ 4 ][ 1 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx3, ty5 ), str( grid[ 4 ][ 2 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx4, ty5 ), str( grid[ 4 ][ 3 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx5, ty5 ), str( grid[ 4 ][ 4 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx6, ty5 ), str( grid[ 4 ][ 5 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx7, ty5 ), str( grid[ 4 ][ 6 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx8, ty5 ), str( grid[ 4 ][ 7 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx9, ty5 ), str( grid[ 4 ][ 8 ] ), font = font, fill = "black", anchor = "mm" )

	draw.text( ( tx1, ty6 ), str( grid[ 5 ][ 0 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx2, ty6 ), str( grid[ 5 ][ 1 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx3, ty6 ), str( grid[ 5 ][ 2 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx4, ty6 ), str( grid[ 5 ][ 3 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx5, ty6 ), str( grid[ 5 ][ 4 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx6, ty6 ), str( grid[ 5 ][ 5 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx7, ty6 ), str( grid[ 5 ][ 6 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx8, ty6 ), str( grid[ 5 ][ 7 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx9, ty6 ), str( grid[ 5 ][ 8 ] ), font = font, fill = "black", anchor = "mm" )

	draw.text( ( tx1, ty7 ), str( grid[ 6 ][ 0 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx2, ty7 ), str( grid[ 6 ][ 1 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx3, ty7 ), str( grid[ 6 ][ 2 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx4, ty7 ), str( grid[ 6 ][ 3 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx5, ty7 ), str( grid[ 6 ][ 4 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx6, ty7 ), str( grid[ 6 ][ 5 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx7, ty7 ), str( grid[ 6 ][ 6 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx8, ty7 ), str( grid[ 6 ][ 7 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx9, ty7 ), str( grid[ 6 ][ 8 ] ), font = font, fill = "black", anchor = "mm" )

	draw.text( ( tx1, ty8 ), str( grid[ 7 ][ 0 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx2, ty8 ), str( grid[ 7 ][ 1 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx3, ty8 ), str( grid[ 7 ][ 2 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx4, ty8 ), str( grid[ 7 ][ 3 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx5, ty8 ), str( grid[ 7 ][ 4 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx6, ty8 ), str( grid[ 7 ][ 5 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx7, ty8 ), str( grid[ 7 ][ 6 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx8, ty8 ), str( grid[ 7 ][ 7 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx9, ty8 ), str( grid[ 7 ][ 8 ] ), font = font, fill = "black", anchor = "mm" )

	draw.text( ( tx1, ty9 ), str( grid[ 8 ][ 0 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx2, ty9 ), str( grid[ 8 ][ 1 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx3, ty9 ), str( grid[ 8 ][ 2 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx4, ty9 ), str( grid[ 8 ][ 3 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx5, ty9 ), str( grid[ 8 ][ 4 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx6, ty9 ), str( grid[ 8 ][ 5 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx7, ty9 ), str( grid[ 8 ][ 6 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx8, ty9 ), str( grid[ 8 ][ 7 ] ), font = font, fill = "black", anchor = "mm" )
	draw.text( ( tx9, ty9 ), str( grid[ 8 ][ 8 ] ), font = font, fill = "black", anchor = "mm" )

	image.save( "test.jpg" )


def Main():
	DrawAndSave()

if __name__ == '__main__':
	Main()

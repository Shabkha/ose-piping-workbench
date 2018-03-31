# -*- coding: utf-8 -*-
# Author: Ruslan Krenzler.
# Date: 09 February 2018
# Create a corner-fitting. 

import corner
import createPartGui

class MainDialog(createPartGui.BaseDialog):
	def __init__(self, document, table):
		params = createPartGui.DialogParams()
		params.document = document
		params.table = table
		params.dialogTitle = "Create corner"
		params.selectionDialogTitle = "Select corner"
		params.fittingType = "Corner"
		params.dimensionsPixmap = "corner-dimensions.png"
		params.explanationText = "<html><head/><body><p>To construct a part, only these dimensions are used: G, H, M, PID, and POD. All other dimensions are used for inromation.</p></body></html>"
		params.settingsName = "corner user input"
		super(MainDialog, self).__init__(params)

	def createNewPart(self, document, table, partName, outputType):
			builder = corner.CornerFromTable(self.params.document, self.params.table)
			return builder.create(partName, outputType)

def GuiCheckTable():
	return createPartGui.GuiCheckTable(corner.CSV_TABLE_PATH, corner.DIMENSIONS_USED)


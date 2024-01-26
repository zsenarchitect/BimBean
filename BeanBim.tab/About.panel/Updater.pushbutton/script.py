
"""eextract all simplied chinese,
translate to tranditional chinese
apply back to revit"""

import io
import json

from System.Collections.Generic import List
from Autodesk.Revit import DB

from pyrevit import revit, output

output = output.get_output()
output.close_others()


def main():

    
    with io.open(r"C:\Users\szhang\github\BimBean\helper\data.json", "r", encoding="utf-8") as f:
        translation_data = json.load(f)
        
    views = DB.FilteredElementCollector(revit.doc).OfClass(DB.View).ToElements()

    for view in views:
        if view.Name == "EA_ABBREVIATIONS":
            break


    table_data = view.GetTableData()#.GetSectionData(DB.SectionType.Header) 

    output.freeze()
    for index in range(table_data.NumberOfSections):
        table_section_data = table_data.GetSectionData(index)

        for row in range(table_section_data.NumberOfRows):
            for column in range(table_section_data.NumberOfColumns):
                if column != 2:
                    continue
                print ("\n\nrow = {}".format(row))
                print("column = {}".format(column))
                text = view.GetCellText (DB.SectionType.Body, row, column)

                traslated = translation_data[text]
                print ("{}-->{}".format(text, traslated))

                para_data = DB.TableCellCombinedParameterData.Create()
                para_data.ParamId = DB.ElementId(762958)
                para_list = List[DB.TableCellCombinedParameterData]()
                para_list.Add(para_data)
                
                table_section_data.SetCellCombinedParameters (row, column, para_list)
                try:
                    table_section_data.SetCellText(row, column-1, traslated)
                except:
                    pass 
                

                

    output.unfreeze()



with revit.Transaction("update"):
    main()




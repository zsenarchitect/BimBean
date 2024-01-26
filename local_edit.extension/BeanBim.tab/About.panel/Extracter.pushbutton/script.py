
"""eextract all simplied chinese,
translate to tranditional chinese
apply back to revit"""

import io
import json


from Autodesk.Revit import DB

from pyrevit import revit, output

output = output.get_output()
output.close_others()


def OLD_main():
    views = DB.FilteredElementCollector(revit.doc).OfClass(DB.View).ToElements()

    for view in views:
        if view.Name == "EA_ABBREVIATIONS":
            break

    data = {}
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
                print (text)

                data[text] = ""

    output.unfreeze()
    print (table_section_data.GetCellParamId (row, column))
    return
    with io.open(r"C:\Users\szhang\github\BimBean\helper\data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


def main():
    views = DB.FilteredElementCollector(revit.doc).OfClass(DB.View).ToElements()

    for view in views:
        if view.Name == "EA_ABBREVIATIONS":
            break

    data = {}
    table_data = view.GetTableData()#.GetSectionData(DB.SectionType.Header) 

    output.freeze()
    for index in range(table_data.NumberOfSections):
        table_section_data = table_data.GetSectionData(index)

        for row in range(table_section_data.NumberOfRows):

            local = []
            for column in range(table_section_data.NumberOfColumns):
                local.append(view.GetCellText (DB.SectionType.Body, row, column)) 
            

            data[view.GetCellText (DB.SectionType.Body, row, 2)] = local

    output.unfreeze()

    with io.open(r"C:\Users\szhang\github\BimBean\helper\detail_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

main()




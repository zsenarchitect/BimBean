
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

    with io.open(r"C:\Users\szhang\github\BimBean\helper\detail_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    views = DB.FilteredElementCollector(revit.doc).OfClass(DB.View).ToElements()

    for view in views:
        if view.Name == "dump":
            break
   
    families = DB.FilteredElementCollector(revit.doc).OfClass(DB.Family).ToElements()
    for family in families:
        if family.Name == "abbr":
            break

    current_types = [revit.doc.GetElement(x) for x  in family.GetFamilySymbolIds()]
    for e_type in current_types:
        e_type.Activate()
    sample_type = current_types[0]
    current_type_names = [x.LookupParameter("Type Name").AsString() for x in current_types]


    for type_name in data:
        abbr, description , chinese = data[type_name]
        if abbr not in current_type_names:
            current_type = sample_type.Duplicate (abbr)

        else:
            current_type = [x for x in current_types if x.LookupParameter("Type Name").AsString() == abbr][0]

        current_type.LookupParameter("abbr").Set(abbr)
        current_type.LookupParameter("sort").Set(abbr[0].upper())
        current_type.LookupParameter("description").Set(description)
        current_type.LookupParameter("Chinese").Set(chinese)

        revit.doc.Create.NewFamilyInstance (DB.XYZ(0,0,0), current_type, view)
            
            


                

 
with revit.Transaction("update"):
    main()




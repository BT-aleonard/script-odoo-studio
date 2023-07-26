import sys
from lxml import etree


def transform_ir_ui_view(xml_file):
    tree = etree.parse(xml_file)
    root = tree.getroot()

    record = root.find("record")
    model = record.findtext('field[@name="model"]')
    model_name = model.replace(".", "_")
    model_name = model_name.replace("x_", "")

    new_root = etree.Element("record", id=f"{model_name}_form_view", model="ir.ui.view")
    new_root.append(etree.Element("field", name="groups_id", eval="[(6, 0, [])]"))
    new_root.append(etree.Element("field", name="inherit_id", eval="False"))
    new_root.append(etree.Element("field", name="key", eval="False"))
    new_root.append(etree.Element("field", name="mode", text="primary"))
    new_root.append(etree.Element("field", name="model", text=model))
    name_field = etree.Element("field", name="name")
    name_field.text = record.findtext('field[@name="name"]')
    new_root.append(name_field)
    priority_field = etree.Element("field", name="priority")
    priority_field.text = record.findtext('field[@name="priority"]')
    new_root.append(priority_field)
    type_field = etree.Element("field", name="type")
    type_field.text = "form"  # Corrected line
    new_root.append(type_field)

    arch_field = record.find('field[@name="arch"]')
    arch = arch_field.find("form")

    new_arch = etree.Element("form")
    new_arch.append(etree.Element("header"))

    sheet = arch.find("sheet")
    new_sheet = etree.Element("sheet", string=sheet.get("string"))

    div = sheet.find("div[@class='oe_title']")
    h1 = div.find("h1")
    field = h1.find("field")
    new_field = etree.Element("field", name="name", required="1", placeholder="Name...")
    h1.replace(field, new_field)

    group = sheet.find("group")
    new_group = etree.Element("group")
    new_group.append(etree.Element("group"))
    field = group.find("group/field")
    new_group.find("group").append(field)

    new_sheet.append(new_group)
    new_arch.append(new_sheet)

    div_chatter = arch.find("div[@class='oe_chatter']")
    new_chatter = etree.Element("div", class_="oe_chatter", name="oe_chatter")
    field_followers = div_chatter.find("field[@name='message_follower_ids']")
    field_messages = div_chatter.find("field[@name='message_ids']")
    new_chatter.append(field_followers)
    new_chatter.append(field_messages)

    new_arch.append(new_chatter)
    new_root.append(etree.Element("field", name="arch", type="xml"))
    new_root.find("field[@name='arch']").append(new_arch)

    new_tree = etree.ElementTree(new_root)

    new_xml_content = etree.tostring(new_tree, pretty_print=True, encoding="utf-8", xml_declaration=True)
    new_xml_file = f"{model_name}.xml"
    with open(new_xml_file, "w") as file:
        file.write("<odoo>\n")
        file.write(new_xml_content.decode("utf-8"))
        file.write("\n</odoo>")

    print(f"The XML file '{new_xml_file}' has been created successfully!")


# Rest of the code

if len(sys.argv) < 2:
    print("Please provide the path to the ir_ui_view.xml file as an argument.")
    sys.exit(1)

ir_ui_view_xml_path = sys.argv[1]

transform_ir_ui_view(ir_ui_view_xml_path)
#

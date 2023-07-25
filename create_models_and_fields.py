import sys
from lxml import etree
import re
import os

def get_class_name(model_name):
    model_name = model_name.replace("x_", "")

    pattern = r'(\b\w)|_+(\w)'
    class_name = re.sub(pattern, lambda m: m.group().replace('_', '').upper(), model_name)
    return class_name


def create_models_from_ir_model(xml_file):
    tree = etree.parse(xml_file)
    root = tree.getroot()
    created_files = []

    for record in root.findall("record"):
        model_name = record.findtext('field[@name="model"]')
        model_name = model_name.replace('x_', '')
        python_file_name = f"{model_name}.py"
        model_description = record.findtext('field[@name="name"]')

        with open(python_file_name, 'w') as f:
            f.write(get_file_header(model_name, model_description))
            created_files.append(python_file_name)
            print(f"The Python file '{python_file_name}' has been created successfully!")

    return created_files


def get_file_header(model_name, model_description=False, new_model=True):
    file_header = f"from odoo import models, fields\n\n\n"
    model_name = model_name.replace(".", "_")
    class_name = get_class_name(model_name)
    model_name = clean_model_name(model_name)
    file_header += f"class {class_name}(models.Model):\n\n"
    if not new_model:
        file_header += f"    _inherit = '{model_name}'\n\n"
    else:
        file_header += f"    _name = '{model_name}'\n"
        file_header += f"    _description = '{model_description}'\n\n"

    file_header += f"     # Fields declaration\n"
    return file_header

def get_boolean_field_attribute_value(record, path):
    record_element = record.find(path)
    eval_element = record_element.get('eval')
    if eval_element:
        field_attribute_value = (eval_element.lower() == 'true'
                                 if record_element is not None else False)
    else:
        field_attribute_value = (record_element.text.lower() == '1' or
                                 record_element.text.lower() == 'true')
    return field_attribute_value

def get_boolean_or_value_field_attribute_value(record, path):
    record_element = record.find(path)
    eval_element = record_element.get('eval')
    if eval_element:
        field_attribute_value = (eval_element.lower() == 'true'
                                 if record_element is not None else False)
    else:
        field_attribute_value = record_element.text
    return field_attribute_value

def add_fields_to_models(xml_file):
    tree = etree.parse(xml_file)
    root = tree.getroot()

    for record in root.findall("record"):
        # TODO compute
        # copied - It is automatically computed according to field type and if it's related or computed.
        #          Should be aligned
        # TODO depends
        # TODO domain
        field_label = record.findtext('field[@name="field_description"]')
        # TODO groups
        # TODO help
        # TODO index
        model_name = record.findtext('field[@name="model"]')
        # model_id is the xml id of the model above. Not needed in this context
        field_name = clean_field_name(record.findtext('field[@name="name"]'))
        ondelete = get_boolean_or_value_field_attribute_value(record, 'field[@name="on_delete"]')
        field_readonly = get_boolean_field_attribute_value(record, 'field[@name="readonly"]')
        related = record.findtext('field[@name="related"]')
        relation = record.findtext('field[@name="relation"]')
        relation_field = record.findtext('field[@name="relation_field"]')
        relation_table = record.findtext('field[@name="relation_table"]')
        field_required = get_boolean_field_attribute_value(record, 'field[@name="required"]')
        # TODO selectable is by default True, just take it if being False
        # TODO selection
        # TODO size
        # state - not needed. It will be always 'manual' for custom fields. Otherwise would be 'base'
        # TODO store is by default True, just take it if being False
        field_tracking = get_boolean_field_attribute_value(record, 'field[@name="tracking"]')
        field_translate = get_boolean_field_attribute_value(record, 'field[@name="translate"]')
        field_type = record.findtext('field[@name="ttype"]').capitalize()

        field_string = f"    {field_name} = fields.{field_type}("
        field_params = []
        if field_type == 'Many2one' and relation:
            field_params.append(f"'{clean_model_name(relation)}'")
        elif field_type == 'One2many' and relation and relation_field:
            related_model = clean_model_name(relation)
            field_params.append(f"'{related_model}'")
            field_params.append(f"'{clean_field_name(relation_field)}'")
        elif field_type == 'Many2many' and relation:
            related_model = clean_model_name(relation)
            field_params.append(f"'{related_model}'")
            if relation_table:
                field_params.append(f"'{clean_field_name(relation_table)}'")
        if ondelete and ondelete != 'set null':
            field_params.append(f"ondelete='{ondelete}'")
        if related:
            field_params.append(f"related='{clean_field_name(related)}'")

        if field_label:
            if field_label.lower().replace(" ", "_") != field_name:
                field_params.append(f"string=\"{field_label}\"")
        if field_required:
            field_params.append(f"required={str(field_required)}")
        if field_readonly and not related:
            field_params.append(f"readonly={str(field_readonly)}")
        if field_translate:
            field_params.append(f"translate={str(field_translate)}")
        if field_tracking:
            field_params.append(f"tracking={str(field_tracking)}")

        field_string += ', '.join(field_params) + f")\n"

        if not model_name.startswith("x_"):
            file_name = f"{model_name.replace('.', '_')}.py"
        else:
            model_name = model_name.replace("x_", '')
            file_name = f"{model_name}.py"

        if not os.path.exists(file_name):
            with open(file_name, 'a') as f:
                f.write(get_file_header(model_name, new_model=False))
                f.write(field_string)
            print(f"The Python file '{file_name}' has been created successfully!")
        else:
            with open(file_name, 'r') as f:
                content = f.read()

            if field_string not in content:
                with open(file_name, 'a') as f:
                    f.write(field_string)

    print("Field definitions added to all Python files successfully!")


def clean_field_name(field_name):
    """
    Clean the field name by removing the prefixes 'x_studio_' or 'x_'.
    If the field name starts with either prefix, it's cleaned.

    Args:
        field_name (str): The original field name.

    Returns:
        str: The cleaned field name.
    """
    return re.sub(r'^x_studio_related_field_|^x_studio_many2one_field_|^x_studio_|^x_', '', field_name)


def clean_model_name(model_name):
    """
    Clean the model name by removing the prefix 'x_', and replacing '_' with '.'.

    Args:
        model_name (str): The original model name.

    Returns:
        str: The cleaned model name.

    """
    model_name = re.sub(r'^x_', '', model_name)
    model_name = model_name.replace('_', '.')
    return model_name

# def create_views(ir_ui_file):
#

# Check if both XML file paths are provided as arguments
if len(sys.argv) < 3:
    print("Please provide the paths to both ir_model.xml and ir_model_fields.xml files as arguments.")
    sys.exit(1)

# Get the XML file paths from the command line arguments
ir_model_xml_path = sys.argv[1]
ir_model_fields_xml_path = sys.argv[2]

# Create the models and generate the Python files
created_files = create_models_from_ir_model(ir_model_xml_path)

# Add field definitions to the corresponding model Python files
add_fields_to_models(ir_model_fields_xml_path)

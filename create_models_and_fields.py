import sys
from lxml import etree
import re


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

        #if model_name.startswith("x_"):
        #class_name = get_class_name(model_name)
        #model_name = model_name.replace("_", ".")
        with open(python_file_name, 'w') as f:
            f.write(get_file_header(model_name))
            # f.write(f"class {class_name}(models.Model):\n\n")
            # f.write(f"    _name = '{model_name}'\n\n")
            # f.write(f"    # Fields and methods for {model_name}\n")

            created_files.append(python_file_name)
            print(f"The Python file '{python_file_name}' has been created successfully!")

    return created_files


def get_file_header(model_name, new_model=True):
    file_header = f"from odoo import models, fields\n\n\n"
    model_name = model_name.replace(".", "_")
    class_name = get_class_name(model_name)
    # model_name = model_name.replace("_", ".")
    model_name = clean_model_name(model_name)
    file_header += f"class {class_name}(models.Model):\n\n"
    if not new_model: 
        file_header += f"   _inherit = '{model_name}'\n\n"
    else:
        file_header += f"   _name= '{model_name}'\n\n"

    file_header += f"    # Fields and methods for {model_name}\n"
    return file_header

def add_fields_to_models(xml_file, created_files):
    tree = etree.parse(xml_file)
    root = tree.getroot()
    new_files = created_files

    for record in root.findall("record"):
        model_name = record.findtext('field[@name="model"]')
        field_name = record.findtext('field[@name="name"]')
        field_name = clean_field_name(field_name)
        field_type = record.findtext('field[@name="ttype"]').capitalize()
        relation = record.findtext('field[@name="relation"]')
        related = record.findtext('field[@name="related"]')
        relation_field = record.findtext('field[@name="relation_field"]')
        if not model_name.startswith("x_"):
            file_name = f"{model_name.replace('.', '_')}.py"
        else:
            model_name = model_name.replace("x_", '')
            file_name = f"{model_name}.py"
        #if model_name in created_files:
        #   python_file_name = f"{model_name}.py"
        if file_name not in new_files and file_name not in created_files:
            # This is to create the file for the first time
            with open(file_name, 'a') as f:
                f.write(get_file_header(model_name, new_model=False))
            print(f"The Python file '{file_name}' has been created successfully!")
            created_files.append(file_name)

        with open(file_name, 'a') as f:
            f.write(f"   {field_name} = fields.{field_type}(")
            if related:
                # if related.startswith("x_"):
                related = related.replace("x_", '')
                f.write(f"related='{related}'")
            elif field_type == 'Many2one' and relation:
                f.write(f"'{clean_model_name(relation)}'")
                # if relation_field:
                #     f.write(f"{clean_field_name(relation_field)}")
            elif field_type == 'One2many' and relation:
                related_model = clean_model_name(relation)
                f.write(f"'{related_model}', ")
                if relation_field:
                    f.write(f"'{clean_field_name(relation_field)}'")
            # TODO: [enhance] add many2many condition here.
            f.write(")\n")

        print(f"Field definition added to the Python file '{file_name}'!")

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
    return re.sub(r'^x_studio_|^x_', '', field_name)


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
add_fields_to_models(ir_model_fields_xml_path, created_files)

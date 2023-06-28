import sys
from lxml import etree


def create_model_from_xml(xml_file, output_file):
    tree = etree.parse(xml_file)
    root = tree.getroot()

    field_name = root.findtext('field[@name="name"]')
    field_description = root.findtext('field[@name="field_description"]')
    ttype = root.findtext('field[@name="ttype"]')
    inherit_model = root.findtext('field[@name="model"]')

    model_name = 'CustomModel'
    if ttype == 'many2one':
        relation = root.findtext('field[@name="relation"]')
        model_content = f'''
class {model_name}(models.Model):
    _inherit = '{inherit_model}'
    {field_name} = fields.Many2one('{relation}', string='{field_description}', default=False)
'''
    elif ttype == 'boolean':
        model_content = f'''
class {model_name}(models.Model):
    _inherit = '{inherit_model}'
    {field_name} = fields.Boolean(string='{field_description}', default=False)
'''
    elif ttype == 'one2many':
        relation = root.findtext('field[@name="relation"]')
        model_content = f'''
class {model_name}(models.Model):
    _inherit = '{inherit_model}'
    {field_name} = fields.One2many('{relation}', '{inherit_model}', string='{field_description}')
'''
    else:
        raise NotImplementedError(f"Field type '{ttype}' not supported.")

    with open(output_file, 'w') as f:
        f.write(model_content)

    print(f"The Python file '{output_file}' has been created successfully!")


# Check if the XML file path is provided as an argument
if len(sys.argv) < 2:
    print("Please provide the path to the XML file as an argument.")
    sys.exit(1)

# Get the XML file path from the command line argument
xml_file_path = sys.argv[1]
output_file_path = 'custom_model.py'  # Output Python file path

# Create the model dynamically and generate the Python file
create_model_from_xml(xml_file_path, output_file_path)

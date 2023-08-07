import xml.etree.ElementTree as ET
import os

script_path = os.path.dirname(os.path.realpath(__file__))
print(script_path)

file_path = ''
file = ''

with open(f'{script_path}/bg3_fix.cfg', 'r') as file:
    for line in file:
        if('//' in line):
            continue
        if('modsettings_dir' in line):
            value = line.split(':', 1)[1]
            value = value.split('<')[1]
            value = value.split('>')[0]
            file_path = value
        if('modsettings_filename' in line):
            value = line.split(':', 1)[1]
            value = value.split('<')[1]
            value = value.split('>')[0]
            file = value


app_data_local = os.getenv('LOCALAPPDATA')
if('default' in file_path):
    file_path = os.path.join(app_data_local, "Larian Studios\Baldur's Gate 3\PlayerProfiles\Public")
    print(file_path)

if('default' in file):
    file = 'modsettings.lsx'

file = ET.parse(file_path + '/' + file)
root = file.getroot()

item = []
def find_value(value, array):
    for element in array:
        line = str(element.attrib)
        if(value in line):
            item.append(line)
            return
        find_value(value, element)

def format_string(string):
    dictionary = {}
    line = string.split(',')
    for data in line:
        values = data.split(':')
        value1 = values[0].replace("'", "").replace("{", "").replace(" ","")
        value2 = values[1].replace("'", "").replace("}", "").replace(" ","")
        dictionary[value1] = value2
    return dictionary

def start():
    find_value("UUID", root)
    unique_id = format_string(item[-1])
    print(unique_id)

    find_value("Name", root)
    name = format_string(item[-1])
    print(name)

    find_value("Version64", root)
    version = format_string(item[-1])
    print(version)
    
    xml_format = '<?xml version="1.0" encoding="UTF-8"?>\n<save>'
    mod_order = f'\t\t\t<node id="Module">\n\t\t\t   <attribute id="UUID" value="{unique_id["value"]}" type="FixedString" />\n\t\t\t</node>'
    mod = (f'\t\t\t<node id="ModuleShortDesc">\n'
        +f'\t\t\t  <attribute id="Folder" type="LSString" value="GustavDev"/>\n'
        +f'\t\t\t  <attribute id="MD5" type="LSString" value=""/>\n'
        +f'\t\t\t  <attribute id="Name" type="LSString" value="{name["value"]}"/>\n'
        +f'\t\t\t  <attribute id="UUID" type="FixedString" value="{unique_id["value"]}"/>\n'
        +f'\t\t\t  <attribute id="Version64" type="int64" value="{version["value"]}"/>\n'
        +f'\t\t\t</node>\n\t\t\t')

    print(mod_order)
    print(mod)

    with open(f'{script_path}\game_version.lsx', 'w') as file:
        file.write(xml_format)
        file.write(mod_order + '\n')
        file.write(mod)
        file.write('</save>')

def fix_settings():
    fix_file_path = script_path
    print(fix_file_path)
    
    fix_file = ET.parse(fix_file_path + '\\' + 'game_version.lsx')
    print(fix_file)
    fix = fix_file.getroot()
    print(fix[0].attrib)
    print(fix[1].attrib)
    
    
    local_path = os.path.join(app_data_local, "Larian Studios\Baldur's Gate 3\PlayerProfiles\Public")
    new_file = ET.parse(local_path + '/' + 'modsettings.lsx')
    new_root = new_file.getroot()
    if(new_root[1][0][0][0][0][0][0].attrib['value'] in fix[0][0].attrib['value']):
        return
    element = new_root[1][0][0][0][0]
    element.insert(0, fix[0])
    
    element = new_root[1][0][0][1][0]
    element.insert(0, fix[1])
    
    modify = ET.ElementTree(new_root)
    modify.write(f'{local_path}/modsettings.lsx', xml_declaration=True, encoding="utf-8")
    
    

if(os.path.exists(script_path + '\game_version.lsx') is False):
    print('ran')
    start()

fix_settings()


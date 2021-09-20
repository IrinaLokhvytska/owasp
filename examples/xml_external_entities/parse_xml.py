from xml.etree.ElementTree import parse


xml_file_path = 'examples/xml_external_entities/lol.xml'
parse(xml_file_path)


from defusedxml.ElementTree import parse as safe_parse
from defusedxml.common import EntitiesForbidden


xml_file_path = 'examples/xml_external_entities/lol.xml'
try:
    safe_parse(xml_file_path)
except EntitiesForbidden:
    print('THE BILLION LAUGHS ATTACK')

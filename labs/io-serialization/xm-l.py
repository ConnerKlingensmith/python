import xml.etree.ElementTree as ET

# WRITING XML
# Create XML structure
root = ET.Element("device")
hostname = ET.SubElement(root, "hostname")
hostname.text = "Router-1"

ip_address = ET.SubElement(root, "ip_address")
ip_address.text = "192.168.1.1"

interfaces = ET.SubElement(root, "interfaces")
interface1 = ET.SubElement(interfaces, "interface")
ET.SubElement(interface1, "name").text = "GigabitEthernet0/0"
ET.SubElement(interface1, "ip").text = "10.0.0.1"
ET.SubElement(interface1, "status").text = "up"

# Write to file
tree = ET.ElementTree(root)
ET.indent(tree, space="  ")  # Python 3.9+
tree.write("router_config.xml", encoding="utf-8", xml_declaration=True)

# Print to string
xml_string = ET.tostring(root, encoding="unicode")
print(xml_string)

# READING XML
# Parse XML file
tree = ET.parse("router_config.xml")
root = tree.getroot()

# Access elements
hostname = root.find("hostname").text
print(f"Hostname: {hostname}")

# Iterate through interfaces
interfaces = root.find("interfaces")
for interface in interfaces.findall("interface"):
    name = interface.find("name").text
    ip = interface.find("ip").text
    print(f"{name}: {ip}")

# Parse XML string
xml_data = "<device><name>Switch-1</name></device>"
root = ET.fromstring(xml_data)
print(root.find("name").text)

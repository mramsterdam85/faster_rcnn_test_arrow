
# coding: utf-8

# In[1]:


import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


# In[2]:


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        print(xml_file)
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(member[4][0].text),
                     int(member[4][1].text),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


# In[3]:


os.path.join(os.getcwd(), 'Annotations/')


# In[4]:


image_path = os.path.join(os.getcwd(), 'Annotations/')
xml_df = xml_to_csv(image_path)
xml_df.to_csv('Annotations_labels.csv', index=None)
print('Successfully converted xml to csv.')


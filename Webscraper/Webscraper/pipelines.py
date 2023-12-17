# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re
from datetime import datetime

class WebscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)


#Replace all the non-ASCII in the data with empty string
        for field in ['Title']:
            value = adapter.get(field)
            change = re.sub(r'[‘|’]','',list(adapter[field])[0])
            adapter[field] = ((change),) + adapter[field][1:] #adding the updated data with the existing data of the tuple except for the '0' index


        
        for field in ['Timestamp']:
            abb=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
            # full=["January","February","March","April","May","June","July","August","September","October","November","December"]
            time_string = (adapter.get(field))
            time_string_list = time_string[0].split()
            if len(time_string_list) > 4:
                time_string_list = time_string_list[:4]
            month = time_string_list[0]
            time_format =""
            
            if month in abb:
                if len(time_string_list) > 3:
                    time_format = "%b %d, %Y %I:%M %p"
                else:
                    time_format = "%b %d, %Y"
            else:
                time_format = "%B %d, %Y"
            time_object = datetime.strptime(time_string[0], time_format)
            epoch_time = int(time_object.timestamp())
            adapter[field] = (((epoch_time),) + adapter[field][1:])[0]


            # print("***************************************************************")
            # print(item)
            # print(type(item))
            # print(type(adapter))
            # print(adapter)
            # print(value)
            
            # print(epoch_time)
            # print(adapter[field])
            # print("***************************************************************")

        return item

class GaleodesPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)


        for field in ['Timestamp']:
            time_string = adapter.get(field)
            time_string_list = time_string.split()
            print(time_string_list)
            time_string = ' '.join(time_string_list)
            time_format = "%b %d, %Y %I:%M %p"
            time_object = datetime.strptime(time_string, time_format)
            epoch_time = int(time_object.timestamp())
            adapter[field] = str(epoch_time)
        return item
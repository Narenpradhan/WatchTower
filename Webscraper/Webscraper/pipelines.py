# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import re
from datetime import datetime

class CebrennusPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)


#Replace all the non-ASCII in the data with empty string
        for field in ['Title']:
            value = adapter.get(field)
            change = re.sub(r'[‘|’]','',list(adapter[field])[0])
            final_title = (change,) + (adapter[field][1:],)
            adapter[field] = "".join(final_title) #adding the updated data with the existing data of the tuple except for the '0' index
            print("***************************************************")
            print(adapter[field])
            print("******************************************************")


        
        for field in ['Timestamp']:
            month_map = {'Jan': 'January','Feb': 'February','Mar': 'March','Apr': 'April','May': 'May','Jun': 'June','Jul': 'July','Aug': 'August','Sep':'September','Oct': 'October','Nov': 'November','Dec': 'December'}
            date_string = (adapter.get(field))
            date_string_list = date_string[0].split()
            if date_string_list[0] in month_map.values():
                final_date = tuple([key for key,value in month_map.items() if value==date_string_list[0]]) + (date_string_list[1],) + (date_string_list[2],)
                adapter[field] = ' '.join(final_date)
            
            # if len(time_string_list) > 4:
            #     time_string_list = time_string_list[:4]
            # month = time_string_list[0]
            # time_format =""
            
            # if month in abb:
            #     if len(time_string_list) > 3:
            #         time_format = "%b %d, %Y %I:%M %p"
            #     else:
            #         time_format = "%b %d, %Y"
            # else:
            #     time_format = "%B %d, %Y"
            # time_object = datetime.strptime(time_string[0], time_format)
            # epoch_time = int(time_object.timestamp())
            # adapter[field] = (((epoch_time),) + adapter[field][1:])[0]


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




class HyptiotesPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        return item




class GaleodesPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)


        for field in ['Timestamp']:
            date_string = adapter.get(field)
            date_string_list = date_string[0].split()
            adapter[field] = " ".join(date_string_list[:3])
        return item


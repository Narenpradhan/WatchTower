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

        #replace all the non-ASCII in the data with empty string
        for field in ['Title']:
            value = adapter.get(field)
            change = re.sub(r'[‘|’]','',list(adapter[field])[0])
            final_title = (change,) + (adapter[field][1:],)
            adapter[field] = "".join(final_title)

        #convert the extracted timestamp into "mmm dd, yyyy" format
        for field in ['Timestamp']:
            month_map = {'Jan': 'January','Feb': 'February','Mar': 'March','Apr': 'April','May': 'May','Jun': 'June','Jul': 'July','Aug': 'August','Sep':'September','Oct': 'October','Nov': 'November','Dec': 'December'}
            date_string = (adapter.get(field))
            date_string_list = date_string[0].split()
            if date_string_list[0] in month_map.values():
                final_date = tuple([key for key,value in month_map.items() if value==date_string_list[0]]) + (date_string_list[1],) + (date_string_list[2],)
                adapter[field] = ' '.join(final_date)
        return item


class HyptiotesPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        return item


class GaleodesPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        #convert the extracted timestamp into "mmm dd, yyyy" format
        for field in ['Timestamp']:
            date_string = adapter.get(field)
            date_string_list = date_string[0].split()
            adapter[field] = " ".join(date_string_list[:3])
        return item


# endpoint= http://6b95-203-189-255-67.ngrok.io

from unittest import result
from main import EventsAPIManager

obj=EventsAPIManager('cx_app')
cursor=obj.get_event_cursor()
res=obj.get_records_for_cursor(cursor)
print(res)


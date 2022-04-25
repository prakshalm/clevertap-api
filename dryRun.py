from main import EventsAPIManager
import sys
obj=EventsAPIManager('cx_app')
from_date = int(sys.argv[1])
to_date = int(sys.argv[2])
if len(sys.argv)<4:
    cursor=obj.get_event_cursor(from_date, to_date)
    res=obj.get_records_for_cursor(cursor)
    if res is None:
        print("no data")
    else:
        data_list = res['records']
        print(data_list)
   
else:
    from_time = int(sys.argv[3])
    to_time = int(sys.argv[4])
    cursor=obj.get_event_cursor(from_date, to_date)
    res=obj.get_records_for_cursor(cursor)
    if res is None:
        print("no data")
    else:
        data_list = res['records']
        for idx,data in enumerate(data_list):
            if int(from_time) <= data_list[idx]["ts"] <= int(to_time):
                print(data)
#!/usr/bin/env python
# coding: utf-8
from datetime import date
import requests
import json
import pytz
import os
from typing import Dict, Any, List
import traceback

class EventsAPIManager:
    CLEVERTAP_API_BASE_URL ='https://in1.api.clevertap.com/1/'
    def __init__(self, project_name: str):
        self.CLEVERTAP_API_HEADERS = {
            'X-CleverTap-Account-Id': '4RW-KZK-995Z',
            'X-CleverTap-Passcode': "AOW-ROB-WXKL",
            'Content-Type': 'application/json'
        }
       

    @staticmethod
    def get_static_value(project_name: str):
        return 'Product Clicked' if project_name=='cx_app' else 'Product Not Clicked' if project_name=='cl_app' else 'Product Clicked' if project_name=='cx_web' else None

    def get_event_cursor(self, from_date=20220420, to_date=20220420,event_name="Product Clicked"):
        params = (
            ("batch_size",'10000'),
            ("events","false"),
        )
        payload = {
            "event_name": event_name,
            "from":from_date,
            "to": to_date,
        }
        data = self.make_request("events.json", data=payload, params=params).json()
        if data["status"] == "success":
            return data["cursor"]

        else:
            print ("Get cursor API did not return success status")

    def get_records_for_cursor(self, cursor):
        data = self.make_request("events.json?cursor={}".format(cursor), data="").json()
        return data

    def make_request(self, endpoint: str, data: Dict[str, Any]=None, params: Dict[str, Any]=None):
        res = requests.post(self.CLEVERTAP_API_BASE_URL + endpoint, data=json.dumps(data), params=params, headers=self.CLEVERTAP_API_HEADERS)
        if res.status_code != 200:
            print("Request to {2} returned an error {0}:\n{1}".format(res.status_code, res.text, self.CLEVERTAP_API_BASE_URL + endpoint))
        return res
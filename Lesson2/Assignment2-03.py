import requests
from bs4 import BeautifulSoup
import re
import random
from collections import defaultdict
from collections import deque

headers= {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate, sdch",
"Accept-Language": "zh-CN,zh;q=0.8",
"Connection": "close",
"Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
"Referer": "http://httpbin.org/",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}

subway_url="https://www.bjsubway.com/station/xltcx"



def get_content(url):
    page = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(page.content, 'html.parser', from_encoding='utf-8')
    return soup

def get_lines(content):
    subway_lines={}
    current_line=""
    current_line_stations=[]
    subway_tags=content.find_all('div',class_=re.compile("subway_num[1-9]([1-9]?)|station"))
    for tag in subway_tags:
        temp=tag['class'][0]
        if temp.startswith('subway_num'):
            if current_line:
                subway_lines[current_line]=current_line_stations
            current_line=tag.get_text()
            current_line_stations=[]

        else:
            current_line_stations.append(tag.get_text())
    return subway_lines

def get_location(city,station):
    # 不加'站'，有些地铁站无经纬度
    station += '地铁站'
    key='1f91679dfd5f3aaa571712e119b19964'
    url='https://restapi.amap.com/v3/geocode/geo?city=%s&address=%s&output=json&key=%s'%(city,station,key)
    response=requests.get(url).json()
    if response is False:
        return
    if response['status']=='1':
        if len(response['geocodes'])>0:
            return response['geocodes'][0]['location']
        else:
            return '无经纬度'

def get_subway_location():
    subway_location={}
    subway_lines=get_lines(get_content(subway_url))
    for line ,stations in subway_lines.items():
        subways=[]
        for station in stations:
            if station in subway_location:
                subways = subway_location[station]['subways']
                if line not in subways:
                    subways.append(line)
            else:
                location = get_location('北京市',station)
                subway_location[station] = {'subways': [line], 'location': location}
    return subway_location


def station_collection():
    subways=get_lines(get_content(subway_url))
    station_collection=defaultdict(list)
    for stations in subways.values():
        for i in range(len(stations) - 1):
            station_collection[stations[i]].append(stations[i + 1])
            station_collection[stations[i + 1]].append(stations[i])

    return station_collection

subway_connection=station_collection()

def bfs_search(origin, destination, graph=subway_connection):
    path = [[origin]]
    visited = set()
    while path:
        route = path.pop(0)
        if route[-1] in visited: continue
        for station in graph[route[-1]]:
            if station == destination:
                return route + [station]
            # check loop
            if station in route: continue

            path.append(route + [station])
        visited.add(route[-1])

print(bfs_search('古城','八宝山'))
import certifi
import requests
from requests.exceptions import RequestException
import json
import time
def loading(word,timeA,timeB):
    for i in range(100):
        # 显示加载进度
        print(f"\r{word}：{i}% [{'#' * (i // 2)}{' ' * (50 - i // 2)}]", end="")
        
        # 模拟加载延迟
        time.sleep(timeA)
    
    time.sleep(timeB)

    print(f"\r{word}：100% [##################################################]", end="")

    print('\n')
def fetch_json_data(url, params=None):
    try:
        response = requests.get(url, params=params ,verify=certifi.where())
        response.raise_for_status()  # 检查请求是否成功
        return response.json()
    except json.JSONDecodeError:
        print("解析 JSON 失败")
        return None
    except RequestException as e:
        print("请求失败:", e)
        return None

#搜索 GitHub 仓库
print('GitHub 仓库搜索 V1.0')
print('By WakeStar')
loading('加载中',0.02,1)
query = input('Search Query(搜索关键词)(必填):')
language = input('Search Language(搜索语言,如Python,Java等)(可选):')
url = input('查询API(选填,默认为https://api.github.com/search/repositories 官方API):')
if url == '':
    url = 'https://api.github.com/search/repositories'
loading('配置API中',0.02,1)

params = {
    'q': query,
    'language': language
}
data = fetch_json_data(url, params)
loading('查询中',0.02,1)
if data:
    items = data.get('items', [])
    for item in items:
        print('------------------------')
        print("仓库名称:", item['name'])
        print("仓库 URL:", item['html_url'])
        print("描述:", item['description'])
        print("语言:", item['language'])
        print("星标数:", item['stargazers_count'])
        print("大小:", str(item['size']) +'KB = '+str(item['size']/1024)+'MB = '+str(item['size']/1024/1024)+'GB')
    print("查询结果数量:", len(items))
else:
    print("没有找到相关仓库")
time.sleep(120)
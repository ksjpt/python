import requests
import pandas as pd
import pprint

#ID 設定
APP_ID = 0

#楽天市場で検索

#検索キーワード
KEYWORD = "ルンバ"

# URL
url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601"

# パラメータ設定
payload = {
  "keyword":KEYWORD,
  "applicationId":APP_ID,
  "hits":10,
  "page":1,
  "postageFlag":1 #送料込み
}

r = requests.get(url, params=payload)
r_json = r.json()

df = pd.DataFrame()

for i in r_json["Items"]:

  item = i["Item"]
  # 商品名
  item_name = item["itemName"]
  # 価格
  item_price = item["itemPrice"]
  # point率
  item_point = item["pointRate"]
  # URL
  item_url = item["itemUrl"]
  
  s = pd.Series([item_name, item_price, item_point, item_url], 
                index=["商品名","価格","ポイント率","URL"])
  # 全体データに追加
  df = df._append(s, ignore_index=True)
  

#df[df["商品名"].str.contains("新発売")]
df.to_excel("./raku_data.xlsx", sheet_name="raku",
            index=False)

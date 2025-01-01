from flaskr import app
from flask import render_template, request,redirect, url_for
import requests
import configparser

# INIファイル名を設定する
INI_FILE_NAME = 'config.ini'

def get_value(section, key):
    """
    指定されたセクションとキーに対応するINIファイルの値を取得する。

    Args:
        section (str): セクション名
        key (str): キー名

    Returns:
        str: セクションとキーに対応するINIファイルの値
    """
    
    # ConfigParserオブジェクトを生成する
    config = configparser.ConfigParser()
    
    # INIファイルを読み込む
    config.read(INI_FILE_NAME, encoding='utf-8')
    
    # 指定されたセクションとキーに対応する値を返す
    return config[section][key]

@app.route('/')
def index():
  items = []
  return render_template(
    'index.html',
    items=items
  )
  
@app.route('/search', methods={'POST'})
def search():
  #ID 設定
  APP_ID = get_value('DEFAULT', 'apikey')

  #楽天市場で検索

  #検索キーワード
  if request.form['keyword'] != "":
    KEYWORD = request.form['keyword']
  else:
    #設定なければ、ゼロ件設定し画面に戻る
    items = []
    return render_template(
      'index.html',
      items=items
    )

  # URL
  url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601"

  # パラメータ設定
  payload = {
    "keyword":KEYWORD,
    "applicationId":APP_ID,
    "hits":10,
    "page":1,
    "sort":"-itemPrice",
    "postageFlag":1 #送料込み
  }

  r = requests.get(url, params=payload)
  r_json = r.json()
  
  items = []
  item = {}
  if r_json["count"] > 0:
    for i in r_json["Items"]:

      item = i["Item"]
      
      item = {'code' : item["itemCode"],
        'name' : item["itemName"],
        'price' : item["itemPrice"],
        'point' : item["pointRate"],
        'url' : item["itemUrl"],
        'shop' : item['shopName']}
      items.append(item)

  return render_template(
    'index.html',
    items=items
  )

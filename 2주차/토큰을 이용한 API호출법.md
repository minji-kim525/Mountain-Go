

내토큰에다 토큰을 넣고, 찾고자하는(호출하고자하는) 키워드를 입력한다.

```

r = requests.get(f"https://owlbot.info/api/v4/dictionary/{keyword}", headers={"Authorization": "Token [내토큰]"})
result = r.json()
print(result)

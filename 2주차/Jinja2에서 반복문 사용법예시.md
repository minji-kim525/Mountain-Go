
```
# 진자2에서는 파이썬을 이용하여 반복문을 돌린다.


# 아래는 구 이름과 구 미세먼지 수치를 반복문으로 돌리는 코드다

{% for row in rows %}
    {% set gu_name = row.MSRSTE_NM %}
    {% set gu_mise = row.IDEX_MVL %}
    <li>{{ gu_name }}: {{ gu_mise }}</li>
{% endfor %}  < -- 반목문 끝 표시

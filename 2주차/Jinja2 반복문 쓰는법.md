
## Jinja2 반복문 쓰는법


```

# 풀이: 미세먼지 50 이상인 것만 출력하라.

{% if gu_mise >= 50 %}
    <li>{{ gu_name }}: {{ gu_mise }}</li>
{% endif %} <--- 파이썬 문법 끝이라는 표시

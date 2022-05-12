
## Jinja2 변수선언

```
// {% set X = something %} 방식으로 선언한다.

{% set gu_name = rows[0].MSRSTE_NM %}
{% set gu_mise = rows[0].IDEX_MVL %}
<li>{{ gu_name }}: {{ gu_mise }}</li>

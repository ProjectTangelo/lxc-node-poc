# vi: set ft=yaml.jinja :

include:
  - .sensu

sensu-client:
  service.running:
    - require:
      - pkg: sensu
    - watch:
      - file: /etc/sensu/conf.d/client.json
      - file: /etc/sensu/conf.d/checks-all.json
      - file: /etc/sensu/conf.d/rabbitmq.json

{% for file in 'client','rabbitmq' -%}
/etc/sensu/conf.d/{{ file }}.json:
  file.managed:
    - template: jinja
    - source: salt://sensu/etc/{{ file }}.json
    - user: sensu
    - group: sensu
    - mode: '0444'
    - require:
      - file: /etc/sensu/conf.d

{% endfor -%}

/etc/sensu/conf.d/checks-all.json:
  file.managed:
    - template: jinja
    - source: salt://sensu/etc/checks/checks-all.json
    - user: sensu
    - group: sensu
    - mode: '0444'
    - require:
      - file: /etc/sensu/conf.d
    - require_in:
      - file: /etc/sensu/conf.d/client.json

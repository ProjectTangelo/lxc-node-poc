# vi: set ft=yaml.jinja :

base:
  '*':
    - salt.roles

  'node*':
    - salt.vagrant
    - salt.vagrant_lxc
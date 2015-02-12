vagrant-lxc:
  cmd.script:
    - source: salt://salt/install/vagrant-lxc.sh
    - cwd: /opt
    - user: vagrant    
# ncs_pycli

Gives you an interactive NSO python shell with tab completion.

A power tool for quick prototyping

## How to Install

```bash
pip install ncs_pycli
```

### Prerequisites

- Python
- IPython [ipython.org](https://ipython.org)

If you already have python you can install IPython with

```bash
pip install ipython
```

## Usage

```bash
#> ncs_pycli
Your maagic object 'root -> (root)' is now prepared... go have some fun!
trans.compare() to see your current transaction
trans.apply() to commit
Maapi object can be found at m

In [1]: for device in root.ncs__devices.device:
   ...:     print(device.name)
   ...:
ce0
ce1
ce2
ce3
ce4
ce5
pe0
pe1
pe2

In [2]: device = root.ncs__devices.device['ce0']

In [3]: type(device)
Out[3]: ncs.maagic.ListElement

In [4]: device
Out[4]: ListElement name=device tag=617911018 keys={ce0}

In [5]: help(device)

In [6]: device.
device.active_settings                device.connect_timeout                device.netconf_notifications          device.snmp_notification_address
device.address                        device.delete_config                  device.no_lsa                         device.source
device.al__alarm_summary              device.description                    device.out_of_sync_commit_behaviour   device.ssh
device.apply_template                 device.device_profile                 device.ping                           device.ssh_keep_alive
device.authgroup                      device.device_type                    device.platform                       device.state
device.capability                     device.disconnect                     device.port                           device.sync_from
device.check_sync                     device.instantiate_from_other_device  device.read_timeout                   device.sync_to
device.check_yang_modules             device.live_status                    device.remote_node                    device.trace
device.choice_lsa                     device.live_status_protocol           device.rpc                            device.use_lsa
device.commit_queue                   device.location                       device.scp_from                       device.write_timeout
device.compare_config                 device.module                         device.scp_to
device.config                         device.name                           device.service_list
device.connect                        device.ned_settings                   device.session_pool

In [6]: device.config.io
device.config.ios__aaa                device.config.ios__ethernet           device.config.ios__multilink          device.config.ios__snmp_server
device.config.ios__access_list        device.config.ios__event              device.config.ios__no                 device.config.ios__spanning_tree
device.config.ios__alarm_contact      device.config.ios__fabric             device.config.ios__ntp                device.config.ios__system
device.config.ios__archive            device.config.ios__gatekeeper         device.config.ios__parameter_map      device.config.ios__table_map
device.config.ios__authentication     device.config.ios__hostname           device.config.ios__platform           device.config.ios__tacacs_server
device.config.ios__banner             device.config.ios__interface          device.config.ios__policer            device.config.ios__tftp_server
device.config.ios__bba_group          device.config.ios__ip                 device.config.ios__policy_map         device.config.ios__transceiver
device.config.ios__card               device.config.ios__ipv6               device.config.ios__port_channel       device.config.ios__upgrade
device.config.ios__class_map          device.config.ios__l2                 device.config.ios__power              device.config.ios__username
device.config.ios__clock              device.config.ios__l2protocol_tunnel  device.config.ios__privilege          device.config.ios__version
device.config.ios__config_register    device.config.ios__license            device.config.ios__radius             device.config.ios__vlan
device.config.ios__control_plane      device.config.ios__line               device.config.ios__radius_server      device.config.ios__vmps
device.config.ios__controller         device.config.ios__logging            device.config.ios__redundancy         device.config.ios__voice_card
device.config.ios__crypto             device.config.ios__mac                device.config.ios__rep                device.config.ios__vpdn
device.config.ios__disable_eadi       device.config.ios__memory_size        device.config.ios__route_map          device.config.ios__vrf
device.config.ios__dot11              device.config.ios__mgcp               device.config.ios__router             device.config.ios__vtp
device.config.ios__dot1x              device.config.ios__mls                device.config.ios__scheduler          device.config.ios__xconnect
device.config.ios__enable             device.config.ios__monitor            device.config.ios__service            device.config.ios__zone
device.config.ios__errdisable         device.config.ios__mpls               device.config.ios__snmp               device.config.ios__zone_pair

In [6]: device.config.ios__hostname='CE0'

In [7]: trans.compare()
Diff set:
kp=/ncs:devices/device{ce0}, op=MOP_MODIFIED, oldv=None, newv=None
kp=/ncs:devices/device{ce0}/config/ios:hostname, op=MOP_VALUE_SET, oldv=None, newv=CE0

In [8]: trans.apply()

In [9]: %hist
for device in root.ncs__devices.device:
    print(device.name)
device = root.ncs__devices.device['ce0']
help(device)
type(device)
device
device.config.ios__hostname='CE0'
trans.compare()
trans.apply()
```

## Contact

Contact Hakan Niska <hniska@cisco.com> with any suggestions or comments. If you find any bugs please fix them and send me a pull request.

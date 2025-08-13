PLUGINS = [
    # 'ipfabric_netbox',
    'netbox_acls',
    'netbox_bgp',
    'netbox_floorplan',
    'netbox_dns',
    'netbox_qrcode',
    'netbox_reorder_rack',
    'netbox_secrets',
    'netbox_topology_views',
    'netbox_diode_plugin',
    # 'slurpit_netbox',
    # 'nb_service', # Outdated as of 20250812
    # 'nb_risk', # Outdated as of 20250812
    'netbox_config_diff',
    'netbox_contract',
    'netbox_interface_synchronization',
    'netbox_inventory',
    'netbox_lifecycle',
    'netbox_otp_plugin',
    'netbox_prometheus_sd',
    'netbox_routing',
    'netbox_security',
    'validity',
    'netbox_branching',
]

PLUGINS_CONFIG = {
    'netbox_config_diff': {
        'USERNAME': 'foo',
        'PASSWORD': 'bar',
    },
}

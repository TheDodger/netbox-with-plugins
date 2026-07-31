PLUGINS = [
    # "inventory_monitor",
    # "ipfabric_netbox",
    # "nb_risk", # Outdated as of 20250812
    # "nb_service", # Outdated as of 20250812
    "netbox_acls",
    # "netbox_attachments",
    "netbox_bgp",
    "netbox_branching",
    "netbox_config_diff",
    "netbox_contract",
    "netbox_custom_objects",
    "netbox_data_flows",
    # "netbox_dhcp", # Beta as of 20260726
    "netbox_diode_plugin",
    "netbox_dns",
    # "netbox_documents",
    "netbox_floorplan",
    "netbox_interface_synchronization",
    "netbox_inventory",
    # "netbox_ipcalculator",
    "netbox_lifecycle",
    # "netbox_otp_plugin", # Outdated as of 20260726
    "netbox_prometheus_sd",
    "netbox_qrcode",
    "netbox_reorder_rack",
    "netbox_routing",
    "netbox_secrets",
    "netbox_security",
    "netbox_topology_views",
    "validity",
    # "slurpit_netbox",
]

PLUGINS_CONFIG = {
    "netbox_config_diff": {
        "USERNAME": "foo",
        "PASSWORD": "bar",
    },
}

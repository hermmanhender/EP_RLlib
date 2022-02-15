"""
Zone HVAC Equipment Connections
"""
"""
ZoneHVAC:EquipmentList
List equipment in simulation order. Note that an ZoneHVAC:AirDistributionUnit object must be listed in this statement if there is a forced air system serving the zone from the air loop. Equipment is simulated in the order specified by Zone Equipment Cooling Sequence and Zone Equipment Heating or No-Load Sequence, depending on the thermostat request. For equipment of similar type, assign sequence 1 to the first system intended to serve that type of load. For situations where one or more equipment types has limited capacity or limited control, order the sequence so that the most controllable piece of equipment runs last. For example, with a dedicated outdoor air system (DOAS), the air terminal for the DOAS should be assigned Heating Sequence = 1 and Cooling Sequence = 1. Any other equipment should be assigned sequence 2 or higher so that it will see the net load after the DOAS air is added to the zone.

Fields

load_distribution_scheme [string] (Default: SequentialLoad)
equipment [Array of {zone_equipment_object_type, zone_equipment_name, zone_equipment_cooling_sequence, zone_equipment_heating_or_no_load_sequence, zone_equipment_sequential_cooling_fraction_schedule_name, zone_equipment_sequential_heating_fraction_schedule_name}]
ZoneHVAC:EquipmentConnections
Specifies the HVAC equipment connections for a zone. Node names are specified for the zone air node, air inlet nodes, air exhaust nodes, and the air return node. A zone equipment list is referenced which lists all HVAC equipment connected to the zone.

Fields

zone_name [string]
zone_conditioning_equipment_list_name [string]
zone_air_inlet_node_or_nodelist_name [string]
zone_air_exhaust_node_or_nodelist_name [string]
zone_air_node_name [string]
zone_return_air_node_or_nodelist_name [string]
zone_return_air_node_1_flow_rate_fraction_schedule_name [string]
zone_return_air_node_1_flow_rate_basis_node_or_nodelist_name [string]
"""
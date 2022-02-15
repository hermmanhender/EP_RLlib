"""
Air Distribution
"""
"""
AirLoopHVAC
Defines a central forced air system.

Fields

controller_list_name [string]
availability_manager_list_name [string]
design_supply_air_flow_rate [unknown field type] (Default: 0.0)
branch_list_name [string]
connector_list_name [string]
supply_side_inlet_node_name [string]
demand_side_outlet_node_name [string]
demand_side_inlet_node_names [string]
supply_side_outlet_node_names [string]
design_return_air_flow_fraction_of_supply_air_flow [number] (Default: 1.0)
AirLoopHVAC:OutdoorAirSystem:EquipmentList
List equipment in simulation order

Fields

component_1_object_type [string]
component_1_name [string]
component_2_object_type [string]
component_2_name [string]
component_3_object_type [string]
component_3_name [string]
component_4_object_type [string]
component_4_name [string]
component_5_object_type [string]
component_5_name [string]
component_6_object_type [string]
component_6_name [string]
component_7_object_type [string]
component_7_name [string]
component_8_object_type [string]
component_8_name [string]
component_9_object_type [string]
component_9_name [string]
AirLoopHVAC:OutdoorAirSystem
Outdoor air subsystem for an AirLoopHVAC. Includes an outdoor air mixing box and optional outdoor air conditioning equipment such as heat recovery, preheat, and precool coils. From the perspective of the primary air loop the outdoor air system is treated as a single component.

Fields

controller_list_name [string]
outdoor_air_equipment_list_name [string]
OutdoorAir:Mixer
Outdoor air mixer. Node names cannot be duplicated within a single OutdoorAir:Mixer object or across all outdoor air mixers.

Fields

mixed_air_node_name [string]
outdoor_air_stream_node_name [string]
relief_air_stream_node_name [string]
return_air_stream_node_name [string]
AirLoopHVAC:ZoneSplitter
Split one air stream into N outlet streams (currently 500 per air loop, but extensible). Node names cannot be duplicated within a single zone splitter (AirLoopHVAC:ZoneSplitter) list.

Fields

inlet_node_name [string]
nodes [Array of {outlet_node_name}]
AirLoopHVAC:SupplyPlenum
Connects 1 zone inlet air stream, through zone supply plenum, to one or more outlets. Node names cannot be duplicated within a single supply plenum list.

Fields

zone_name [string]
zone_node_name [string]
inlet_node_name [string]
nodes [Array of {outlet_node_name}]
AirLoopHVAC:SupplyPath
A supply path can only contain AirLoopHVAC:ZoneSplitter and AirLoopHVAC:SupplyPlenum objects which may be in series or parallel.

Fields

supply_air_path_inlet_node_name [string]
components [Array of {component_object_type, component_name}]
AirLoopHVAC:ZoneMixer
Mix N inlet air streams into one (currently 500 per air loop, but extensible). Node names cannot be duplicated within a single zone mixer (AirLoopHVAC:ZoneMixer) list.

Fields

outlet_node_name [string]
nodes [Array of {inlet_node_name}]
AirLoopHVAC:ReturnPlenum
Connects N zone inlet air streams, through zone return plenum, to outlet (currently 500 per air loop) Node names cannot be duplicated within a single plenum list.

Fields

zone_name [string]
zone_node_name [string]
outlet_node_name [string]
induced_air_outlet_node_or_nodelist_name [string]
nodes [Array of {inlet_node_name}]
AirLoopHVAC:ReturnPath
A return air path can only contain one AirLoopHVAC:ZoneMixer and one or more AirLoopHVAC:ReturnPlenum objects.

Fields

return_air_path_outlet_node_name [string]
components [Array of {component_object_type, component_name}]
AirLoopHVAC:DedicatedOutdoorAirSystem
Defines a central forced air system to provide dedicated outdoor air to multiple AirLoopHVACs.

Fields

airloophvac_outdoorairsystem_name [string]
availability_schedule_name [string]
airloophvac_mixer_name [string]
airloophvac_splitter_name [string]
preheat_design_temperature [number]
preheat_design_humidity_ratio [number]
precool_design_temperature [number]
precool_design_humidity_ratio [number]
number_of_airloophvac [number]
airloophvacs [Array of {airloophvac_name}]
AirLoopHVAC:Mixer
Mix N inlet air streams from Relief Air Stream Node in OutdoorAir:Mixer objects served by AirLoopHVAC objects listed in AirLoopHVAC:DedicatedOutdoorAirSystem into one (currently 10 as default, but extensible). Node names cannot be duplicated within a single mixer list.

Fields

outlet_node_name [string]
nodes [Array of {inlet_node_name}]
AirLoopHVAC:Splitter
Split one air stream from AirLoopHVAC:DedicatedOutdoorAirSystem outlet node into N outlet streams (currently 10 as default, but extensible). Node names should be Outdoor Air Stream Node Name in OutdoorAir:Mixer objects served by AirLoopHVAC objects listed in AirLoopHVAC:DedicatedOutdoorAirSystem.

Fields

inlet_node_name [string]
nodes [Array of {outlet_node_name}]
"""
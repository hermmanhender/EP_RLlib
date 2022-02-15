"""
# Water Systems
"""
"""
WaterUse:Equipment
A generalized object for simulating all water end uses. Hot and cold water uses are included, as well as controlled mixing of hot and cold water at the tap. The WaterUse:Equipment object can be used stand-alone, or coupled into a plant loop using the WaterUse:Connections object (see below). The WaterUse:Connections object allows water uses to be linked to WaterUse:Storage objects to store and draw reclaimed water. The object can also simulate drainwater heat recovery.

Fields

end_use_subcategory [string] (Default: General)
peak_flow_rate [number]
flow_rate_fraction_schedule_name [string]
target_temperature_schedule_name [string]
hot_water_supply_temperature_schedule_name [string]
cold_water_supply_temperature_schedule_name [string]
zone_name [string]
sensible_fraction_schedule_name [string]
latent_fraction_schedule_name [string]
WaterUse:Connections
A subsystem that groups together multiple WaterUse:Equipment components. As its name suggests, the object provides connections that are shared by these components, including: 1. Inlet node and outlet node connections to a plant loop 2. Connections to WaterUse:Storage objects to store and draw reclaimed water 3. Internal connections to simulate drainwater heat recovery.

Fields

inlet_node_name [string]
outlet_node_name [string]
supply_water_storage_tank_name [string]
reclamation_water_storage_tank_name [string]
hot_water_supply_temperature_schedule_name [string]
cold_water_supply_temperature_schedule_name [string]
drain_water_heat_exchanger_type [string] (Default: None)
drain_water_heat_exchanger_destination [string] (Default: Plant)
drain_water_heat_exchanger_u_factor_times_area [number]
connections [Array of {water_use_equipment_name}]
WaterUse:Storage
A water storage tank. If the building model is to include any on-site water collection, wells, or storing and reuse of graywater, then a WaterUse:Storage object is needed. Each WaterUse:Storage can serve as a central node and make connections to numerous sources of supply or numerous components with demand. If a maximum capacity is not specified, the tank is assumed to have unlimited capacity.

Fields

water_quality_subcategory [string]
maximum_capacity [number]
initial_volume [number]
design_in_flow_rate [number]
design_out_flow_rate [number]
overflow_destination [string]
type_of_supply_controlled_by_float_valve [string]
float_valve_on_capacity [number]
float_valve_off_capacity [number]
backup_mains_capacity [number]
other_tank_name [string]
water_thermal_mode [string]
water_temperature_schedule_name [string]
ambient_temperature_indicator [string]
ambient_temperature_schedule_name [string]
zone_name [string]
tank_surface_area [number]
tank_u_value [number]
tank_outside_surface_material_name [string]
WaterUse:Well
Simulates on-site water supply from a well. Well water is pumped out of the ground into a WaterUse:Storage. The operation of the ground water well is controlled by the associated WaterUse:Storage which is assumed to be operated as a vented cistern with no pressure tank.

Fields

storage_tank_name [string]
pump_depth [number]
pump_rated_flow_rate [number]
pump_rated_head [number]
pump_rated_power_consumption [number]
pump_efficiency [number]
well_recovery_rate [number]
nominal_well_storage_volume [number]
water_table_depth_mode [string]
water_table_depth [number]
water_table_depth_schedule_name [string]
WaterUse:RainCollector
Used for harvesting rainwater falling on building surfaces. The rainwater is sent to a WaterUse:Storage object. In order to use this object it is necessary to also include a Site:Precipitation object to describe the rates of rainfall.

Fields

storage_tank_name [string]
loss_factor_mode [string]
collection_loss_factor [number]
collection_loss_factor_schedule_name [string]
maximum_collection_rate [number]
surfaces [Array of {collection_surface_name}]
"""
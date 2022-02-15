"""
Evaporative Coolers
"""
"""
EvaporativeCooler:Direct:CelDekPad
Direct evaporative cooler with rigid media evaporative pad and recirculating water pump. This model has no controls other than its availability schedule.

Fields

availability_schedule_name [string]
direct_pad_area [unknown field type] (Default: Autosize)
direct_pad_depth [unknown field type] (Default: Autosize)
recirculating_water_pump_power_consumption [number]
air_inlet_node_name [string]
air_outlet_node_name [string]
control_type [string]
water_supply_storage_tank_name [string]
EvaporativeCooler:Indirect:CelDekPad
Indirect evaporative cooler with rigid media evaporative pad, recirculating water pump, and secondary air fan. This model has no controls other than its availability schedule.

Fields

availability_schedule_name [string]
direct_pad_area [unknown field type] (Default: Autosize)
direct_pad_depth [unknown field type] (Default: Autosize)
recirculating_water_pump_power_consumption [number]
secondary_air_fan_flow_rate [number]
secondary_air_fan_total_efficiency [number]
secondary_air_fan_delta_pressure [number]
indirect_heat_exchanger_effectiveness [number]
primary_air_inlet_node_name [string]
primary_air_outlet_node_name [string]
control_type [string]
water_supply_storage_tank_name [string]
secondary_air_inlet_node_name [string]
EvaporativeCooler:Indirect:WetCoil
Indirect evaporative cooler with wetted coil, recirculating water pump, and secondary air fan. This model has no controls other than its availability schedule.

Fields

availability_schedule_name [string]
coil_maximum_efficiency [number]
coil_flow_ratio [number]
recirculating_water_pump_power_consumption [number]
secondary_air_fan_flow_rate [number]
secondary_air_fan_total_efficiency [number]
secondary_air_fan_delta_pressure [number]
primary_air_inlet_node_name [string]
primary_air_outlet_node_name [string]
control_type [string]
water_supply_storage_tank_name [string]
secondary_air_inlet_node_name [string]
EvaporativeCooler:Indirect:ResearchSpecial
Indirect evaporative cooler with user-specified effectiveness (can represent rigid pad or wetted coil), recirculating water pump, and secondary air fan. This model is controlled to meet the primary air outlet temperature setpoint.

Fields

availability_schedule_name [string]
cooler_wetbulb_design_effectiveness [number]
wetbulb_effectiveness_flow_ratio_modifier_curve_name [string]
cooler_drybulb_design_effectiveness [number]
drybulb_effectiveness_flow_ratio_modifier_curve_name [string]
recirculating_water_pump_design_power [unknown field type] (Default: Autosize)
water_pump_power_sizing_factor [number] (Default: 90.0)
water_pump_power_modifier_curve_name [string]
secondary_air_design_flow_rate [unknown field type] (Default: Autosize)
secondary_air_flow_scaling_factor [number] (Default: 1.0)
secondary_air_fan_design_power [unknown field type] (Default: Autosize)
secondary_air_fan_sizing_specific_power [number] (Default: 250.0)
secondary_air_fan_power_modifier_curve_name [string]
primary_air_inlet_node_name [string]
primary_air_outlet_node_name [string]
primary_air_design_flow_rate [unknown field type] (Default: Autosize)
dewpoint_effectiveness_factor [number]
secondary_air_inlet_node_name [string]
secondary_air_outlet_node_name [string]
sensor_node_name [string]
relief_air_inlet_node_name [string]
water_supply_storage_tank_name [string]
drift_loss_fraction [number] (Default: 0.0)
blowdown_concentration_ratio [number]
evaporative_operation_minimum_limit_secondary_air_drybulb_temperature [number]
evaporative_operation_maximum_limit_outdoor_wetbulb_temperature [number]
dry_operation_maximum_limit_outdoor_drybulb_temperature [number]
EvaporativeCooler:Direct:ResearchSpecial
Direct evaporative cooler with user-specified effectiveness (can represent rigid pad or similar media), and recirculating water pump, and secondary air fan. This model is controlled to meet the primary air outlet temperature setpoint.

Fields

availability_schedule_name [string]
cooler_design_effectiveness [number]
effectiveness_flow_ratio_modifier_curve_name [string]
primary_air_design_flow_rate [unknown field type] (Default: Autosize)
recirculating_water_pump_design_power [unknown field type] (Default: Autosize)
water_pump_power_sizing_factor [number] (Default: 90.0)
water_pump_power_modifier_curve_name [string]
air_inlet_node_name [string]
air_outlet_node_name [string]
sensor_node_name [string]
water_supply_storage_tank_name [string]
drift_loss_fraction [number]
blowdown_concentration_ratio [number]
evaporative_operation_minimum_drybulb_temperature [number]
evaporative_operation_maximum_limit_wetbulb_temperature [number]
evaporative_operation_maximum_limit_drybulb_temperature [number]
"""
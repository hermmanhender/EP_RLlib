"""
# Water Heaters and Thermal Storage
"""
"""
WaterHeater:Mixed
Water heater with well-mixed, single-node water tank. May be used to model a tankless water heater (small tank volume), a hot water storage tank (zero heater capacity), or a heat pump water heater (see WaterHeater:HeatPump:PumpedCondenser.)

Fields

tank_volume [unknown field type] (Default: 0.0)
setpoint_temperature_schedule_name [string]
deadband_temperature_difference [number] (Default: 0.0)
maximum_temperature_limit [number]
heater_control_type [string] (Default: Cycle)
heater_maximum_capacity [unknown field type]
heater_minimum_capacity [number]
heater_ignition_minimum_flow_rate [number] (Default: 0.0)
heater_ignition_delay [number] (Default: 0.0)
heater_fuel_type [string]
heater_thermal_efficiency [number]
part_load_factor_curve_name [string]
off_cycle_parasitic_fuel_consumption_rate [number] (Default: 0.0)
off_cycle_parasitic_fuel_type [string]
off_cycle_parasitic_heat_fraction_to_tank [number] (Default: 0.0)
on_cycle_parasitic_fuel_consumption_rate [number] (Default: 0.0)
on_cycle_parasitic_fuel_type [string]
on_cycle_parasitic_heat_fraction_to_tank [number] (Default: 0.0)
ambient_temperature_indicator [string]
ambient_temperature_schedule_name [string]
ambient_temperature_zone_name [string]
ambient_temperature_outdoor_air_node_name [string]
off_cycle_loss_coefficient_to_ambient_temperature [number]
off_cycle_loss_fraction_to_zone [number] (Default: 1.0)
on_cycle_loss_coefficient_to_ambient_temperature [number]
on_cycle_loss_fraction_to_zone [number] (Default: 1.0)
peak_use_flow_rate [number]
use_flow_rate_fraction_schedule_name [string]
cold_water_supply_temperature_schedule_name [string]
use_side_inlet_node_name [string]
use_side_outlet_node_name [string]
use_side_effectiveness [number] (Default: 1.0)
source_side_inlet_node_name [string]
source_side_outlet_node_name [string]
source_side_effectiveness [number] (Default: 1.0)
use_side_design_flow_rate [unknown field type] (Default: Autosize)
source_side_design_flow_rate [unknown field type] (Default: Autosize)
indirect_water_heating_recovery_time [number] (Default: 1.5)
source_side_flow_control_mode [string] (Default: IndirectHeatPrimarySetpoint)
indirect_alternate_setpoint_temperature_schedule_name [string]
end_use_subcategory [string] (Default: General)
WaterHeater:Stratified
Water heater with stratified, multi-node water tank. May be used to model a tankless water heater (small tank volume), a hot water storage tank (zero heater capacity), or a heat pump water heater (see WaterHeater:HeatPump:*.)

Fields

end_use_subcategory [string] (Default: General)
tank_volume [unknown field type]
tank_height [unknown field type]
tank_shape [string] (Default: VerticalCylinder)
tank_perimeter [number]
maximum_temperature_limit [number]
heater_priority_control [string] (Default: MasterSlave)
heater_1_setpoint_temperature_schedule_name [string]
heater_1_deadband_temperature_difference [number] (Default: 0.0)
heater_1_capacity [unknown field type]
heater_1_height [number]
heater_2_setpoint_temperature_schedule_name [string]
heater_2_deadband_temperature_difference [number] (Default: 0.0)
heater_2_capacity [number]
heater_2_height [number]
heater_fuel_type [string]
heater_thermal_efficiency [number]
off_cycle_parasitic_fuel_consumption_rate [number] (Default: 0.0)
off_cycle_parasitic_fuel_type [string]
off_cycle_parasitic_heat_fraction_to_tank [number] (Default: 0.0)
off_cycle_parasitic_height [number] (Default: 0.0)
on_cycle_parasitic_fuel_consumption_rate [number] (Default: 0.0)
on_cycle_parasitic_fuel_type [string]
on_cycle_parasitic_heat_fraction_to_tank [number] (Default: 0.0)
on_cycle_parasitic_height [number] (Default: 0.0)
ambient_temperature_indicator [string]
ambient_temperature_schedule_name [string]
ambient_temperature_zone_name [string]
ambient_temperature_outdoor_air_node_name [string]
uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature [number]
skin_loss_fraction_to_zone [number] (Default: 1.0)
off_cycle_flue_loss_coefficient_to_ambient_temperature [number]
off_cycle_flue_loss_fraction_to_zone [number] (Default: 1.0)
peak_use_flow_rate [number]
use_flow_rate_fraction_schedule_name [string]
cold_water_supply_temperature_schedule_name [string]
use_side_inlet_node_name [string]
use_side_outlet_node_name [string]
use_side_effectiveness [number] (Default: 1.0)
use_side_inlet_height [number] (Default: 0.0)
use_side_outlet_height [unknown field type] (Default: Autocalculate)
source_side_inlet_node_name [string]
source_side_outlet_node_name [string]
source_side_effectiveness [number] (Default: 1.0)
source_side_inlet_height [unknown field type] (Default: Autocalculate)
source_side_outlet_height [number] (Default: 0.0)
inlet_mode [string] (Default: Fixed)
use_side_design_flow_rate [unknown field type] (Default: Autosize)
source_side_design_flow_rate [unknown field type] (Default: Autosize)
indirect_water_heating_recovery_time [number] (Default: 1.5)
number_of_nodes [number] (Default: 1.0)
additional_destratification_conductivity [number] (Default: 0.0)
node_1_additional_loss_coefficient [number] (Default: 0.0)
node_2_additional_loss_coefficient [number] (Default: 0.0)
node_3_additional_loss_coefficient [number] (Default: 0.0)
node_4_additional_loss_coefficient [number] (Default: 0.0)
node_5_additional_loss_coefficient [number] (Default: 0.0)
node_6_additional_loss_coefficient [number] (Default: 0.0)
node_7_additional_loss_coefficient [number] (Default: 0.0)
node_8_additional_loss_coefficient [number] (Default: 0.0)
node_9_additional_loss_coefficient [number] (Default: 0.0)
node_10_additional_loss_coefficient [number] (Default: 0.0)
node_11_additional_loss_coefficient [number] (Default: 0.0)
node_12_additional_loss_coefficient [number] (Default: 0.0)
source_side_flow_control_mode [string] (Default: IndirectHeatPrimarySetpoint)
indirect_alternate_setpoint_temperature_schedule_name [string]
WaterHeater:Sizing
This input object is used with WaterHeater:Mixed or with WaterHeater:Stratified to autosize tank volume and heater capacity This object is not needed if water heaters are not autosized.

Fields

waterheater_name [string]
design_mode [string]
time_storage_can_meet_peak_draw [number]
time_for_tank_recovery [number]
nominal_tank_volume_for_autosizing_plant_connections [number]
number_of_bedrooms [number]
number_of_bathrooms [number]
storage_capacity_per_person [number]
recovery_capacity_per_person [number]
storage_capacity_per_floor_area [number]
recovery_capacity_per_floor_area [number]
number_of_units [number]
storage_capacity_per_unit [number]
recovery_capacity_perunit [number]
storage_capacity_per_collector_area [number]
height_aspect_ratio [number]
WaterHeater:HeatPump:PumpedCondenser
This object models an air-source heat pump for water heating where the water is pumped out of the tank, through a heating coil and returned to the tank. For wrapped condenser HPWHs, see WaterHeater:HeatPump:WrappedCondenser. WaterHeater:HeatPump:PumpedCondenser is a compound object that references other component objects - Coil:WaterHeating:AirToWaterHeatPump:*, Fan:OnOff, WaterHeater:Mixed or WaterHeater:Stratified

Fields

availability_schedule_name [string]
compressor_setpoint_temperature_schedule_name [string]
dead_band_temperature_difference [number] (Default: 5.0)
condenser_water_inlet_node_name [string]
condenser_water_outlet_node_name [string]
condenser_water_flow_rate [unknown field type]
evaporator_air_flow_rate [unknown field type]
inlet_air_configuration [string]
air_inlet_node_name [string]
air_outlet_node_name [string]
outdoor_air_node_name [string]
exhaust_air_node_name [string]
inlet_air_temperature_schedule_name [string]
inlet_air_humidity_schedule_name [string]
inlet_air_zone_name [string]
tank_object_type [string] (Default: WaterHeater:Mixed)
tank_name [string]
tank_use_side_inlet_node_name [string]
tank_use_side_outlet_node_name [string]
dx_coil_object_type [string] (Default: Coil:WaterHeating:AirToWaterHeatPump:Pumped)
dx_coil_name [string]
minimum_inlet_air_temperature_for_compressor_operation [number] (Default: 10.0)
maximum_inlet_air_temperature_for_compressor_operation [number] (Default: 48.88888888889)
compressor_location [string]
compressor_ambient_temperature_schedule_name [string]
fan_object_type [string] (Default: Fan:OnOff)
fan_name [string]
fan_placement [string] (Default: DrawThrough)
on_cycle_parasitic_electric_load [number] (Default: 0.0)
off_cycle_parasitic_electric_load [number] (Default: 0.0)
parasitic_heat_rejection_location [string] (Default: Outdoors)
inlet_air_mixer_node_name [string]
outlet_air_splitter_node_name [string]
inlet_air_mixer_schedule_name [string]
tank_element_control_logic [string] (Default: Simultaneous)
control_sensor_1_height_in_stratified_tank [number]
control_sensor_1_weight [number] (Default: 1.0)
control_sensor_2_height_in_stratified_tank [number]
WaterHeater:HeatPump:WrappedCondenser
This object models an air-source heat pump for water heating where the heating coil is wrapped around the tank, which is typical of residential HPWHs. For pumped condenser HPWHs, see WaterHeater:HeatPump:PumpedCondenser. WaterHeater:HeatPump:WrappedCondenser is a compound object that references other component objects - Coil:WaterHeating:AirToWaterHeatPump:Pumped, Fan:OnOff, WaterHeater:Mixed

Fields

availability_schedule_name [string]
compressor_setpoint_temperature_schedule_name [string]
dead_band_temperature_difference [number] (Default: 5.0)
condenser_bottom_location [number] (Default: 0.0)
condenser_top_location [number]
evaporator_air_flow_rate [unknown field type]
inlet_air_configuration [string]
air_inlet_node_name [string]
air_outlet_node_name [string]
outdoor_air_node_name [string]
exhaust_air_node_name [string]
inlet_air_temperature_schedule_name [string]
inlet_air_humidity_schedule_name [string]
inlet_air_zone_name [string]
tank_object_type [string] (Default: WaterHeater:Stratified)
tank_name [string]
tank_use_side_inlet_node_name [string]
tank_use_side_outlet_node_name [string]
dx_coil_object_type [string] (Default: Coil:WaterHeating:AirToWaterHeatPump:Wrapped)
dx_coil_name [string]
minimum_inlet_air_temperature_for_compressor_operation [number] (Default: 10.0)
maximum_inlet_air_temperature_for_compressor_operation [number] (Default: 48.88888888889)
compressor_location [string]
compressor_ambient_temperature_schedule_name [string]
fan_object_type [string] (Default: Fan:OnOff)
fan_name [string]
fan_placement [string] (Default: DrawThrough)
on_cycle_parasitic_electric_load [number] (Default: 0.0)
off_cycle_parasitic_electric_load [number] (Default: 0.0)
parasitic_heat_rejection_location [string] (Default: Outdoors)
inlet_air_mixer_node_name [string]
outlet_air_splitter_node_name [string]
inlet_air_mixer_schedule_name [string]
tank_element_control_logic [string] (Default: Simultaneous)
control_sensor_1_height_in_stratified_tank [number]
control_sensor_1_weight [number] (Default: 1.0)
control_sensor_2_height_in_stratified_tank [number]
ThermalStorage:Ice:Simple
This ice storage model is a simplified model It requires a setpoint placed on the Chilled Water Side Outlet Node It should be placed in the chilled water supply side outlet branch followed by a pipe. Use the PlantEquipmentOperation:ComponentSetpoint plant operation scheme.

Fields

ice_storage_type [string]
capacity [number]
inlet_node_name [string]
outlet_node_name [string]
ThermalStorage:Ice:Detailed
This input syntax is intended to describe a thermal storage system that includes smaller containers filled with water that are placed in a larger tank or series of tanks. The model uses polynomial equations to describe the system performance.

Fields

availability_schedule_name [string]
capacity [number]
inlet_node_name [string]
outlet_node_name [string]
discharging_curve_variable_specifications [string]
discharging_curve_name [string]
charging_curve_variable_specifications [string]
charging_curve_name [string]
timestep_of_the_curve_data [number]
parasitic_electric_load_during_discharging [number]
parasitic_electric_load_during_charging [number]
tank_loss_coefficient [number]
freezing_temperature_of_storage_medium [number] (Default: 0.0)
thaw_process_indicator [string] (Default: OutsideMelt)
ThermalStorage:ChilledWater:Mixed
Chilled water storage with a well-mixed, single-node tank. The chilled water is “used” by drawing from the “Use Side” of the water tank. The tank is indirectly charged by circulating cold water through the “Source Side” of the water tank.

Fields

tank_volume [number] (Default: 0.1)
setpoint_temperature_schedule_name [string]
deadband_temperature_difference [number] (Default: 0.5)
minimum_temperature_limit [number]
nominal_cooling_capacity [number]
ambient_temperature_indicator [string]
ambient_temperature_schedule_name [string]
ambient_temperature_zone_name [string]
ambient_temperature_outdoor_air_node_name [string]
heat_gain_coefficient_from_ambient_temperature [number]
use_side_inlet_node_name [string]
use_side_outlet_node_name [string]
use_side_heat_transfer_effectiveness [number] (Default: 1.0)
use_side_availability_schedule_name [string]
use_side_design_flow_rate [unknown field type] (Default: Autosize)
source_side_inlet_node_name [string]
source_side_outlet_node_name [string]
source_side_heat_transfer_effectiveness [number] (Default: 1.0)
source_side_availability_schedule_name [string]
source_side_design_flow_rate [unknown field type] (Default: Autosize)
tank_recovery_time [number] (Default: 4.0)
ThermalStorage:ChilledWater:Stratified
Chilled water storage with a stratified, multi-node tank. The chilled water is “used” by drawing from the “Use Side” of the water tank. The tank is indirectly charged by circulating cold water through the “Source Side” of the water tank.

Fields

tank_volume [number]
tank_height [number]
tank_shape [string] (Default: VerticalCylinder)
tank_perimeter [number]
setpoint_temperature_schedule_name [string]
deadband_temperature_difference [number] (Default: 0.0)
temperature_sensor_height [number]
minimum_temperature_limit [number]
nominal_cooling_capacity [number]
ambient_temperature_indicator [string]
ambient_temperature_schedule_name [string]
ambient_temperature_zone_name [string]
ambient_temperature_outdoor_air_node_name [string]
uniform_skin_loss_coefficient_per_unit_area_to_ambient_temperature [number]
use_side_inlet_node_name [string]
use_side_outlet_node_name [string]
use_side_heat_transfer_effectiveness [number] (Default: 1.0)
use_side_availability_schedule_name [string]
use_side_inlet_height [unknown field type] (Default: Autocalculate)
use_side_outlet_height [number] (Default: 0.0)
use_side_design_flow_rate [unknown field type] (Default: Autosize)
source_side_inlet_node_name [string]
source_side_outlet_node_name [string]
source_side_heat_transfer_effectiveness [number] (Default: 1.0)
source_side_availability_schedule_name [string]
source_side_inlet_height [number] (Default: 0.0)
source_side_outlet_height [unknown field type] (Default: Autocalculate)
source_side_design_flow_rate [unknown field type] (Default: Autosize)
tank_recovery_time [number] (Default: 4.0)
inlet_mode [string] (Default: Fixed)
number_of_nodes [number] (Default: 1.0)
additional_destratification_conductivity [number] (Default: 0.0)
node_1_additional_loss_coefficient [number] (Default: 0.0)
node_2_additional_loss_coefficient [number] (Default: 0.0)
node_3_additional_loss_coefficient [number] (Default: 0.0)
node_4_additional_loss_coefficient [number] (Default: 0.0)
node_5_additional_loss_coefficient [number] (Default: 0.0)
node_6_additional_loss_coefficient [number] (Default: 0.0)
node_7_additional_loss_coefficient [number] (Default: 0.0)
node_8_additional_loss_coefficient [number] (Default: 0.0)
node_9_additional_loss_coefficient [number] (Default: 0.0)
node_10_additional_loss_coefficient [number] (Default: 0.0)
"""
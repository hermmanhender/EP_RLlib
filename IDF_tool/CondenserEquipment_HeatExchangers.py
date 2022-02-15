"""
Condenser Equipment and Heat Exchangers
"""
"""
CoolingTower:SingleSpeed
This tower model is based on Merkel's theory, which is also the basis for the tower model in ASHRAE's HVAC1 Toolkit. The open wet cooling tower is modeled as a counter flow heat exchanger with a single-speed fan drawing air through the tower (induced-draft configuration). Added fluid bypass as an additional capacity control. 8/2008. For a multi-cell tower, the capacity and air/water flow rate inputs are for the entire tower.

Fields

water_inlet_node_name [string]
water_outlet_node_name [string]
design_water_flow_rate [unknown field type]
design_air_flow_rate [unknown field type]
design_fan_power [unknown field type]
design_u_factor_times_area_value [unknown field type]
free_convection_regime_air_flow_rate [unknown field type] (Default: 0.0)
free_convection_regime_air_flow_rate_sizing_factor [number] (Default: 0.1)
free_convection_regime_u_factor_times_area_value [unknown field type] (Default: 0.0)
free_convection_u_factor_times_area_value_sizing_factor [number] (Default: 0.1)
performance_input_method [string] (Default: UFactorTimesAreaAndDesignWaterFlowRate)
heat_rejection_capacity_and_nominal_capacity_sizing_ratio [number] (Default: 1.25)
nominal_capacity [number]
free_convection_capacity [unknown field type]
free_convection_nominal_capacity_sizing_factor [number] (Default: 0.1)
design_inlet_air_dry_bulb_temperature [number] (Default: 35.0)
design_inlet_air_wet_bulb_temperature [number] (Default: 25.6)
design_approach_temperature [unknown field type] (Default: Autosize)
design_range_temperature [unknown field type] (Default: Autosize)
basin_heater_capacity [number] (Default: 0.0)
basin_heater_setpoint_temperature [number] (Default: 2.0)
basin_heater_operating_schedule_name [string]
evaporation_loss_mode [string]
evaporation_loss_factor [number] (Default: 0.2)
drift_loss_percent [number] (Default: 0.008)
blowdown_calculation_mode [string]
blowdown_concentration_ratio [number] (Default: 3.0)
blowdown_makeup_water_usage_schedule_name [string]
supply_water_storage_tank_name [string]
outdoor_air_inlet_node_name [string]
capacity_control [string] (Default: FanCycling)
number_of_cells [number] (Default: 1.0)
cell_control [string] (Default: MinimalCell)
cell_minimum_water_flow_rate_fraction [number] (Default: 0.33)
cell_maximum_water_flow_rate_fraction [number] (Default: 2.5)
sizing_factor [number] (Default: 1.0)
end_use_subcategory [string] (Default: General)
CoolingTower:TwoSpeed
This tower model is based on Merkel's theory, which is also the basis for the tower model in ASHRAE's HVAC1 Toolkit. The open wet cooling tower is modeled as a counter flow heat exchanger with a two-speed fan drawing air through the tower (induced-draft configuration). For a multi-cell tower, the capacity and air/water flow rate inputs are for the entire tower.

Fields

water_inlet_node_name [string]
water_outlet_node_name [string]
design_water_flow_rate [unknown field type]
high_fan_speed_air_flow_rate [unknown field type]
high_fan_speed_fan_power [unknown field type]
high_fan_speed_u_factor_times_area_value [unknown field type]
low_fan_speed_air_flow_rate [unknown field type]
low_fan_speed_air_flow_rate_sizing_factor [number] (Default: 0.5)
low_fan_speed_fan_power [unknown field type]
low_fan_speed_fan_power_sizing_factor [number] (Default: 0.16)
low_fan_speed_u_factor_times_area_value [unknown field type]
low_fan_speed_u_factor_times_area_sizing_factor [number] (Default: 0.6)
free_convection_regime_air_flow_rate [unknown field type] (Default: 0.0)
free_convection_regime_air_flow_rate_sizing_factor [number] (Default: 0.1)
free_convection_regime_u_factor_times_area_value [unknown field type] (Default: 0.0)
free_convection_u_factor_times_area_value_sizing_factor [number] (Default: 0.1)
performance_input_method [string] (Default: UFactorTimesAreaAndDesignWaterFlowRate)
heat_rejection_capacity_and_nominal_capacity_sizing_ratio [number] (Default: 1.25)
high_speed_nominal_capacity [number]
low_speed_nominal_capacity [unknown field type]
low_speed_nominal_capacity_sizing_factor [number] (Default: 0.5)
free_convection_nominal_capacity [unknown field type]
free_convection_nominal_capacity_sizing_factor [number] (Default: 0.1)
design_inlet_air_dry_bulb_temperature [number] (Default: 35.0)
design_inlet_air_wet_bulb_temperature [number] (Default: 25.6)
design_approach_temperature [unknown field type] (Default: Autosize)
design_range_temperature [unknown field type] (Default: Autosize)
basin_heater_capacity [number] (Default: 0.0)
basin_heater_setpoint_temperature [number] (Default: 2.0)
basin_heater_operating_schedule_name [string]
evaporation_loss_mode [string]
evaporation_loss_factor [number] (Default: 0.2)
drift_loss_percent [number] (Default: 0.008)
blowdown_calculation_mode [string]
blowdown_concentration_ratio [number] (Default: 3.0)
blowdown_makeup_water_usage_schedule_name [string]
supply_water_storage_tank_name [string]
outdoor_air_inlet_node_name [string]
number_of_cells [number] (Default: 1.0)
cell_control [string] (Default: MinimalCell)
cell_minimum_water_flow_rate_fraction [number] (Default: 0.33)
cell_maximum_water_flow_rate_fraction [number] (Default: 2.5)
sizing_factor [number] (Default: 1.0)
end_use_subcategory [string] (Default: General)
CoolingTower:VariableSpeed:Merkel
This tower model is based on Merkel's theory, which is also the basis for the tower model in ASHRAE's HVAC1 Toolkit. The open wet cooling tower is modeled as a counter flow heat exchanger with a variable-speed fan drawing air through the tower (induced-draft configuration). For a multi-cell tower, the capacity and air/water flow rate inputs are for the entire tower.

Fields

water_inlet_node_name [string]
water_outlet_node_name [string]
performance_input_method [string] (Default: NominalCapacity)
heat_rejection_capacity_and_nominal_capacity_sizing_ratio [number] (Default: 1.25)
nominal_capacity [unknown field type]
free_convection_nominal_capacity [unknown field type]
free_convection_nominal_capacity_sizing_factor [number] (Default: 0.1)
design_water_flow_rate [unknown field type]
design_water_flow_rate_per_unit_of_nominal_capacity [number] (Default: 5.382e-08)
design_air_flow_rate [unknown field type]
design_air_flow_rate_per_unit_of_nominal_capacity [number] (Default: 2.76316e-05)
minimum_air_flow_rate_ratio [number] (Default: 0.2)
design_fan_power [unknown field type]
design_fan_power_per_unit_of_nominal_capacity [number] (Default: 0.0105)
fan_power_modifier_function_of_air_flow_rate_ratio_curve_name [string]
free_convection_regime_air_flow_rate [unknown field type] (Default: 0.0)
free_convection_regime_air_flow_rate_sizing_factor [number] (Default: 0.1)
design_air_flow_rate_u_factor_times_area_value [unknown field type]
free_convection_regime_u_factor_times_area_value [unknown field type] (Default: 0.0)
free_convection_u_factor_times_area_value_sizing_factor [number] (Default: 0.1)
u_factor_times_area_modifier_function_of_air_flow_ratio_curve_name [string]
u_factor_times_area_modifier_function_of_wetbulb_temperature_difference_curve_name [string]
u_factor_times_area_modifier_function_of_water_flow_ratio_curve_name [string]
design_inlet_air_dry_bulb_temperature [number] (Default: 35.0)
design_inlet_air_wet_bulb_temperature [number] (Default: 25.6)
design_approach_temperature [unknown field type] (Default: Autosize)
design_range_temperature [unknown field type] (Default: Autosize)
basin_heater_capacity [number] (Default: 0.0)
basin_heater_setpoint_temperature [number] (Default: 2.0)
basin_heater_operating_schedule_name [string]
evaporation_loss_mode [string]
evaporation_loss_factor [number] (Default: 0.2)
drift_loss_percent [number] (Default: 0.008)
blowdown_calculation_mode [string]
blowdown_concentration_ratio [number] (Default: 3.0)
blowdown_makeup_water_usage_schedule_name [string]
supply_water_storage_tank_name [string]
outdoor_air_inlet_node_name [string]
number_of_cells [number] (Default: 1.0)
cell_control [string] (Default: MinimalCell)
cell_minimum_water_flow_rate_fraction [number] (Default: 0.33)
cell_maximum_water_flow_rate_fraction [number] (Default: 2.5)
sizing_factor [number] (Default: 1.0)
end_use_subcategory [string] (Default: General)
CoolingTower:VariableSpeed
This open wet tower model is based on purely empirical algorithms derived from manufacturer's performance data or field measurements. The user can select from two existing algorithms (CoolTools or YorkCalc), or they can enter their own correlation for approach temperature by using a variable speed tower model coefficient object. For a multi-cell tower, the capacity and air/water flow rate inputs are for the entire tower.

Fields

water_inlet_node_name [string]
water_outlet_node_name [string]
model_type [string] (Default: YorkCalc)
model_coefficient_name [string]
design_inlet_air_wet_bulb_temperature [number] (Default: 25.6)
design_approach_temperature [number] (Default: 3.9)
design_range_temperature [number] (Default: 5.6)
design_water_flow_rate [unknown field type]
design_air_flow_rate [unknown field type]
design_fan_power [unknown field type]
fan_power_ratio_function_of_air_flow_rate_ratio_curve_name [string]
minimum_air_flow_rate_ratio [number] (Default: 0.2)
fraction_of_tower_capacity_in_free_convection_regime [number] (Default: 0.125)
basin_heater_capacity [number] (Default: 0.0)
basin_heater_setpoint_temperature [number] (Default: 2.0)
basin_heater_operating_schedule_name [string]
evaporation_loss_mode [string]
evaporation_loss_factor [number] (Default: 0.2)
drift_loss_percent [number]
blowdown_calculation_mode [string]
blowdown_concentration_ratio [number] (Default: 3.0)
blowdown_makeup_water_usage_schedule_name [string]
supply_water_storage_tank_name [string]
outdoor_air_inlet_node_name [string]
number_of_cells [number] (Default: 1.0)
cell_control [string] (Default: MinimalCell)
cell_minimum_water_flow_rate_fraction [number] (Default: 0.33)
cell_maximum_water_flow_rate_fraction [number] (Default: 2.5)
sizing_factor [number] (Default: 1.0)
end_use_subcategory [string] (Default: General)
CoolingTowerPerformance:CoolTools
This object is used to define coefficients for the approach temperature correlation for a variable speed cooling tower when tower Model Type is specified as CoolToolsUserDefined in the object CoolingTower:VariableSpeed.

Fields

minimum_inlet_air_wet_bulb_temperature [number]
maximum_inlet_air_wet_bulb_temperature [number]
minimum_range_temperature [number]
maximum_range_temperature [number]
minimum_approach_temperature [number]
maximum_approach_temperature [number]
minimum_water_flow_rate_ratio [number]
maximum_water_flow_rate_ratio [number]
coefficient_1 [number]
coefficient_2 [number]
coefficient_3 [number]
coefficient_4 [number]
coefficient_5 [number]
coefficient_6 [number]
coefficient_7 [number]
coefficient_8 [number]
coefficient_9 [number]
coefficient_10 [number]
coefficient_11 [number]
coefficient_12 [number]
coefficient_13 [number]
coefficient_14 [number]
coefficient_15 [number]
coefficient_16 [number]
coefficient_17 [number]
coefficient_18 [number]
coefficient_19 [number]
coefficient_20 [number]
coefficient_21 [number]
coefficient_22 [number]
coefficient_23 [number]
coefficient_24 [number]
coefficient_25 [number]
coefficient_26 [number]
coefficient_27 [number]
coefficient_28 [number]
coefficient_29 [number]
coefficient_30 [number]
coefficient_31 [number]
coefficient_32 [number]
coefficient_33 [number]
coefficient_34 [number]
coefficient_35 [number]
CoolingTowerPerformance:YorkCalc
This object is used to define coefficients for the approach temperature correlation for a variable speed cooling tower when tower Model Type is specified as YorkCalcUserDefined in the object CoolingTower:VariableSpeed.

Fields

minimum_inlet_air_wet_bulb_temperature [number]
maximum_inlet_air_wet_bulb_temperature [number]
minimum_range_temperature [number]
maximum_range_temperature [number]
minimum_approach_temperature [number]
maximum_approach_temperature [number]
minimum_water_flow_rate_ratio [number]
maximum_water_flow_rate_ratio [number]
maximum_liquid_to_gas_ratio [number]
coefficient_1 [number]
coefficient_2 [number]
coefficient_3 [number]
coefficient_4 [number]
coefficient_5 [number]
coefficient_6 [number]
coefficient_7 [number]
coefficient_8 [number]
coefficient_9 [number]
coefficient_10 [number]
coefficient_11 [number]
coefficient_12 [number]
coefficient_13 [number]
coefficient_14 [number]
coefficient_15 [number]
coefficient_16 [number]
coefficient_17 [number]
coefficient_18 [number]
coefficient_19 [number]
coefficient_20 [number]
coefficient_21 [number]
coefficient_22 [number]
coefficient_23 [number]
coefficient_24 [number]
coefficient_25 [number]
coefficient_26 [number]
coefficient_27 [number]
EvaporativeFluidCooler:SingleSpeed
This model is based on Merkel's theory, which is also the basis for the cooling tower model in EnergyPlus. The Evaporative fluid cooler is modeled as a counter flow heat exchanger.

Fields

water_inlet_node_name [string]
water_outlet_node_name [string]
design_air_flow_rate [unknown field type]
design_air_flow_rate_fan_power [unknown field type]
design_spray_water_flow_rate [number]
performance_input_method [string]
outdoor_air_inlet_node_name [string]
heat_rejection_capacity_and_nominal_capacity_sizing_ratio [number] (Default: 1.25)
standard_design_capacity [number]
design_air_flow_rate_u_factor_times_area_value [unknown field type]
design_water_flow_rate [unknown field type]
user_specified_design_capacity [number]
design_entering_water_temperature [number]
design_entering_air_temperature [number]
design_entering_air_wet_bulb_temperature [number]
capacity_control [string] (Default: FanCycling)
sizing_factor [number] (Default: 1.0)
evaporation_loss_mode [string] (Default: SaturatedExit)
evaporation_loss_factor [number]
drift_loss_percent [number] (Default: 0.008)
blowdown_calculation_mode [string] (Default: ConcentrationRatio)
blowdown_concentration_ratio [number] (Default: 3.0)
blowdown_makeup_water_usage_schedule_name [string]
supply_water_storage_tank_name [string]
EvaporativeFluidCooler:TwoSpeed
This model is based on Merkel's theory, which is also the basis for the cooling tower model in EnergyPlus. The Evaporative fluid cooler is modeled as a counter flow heat exchanger.

Fields

water_inlet_node_name [string]
water_outlet_node_name [string]
high_fan_speed_air_flow_rate [unknown field type]
high_fan_speed_fan_power [unknown field type]
low_fan_speed_air_flow_rate [unknown field type]
low_fan_speed_air_flow_rate_sizing_factor [number] (Default: 0.5)
low_fan_speed_fan_power [unknown field type]
low_fan_speed_fan_power_sizing_factor [number] (Default: 0.16)
design_spray_water_flow_rate [number]
performance_input_method [string]
outdoor_air_inlet_node_name [string]
heat_rejection_capacity_and_nominal_capacity_sizing_ratio [number] (Default: 1.25)
high_speed_standard_design_capacity [number]
low_speed_standard_design_capacity [unknown field type]
low_speed_standard_capacity_sizing_factor [number] (Default: 0.5)
high_fan_speed_u_factor_times_area_value [unknown field type]
low_fan_speed_u_factor_times_area_value [unknown field type]
low_fan_speed_u_factor_times_area_sizing_factor [number] (Default: 0.6)
design_water_flow_rate [unknown field type]
high_speed_user_specified_design_capacity [number]
low_speed_user_specified_design_capacity [unknown field type]
low_speed_user_specified_design_capacity_sizing_factor [number] (Default: 0.5)
design_entering_water_temperature [number]
design_entering_air_temperature [number]
design_entering_air_wet_bulb_temperature [number]
high_speed_sizing_factor [number] (Default: 1.0)
evaporation_loss_mode [string] (Default: SaturatedExit)
evaporation_loss_factor [number]
drift_loss_percent [number] (Default: 0.008)
blowdown_calculation_mode [string] (Default: ConcentrationRatio)
blowdown_concentration_ratio [number] (Default: 3.0)
blowdown_makeup_water_usage_schedule_name [string]
supply_water_storage_tank_name [string]
FluidCooler:SingleSpeed
The fluid cooler is modeled as a cross flow heat exchanger (both streams unmixed) with single-speed fans (induced draft configuration).

Fields

water_inlet_node_name [string]
water_outlet_node_name [string]
performance_input_method [string] (Default: NominalCapacity)
design_air_flow_rate_u_factor_times_area_value [unknown field type]
nominal_capacity [number]
design_entering_water_temperature [number]
design_entering_air_temperature [number]
design_entering_air_wetbulb_temperature [number]
design_water_flow_rate [unknown field type]
design_air_flow_rate [unknown field type]
design_air_flow_rate_fan_power [unknown field type]
outdoor_air_inlet_node_name [string]
FluidCooler:TwoSpeed
The fluid cooler is modeled as a cross flow heat exchanger (both streams unmixed) with two-speed fans (induced draft configuration).

Fields

water_inlet_node_name [string]
water_outlet_node_name [string]
performance_input_method [string] (Default: NominalCapacity)
high_fan_speed_u_factor_times_area_value [unknown field type]
low_fan_speed_u_factor_times_area_value [unknown field type]
low_fan_speed_u_factor_times_area_sizing_factor [number] (Default: 0.6)
high_speed_nominal_capacity [number]
low_speed_nominal_capacity [unknown field type]
low_speed_nominal_capacity_sizing_factor [number] (Default: 0.5)
design_entering_water_temperature [number]
design_entering_air_temperature [number]
design_entering_air_wet_bulb_temperature [number]
design_water_flow_rate [unknown field type]
high_fan_speed_air_flow_rate [unknown field type]
high_fan_speed_fan_power [unknown field type]
low_fan_speed_air_flow_rate [unknown field type]
low_fan_speed_air_flow_rate_sizing_factor [number] (Default: 0.5)
low_fan_speed_fan_power [unknown field type]
low_fan_speed_fan_power_sizing_factor [number] (Default: 0.16)
outdoor_air_inlet_node_name [string]
GroundHeatExchanger:System
Models vertical ground heat exchangers systems using the response factor approach developed by Eskilson. Response factors are calculated using a finite line source model assuming uniform heat flux at the borehole wall if UHFcalc is specified, or uniform borehole wall temperature if UBHWTcalc is specified.

Fields

inlet_node_name [string]
outlet_node_name [string]
design_flow_rate [number]
undisturbed_ground_temperature_model_type [string]
undisturbed_ground_temperature_model_name [string]
ground_thermal_conductivity [number]
ground_thermal_heat_capacity [number]
ghe_vertical_responsefactors_object_name [string]
g_function_calculation_method [string] (Default: UHFcalc)
ghe_vertical_array_object_name [string]
vertical_well_locations [Array of {ghe_vertical_single_object_name}]
GroundHeatExchanger:Vertical:Properties
Properties for vertical ground heat exchanger systems

Fields

depth_of_top_of_borehole [number]
borehole_length [number]
borehole_diameter [number]
grout_thermal_conductivity [number]
grout_thermal_heat_capacity [number]
pipe_thermal_conductivity [number]
pipe_thermal_heat_capacity [number]
pipe_outer_diameter [number]
pipe_thickness [number]
u_tube_distance [number]
GroundHeatExchanger:Vertical:Array
Fields

ghe_vertical_properties_object_name [string]
number_of_boreholes_in_x_direction [number]
number_of_boreholes_in_y_direction [number]
borehole_spacing [number]
GroundHeatExchanger:Vertical:Single
Fields

ghe_vertical_properties_object_name [string]
x_location [number]
y_location [number]
GroundHeatExchanger:ResponseFactors
Response factor definitions from third-party tool, commonly referred to a “g-functions”

Fields

ghe_vertical_properties_object_name [string]
number_of_boreholes [number]
g_function_reference_ratio [number] (Default: 0.0005)
g_functions [Array of {g_function_ln_t_ts_value, g_function_g_value}]
GroundHeatExchanger:Pond
A model of a shallow pond with immersed pipe loops. Typically used in hybrid geothermal systems and included in the condenser loop. This component may also be used as a simple solar collector.

Fields

fluid_inlet_node_name [string]
fluid_outlet_node_name [string]
pond_depth [number]
pond_area [number]
hydronic_tubing_inside_diameter [number]
hydronic_tubing_outside_diameter [number]
hydronic_tubing_thermal_conductivity [number]
ground_thermal_conductivity [number]
number_of_tubing_circuits [number]
length_of_each_tubing_circuit [number]
GroundHeatExchanger:Surface
A hydronic surface/panel consisting of a multi-layer construction with embedded rows of tubes. Typically used in hybrid geothermal systems and included in the condenser loop. This component may also be used as a simple solar collector. The bottom surface may be defined as ground-coupled or exposed to wind (eg. bridge deck).

Fields

construction_name [string]
fluid_inlet_node_name [string]
fluid_outlet_node_name [string]
hydronic_tubing_inside_diameter [number]
number_of_tubing_circuits [number]
hydronic_tube_spacing [number]
surface_length [number]
surface_width [number]
lower_surface_environment [string] (Default: Ground)
GroundHeatExchanger:HorizontalTrench
This models a horizontal heat exchanger placed in a series of trenches The model uses the PipingSystem:Underground underlying algorithms, but provides a more usable input interface.

Fields

inlet_node_name [string]
outlet_node_name [string]
design_flow_rate [number]
trench_length_in_pipe_axial_direction [number] (Default: 50.0)
number_of_trenches [number] (Default: 1.0)
horizontal_spacing_between_pipes [number] (Default: 1.0)
pipe_inner_diameter [number] (Default: 0.016)
pipe_outer_diameter [number] (Default: 0.026)
burial_depth [number] (Default: 1.5)
soil_thermal_conductivity [number] (Default: 1.08)
soil_density [number] (Default: 962.0)
soil_specific_heat [number] (Default: 2576.0)
pipe_thermal_conductivity [number] (Default: 0.3895)
pipe_density [number] (Default: 641.0)
pipe_specific_heat [number] (Default: 2405.0)
soil_moisture_content_percent [number] (Default: 30.0)
soil_moisture_content_percent_at_saturation [number] (Default: 50.0)
undisturbed_ground_temperature_model_type [string]
undisturbed_ground_temperature_model_name [string]
evapotranspiration_ground_cover_parameter [number] (Default: 0.4)
GroundHeatExchanger:Slinky
This models a slinky horizontal heat exchanger placed in a series of trenches The model uses the model developed by: Xiong, Z., D.E. Fisher, and J.D. Spitler. 2015. Development and Validation of a Slinky Ground Heat Exchanger Model. Applied Energy 141: 57-69.

Fields

inlet_node_name [string]
outlet_node_name [string]
design_flow_rate [number] (Default: 0.002)
soil_thermal_conductivity [number] (Default: 1.08)
soil_density [number] (Default: 962.0)
soil_specific_heat [number] (Default: 2576.0)
pipe_thermal_conductivity [number] (Default: 0.4)
pipe_density [number] (Default: 641.0)
pipe_specific_heat [number] (Default: 2405.0)
pipe_outer_diameter [number] (Default: 0.02667)
pipe_thickness [number] (Default: 0.002413)
heat_exchanger_configuration [string]
coil_diameter [number] (Default: 1.0)
coil_pitch [number] (Default: 0.2)
trench_depth [number] (Default: 1.8)
trench_length [number] (Default: 10.0)
number_of_trenches [number] (Default: 1.0)
horizontal_spacing_between_pipes [number] (Default: 2.0)
undisturbed_ground_temperature_model_type [string]
undisturbed_ground_temperature_model_name [string]
maximum_length_of_simulation [number]
HeatExchanger:FluidToFluid
A fluid/fluid heat exchanger designed to couple the supply side of one loop to the demand side of another loop Loops can be either plant or condenser loops but no air side connections are allowed

Fields

availability_schedule_name [string]
loop_demand_side_inlet_node_name [string]
loop_demand_side_outlet_node_name [string]
loop_demand_side_design_flow_rate [unknown field type]
loop_supply_side_inlet_node_name [string]
loop_supply_side_outlet_node_name [string]
loop_supply_side_design_flow_rate [unknown field type]
heat_exchange_model_type [string] (Default: Ideal)
heat_exchanger_u_factor_times_area_value [unknown field type]
control_type [string] (Default: UncontrolledOn)
heat_exchanger_setpoint_node_name [string]
minimum_temperature_difference_to_activate_heat_exchanger [number] (Default: 0.01)
heat_transfer_metering_end_use_type [string] (Default: LoopToLoop)
component_override_loop_supply_side_inlet_node_name [string]
component_override_loop_demand_side_inlet_node_name [string]
component_override_cooling_control_temperature_mode [string] (Default: Loop)
sizing_factor [number] (Default: 1.0)
operation_minimum_temperature_limit [number]
operation_maximum_temperature_limit [number]
"""
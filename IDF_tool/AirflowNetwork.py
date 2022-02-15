"""
# AirflowNetwork
"""
"""
AirflowNetwork:SimulationControl
This object defines the global parameters used in an Airflow Network simulation.

Fields

airflownetwork_control [string] (Default: NoMultizoneOrDistribution)
wind_pressure_coefficient_type [string] (Default: SurfaceAverageCalculation)
height_selection_for_local_wind_pressure_calculation [string] (Default: OpeningHeight)
building_type [string] (Default: LowRise)
maximum_number_of_iterations [number] (Default: 500.0)
initialization_type [string] (Default: ZeroNodePressures)
relative_airflow_convergence_tolerance [number] (Default: 0.0001)
absolute_airflow_convergence_tolerance [number] (Default: 1e-06)
convergence_acceleration_limit [number] (Default: -0.5)
azimuth_angle_of_long_axis_of_building [number] (Default: 0.0)
ratio_of_building_width_along_short_axis_to_width_along_long_axis [number] (Default: 1.0)
height_dependence_of_external_node_temperature [string] (Default: No)
solver [string] (Default: SkylineLU)
allow_unsupported_zone_equipment [string] (Default: No)
AirflowNetwork:MultiZone:Zone
This object is used to simultaneously control a thermal zone’s window and door openings, both exterior and interior.

Fields

zone_name [string]
ventilation_control_mode [string] (Default: NoVent)
ventilation_control_zone_temperature_setpoint_schedule_name [string]
minimum_venting_open_factor [number] (Default: 0.0)
indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor [number] (Default: 0.0)
indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor [number] (Default: 100.0)
indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor [number] (Default: 0.0)
indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor [number] (Default: 300000.0)
venting_availability_schedule_name [string]
single_sided_wind_pressure_coefficient_algorithm [string] (Default: Standard)
facade_width [number] (Default: 10.0)
occupant_ventilation_control_name [string]
AirflowNetwork:MultiZone:Surface
This object specifies the properties of a surface linkage through which air flows. Airflow Report: Node 1 as an inside face zone; Node 2 as an outside face zone or external node.

Fields

surface_name [string]
leakage_component_name [string]
external_node_name [string]
window_door_opening_factor_or_crack_factor [number] (Default: 1.0)
ventilation_control_mode [string] (Default: ZoneLevel)
ventilation_control_zone_temperature_setpoint_schedule_name [string]
minimum_venting_open_factor [number] (Default: 0.0)
indoor_and_outdoor_temperature_difference_lower_limit_for_maximum_venting_open_factor [number] (Default: 0.0)
indoor_and_outdoor_temperature_difference_upper_limit_for_minimum_venting_open_factor [number] (Default: 100.0)
indoor_and_outdoor_enthalpy_difference_lower_limit_for_maximum_venting_open_factor [number] (Default: 0.0)
indoor_and_outdoor_enthalpy_difference_upper_limit_for_minimum_venting_open_factor [number] (Default: 300000.0)
venting_availability_schedule_name [string]
occupant_ventilation_control_name [string]
equivalent_rectangle_method [string] (Default: PolygonHeight)
equivalent_rectangle_aspect_ratio [number] (Default: 1.0)
AirflowNetwork:MultiZone:ReferenceCrackConditions
This object specifies the conditions under which the air mass flow coefficient was measured.

Fields

reference_temperature [number]
reference_barometric_pressure [number] (Default: 101325.0)
reference_humidity_ratio [number] (Default: 0.0)
AirflowNetwork:MultiZone:Surface:Crack
This object specifies the properties of airflow through a crack.

Fields

air_mass_flow_coefficient_at_reference_conditions [number]
air_mass_flow_exponent [number] (Default: 0.65)
reference_crack_conditions [string]
AirflowNetwork:MultiZone:Surface:EffectiveLeakageArea
This object is used to define surface air leakage.

Fields

effective_leakage_area [number]
discharge_coefficient [number] (Default: 1.0)
reference_pressure_difference [number] (Default: 4.0)
air_mass_flow_exponent [number] (Default: 0.65)
AirflowNetwork:MultiZone:SpecifiedFlowRate
This object is used to define specified flow through a linkage.

Fields

air_flow_value [number]
air_flow_units [string] (Default: MassFlow)
AirflowNetwork:MultiZone:Component:DetailedOpening
This object specifies the properties of airflow through windows and doors (window, door and glass door heat transfer subsurfaces) when they are closed or open.

Fields

air_mass_flow_coefficient_when_opening_is_closed [number]
air_mass_flow_exponent_when_opening_is_closed [number] (Default: 0.65)
type_of_rectangular_large_vertical_opening_lvo_ [string] (Default: NonPivoted)
extra_crack_length_or_height_of_pivoting_axis [number] (Default: 0.0)
number_of_sets_of_opening_factor_data [number]
opening_factor_1 [number] (Default: 0.0)
discharge_coefficient_for_opening_factor_1 [number] (Default: 0.001)
width_factor_for_opening_factor_1 [number] (Default: 0.0)
height_factor_for_opening_factor_1 [number] (Default: 0.0)
start_height_factor_for_opening_factor_1 [number] (Default: 0.0)
opening_factor_2 [number]
discharge_coefficient_for_opening_factor_2 [number] (Default: 1.0)
width_factor_for_opening_factor_2 [number] (Default: 1.0)
height_factor_for_opening_factor_2 [number] (Default: 1.0)
start_height_factor_for_opening_factor_2 [number] (Default: 0.0)
opening_factor_3 [number]
discharge_coefficient_for_opening_factor_3 [number] (Default: 0.0)
width_factor_for_opening_factor_3 [number] (Default: 0.0)
height_factor_for_opening_factor_3 [number] (Default: 0.0)
start_height_factor_for_opening_factor_3 [number] (Default: 0.0)
opening_factor_4 [number]
discharge_coefficient_for_opening_factor_4 [number] (Default: 0.0)
width_factor_for_opening_factor_4 [number] (Default: 0.0)
height_factor_for_opening_factor_4 [number] (Default: 0.0)
start_height_factor_for_opening_factor_4 [number] (Default: 0.0)
AirflowNetwork:MultiZone:Component:SimpleOpening
This object specifies the properties of air flow through windows and doors (window, door and glass door heat transfer subsurfaces) when they are closed or open.

Fields

air_mass_flow_coefficient_when_opening_is_closed [number]
air_mass_flow_exponent_when_opening_is_closed [number] (Default: 0.65)
minimum_density_difference_for_two_way_flow [number]
discharge_coefficient [number]
AirflowNetwork:MultiZone:Component:HorizontalOpening
This object specifies the properties of air flow through a horizontal opening

Fields

air_mass_flow_coefficient_when_opening_is_closed [number]
air_mass_flow_exponent_when_opening_is_closed [number] (Default: 0.65)
sloping_plane_angle [number] (Default: 90.0)
discharge_coefficient [number]
AirflowNetwork:MultiZone:Component:ZoneExhaustFan
This object specifies the additional properties for a zone exhaust fan to perform multizone airflow calculations.

Fields

air_mass_flow_coefficient_when_the_zone_exhaust_fan_is_off_at_reference_conditions [number]
air_mass_flow_exponent_when_the_zone_exhaust_fan_is_off [number] (Default: 0.65)
reference_crack_conditions [string]
AirflowNetwork:MultiZone:ExternalNode
This object defines outdoor environmental conditions outside of the building.

Fields

external_node_height [number] (Default: 0.0)
wind_pressure_coefficient_curve_name [string]
symmetric_wind_pressure_coefficient_curve [string] (Default: No)
wind_angle_type [string] (Default: Absolute)
AirflowNetwork:MultiZone:WindPressureCoefficientArray
Used only if Wind Pressure Coefficient (WPC) Type = Input in the AirflowNetwork:SimulationControl object. Number of WPC Values in the corresponding AirflowNetwork:MultiZone:WindPressureCoefficientValues object must be the same as the number of wind directions specified for this AirflowNetwork:MultiZone:WindPressureCoefficientArray object.

Fields

wind_direction_1 [number]
wind_direction_2 [number]
wind_direction_3 [number]
wind_direction_4 [number]
wind_direction_5 [number]
wind_direction_6 [number]
wind_direction_7 [number]
wind_direction_8 [number]
wind_direction_9 [number]
wind_direction_10 [number]
wind_direction_11 [number]
wind_direction_12 [number]
wind_direction_13 [number]
wind_direction_14 [number]
wind_direction_15 [number]
wind_direction_16 [number]
wind_direction_17 [number]
wind_direction_18 [number]
wind_direction_19 [number]
wind_direction_20 [number]
wind_direction_21 [number]
wind_direction_22 [number]
wind_direction_23 [number]
wind_direction_24 [number]
wind_direction_25 [number]
wind_direction_26 [number]
wind_direction_27 [number]
wind_direction_28 [number]
wind_direction_29 [number]
wind_direction_30 [number]
wind_direction_31 [number]
wind_direction_32 [number]
wind_direction_33 [number]
wind_direction_34 [number]
wind_direction_35 [number]
wind_direction_36 [number]
AirflowNetwork:MultiZone:WindPressureCoefficientValues
Used only if Wind Pressure Coefficient (WPC) Type = INPUT in the AirflowNetwork:SimulationControl object. The number of WPC numeric inputs must correspond to the number of wind direction inputs in the AirflowNetwork:Multizone:WindPressureCoefficientArray object.

Fields

airflownetwork_multizone_windpressurecoefficientarray_name [string]
wind_pressure_coefficient_value_1 [number]
wind_pressure_coefficient_value_2 [number]
wind_pressure_coefficient_value_3 [number]
wind_pressure_coefficient_value_4 [number]
wind_pressure_coefficient_value_5 [number]
wind_pressure_coefficient_value_6 [number]
wind_pressure_coefficient_value_7 [number]
wind_pressure_coefficient_value_8 [number]
wind_pressure_coefficient_value_9 [number]
wind_pressure_coefficient_value_10 [number]
wind_pressure_coefficient_value_11 [number]
wind_pressure_coefficient_value_12 [number]
wind_pressure_coefficient_value_13 [number]
wind_pressure_coefficient_value_14 [number]
wind_pressure_coefficient_value_15 [number]
wind_pressure_coefficient_value_16 [number]
wind_pressure_coefficient_value_17 [number]
wind_pressure_coefficient_value_18 [number]
wind_pressure_coefficient_value_19 [number]
wind_pressure_coefficient_value_20 [number]
wind_pressure_coefficient_value_21 [number]
wind_pressure_coefficient_value_22 [number]
wind_pressure_coefficient_value_23 [number]
wind_pressure_coefficient_value_24 [number]
wind_pressure_coefficient_value_25 [number]
wind_pressure_coefficient_value_26 [number]
wind_pressure_coefficient_value_27 [number]
wind_pressure_coefficient_value_28 [number]
wind_pressure_coefficient_value_29 [number]
wind_pressure_coefficient_value_30 [number]
wind_pressure_coefficient_value_31 [number]
wind_pressure_coefficient_value_32 [number]
wind_pressure_coefficient_value_33 [number]
wind_pressure_coefficient_value_34 [number]
wind_pressure_coefficient_value_35 [number]
wind_pressure_coefficient_value_36 [number]
AirflowNetwork:ZoneControl:PressureController
This object is used to control a zone to a specified indoor pressure using the AirflowNetwork model. The specified pressure setpoint is used to control the zone exhaust fan flow rate in a controlled zone or the relief air flow rate in an air loop.

Fields

control_zone_name [string]
control_object_type [string]
control_object_name [string]
pressure_control_availability_schedule_name [string]
pressure_setpoint_schedule_name [string]
AirflowNetwork:Distribution:Node
This object represents an air distribution node in the AirflowNetwork model.

Fields

component_name_or_node_name [string]
component_object_type_or_node_type [string] (Default: Other)
node_height [number] (Default: 0.0)
AirflowNetwork:Distribution:Component:Leak
This object defines the characteristics of a supply or return air leak.

Fields

air_mass_flow_coefficient [number]
air_mass_flow_exponent [number] (Default: 0.65)
AirflowNetwork:Distribution:Component:LeakageRatio
This object is used to define supply and return air leaks with respect to the fan’s maximum air flow rate.

Fields

effective_leakage_ratio [number]
maximum_flow_rate [number]
reference_pressure_difference [number]
air_mass_flow_exponent [number] (Default: 0.65)
AirflowNetwork:Distribution:Component:Duct
This object defines the relationship between pressure and air flow through the duct.

Fields

duct_length [number]
hydraulic_diameter [number]
cross_section_area [number]
surface_roughness [number] (Default: 0.0009)
coefficient_for_local_dynamic_loss_due_to_fitting [number] (Default: 0.0)
heat_transmittance_coefficient_u_factor_for_duct_wall_construction [number] (Default: 0.943)
overall_moisture_transmittance_coefficient_from_air_to_air [number] (Default: 0.001)
outside_convection_coefficient [number]
inside_convection_coefficient [number]
AirflowNetwork:Distribution:Component:Fan
This object defines the name of the supply Air Fan used in an Air loop.

Fields

fan_name [string]
supply_fan_object_type [string] (Default: Fan:ConstantVolume)
AirflowNetwork:Distribution:Component:Coil
This object defines the name of a coil used in an air loop.

Fields

coil_name [string]
coil_object_type [string]
air_path_length [number]
air_path_hydraulic_diameter [number]
AirflowNetwork:Distribution:Component:HeatExchanger
This object defines the name of an air-to-air heat exchanger used in an air loop.

Fields

heatexchanger_name [string]
heatexchanger_object_type [string]
air_path_length [number]
air_path_hydraulic_diameter [number]
AirflowNetwork:Distribution:Component:TerminalUnit
This object defines the name of a terminal unit in an air loop.

Fields

terminal_unit_name [string]
terminal_unit_object_type [string]
air_path_length [number]
air_path_hydraulic_diameter [number]
AirflowNetwork:Distribution:Component:ConstantPressureDrop
This object defines the characteristics of a constant pressure drop component (e.g. filter). Each node connected to this object can not be a node of mixer, splitter, a node of air primary loop, or zone equipment loop. It is recommended to connect to a duct component at both ends.

Fields

pressure_difference_across_the_component [number]
AirflowNetwork:Distribution:Component:OutdoorAirFlow
This object includes the outdoor air flow rate set by the Controller:OutdoorAir object in the airflow network.

Fields

outdoor_air_mixer_name [string]
air_mass_flow_coefficient_when_no_outdoor_air_flow_at_reference_conditions [number]
air_mass_flow_exponent_when_no_outdoor_air_flow [number] (Default: 0.65)
reference_crack_conditions [string]
AirflowNetwork:Distribution:Component:ReliefAirFlow
This object allows variation of air flow rate to perform pressure.

Fields

outdoor_air_mixer_name [string]
air_mass_flow_coefficient_when_no_outdoor_air_flow_at_reference_conditions [number]
air_mass_flow_exponent_when_no_outdoor_air_flow [number] (Default: 0.65)
reference_crack_conditions [string]
AirflowNetwork:Distribution:Linkage
This object defines the connection between two nodes and a component.

Fields

node_1_name [string]
node_2_name [string]
component_name [string]
thermal_zone_name [string]
AirflowNetwork:Distribution:DuctViewFactors
This object is used to allow user-defined view factors to be used for duct-surface radiation calculations.

Fields

linkage_name [string]
duct_surface_exposure_fraction [number] (Default: 0.0)
duct_surface_emittance [number] (Default: 0.9)
surfaces [Array of {surface_name, surface_view_factor}]
AirflowNetwork:OccupantVentilationControl
This object is used to provide advanced thermal comfort control of window opening and closing for both exterior and interior windows.

Fields

minimum_opening_time [number] (Default: 0.0)
minimum_closing_time [number] (Default: 0.0)
thermal_comfort_low_temperature_curve_name [string]
thermal_comfort_temperature_boundary_point [number] (Default: 10.0)
thermal_comfort_high_temperature_curve_name [string]
maximum_threshold_for_persons_dissatisfied_ppd [number] (Default: 10.0)
occupancy_check [string] (Default: No)
opening_probability_schedule_name [string]
closing_probability_schedule_name [string]
AirflowNetwork:IntraZone:Node
This object represents a node in a zone in the combination of RoomAir and AirflowNetwork model.

Fields

roomair_node_airflownetwork_name [string]
zone_name [string]
node_height [number] (Default: 0.0)
AirflowNetwork:IntraZone:Linkage
This object defines the connection between two nodes and a component used in the combination of RoomAir and AirflowNetwork model.

Fields

node_1_name [string]
node_2_name [string]
component_name [string]
airflownetwork_multizone_surface_name [string]
"""
"""
Pumps
"""
"""
Pump:VariableSpeed
This pump model is described in the ASHRAE secondary HVAC toolkit.

Fields

inlet_node_name [string]
outlet_node_name [string]
design_maximum_flow_rate [unknown field type]
design_pump_head [number] (Default: 179352.0)
design_power_consumption [unknown field type]
motor_efficiency [number] (Default: 0.9)
fraction_of_motor_inefficiencies_to_fluid_stream [number] (Default: 0.0)
coefficient_1_of_the_part_load_performance_curve [number] (Default: 0.0)
coefficient_2_of_the_part_load_performance_curve [number] (Default: 1.0)
coefficient_3_of_the_part_load_performance_curve [number] (Default: 0.0)
coefficient_4_of_the_part_load_performance_curve [number] (Default: 0.0)
design_minimum_flow_rate [unknown field type] (Default: Autosize)
pump_control_type [string] (Default: Continuous)
pump_flow_rate_schedule_name [string]
pump_curve_name [string]
impeller_diameter [number]
vfd_control_type [string]
pump_rpm_schedule_name [string]
minimum_pressure_schedule [string]
maximum_pressure_schedule [string]
minimum_rpm_schedule [string]
maximum_rpm_schedule [string]
zone_name [string]
skin_loss_radiative_fraction [number]
design_power_sizing_method [string] (Default: PowerPerFlowPerPressure)
design_electric_power_per_unit_flow_rate [number] (Default: 348701.1)
design_shaft_power_per_unit_flow_rate_per_unit_head [number] (Default: 1.282051282)
design_minimum_flow_rate_fraction [number] (Default: 0.0)
end_use_subcategory [string] (Default: General)
Pump:ConstantSpeed
This pump model is described in the ASHRAE secondary HVAC toolkit.

Fields

inlet_node_name [string]
outlet_node_name [string]
design_flow_rate [unknown field type]
design_pump_head [number] (Default: 179352.0)
design_power_consumption [unknown field type]
motor_efficiency [number] (Default: 0.9)
fraction_of_motor_inefficiencies_to_fluid_stream [number] (Default: 0.0)
pump_control_type [string] (Default: Continuous)
pump_flow_rate_schedule_name [string]
pump_curve_name [string]
impeller_diameter [number]
rotational_speed [number]
zone_name [string]
skin_loss_radiative_fraction [number]
design_power_sizing_method [string] (Default: PowerPerFlowPerPressure)
design_electric_power_per_unit_flow_rate [number] (Default: 348701.1)
design_shaft_power_per_unit_flow_rate_per_unit_head [number] (Default: 1.282051282)
end_use_subcategory [string] (Default: General)
Pump:VariableSpeed:Condensate
This pump model is described in the ASHRAE secondary HVAC toolkit. Variable Speed Condensate pump for Steam Systems

Fields

inlet_node_name [string]
outlet_node_name [string]
design_steam_volume_flow_rate [unknown field type]
design_pump_head [number] (Default: 179352.0)
design_power_consumption [unknown field type]
motor_efficiency [number] (Default: 0.9)
fraction_of_motor_inefficiencies_to_fluid_stream [number] (Default: 0.0)
coefficient_1_of_the_part_load_performance_curve [number] (Default: 0.0)
coefficient_2_of_the_part_load_performance_curve [number] (Default: 1.0)
coefficient_3_of_the_part_load_performance_curve [number] (Default: 0.0)
coefficient_4_of_the_part_load_performance_curve [number] (Default: 0.0)
pump_flow_rate_schedule_name [string]
zone_name [string]
skin_loss_radiative_fraction [number]
design_power_sizing_method [string] (Default: PowerPerFlowPerPressure)
design_electric_power_per_unit_flow_rate [number] (Default: 348701.1)
design_shaft_power_per_unit_flow_rate_per_unit_head [number] (Default: 1.282051282)
end_use_subcategory [string] (Default: General)
HeaderedPumps:ConstantSpeed
This Headered pump object describes a pump bank with more than 1 pump in parallel

Fields

inlet_node_name [string]
outlet_node_name [string]
total_design_flow_rate [unknown field type]
number_of_pumps_in_bank [number]
flow_sequencing_control_scheme [string] (Default: Sequential)
design_pump_head [number] (Default: 179352.0)
design_power_consumption [unknown field type]
motor_efficiency [number] (Default: 0.9)
fraction_of_motor_inefficiencies_to_fluid_stream [number] (Default: 0.0)
pump_control_type [string] (Default: Continuous)
pump_flow_rate_schedule_name [string]
zone_name [string]
skin_loss_radiative_fraction [number]
design_power_sizing_method [string] (Default: PowerPerFlowPerPressure)
design_electric_power_per_unit_flow_rate [number] (Default: 348701.1)
design_shaft_power_per_unit_flow_rate_per_unit_head [number] (Default: 1.282051282)
end_use_subcategory [string] (Default: General)
HeaderedPumps:VariableSpeed
This Headered pump object describes a pump bank with more than 1 pump in parallel

Fields

inlet_node_name [string]
outlet_node_name [string]
total_design_flow_rate [unknown field type]
number_of_pumps_in_bank [number]
flow_sequencing_control_scheme [string] (Default: Sequential)
design_pump_head [number] (Default: 179352.0)
design_power_consumption [unknown field type]
motor_efficiency [number] (Default: 0.9)
fraction_of_motor_inefficiencies_to_fluid_stream [number] (Default: 0.0)
coefficient_1_of_the_part_load_performance_curve [number] (Default: 0.0)
coefficient_2_of_the_part_load_performance_curve [number] (Default: 1.0)
coefficient_3_of_the_part_load_performance_curve [number] (Default: 0.0)
coefficient_4_of_the_part_load_performance_curve [number] (Default: 0.0)
minimum_flow_rate_fraction [number] (Default: 0.0)
pump_control_type [string] (Default: Continuous)
pump_flow_rate_schedule_name [string]
zone_name [string]
skin_loss_radiative_fraction [number]
design_power_sizing_method [string] (Default: PowerPerFlowPerPressure)
design_electric_power_per_unit_flow_rate [number] (Default: 348701.1)
design_shaft_power_per_unit_flow_rate_per_unit_head [number] (Default: 1.282051282)
end_use_subcategory [string] (Default: General)
"""
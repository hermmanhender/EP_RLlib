"""
# Plant-Condenser Loops
"""
"""
PlantLoop
Defines a central plant loop.

Fields

fluid_type [string] (Default: Water)
user_defined_fluid_type [string]
plant_equipment_operation_scheme_name [string]
loop_temperature_setpoint_node_name [string]
maximum_loop_temperature [number]
minimum_loop_temperature [number]
maximum_loop_flow_rate [unknown field type]
minimum_loop_flow_rate [number] (Default: 0.0)
plant_loop_volume [unknown field type] (Default: Autocalculate)
plant_side_inlet_node_name [string]
plant_side_outlet_node_name [string]
plant_side_branch_list_name [string]
plant_side_connector_list_name [string]
demand_side_inlet_node_name [string]
demand_side_outlet_node_name [string]
demand_side_branch_list_name [string]
demand_side_connector_list_name [string]
load_distribution_scheme [string] (Default: SequentialLoad)
availability_manager_list_name [string]
plant_loop_demand_calculation_scheme [string] (Default: SingleSetpoint)
common_pipe_simulation [string] (Default: None)
pressure_simulation_type [string] (Default: None)
loop_circulation_time [number] (Default: 2.0)
CondenserLoop
Defines a central plant condenser loop. CondenserLoop and PlantLoop are nearly identical except some components and operation schemes are applicable to only one loop type or the other.

Fields

fluid_type [string] (Default: Water)
user_defined_fluid_type [string]
condenser_equipment_operation_scheme_name [string]
condenser_loop_temperature_setpoint_node_name [string]
maximum_loop_temperature [number]
minimum_loop_temperature [number]
maximum_loop_flow_rate [unknown field type]
minimum_loop_flow_rate [number] (Default: 0.0)
condenser_loop_volume [unknown field type] (Default: Autocalculate)
condenser_side_inlet_node_name [string]
condenser_side_outlet_node_name [string]
condenser_side_branch_list_name [string]
condenser_side_connector_list_name [string]
demand_side_inlet_node_name [string]
demand_side_outlet_node_name [string]
condenser_demand_side_branch_list_name [string]
condenser_demand_side_connector_list_name [string]
load_distribution_scheme [string] (Default: SequentialLoad)
pressure_simulation_type [string] (Default: None)
loop_circulation_time [number] (Default: 2.0)
"""
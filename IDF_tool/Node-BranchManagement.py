"""
# Node-Branch Management
"""
"""
Branch
List components on the branch in simulation and connection order Note: this should NOT include splitters or mixers which define endpoints of branches

Fields

pressure_drop_curve_name [string]
components [Array of {component_object_type, component_name, component_inlet_node_name, component_outlet_node_name}]
BranchList
Branches MUST be listed in Flow order: Inlet branch, then parallel branches, then Outlet branch. Branches are simulated in the order listed. Branch names cannot be duplicated within a single branch list.

Fields

branches [Array of {branch_name}]
Connector:Splitter
Split one air/water stream into N outlet streams. Branch names cannot be duplicated within a single Splitter list.

Fields

inlet_branch_name [string]
branches [Array of {outlet_branch_name}]
Connector:Mixer
Mix N inlet air/water streams into one. Branch names cannot be duplicated within a single mixer list.

Fields

outlet_branch_name [string]
branches [Array of {inlet_branch_name}]
ConnectorList
only two connectors allowed per loop if two entered, one must be Connector:Splitter and one must be Connector:Mixer

Fields

connector_1_object_type [string]
connector_1_name [string]
connector_2_object_type [string]
connector_2_name [string]
NodeList
This object is used in places where lists of nodes may be needed, e.g. ZoneHVAC:EquipmentConnections field Zone Air Inlet Node or NodeList Name

Fields

nodes [Array of {node_name}]
OutdoorAir:Node
This object sets the temperature and humidity conditions for an outdoor air node. It allows the height above ground to be specified. This object may be used more than once. The same node name may not appear in both an OutdoorAir:Node object and an OutdoorAir:NodeList object. This object defines local outdoor air environmental conditions.

Fields

height_above_ground [number] (Default: -1.0)
drybulb_temperature_schedule_name [string]
wetbulb_temperature_schedule_name [string]
wind_speed_schedule_name [string]
wind_direction_schedule_name [string]
wind_pressure_coefficient_curve_name [string]
symmetric_wind_pressure_coefficient_curve [string] (Default: No)
wind_angle_type [string] (Default: Absolute)
OutdoorAir:NodeList
This object sets the temperature and humidity conditions for an outdoor air node using the weather data values. to vary outdoor air node conditions with height above ground use OutdoorAir:Node instead of this object. This object may be used more than once. The same node name may not appear in both an OutdoorAir:Node object and an OutdoorAir:NodeList object.

Fields

nodes [Array of {node_or_nodelist_name}]
Pipe:Adiabatic
Passes Inlet Node state variables to Outlet Node state variables

Fields

inlet_node_name [string]
outlet_node_name [string]
Pipe:Adiabatic:Steam
Passes Inlet Node state variables to Outlet Node state variables

Fields

inlet_node_name [string]
outlet_node_name [string]
Pipe:Indoor
Pipe model with transport delay and heat transfer to the environment.

Fields

construction_name [string]
fluid_inlet_node_name [string]
fluid_outlet_node_name [string]
environment_type [string] (Default: Zone)
ambient_temperature_zone_name [string]
ambient_temperature_schedule_name [string]
ambient_air_velocity_schedule_name [string]
pipe_inside_diameter [number]
pipe_length [number]
Pipe:Outdoor
Pipe model with transport delay and heat transfer to the environment.

Fields

construction_name [string]
fluid_inlet_node_name [string]
fluid_outlet_node_name [string]
ambient_temperature_outdoor_air_node_name [string]
pipe_inside_diameter [number]
pipe_length [number]
Pipe:Underground
Buried Pipe model: For pipes buried at a depth less than one meter, this is an alternative object to: HeatExchanger:Surface

Fields

construction_name [string]
fluid_inlet_node_name [string]
fluid_outlet_node_name [string]
sun_exposure [string]
pipe_inside_diameter [number]
pipe_length [number]
soil_material_name [string]
undisturbed_ground_temperature_model_type [string]
undisturbed_ground_temperature_model_name [string]
PipingSystem:Underground:Domain
The ground domain object for underground piping system simulation.

Fields

xmax [number]
ymax [number]
zmax [number]
x_direction_mesh_density_parameter [number] (Default: 4.0)
x_direction_mesh_type [string]
x_direction_geometric_coefficient [number] (Default: 1.3)
y_direction_mesh_density_parameter [number] (Default: 4.0)
y_direction_mesh_type [string]
y_direction_geometric_coefficient [number] (Default: 1.3)
z_direction_mesh_density_parameter [number] (Default: 4.0)
z_direction_mesh_type [string]
z_direction_geometric_coefficient [number] (Default: 1.3)
soil_thermal_conductivity [number]
soil_density [number]
soil_specific_heat [number]
soil_moisture_content_volume_fraction [number] (Default: 30.0)
soil_moisture_content_volume_fraction_at_saturation [number] (Default: 50.0)
undisturbed_ground_temperature_model_type [string]
undisturbed_ground_temperature_model_name [string]
this_domain_includes_basement_surface_interaction [string] (Default: No)
width_of_basement_floor_in_ground_domain [number]
depth_of_basement_wall_in_ground_domain [number]
shift_pipe_x_coordinates_by_basement_width [string]
name_of_basement_wall_boundary_condition_model [string]
name_of_basement_floor_boundary_condition_model [string]
convergence_criterion_for_the_outer_cartesian_domain_iteration_loop [number] (Default: 0.001)
maximum_iterations_in_the_outer_cartesian_domain_iteration_loop [number] (Default: 500.0)
evapotranspiration_ground_cover_parameter [number] (Default: 0.4)
number_of_pipe_circuits_entered_for_this_domain [number]
pipe_circuits [Array of {pipe_circuit}]
PipingSystem:Underground:PipeCircuit
The pipe circuit object in an underground piping system. This object is simulated within an underground piping domain object and connected on a branch on a plant loop.

Fields

pipe_thermal_conductivity [number]
pipe_density [number]
pipe_specific_heat [number]
pipe_inner_diameter [number]
pipe_outer_diameter [number]
design_flow_rate [number]
circuit_inlet_node [string]
circuit_outlet_node [string]
convergence_criterion_for_the_inner_radial_iteration_loop [number] (Default: 0.001)
maximum_iterations_in_the_inner_radial_iteration_loop [number] (Default: 500.0)
number_of_soil_nodes_in_the_inner_radial_near_pipe_mesh_region [number] (Default: 3.0)
radial_thickness_of_inner_radial_near_pipe_mesh_region [number]
number_of_pipe_segments_entered_for_this_pipe_circuit [number]
pipe_segments [Array of {pipe_segment}]
PipingSystem:Underground:PipeSegment
The pipe segment to be used in an underground piping system This object represents a single pipe leg positioned axially in the local z-direction, at a given x, y location in the domain

Fields

x_position [number]
y_position [number]
flow_direction [string]
Duct
Passes inlet node state variables to outlet node state variables

Fields

inlet_node_name [string]
outlet_node_name [string]
"""
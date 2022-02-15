"""
# Detailed Ground Heat Transfer
"""

"""
class GroundHeatTransfer:Control():
    '''
    Object determines if the Slab and Basement preprocessors are going to be executed.
    '''

run_basement_preprocessor [string] (Default: No)
run_slab_preprocessor [string] (Default: No)

class GroundHeatTransfer:Slab:Materials():
    '''
    Object gives an overall description of the slab ground heat transfer model.
    '''

nmat_number_of_materials [number]
albedo_surface_albedo_no_snow [number] (Default: 0.16)
albedo_surface_albedo_snow [number] (Default: 0.4)
epslw_surface_emissivity_no_snow [number] (Default: 0.94)
epslw_surface_emissivity_snow [number] (Default: 0.86)
z0_surface_roughness_no_snow [number] (Default: 0.75)
z0_surface_roughness_snow [number] (Default: 0.25)
hin_indoor_hconv_downward_flow [number] (Default: 6.13)
hin_indoor_hconv_upward [number] (Default: 9.26)

class GroundHeatTransfer:Slab:MatlProps():
    '''
    This object contains the material properties for the materials used in the model. The fields are mostly self explanatory.
    '''

rho_slab_material_density [number] (Default: 2300.0)
rho_soil_density [number] (Default: 1200.0)
cp_slab_cp [number] (Default: 650.0)
cp_soil_cp [number] (Default: 1200.0)
tcon_slab_k [number] (Default: 0.9)
tcon_soil_k [number] (Default: 1.0)

class GroundHeatTransfer:Slab:BoundConds():
    '''
    Supplies some of the boundary conditions used in the ground heat transfer calculations.
    '''

evtr_is_surface_evapotranspiration_modeled [string]
fixbc_is_the_lower_boundary_at_a_fixed_temperature [string]
tdeepin [number]
usrhflag_is_the_ground_surface_h_specified_by_the_user_ [string]
userh_user_specified_ground_surface_heat_transfer_coefficient [number]

class GroundHeatTransfer:Slab:BldgProps():
    '''
    Object provides information about the building and its operating conditions Monthly Average Temperature SetPoint fields specify the average indoor building set point temperatures for each month of the year. These fields are useful for simulating a building that is not temperature controlled for some of the year. In such a case, the average indoor set point temperatures can be obtained by first running the model in EnergyPlus with an insulated floor boundary condition, and then using the resulting monthly average zone temperatures in these fields.
    '''

iyrs_number_of_years_to_iterate [number] (Default: 10.0)
shape_slab_shape [number]
hbldg_building_height [number]
tin1_january_indoor_average_temperature_setpoint [number] (Default: 22.0)
tin2_february_indoor_average_temperature_setpoint [number] (Default: 22.0)
tin3_march_indoor_average_temperature_setpoint [number] (Default: 22.0)
tin4_april_indoor_average_temperature_setpoint [number] (Default: 22.0)
tin5_may_indoor_average_temperature_setpoint [number] (Default: 22.0)
tin6_june_indoor_average_temperature_setpoint [number] (Default: 22.0)
tin7_july_indoor_average_temperature_setpoint [number] (Default: 22.0)
tin8_august_indoor_average_temperature_setpoint [number] (Default: 22.0)
tin9_september_indoor_average_temperature_setpoint [number] (Default: 22.0)
tin10_october_indoor_average_temperature_setpoint [number] (Default: 22.0)
tin11_november_indoor_average_temperature_setpoint [number] (Default: 22.0)
tin12_december_indoor_average_temperature_setpoint [number] (Default: 22.0)
tinamp_daily_indoor_sine_wave_variation_amplitude [number] (Default: 0.0)
convtol_convergence_tolerance [number] (Default: 0.1)

class GroundHeatTransfer:Slab:Insulation():
    '''
    This object supplies the information about insulation used around the slab. There are two possible configurations: under the slab or vertical insulation around the slab.
    '''

rins_r_value_of_under_slab_insulation [number] (Default: 0.0)
dins_width_of_strip_of_under_slab_insulation [number] (Default: 0.0)
rvins_r_value_of_vertical_insulation [number] (Default: 0.0)
zvins_depth_of_vertical_insulation [number] (Default: 0.0)
ivins_flag_is_there_vertical_insulation [unknown field type] (Default: 0.0)

class GroundHeatTransfer:Slab:EquivalentSlab():
    '''
    Using an equivalent slab allows non-rectangular shapes to be modeled accurately. Object uses the area - perimeter (area/perimeter) ratio to determine the size of an equivalent rectangular slab. EnergyPlus users normally use this option.
    '''

apratio_the_area_to_perimeter_ratio_for_this_slab [number]
slabdepth_thickness_of_slab_on_grade [number] (Default: 0.1)
clearance_distance_from_edge_of_slab_to_domain_edge [number] (Default: 15.0)
zclearance_distance_from_bottom_of_slab_to_domain_bottom [number] (Default: 15.0)

class GroundHeatTransfer:Slab:AutoGrid():
    '''
    AutoGrid only necessary when EquivalentSlab option not chosen. Not normally needed by EnergyPlus users. This object permits user selection of rectangular slab dimensions. NO SLAB DIMENSIONS LESS THAN 6 m.
    '''

slabx_x_dimension_of_the_building_slab [number]
slaby_y_dimension_of_the_building_slab [number]
slabdepth_thickness_of_slab_on_grade [number] (Default: 0.1)
clearance_distance_from_edge_of_slab_to_domain_edge [number] (Default: 15.0)
zclearance_distance_from_bottom_of_slab_to_domain_bottom [number] (Default: 15.0)

class GroundHeatTransfer:Slab:ManualGrid():
    '''
    Manual Grid only necessary when using manual gridding (not recommended) Used only in special cases when previous two objects are not used. User must input complete gridding information.
    '''

nx_number_of_cells_in_the_x_direction [number]
ny_number_of_cells_in_the_y_direction [number]
nz_number_of_cells_in_the_z_direction [number]
ibox_x_direction_cell_indicator_of_slab_edge [number]
jbox_y_direction_cell_indicator_of_slab_edge [number]

class GroundHeatTransfer:Slab:XFACE():
    '''
    This is only needed when using manual gridding (not recommended) XFACE: X Direction cell face coordinates: m
    '''

class GroundHeatTransfer:Slab:YFACE():
    '''
    This is only needed when using manual gridding (not recommended) YFACE: Y Direction cell face coordinates: m,
    '''

class GroundHeatTransfer:Slab:ZFACE():
    '''
    This is only needed when using manual gridding (not recommended) ZFACE: Z Direction cell face coordinates: m
    '''

class GroundHeatTransfer:Basement:SimParameters():
    '''
    Specifies certain parameters that control the Basement preprocessor ground heat transfer simulation.
    '''

f_multiplier_for_the_adi_solution [number]
iyrs_maximum_number_of_yearly_iterations_ [number] (Default: 15.0)

class GroundHeatTransfer:Basement:MatlProps():
    '''
    Specifies the material properties for the Basement preprocessor ground heat transfer simulation. Only the Foundation Wall, Floor Slab, Soil, and Gravel properties are currently used.
    '''

nmat_number_of_materials_in_this_domain [number]
density_for_foundation_wall [number] (Default: 2243.0)
density_for_floor_slab [number] (Default: 2243.0)
density_for_ceiling [number] (Default: 311.0)
density_for_soil [number] (Default: 1500.0)
density_for_gravel [number] (Default: 2000.0)
density_for_wood [number] (Default: 449.0)
specific_heat_for_foundation_wall [number] (Default: 880.0)
specific_heat_for_floor_slab [number] (Default: 880.0)
specific_heat_for_ceiling [number] (Default: 1530.0)
specific_heat_for_soil [number] (Default: 840.0)
specific_heat_for_gravel [number] (Default: 720.0)
specific_heat_for_wood [number] (Default: 1530.0)
thermal_conductivity_for_foundation_wall [number] (Default: 1.4)
thermal_conductivity_for_floor_slab [number] (Default: 1.4)
thermal_conductivity_for_ceiling [number] (Default: 0.09)
thermal_conductivity_for_soil [number] (Default: 1.1)
thermal_conductivity_for_gravel [number] (Default: 1.9)
thermal_conductivity_for_wood [number] (Default: 0.12)

class GroundHeatTransfer:Basement:Insulation():
    '''
    Describes the insulation used on an exterior basement wall for the Basement preprocessor ground heat transfer simulation.
    '''

rext_r_value_of_any_exterior_insulation [number]
insfull_flag_is_the_wall_fully_insulated_ [string]

class GroundHeatTransfer:Basement:SurfaceProps():
    '''
    Specifies the soil surface properties for the Basement preprocessor ground heat transfer simulation.
    '''

albedo_surface_albedo_for_no_snow_conditions [number] (Default: 0.16)
albedo_surface_albedo_for_snow_conditions [number] (Default: 0.4)
epsln_surface_emissivity_no_snow [number] (Default: 0.94)
epsln_surface_emissivity_with_snow [number] (Default: 0.86)
veght_surface_roughness_no_snow_conditions [number] (Default: 6.0)
veght_surface_roughness_snow_conditions [number] (Default: 0.25)
pet_flag_potential_evapotranspiration_on_ [string] (Default: FALSE)

class GroundHeatTransfer:Basement:BldgData():
    '''
    Specifies the surface and gravel thicknesses used for the Basement preprocessor ground heat transfer simulation.
    '''

dwall_wall_thickness [number] (Default: 0.2)
dslab_floor_slab_thickness [number] (Default: 0.1)
dgravxy_width_of_gravel_pit_beside_basement_wall [number] (Default: 0.3)
dgravzn_gravel_depth_extending_above_the_floor_slab [number] (Default: 0.2)
dgravzp_gravel_depth_below_the_floor_slab [number] (Default: 0.1)

class GroundHeatTransfer:Basement:Interior():
    '''
    Provides the information needed to simulate the inside boundary conditions for the Basement preprocessor ground heat transfer simulation.
    '''

cond_flag_is_the_basement_conditioned_ [string] (Default: TRUE)
hin_downward_convection_only_heat_transfer_coefficient [number] (Default: 0.92)
hin_upward_convection_only_heat_transfer_coefficient [number] (Default: 4.04)
hin_horizontal_convection_only_heat_transfer_coefficient [number] (Default: 3.08)
hin_downward_combined_convection_and_radiation_heat_transfer_coefficient [number] (Default: 6.13)
hin_upward_combined_convection_and_radiation_heat_transfer_coefficient [number] (Default: 9.26)
hin_horizontal_combined_convection_and_radiation_heat_transfer_coefficient [number] (Default: 8.29)

class GroundHeatTransfer:Basement:ComBldg():
    '''
    ComBldg contains the monthly average temperatures (C) and possibility of daily variation amplitude
    '''

january_average_temperature [number] (Default: 22.0)
february_average_temperature [number] (Default: 22.0)
march_average_temperature [number] (Default: 22.0)
april_average_temperature [number] (Default: 22.0)
may_average_temperature [number] (Default: 22.0)
june_average_temperature [number] (Default: 22.0)
july_average_temperature [number] (Default: 22.0)
august_average_temperature [number] (Default: 22.0)
september_average_temperature [number] (Default: 22.0)
october_average_temperature [number] (Default: 22.0)
november_average_temperature [number] (Default: 22.0)
december_average_temperature [number] (Default: 22.0)
daily_variation_sine_wave_amplitude [number] (Default: 0.0)

class GroundHeatTransfer:Basement:EquivSlab():
    '''
    Using an equivalent slab allows non-rectangular shapes to be modeled accurately. The simulation default should be EquivSizing=True
    '''

apratio_the_area_to_perimeter_ratio_for_this_slab [number]
equivsizing_flag [string]

class GroundHeatTransfer:Basement:EquivAutoGrid():
    '''
    EquivAutoGrid necessary when EquivSizing=TRUE, TRUE is is the normal case.
    '''

clearance_distance_from_outside_of_wall_to_edge_of_3_d_ground_domain [number] (Default: 15.0)
slabdepth_thickness_of_the_floor_slab [number] (Default: 0.1)
basedepth_depth_of_the_basement_wall_below_grade [number] (Default: 2.0)

class GroundHeatTransfer:Basement:AutoGrid():
    '''
    AutoGrid only necessary when EquivSizing is false If the modeled building is not a rectangle or square, Equivalent sizing MUST be used to get accurate results
    '''

clearance_distance_from_outside_of_wall_to_edge_ [number] (Default: 15.0)
slabx_x_dimension_of_the_building_slab [number]
slaby_y_dimension_of_the_building_slab [number]
concagheight_height_of_the_foundation_wall_above_grade [number] (Default: 0.0)
slabdepth_thickness_of_the_floor_slab [number] (Default: 0.1)
basedepth_depth_of_the_basement_wall_below_grade [number] (Default: 2.0)

class GroundHeatTransfer:Basement:ManualGrid():
    '''
    Manual Grid only necessary using manual gridding (not recommended)
    '''

nx_number_of_cells_in_the_x_direction_20_ [number]
ny_number_of_cells_in_the_y_direction_20_ [number]
nzag_number_of_cells_in_the_z_direction_above_grade_4_always_ [number]
nzbg_number_of_cells_in_z_direction_below_grade_10_35_ [number]
ibase_x_direction_cell_indicator_of_slab_edge_5_20_ [number]
jbase_y_direction_cell_indicator_of_slab_edge_5_20_ [number]
kbase_z_direction_cell_indicator_of_the_top_of_the_floor_slab_5_20_ [number]

class GroundHeatTransfer:Basement:XFACE():
    '''
    This is only needed when using manual gridding (not recommended) XFACE: X Direction cell face coordinates: m
    '''

class GroundHeatTransfer:Basement:YFACE():
    '''
    This is only needed when using manual gridding (not recommended) YFACE: Y Direction cell face coordinates: m
    '''

class GroundHeatTransfer:Basement:ZFACE():
    '''
    This is only needed when using manual gridding (not recommended) ZFACE: Z Direction cell face coordinates: m
    '''

"""
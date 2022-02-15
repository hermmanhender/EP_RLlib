"""
# Advanced Construction, Surface, Zone Concepts
"""

"""
class SurfaceProperty:HeatTransferAlgorithm():
    '''
    Determines which Heat Balance Algorithm will be used for a specific surface Allows selectively overriding the global setting in HeatBalanceAlgorithm CTF (Conduction Transfer Functions), EMPD (Effective Moisture Penetration Depth with Conduction Transfer Functions). Advanced/Research Usage: CondFD (Conduction Finite Difference) Advanced/Research Usage: HAMT (Combined Heat And Moisture Finite Element)
    '''
    
surface_name [string]
algorithm [string] (Default: ConductionTransferFunction)

class SurfaceProperty:HeatTransferAlgorithm:MultipleSurface():
    '''
    Determines which Heat Balance Algorithm will be used for a group of surface types Allows selectively overriding the global setting in HeatBalanceAlgorithm CTF (Conduction Transfer Functions), EMPD (Effective Moisture Penetration Depth with Conduction Transfer Functions). Advanced/Research Usage: CondFD (Conduction Finite Difference) Advanced/Research Usage: HAMT (Combined Heat And Moisture Finite Element)
    '''

surface_type [string]
algorithm [string] (Default: ConductionTransferFunction)

class SurfaceProperty:HeatTransferAlgorithm:SurfaceList():
    '''
    Determines which Heat Balance Algorithm will be used for a list of surfaces Allows selectively overriding the global setting in HeatBalanceAlgorithm CTF (Conduction Transfer Functions), EMPD (Effective Moisture Penetration Depth with Conduction Transfer Functions). Advanced/Research Usage: CondFD (Conduction Finite Difference) Advanced/Research Usage: HAMT (Combined Heat And Moisture Finite Element)
    '''

algorithm [string] (Default: ConductionTransferFunction)
surface [Array of {surface_name}]

class SurfaceProperty:HeatTransferAlgorithm:Construction():
    '''
    Determines which Heat Balance Algorithm will be used for surfaces that have a specific type of construction Allows selectively overriding the global setting in HeatBalanceAlgorithm CTF (Conduction Transfer Functions), EMPD (Effective Moisture Penetration Depth with Conduction Transfer Functions). Advanced/Research Usage: CondFD (Conduction Finite Difference) Advanced/Research Usage: HAMT (Combined Heat And Moisture Finite Element)
    '''

algorithm [string] (Default: ConductionTransferFunction)
construction_name [string]

class SurfaceProperty:HeatBalanceSourceTerm():
    '''
    Allows an additional heat source term to be added to the inside or outside surface boundary. A heat source can be added to either or both the inside and outside of the same surface.
    '''

surface_name [string]
inside_face_heat_source_term_schedule_name [string]
outside_face_heat_source_term_schedule_name [string]

class SurfaceControl:MovableInsulation():
    '''
    Exterior or Interior Insulation on opaque surfaces
    '''

insulation_type [string]
surface_name [string]
material_name [string]
schedule_name [string]

class SurfaceProperty:OtherSideCoefficients():
    '''
    This object sets the other side conditions for a surface in a variety of ways.
    '''

combined_convective_radiative_film_coefficient [number]
constant_temperature [number] (Default: 0.0)
constant_temperature_coefficient [number] (Default: 1.0)
external_dry_bulb_temperature_coefficient [number] (Default: 0.0)
ground_temperature_coefficient [number] (Default: 0.0)
wind_speed_coefficient [number] (Default: 0.0)
zone_air_temperature_coefficient [number] (Default: 0.0)
constant_temperature_schedule_name [string]
sinusoidal_variation_of_constant_temperature_coefficient [string] (Default: No)
period_of_sinusoidal_variation [number] (Default: 24.0)
previous_other_side_temperature_coefficient [number] (Default: 0.0)
minimum_other_side_temperature_limit [number]
maximum_other_side_temperature_limit [number]

class SurfaceProperty:OtherSideConditionsModel():
    '''
    This object sets up modifying the other side conditions for a surface from other model results.
    '''

type_of_modeling [string] (Default: GapConvectionRadiation)

class SurfaceProperty:Underwater():
    '''
    This object sets up a convective water boundary condition for a surface The free stream temperature and velocity are scheduled. If the free stream velocity is zero, the surface will naturally convect with the surrounding water.
    '''

distance_from_surface_centroid_to_leading_edge_of_boundary_layer [number]
free_stream_water_temperature_schedule [string]
free_stream_water_velocity_schedule [string]

class Foundation:Kiva():
    '''
    Refined definition of the foundation surface construction used to inform two-dimensional heat transfer calculated using the Kiva ground heat transfer methodology.
    '''

initial_indoor_air_temperature [number]
interior_horizontal_insulation_material_name [string]
interior_horizontal_insulation_depth [number] (Default: 0.0)
interior_horizontal_insulation_width [number]
interior_vertical_insulation_material_name [string]
interior_vertical_insulation_depth [number]
exterior_horizontal_insulation_material_name [string]
exterior_horizontal_insulation_depth [number]
exterior_horizontal_insulation_width [number] (Default: 0.0)
exterior_vertical_insulation_material_name [string]
exterior_vertical_insulation_depth [number]
wall_height_above_grade [number] (Default: 0.2)
wall_depth_below_slab [number] (Default: 0.0)
footing_wall_construction_name [string]
footing_material_name [string]
footing_depth [number] (Default: 0.3)
blocks [Array of {custom_block_material_name, custom_block_depth, custom_block_x_position, custom_block_z_position}]

class Foundation:Kiva:Settings():
    '''
    Settings applied across all Kiva foundation calculations. Object is not required. If not defined, defaults will be applied.
    '''

soil_conductivity [number] (Default: 1.73)
soil_density [number] (Default: 1842.0)
soil_specific_heat [number] (Default: 419.0)
ground_solar_absorptivity [number] (Default: 0.9)
ground_thermal_absorptivity [number] (Default: 0.9)
ground_surface_roughness [number] (Default: 0.03)
far_field_width [number] (Default: 40.0)
deep_ground_boundary_condition [string] (Default: Autoselect)
deep_ground_depth [unknown field type] (Default: Autocalculate)
minimum_cell_dimension [number] (Default: 0.02)
maximum_cell_growth_coefficient [number] (Default: 1.5)
simulation_timestep [string] (Default: Hourly)

class SurfaceProperty:ExposedFoundationPerimeter():
    '''
    Defines the perimeter of a foundation floor that is exposed to the exterior environment through the floor. User may either define the total exposed perimeter, fraction of perimeter exposed or individually define which segments of the floor surface perimeter are exposed.
    '''

surface_name [string]
exposed_perimeter_calculation_method [string]
total_exposed_perimeter [number]
exposed_perimeter_fraction [number] (Default: 1.0)
surfaces [Array of {surface_segment_exposed}]

class SurfaceConvectionAlgorithm:Inside:AdaptiveModelSelections():
    '''
    Options to change the individual convection model equations for dynamic selection when using AdaptiveConvectiongAlgorithm This object is only needed to make changes to the default model selections for any or all of the surface categories. This object is for the inside face, the side of the surface facing a thermal zone.
    '''

simple_buoyancy_vertical_wall_equation_source [string] (Default: FohannoPolidoriVerticalWall)
simple_buoyancy_vertical_wall_user_curve_name [string]
simple_buoyancy_stable_horizontal_equation_source [string] (Default: AlamdariHammondStableHorizontal)
simple_buoyancy_stable_horizontal_equation_user_curve_name [string]
simple_buoyancy_unstable_horizontal_equation_source [string] (Default: AlamdariHammondUnstableHorizontal)
simple_buoyancy_unstable_horizontal_equation_user_curve_name [string]
simple_buoyancy_stable_tilted_equation_source [string] (Default: WaltonStableHorizontalOrTilt)
simple_buoyancy_stable_tilted_equation_user_curve_name [string]
simple_buoyancy_unstable_tilted_equation_source [string] (Default: WaltonUnstableHorizontalOrTilt)
simple_buoyancy_unstable_tilted_equation_user_curve_name [string]
simple_buoyancy_windows_equation_source [string] (Default: ISO15099Windows)
simple_buoyancy_windows_equation_user_curve_name [string]
floor_heat_ceiling_cool_vertical_wall_equation_source [string] (Default: KhalifaEq3WallAwayFromHeat)
floor_heat_ceiling_cool_vertical_wall_equation_user_curve_name [string]
floor_heat_ceiling_cool_stable_horizontal_equation_source [string] (Default: AlamdariHammondStableHorizontal)
floor_heat_ceiling_cool_stable_horizontal_equation_user_curve_name [string]
floor_heat_ceiling_cool_unstable_horizontal_equation_source [string] (Default: KhalifaEq4CeilingAwayFromHeat)
floor_heat_ceiling_cool_unstable_horizontal_equation_user_curve_name [string]
floor_heat_ceiling_cool_heated_floor_equation_source [string] (Default: AwbiHattonHeatedFloor)
floor_heat_ceiling_cool_heated_floor_equation_user_curve_name [string]
floor_heat_ceiling_cool_chilled_ceiling_equation_source [string] (Default: KaradagChilledCeiling)
floor_heat_ceiling_cool_chilled_ceiling_equation_user_curve_name [string]
floor_heat_ceiling_cool_stable_tilted_equation_source [string] (Default: WaltonStableHorizontalOrTilt)
floor_heat_ceiling_cool_stable_tilted_equation_user_curve_name [string]
floor_heat_ceiling_cool_unstable_tilted_equation_source [string] (Default: WaltonUnstableHorizontalOrTilt)
floor_heat_ceiling_cool_unstable_tilted_equation_user_curve_name [string]
floor_heat_ceiling_cool_window_equation_source [string] (Default: ISO15099Windows)
floor_heat_ceiling_cool_window_equation_user_curve_name [string]
wall_panel_heating_vertical_wall_equation_source [string] (Default: KhalifaEq6NonHeatedWalls)
wall_panel_heating_vertical_wall_equation_user_curve_name [string]
wall_panel_heating_heated_wall_equation_source [string] (Default: AwbiHattonHeatedWall)
wall_panel_heating_heated_wall_equation_user_curve_name [string]
wall_panel_heating_stable_horizontal_equation_source [string] (Default: AlamdariHammondStableHorizontal)
wall_panel_heating_stable_horizontal_equation_user_curve_name [string]
wall_panel_heating_unstable_horizontal_equation_source [string] (Default: KhalifaEq7Ceiling)
wall_panel_heating_unstable_horizontal_equation_user_curve_name [string]
wall_panel_heating_stable_tilted_equation_source [string] (Default: WaltonStableHorizontalOrTilt)
wall_panel_heating_stable_tilted_equation_user_curve_name [string]
wall_panel_heating_unstable_tilted_equation_source [string] (Default: WaltonUnstableHorizontalOrTilt)
wall_panel_heating_unstable_tilted_equation_user_curve_name [string]
wall_panel_heating_window_equation_source [string] (Default: ISO15099Windows)
wall_panel_heating_window_equation_user_curve_name [string]
convective_zone_heater_vertical_wall_equation_source [string] (Default: FohannoPolidoriVerticalWall)
convective_zone_heater_vertical_wall_equation_user_curve_name [string]
convective_zone_heater_vertical_walls_near_heater_equation_source [string] (Default: KhalifaEq5WallNearHeat)
convective_zone_heater_vertical_walls_near_heater_equation_user_curve_name [string]
convective_zone_heater_stable_horizontal_equation_source [string] (Default: AlamdariHammondStableHorizontal)
convective_zone_heater_stable_horizontal_equation_user_curve_name [string]
convective_zone_heater_unstable_horizontal_equation_source [string] (Default: KhalifaEq7Ceiling)
convective_zone_heater_unstable_horizontal_equation_user_curve_name [string]
convective_zone_heater_stable_tilted_equation_source [string] (Default: WaltonStableHorizontalOrTilt)
convective_zone_heater_stable_tilted_equation_user_curve_name [string]
convective_zone_heater_unstable_tilted_equation_source [string] (Default: WaltonUnstableHorizontalOrTilt)
convective_zone_heater_unstable_tilted_equation_user_curve_name [string]
convective_zone_heater_windows_equation_source [string] (Default: ISO15099Windows)
convective_zone_heater_windows_equation_user_curve_name [string]
central_air_diffuser_wall_equation_source [string] (Default: GoldsteinNovoselacCeilingDiffuserWalls)
central_air_diffuser_wall_equation_user_curve_name [string]
central_air_diffuser_ceiling_equation_source [string] (Default: FisherPedersenCeilingDiffuserCeiling)
central_air_diffuser_ceiling_equation_user_curve_name [string]
central_air_diffuser_floor_equation_source [string] (Default: GoldsteinNovoselacCeilingDiffuserFloor)
central_air_diffuser_floor_equation_user_curve_name [string]
central_air_diffuser_window_equation_source [string] (Default: GoldsteinNovoselacCeilingDiffuserWindow)
central_air_diffuser_window_equation_user_curve_name [string]
mechanical_zone_fan_circulation_vertical_wall_equation_source [string] (Default: KhalifaEq3WallAwayFromHeat)
mechanical_zone_fan_circulation_vertical_wall_equation_user_curve_name [string]
mechanical_zone_fan_circulation_stable_horizontal_equation_source [string] (Default: AlamdariHammondStableHorizontal)
mechanical_zone_fan_circulation_stable_horizontal_equation_user_curve_name [string]
mechanical_zone_fan_circulation_unstable_horizontal_equation_source [string] (Default: KhalifaEq4CeilingAwayFromHeat)
mechanical_zone_fan_circulation_unstable_horizontal_equation_user_curve_name [string]
mechanical_zone_fan_circulation_stable_tilted_equation_source [string] (Default: WaltonStableHorizontalOrTilt)
mechanical_zone_fan_circulation_stable_tilted_equation_user_curve_name [string]
mechanical_zone_fan_circulation_unstable_tilted_equation_source [string] (Default: WaltonUnstableHorizontalOrTilt)
mechanical_zone_fan_circulation_unstable_tilted_equation_user_curve_name [string]
mechanical_zone_fan_circulation_window_equation_source [string] (Default: ISO15099Windows)
mechanical_zone_fan_circulation_window_equation_user_curve_name [string]
mixed_regime_buoyancy_assisting_flow_on_walls_equation_source [string] (Default: BeausoleilMorrisonMixedAssistedWall)
mixed_regime_buoyancy_assisting_flow_on_walls_equation_user_curve_name [string]
mixed_regime_buoyancy_opposing_flow_on_walls_equation_source [string] (Default: BeausoleilMorrisonMixedOpposingWall)
mixed_regime_buoyancy_opposing_flow_on_walls_equation_user_curve_name [string]
mixed_regime_stable_floor_equation_source [string] (Default: BeausoleilMorrisonMixedStableFloor)
mixed_regime_stable_floor_equation_user_curve_name [string]
mixed_regime_unstable_floor_equation_source [string] (Default: BeausoleilMorrisonMixedUnstableFloor)
mixed_regime_unstable_floor_equation_user_curve_name [string]
mixed_regime_stable_ceiling_equation_source [string] (Default: BeausoleilMorrisonMixedStableCeiling)
mixed_regime_stable_ceiling_equation_user_curve_name [string]
mixed_regime_unstable_ceiling_equation_source [string] (Default: BeausoleilMorrisonMixedUnstableCeiling)
mixed_regime_unstable_ceiling_equation_user_curve_name [string]
mixed_regime_window_equation_source [string] (Default: GoldsteinNovoselacCeilingDiffuserWindow)
mixed_regime_window_equation_user_curve_name [string]

class SurfaceConvectionAlgorithm:Outside:AdaptiveModelSelections():
    '''
    Options to change the individual convection model equations for dynamic selection when using AdaptiveConvectiongAlgorithm This object is only needed to make changes to the default model selections for any or all of the surface categories. This object is for the outside face, the side of the surface facing away from the thermal zone.
    '''

wind_convection_windward_vertical_wall_equation_source [string] (Default: TARPWindward)
wind_convection_windward_equation_vertical_wall_user_curve_name [string]
wind_convection_leeward_vertical_wall_equation_source [string] (Default: TARPLeeward)
wind_convection_leeward_vertical_wall_equation_user_curve_name [string]
wind_convection_horizontal_roof_equation_source [string] (Default: ClearRoof)
wind_convection_horizontal_roof_user_curve_name [string]
natural_convection_vertical_wall_equation_source [string] (Default: ASHRAEVerticalWall)
natural_convection_vertical_wall_equation_user_curve_name [string]
natural_convection_stable_horizontal_equation_source [string] (Default: WaltonStableHorizontalOrTilt)
natural_convection_stable_horizontal_equation_user_curve_name [string]
natural_convection_unstable_horizontal_equation_source [string] (Default: WaltonUnstableHorizontalOrTilt)
natural_convection_unstable_horizontal_equation_user_curve_name [string]

class SurfaceConvectionAlgorithm:Inside:UserCurve():
    '''
    Used to describe a custom model equation for surface convection heat transfer coefficient If more than one curve is referenced they are all used and added together.
    '''

reference_temperature_for_convection_heat_transfer [string]
hc_function_of_temperature_difference_curve_name [string]
hc_function_of_temperature_difference_divided_by_height_curve_name [string]
hc_function_of_air_change_rate_curve_name [string]
hc_function_of_air_system_volume_flow_rate_divided_by_zone_perimeter_length_curve_name [string]

class SurfaceConvectionAlgorithm:Outside:UserCurve():
    '''
    Used to describe a custom model equation for surface convection heat transfer coefficient If more than one curve is referenced they are all used and added together.
    '''

wind_speed_type_for_curve [string] (Default: HeightAdjust)
hf_function_of_wind_speed_curve_name [string]
hn_function_of_temperature_difference_curve_name [string]
hn_function_of_temperature_difference_divided_by_height_curve_name [string]

class SurfaceProperty:ConvectionCoefficients():
    '''
    Allow user settable interior and/or exterior convection coefficients. Note that some other factors may limit the lower bounds for these values, such as for windows, the interior convection coefficient must be >.28, for trombe wall algorithm selection (zone), the interior convection coefficient must be >.1 for TARP interior convection, the lower limit is also .1 Minimum and maximum limits are set in HeatBalanceAlgorithm object. Defaults in HeatBalanceAlgorithm object are [.1,1000].
    '''

surface_name [string]
convection_coefficient_1_location [string]
convection_coefficient_1_type [string]
convection_coefficient_1 [number]
convection_coefficient_1_schedule_name [string]
convection_coefficient_1_user_curve_name [string]
convection_coefficient_2_location [string]
convection_coefficient_2_type [string]
convection_coefficient_2 [number] (Default: 0.1)
convection_coefficient_2_schedule_name [string]
convection_coefficient_2_user_curve_name [string]

class SurfaceProperty:ConvectionCoefficients:MultipleSurface():
    '''
    Allow user settable interior and/or exterior convection coefficients. Note that some other factors may limit the lower bounds for these values, such as for windows, the interior convection coefficient must be >.28, for trombe wall algorithm selection (zone), the interior convection coefficient must be >.1 for TARP interior convection, the lower limit is also .1 Minimum and maximum limits are set in HeatBalanceAlgorithm object. Defaults in HeatBalanceAlgorithm object are [.1,1000].
    '''

surface_type [string]
convection_coefficient_1_location [string]
convection_coefficient_1_type [string]
convection_coefficient_1 [number]
convection_coefficient_1_schedule_name [string]
convection_coefficient_1_user_curve_name [string]
convection_coefficient_2_location [string]
convection_coefficient_2_type [string]
convection_coefficient_2 [number] (Default: 0.1)
convection_coefficient_2_schedule_name [string]
convection_coefficient_2_user_curve_name [string]

class SurfaceProperties:VaporCoefficients():
    '''
    The interior and external vapor transfer coefficients. Normally these value are calculated using the heat convection coefficient values. Use this object to used fixed constant values. Units are kg/Pa.s.m2 This will only work with the CombinedHeatAndMoistureFiniteElement algorithm for surfaces. Other algorithms will ignore these coefficients
    '''

surface_name [string]
constant_external_vapor_transfer_coefficient [string] (Default: No)
external_vapor_coefficient_value [number] (Default: 0.0)
constant_internal_vapor_transfer_coefficient [string] (Default: No)
internal_vapor_coefficient_value [number] (Default: 0.0)

class SurfaceProperty:ExteriorNaturalVentedCavity():
    '''
    Used to describe the decoupled layer, or baffle, and the characteristics of the cavity and openings for naturally ventilated exterior surfaces. This object is also used in conjunction with the OtherSideConditionsModel.
    '''

boundary_conditions_model_name [string]
area_fraction_of_openings [number]
thermal_emissivity_of_exterior_baffle_material [number]
solar_absorbtivity_of_exterior_baffle [number]
height_scale_for_buoyancy_driven_ventilation [number]
effective_thickness_of_cavity_behind_exterior_baffle [number]
ratio_of_actual_surface_area_to_projected_surface_area [number] (Default: 1.0)
roughness_of_exterior_surface [string]
effectiveness_for_perforations_with_respect_to_wind [number] (Default: 0.25)
discharge_coefficient_for_openings_with_respect_to_buoyancy_driven_flow [number] (Default: 0.65)
surface [Array of {surface_name}]

class SurfaceProperty:SolarIncidentInside():
    '''
    Used to provide incident solar radiation on the inside of the surface. Reference surface-construction pair and if that pair is used in a simulation, then program will use value provided in schedule instead of calculating it.
    '''

surface_name [string]
construction_name [string]
inside_surface_incident_sun_solar_radiation_schedule_name [string]

class SurfaceProperty:LocalEnvironment():
    '''
    This object defines the local environment properties of an exterior surface. One or more environment properties have to be defined and linked to the exterior surface.
    '''

exterior_surface_name [string]
external_shading_fraction_schedule_name [string]
surrounding_surfaces_object_name [string]
outdoor_air_node_name [string]

class ZoneProperty:LocalEnvironment():
    '''
    This object defines the local environment properties of a zone object. A corresponding outdoor air node should be defined and linked to the zone object.
    '''

zone_name [string]
outdoor_air_node_name [string]

class SurfaceProperty:SurroundingSurfaces():
    '''
    This object defines a list of surrounding surfaces for an exterior surface.
    '''

sky_view_factor [number] (Default: 0.5)
sky_temperature_schedule_name [string]
ground_view_factor [number] (Default: 0.5)
ground_temperature_schedule_name [string]
surfaces [Array of {surrounding_surface_name, surrounding_surface_view_factor, surrounding_surface_temperature_schedule_name}]

class ComplexFenestrationProperty:SolarAbsorbedLayers():
    '''
    Used to provide solar radiation absorbed in fenestration layers. References surface-construction pair and if that pair is used in a simulation, then program will use value provided in schedules instead of calculating it.
    '''

fenestration_surface [string]
construction_name [string]
layer_1_solar_radiation_absorbed_schedule_name [string]
layer_2_solar_radiation_absorbed_schedule_name [string]
layer_3_solar_radiation_absorbed_schedule_name [string]
layer_4_solar_radiation_absorbed_schedule_name [string]
layer_5_solar_radiation_absorbed_schedule_name [string]

class ZoneProperty:UserViewFactors:BySurfaceName():
    '''
    View factors for Surface to Surface in a zone. (Number of Surfaces)**2 are expected. Any omitted surface pairs will be assumed to have a view factor of zero.
    '''

zone_or_zonelist_or_space_or_spacelist_name [string]
view_factors [Array of {from_surface, to_surface, view_factor}]
"""
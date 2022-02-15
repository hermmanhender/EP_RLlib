'''
# Simulation parameters


'''
def Version(epJSON):
        """
        Specifies the EnergyPlus version of the IDF file.
        """
        version = epJSON["Version"]["Version 1"]["version_identifier"]
        return version

class SimulationControl():
    """
    Note that the following 3 fields are related to the Sizing:Zone, Sizing:System, and Sizing:Plant objects. Having these fields set to Yes but no corresponding Sizing object will not cause the sizing to be done. However, having any of these fields set to No, the corresponding Sizing object is ignored. Note also, if you want to do system sizing, you must also do zone sizing in the same run or an error will result.
    """
    def do_zone_sizing_calculation(epJSON, data="No"):
        epJSON["SimulationControl"]["SimulationControl 1"]["do_zone_sizing_calculation"] = data#[data] (Default: No)
        return epJSON
    
    def do_system_sizing_calculation(epJSON, data="No"):
        epJSON["SimulationControl"]["SimulationControl 1"]["do_system_sizing_calculation"] = data #[data] (Default: No)
        return epJSON
    
    def do_plant_sizing_calculation(epJSON, data="No"):
        epJSON["SimulationControl"]["SimulationControl 1"]["do_plant_sizing_calculation"] = data #[data] (Default: No)
        return epJSON

    def run_simulation_for_sizing_periods(epJSON, data="Yes"):
        epJSON["SimulationControl"]["SimulationControl 1"]["run_simulation_for_sizing_periods"] = data #[data] (Default: Yes)
        return epJSON

    def run_simulation_for_weather_file_run_periods(epJSON, data="Yes"):
        epJSON["SimulationControl"]["SimulationControl 1"]["run_simulation_for_weather_file_run_periods"] = data #[data] (Default: Yes)
        return epJSON

    def do_hvac_sizing_simulation_for_sizing_periods(epJSON, data="No"):
        epJSON["SimulationControl"]["SimulationControl 1"]["do_hvac_sizing_simulation_for_sizing_periods"] = data #[data] (Default: No)
        return epJSON
    
    def maximum_data_of_hvac_sizing_simulation_passes(epJSON, data=1.0):
        epJSON["SimulationControl"]["SimulationControl 1"]["maximum_data_of_hvac_sizing_simulation_passes"] = data #[data] (Default: 1.0)
        return epJSON

class PerformancePrecisionTradeoffs():
    """
    This object enables users to choose certain options that speed up EnergyPlus simulation, but may lead to small decreases in accuracy of results.
    """
    def use_coil_direct_solutions(epJSON, data="No"):
        epJSON["PerformancePrecisionTradeoffs"]["PerformancePrecisionTradeoffs 1"]["use_coil_direct_solutions"] = data # [data] (Default: No)
        return epJSON

    def zone_radiant_exchange_algorithm(epJSON, data="ScriptF"):
        epJSON["PerformancePrecisionTradeoffs"]["PerformancePrecisionTradeoffs 1"]["zone_radiant_exchange_algorithm"] = data # [data] (Default: ScriptF)
        return epJSON

    def override_mode(epJSON, data="Normal"):
        epJSON["PerformancePrecisionTradeoffs"]["PerformancePrecisionTradeoffs 1"]["override_mode"] = data # [data] (Default: Normal)
        return epJSON

    def maxzonetempdiff(epJSON, data=0.3):
        epJSON["PerformancePrecisionTradeoffs"]["PerformancePrecisionTradeoffs 1"]["maxzonetempdiff"] = data # [data] (Default: 0.3)
        return epJSON

    def maxalloweddeltemp(epJSON, data=0.002):
        epJSON["PerformancePrecisionTradeoffs"]["PerformancePrecisionTradeoffs 1"]["maxalloweddeltemp"] = data # [data] (Default: 0.002)
        return epJSON

    def use_representative_surfaces_for_calculations(epJSON, data="No"):
        epJSON["PerformancePrecisionTradeoffs"]["PerformancePrecisionTradeoffs 1"]["use_representative_surfaces_for_calculations"] = data # [data] (Default: No)
        return epJSON

class Building():
    """
    Describes parameters that are used during the simulation of the building. There are necessary correlations between the entries for this object and some entries in the Site:WeatherStation and Site:HeightVariation objects, specifically the Terrain field.
    """
    def north_axis(epJSON, data=0.0):
        epJSON["Building"]["Building 1"]["north_axis"] = data # [data] (Default: 0.0)
        return epJSON

    def terrain(epJSON, data="Suburbs"):
        epJSON["Building"]["Building 1"]["terrain"] = data # [data] (Default: Suburbs)
        return epJSON
    
    def loads_convergence_tolerance_value(epJSON, data=0.04):
        epJSON["Building"]["Building 1"]["loads_convergence_tolerance_value"] = data # [data] (Default: 0.04)
        return epJSON

    def temperature_convergence_tolerance_value(epJSON, data=0.4):
        epJSON["Building"]["Building 1"]["temperature_convergence_tolerance_value"] = data # [data] (Default: 0.4)
        return epJSON
    
    def solar_distribution(epJSON, data="FullExterior"):
        epJSON["Building"]["Building 1"]["solar_distribution"] = data # [data] (Default: FullExterior)
        return epJSON
    
    def maximum_data_of_warmup_days(epJSON, data=25.0):
        epJSON["Building"]["Building 1"]["maximum_data_of_warmup_days"] = data # [data] (Default: 25.0)
        return epJSON
    
    def minimum_data_of_warmup_days(epJSON, data=1.0):
        epJSON["Building"]["Building 1"]["minimum_data_of_warmup_days"] = data # [data] (Default: 1.0)
        return epJSON

class ShadowCalculation():
    """
    This object is used to control details of the solar, shading, and daylighting models.
    """
    def shading_calculation_method(epJSON, data="PolygonClipping", ObjectName="ShadowCalculation 1"):
        epJSON["ShadowCalculation"][ObjectName]["shading_calculation_method"] = data # shading_calculation_method [data] (Default: PolygonClipping)
        return epJSON

    def shading_calculation_update_frequency_method(epJSON, data="Periodic", ObjectName="ShadowCalculation 1"):
        epJSON["ShadowCalculation"][ObjectName]["shading_calculation_update_frequency_method"] = data # shading_calculation_update_frequency_method [data] (Default: Periodic)
        return epJSON

    def shading_calculation_update_frequency(epJSON, data=20.0, ObjectName="ShadowCalculation 1"):
        epJSON["ShadowCalculation"][ObjectName]["shading_calculation_update_frequency"] = data # shading_calculation_update_frequency [data] (Default: 20.0)
        return epJSON

    def maximum_figures_in_shadow_overlap_calculations(epJSON, data=15000.0, ObjectName="ShadowCalculation 1"):
        epJSON["ShadowCalculation"][ObjectName]["maximum_figures_in_shadow_overlap_calculations"] = data #maximum_figures_in_shadow_overlap_calculations [data] (Default: 15000.0)
        return epJSON

    def polygon_clipping_algorithm(epJSON, data="SutherlandHodgman", ObjectName="ShadowCalculation 1"):
        epJSON["ShadowCalculation"][ObjectName]["polygon_clipping_algorithm"] = data # polygon_clipping_algorithm [data] (Default: SutherlandHodgman)
        return epJSON

    def pixel_counting_resolution(epJSON, data=512.0, ObjectName="ShadowCalculation 1"):
        epJSON["ShadowCalculation"][ObjectName]["pixel_counting_resolution"] = data #pixel_counting_resolution [data] (Default: 512.0)
        return epJSON

    def sky_diffuse_modeling_algorithm(epJSON, data="SimpleSkyDiffuseModeling", ObjectName="ShadowCalculation 1"):
        epJSON["ShadowCalculation"][ObjectName]["sky_diffuse_modeling_algorithm"] = data #sky_diffuse_modeling_algorithm [data] (Default: SimpleSkyDiffuseModeling)
        return epJSON

    def output_external_shading_calculation_results(epJSON, data="No", ObjectName="ShadowCalculation 1"):
        epJSON["ShadowCalculation"][ObjectName]["output_external_shading_calculation_results"] = data # output_external_shading_calculation_results [data] (Default: No)
        return epJSON

    def disable_self_shading_within_shading_zone_groups(epJSON, data="No", ObjectName="ShadowCalculation 1"):
        epJSON["ShadowCalculation"][ObjectName]["disable_self_shading_within_shading_zone_groups"] = data # disable_self_shading_within_shading_zone_groups [data] (Default: No)
        return epJSON

    def disable_self_shading_from_shading_zone_groups_to_other_zones(epJSON, data="No", ObjectName="ShadowCalculation 1"):
        epJSON["ShadowCalculation"][ObjectName]["disable_self_shading_from_shading_zone_groups_to_other_zones"] = data # disable_self_shading_from_shading_zone_groups_to_other_zones [data] (Default: No)
        return epJSON

    def shading_zone_groups(epJSON, data, ObjectName="ShadowCalculation 1"):
        """
        data is an [Array of {shading_zone_group_zonelist_name}]
        """
        epJSON["ShadowCalculation"][ObjectName]["shading_zone_groups"] = data
        return epJSON

class SurfaceConvectionAlgorithm_Inside():
    """
    Default indoor surface heat transfer convection algorithm to be used for all zones.
    """
    def algorithm(epJSON, data="TARP"):
        epJSON["SurfaceConvectionAlgorithm:Inside"]["SurfaceConvectionAlgorithm:Inside 1"]["algorithm"] = data # [data] (Default: TARP)
        return epJSON

class SurfaceConvectionAlgorithm_Outside():
    """
    Default outside surface heat transfer convection algorithm to be used for all zones.
    """
    def algorithm(epJSON, data="DOE-2"):
        epJSON["SurfaceConvectionAlgorithm:Outside"]["SurfaceConvectionAlgorithm:Outside 1"]["algorithm"] = data # [data] (Default: TARP)
        return epJSON

class HeatBalanceAlgorithm():
    """
    Determines which Heat Balance Algorithm will be used ie. CTF (Conduction Transfer Functions),     EMPD (Effective Moisture Penetration Depth with Conduction Transfer Functions). Advanced/Research Usage: CondFD (Conduction Finite Difference) Advanced/Research Usage: ConductionFiniteDifferenceSimplified Advanced/Research Usage: HAMT (Combined Heat And Moisture Finite Element).
    """
    def algorithm(epJSON, data="ConductionTransferFunction"):
        epJSON["HeatBalanceAlgorithm"]["HeatBalanceAlgorithm 1"]["algorithm"] = data # [data] (Default: ConductionTransferFunction)
        return epJSON
    
    def surface_temperature_upper_limit(epJSON, data=200.0):
        epJSON["HeatBalanceAlgorithm"]["HeatBalanceAlgorithm 1"]["surface_temperature_upper_limit"] = data # [data] (Default: 200.0)
        return epJSON

    def minimum_surface_convection_heat_transfer_coefficient_value(epJSON, data=0.1):
        epJSON["HeatBalanceAlgorithm"]["HeatBalanceAlgorithm 1"]["minimum_surface_convection_heat_transfer_coefficient_value"] = data # [data] (Default: 0.1)
        return epJSON

    def maximum_surface_convection_heat_transfer_coefficient_value(epJSON, data=1000.0):
        epJSON["HeatBalanceAlgorithm"]["HeatBalanceAlgorithm 1"]["maximum_surface_convection_heat_transfer_coefficient_value"] = data # [data] (Default: 1000.0)
        return epJSON

class HeatBalanceSettings_ConductionFiniteDifference():
    """
    Determines settings for the Conduction Finite Difference algorithm for surface heat transfer modeling.
    """
    def difference_scheme(epJSON, data="FullyImplicitFirstOrder"):
        epJSON["HeatBalanceSettings:ConductionFiniteDifference"]["HeatBalanceSettings:ConductionFiniteDifference 1 "]["difference_scheme"] = data # [data] (Default: FullyImplicitFirstOrder)
        return epJSON
    
    def space_discretization_constant(epJSON, data=3.0):
        epJSON["HeatBalanceSettings:ConductionFiniteDifference"]["HeatBalanceSettings:ConductionFiniteDifference 1 "]["space_discretization_constant"] = data # [data] (Default: 3.0)
        return epJSON
    
    def relaxation_factor(epJSON, data=1.0):
        epJSON["HeatBalanceSettings:ConductionFiniteDifference"]["HeatBalanceSettings:ConductionFiniteDifference 1 "]["relaxation_factor"] = data # [data] (Default: 1.0)
        return epJSON
    
    def inside_face_surface_temperature_convergence_criteria(epJSON, data=0.002):
        epJSON["HeatBalanceSettings:ConductionFiniteDifference"]["HeatBalanceSettings:ConductionFiniteDifference 1 "]["inside_face_surface_temperature_convergence_criteria"] = data # [data] (Default: 0.002)
        return epJSON

class ZoneAirHeatBalanceAlgorithm():
    """
    Determines which algorithm will be used to solve the zone air heat balance.
    """
    def algorithm(epJSON, data="ThirdOrderBackwardDifference"):
        epJSON["ZoneAirHeatBalanceAlgorithm"]["ZoneAirHeatBalanceAlgorithm 1"]["algorithm"] = data # [data] (Default: ThirdOrderBackwardDifference)
        return epJSON

class ZoneAirContaminantBalance():
    """
    Determines which contaminant concentration will be simulates.
    """
    def carbon_dioxide_concentration(epJSON, data="No"):
        epJSON["ZoneAirContaminantBalance"]["ZoneAirContaminantBalance 1"]["carbon_dioxide_concentration"] = data #[data] (Default: No)
        return epJSON

    def outdoor_carbon_dioxide_schedule_name(epJSON, data=str):
        epJSON["ZoneAirContaminantBalance"]["ZoneAirContaminantBalance 1"]["outdoor_carbon_dioxide_schedule_name"] = data #[data]
        return epJSON

    def generic_contaminant_concentration(epJSON, data="No"):
        epJSON["ZoneAirContaminantBalance"]["ZoneAirContaminantBalance 1"]["generic_contaminant_concentration"] = data #[data] (Default: No)
        return epJSON

    def outdoor_generic_contaminant_schedule_name(epJSON, data=str):
        epJSON["ZoneAirContaminantBalance"]["ZoneAirContaminantBalance 1"]["outdoor_generic_contaminant_schedule_name"] = data #[data]
        return epJSON

class ZoneAirMassFlowConservation():
    """
    Enforces the zone air mass flow balance by either adjusting zone mixing object flow only, adjusting zone total return flow only, zone mixing and the zone total return flows, or adjusting the zone total return and zone mixing object flows. Zone infiltration flow air flow is increased or decreased depending user selection in the infiltration treatment method. If either of zone mixing or zone return flow adjusting methods or infiltration is active, then the zone air mass flow balance calculation will attempt to enforce conservation of mass for each zone. If flow balancing method is “None” and infiltration is “None”, then the zone air mass flow calculation defaults to assume self-balanced simple flow mixing and infiltration objects.
    """
    def adjust_zone_mixing_and_return_for_air_mass_flow_balance(epJSON, data="None"):
        epJSON["ZoneAirMassFlowConservation"]["ZoneAirMassFlowConservation 1"]["adjust_zone_mixing_and_return_for_air_mass_flow_balance"] = data # [data] (Default: None)
        return epJSON

    def infiltration_balancing_method(epJSON, data="AddInfiltrationFlow"):
        epJSON["ZoneAirMassFlowConservation"]["ZoneAirMassFlowConservation 1"]["infiltration_balancing_method"] = data  # [data] (Default: AddInfiltrationFlow)
        return epJSON

    def infiltration_balancing_zones(epJSON, data="MixingSourceZonesOnly"):    
        epJSON["ZoneAirMassFlowConservation"]["ZoneAirMassFlowConservation 1"]["infiltration_balancing_zones"] = data  # [data] (Default: MixingSourceZonesOnly)
        return epJSON

class ZoneCapacitanceMultiplier_ResearchSpecial():
    """
    Multiplier altering the relative capacitance of the air compared to an empty zone
    """
    def zone_or_zonelist_name(epJSON, data=str):
        epJSON["ZoneCapacitanceMultiplier:ResearchSpecial"]["ZoneCapacitanceMultiplier:ResearchSpecial 1"]["zone_or_zonelist_name"] = data # [data]
        return epJSON

    def temperature_capacity_multiplier(epJSON, data=1.0):
        epJSON["ZoneCapacitanceMultiplier:ResearchSpecial"]["ZoneCapacitanceMultiplier:ResearchSpecial 1"]["temperature_capacity_multiplier"] = data # [data] (Default: 1.0)
        return epJSON

    def humidity_capacity_multiplier(epJSON, data=1.0):
        epJSON["ZoneCapacitanceMultiplier:ResearchSpecial"]["ZoneCapacitanceMultiplier:ResearchSpecial 1"]["humidity_capacity_multiplier"] = data # [data] (Default: 1.0)
        return epJSON

    def carbon_dioxide_capacity_multiplier(epJSON, data=1.0):
        epJSON["ZoneCapacitanceMultiplier:ResearchSpecial"]["ZoneCapacitanceMultiplier:ResearchSpecial 1"]["carbon_dioxide_capacity_multiplier"] = data # [data] (Default: 1.0)
        return epJSON

    def generic_contaminant_capacity_multiplier(epJSON, data=1.0):
        epJSON["ZoneCapacitanceMultiplier:ResearchSpecial"]["ZoneCapacitanceMultiplier:ResearchSpecial 1"]["generic_contaminant_capacity_multiplier"] = data # [data] (Default: 1.0)
        return epJSON

class Timestep():
    """
    Specifies the “basic” timestep for the simulation. The value entered here is also known as the Zone Timestep. This is used in the Zone Heat Balance Model calculation as the driving timestep for heat transfer and load calculations.
    """
    def data_of_timesteps_per_hour(epJSON, data=6.0):
        epJSON["Timestep"]["Timestep 1"]["data_of_timesteps_per_hour"] = data # [data] (Default: 6.0)
        return epJSON

class ConvergenceLimits():
    """
    Specifies limits on HVAC system simulation timesteps and iterations. This item is an advanced feature that should be used only with caution.
    """
    def minimum_system_timestep(epJSON, data):
        epJSON["ConvergenceLimits"]["ConvergenceLimits 1"]["minimum_system_timestep"] = data # [data]
        return epJSON
        
    def maximum_hvac_iterations(epJSON, data):
        epJSON["ConvergenceLimits"]["ConvergenceLimits 1"]["maximum_hvac_iterations"] = data # [data] (Default: 20.0)
        return epJSON
        
    def minimum_plant_iterations(epJSON, data):
        epJSON["ConvergenceLimits"]["ConvergenceLimits 1"]["minimum_plant_iterations"] = data # [data] (Default: 2.0)
        return epJSON
        
    def maximum_plant_iterations(epJSON, data):
        epJSON["ConvergenceLimits"]["ConvergenceLimits 1"]["maximum_plant_iterations"] = data # [data] (Default: 8.0)
        return epJSON


class HVACSystemRootFindingAlgorithm():
    """
    Specifies a HVAC system solver algorithm to find a root
    """
    def algorithm(epJSON, data="RegulaFalsi"):
        epJSON["HVACSystemRootFindingAlgorithm"]["HVACSystemRootFindingAlgorithm 1"]["algorithm"] = data # [data] (Default: RegulaFalsi)
        return epJSON

    def data_of_iterations_before_algorithm_switch(epJSON, data=5.0):
        epJSON["HVACSystemRootFindingAlgorithm"]["HVACSystemRootFindingAlgorithm 1"]["data_of_iterations_before_algorithm_switch"] = data # [data] (Default: 5.0)
        return epJSON
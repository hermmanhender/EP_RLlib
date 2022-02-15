"""
# Economics
"""
"""
CurrencyType
If CurrencyType is not specified, it will default to USD and produce $ in the reports.

Fields

monetary_unit [string]
ComponentCost:Adjustments
Used to perform various modifications to the construction costs to arrive at an estimate for total project costs. This object allows extending the line item model so that the overall costs of the project will reflect various profit and fees.

Fields

miscellaneous_cost_per_conditioned_area [number]
design_and_engineering_fees [number]
contractor_fee [number]
contingency [number]
permits_bonding_and_insurance [number]
commissioning_fee [number]
regional_adjustment_factor [number]
ComponentCost:Reference
Used to allow comparing the current cost estimate to the results of a previous estimate for a reference building. This object parallels the ComponentCost:Adjustments object but adds a field for entering the cost line item model result for the reference building. The factors entered in this object are applied to the reference building while the factors listed in the ComponentCost:Adjustments object are applied to the current building model cost estimate.

Fields

reference_building_line_item_costs [number]
reference_building_miscellaneous_cost_per_conditioned_area [number]
reference_building_design_and_engineering_fees [number]
reference_building_contractor_fee [number]
reference_building_contingency [number]
reference_building_permits_bonding_and_insurance [number]
reference_building_commissioning_fee [number]
reference_building_regional_adjustment_factor [number]
ComponentCost:LineItem
Each instance of this object creates a cost line item and will contribute to the total for a cost estimate.

Fields

type [string]
line_item_type [string]
item_name [string]
object_end_use_key [string]
cost_per_each [number]
cost_per_area [number]
cost_per_unit_of_output_capacity [number]
cost_per_unit_of_output_capacity_per_cop [number]
cost_per_volume [number]
cost_per_volume_rate [number]
cost_per_energy_per_temperature_difference [number]
quantity [number]
UtilityCost:Tariff
Defines the name of a utility cost tariff, the type of tariff, and other details about the overall tariff. Each other object that is part of the tariff model references the tariff name. See UtilityCost:Charge:Simple, UtilityCost:Charge:Block, UtilityCost:Ratchet, UtilityCost:Qualify, UtilityCost:Variable and UtilityCost:Computation objects.

Fields

output_meter_name [string]
conversion_factor_choice [string]
energy_conversion_factor [number]
demand_conversion_factor [number]
time_of_use_period_schedule_name [string]
season_schedule_name [string]
month_schedule_name [string]
demand_window_length [string]
monthly_charge_or_variable_name [unknown field type]
minimum_monthly_charge_or_variable_name [unknown field type]
real_time_pricing_charge_schedule_name [string]
customer_baseline_load_schedule_name [string]
group_name [string]
buy_or_sell [string] (Default: BuyFromUtility)
UtilityCost:Qualify
The qualify object allows only tariffs to be selected based on limits which may apply such as maximum or minimum demand requirements. If the results of the simulation fall outside of the range of qualifications, that tariff is still calculated but the “Qualified” entry will say “No” and the UtilityCost:Qualify that caused its exclusion is shown. Multiple UtilityCost:Qualify objects can appear for the same tariff and they can be based on any variable.

Fields

utility_cost_qualify_name [string]
tariff_name [string]
variable_name [string]
qualify_type [string] (Default: Maximum)
threshold_value_or_variable_name [unknown field type]
season [string]
threshold_test [string] (Default: Consecutive)
number_of_months [number]
UtilityCost:Charge:Simple
UtilityCost:Charge:Simple is one of the most often used objects for tariff calculation. It is used to compute energy and demand charges that are very simple. It may also be used for taxes, surcharges and any other charges that occur on a utility bill. Multiple UtilityCost:Charge:Simple objects may be defined for a single tariff and they will be added together.

Fields

utility_cost_charge_simple_name [string]
tariff_name [string]
source_variable [string]
season [string]
category_variable_name [string]
cost_per_unit_value_or_variable_name [unknown field type]
UtilityCost:Charge:Block
Used to compute energy and demand charges (or any other charges) that are structured in blocks of charges. Multiple UtilityCost:Charge:Block objects may be defined for a single tariff and they will be added together.

Fields

utility_cost_charge_block_name [string]
tariff_name [string]
source_variable [string]
season [string] (Default: Annual)
category_variable_name [string]
remaining_into_variable [string]
block_size_multiplier_value_or_variable_name [unknown field type]
block_size_1_value_or_variable_name [unknown field type]
block_1_cost_per_unit_value_or_variable_name [unknown field type]
block_size_2_value_or_variable_name [unknown field type]
block_2_cost_per_unit_value_or_variable_name [unknown field type]
block_size_3_value_or_variable_name [unknown field type]
block_3_cost_per_unit_value_or_variable_name [unknown field type]
block_size_4_value_or_variable_name [unknown field type]
block_4_cost_per_unit_value_or_variable_name [unknown field type]
block_size_5_value_or_variable_name [unknown field type]
block_5_cost_per_unit_value_or_variable_name [unknown field type]
block_size_6_value_or_variable_name [unknown field type]
block_6_cost_per_unit_value_or_variable_name [unknown field type]
block_size_7_value_or_variable_name [unknown field type]
block_7_cost_per_unit_value_or_variable_name [unknown field type]
block_size_8_value_or_variable_name [unknown field type]
block_8_cost_per_unit_value_or_variable_name [unknown field type]
block_size_9_value_or_variable_name [unknown field type]
block_9_cost_per_unit_value_or_variable_name [unknown field type]
block_size_10_value_or_variable_name [unknown field type]
block_10_cost_per_unit_value_or_variable_name [unknown field type]
block_size_11_value_or_variable_name [unknown field type]
block_11_cost_per_unit_value_or_variable_name [unknown field type]
block_size_12_value_or_variable_name [unknown field type]
block_12_cost_per_unit_value_or_variable_name [unknown field type]
block_size_13_value_or_variable_name [unknown field type]
block_13_cost_per_unit_value_or_variable_name [unknown field type]
block_size_14_value_or_variable_name [unknown field type]
block_14_cost_per_unit_value_or_variable_name [unknown field type]
block_size_15_value_or_variable_name [unknown field type]
block_15_cost_per_unit_value_or_variable_name [unknown field type]
UtilityCost:Ratchet
Allows the modeling of tariffs that include some type of seasonal ratcheting. Ratchets are most common when used with electric demand charges. A ratchet is when a utility requires that the demand charge for a month with a low demand may be increased to be more consistent with a month that set a higher demand charge.

Fields

tariff_name [string]
baseline_source_variable [string]
adjustment_source_variable [string]
season_from [string]
season_to [string]
multiplier_value_or_variable_name [unknown field type]
offset_value_or_variable_name [unknown field type]
UtilityCost:Variable
Allows for the direct entry of monthly values into a utility tariff variable.

Fields

tariff_name [string]
variable_type [string] (Default: Dimensionless)
january_value [number]
february_value [number]
march_value [number]
april_value [number]
may_value [number]
june_value [number]
july_value [number]
august_value [number]
september_value [number]
october_value [number]
november_value [number]
december_value [number]
UtilityCost:Computation
The object lists a series of computations that are used to perform the utility bill calculation. The object is only used for complex tariffs that cannot be modeled any other way. For most utility tariffs, UtilityCost:Computation is unnecessary and should be avoided. If UtilityCost:Computation is used, it must contain references to all objects involved in the rate in the order that they should be computed.

Fields

tariff_name [string]
compute_step_1 [string]
compute_step_2 [string]
compute_step_3 [string]
compute_step_4 [string]
compute_step_5 [string]
compute_step_6 [string]
compute_step_7 [string]
compute_step_8 [string]
compute_step_9 [string]
compute_step_10 [string]
compute_step_11 [string]
compute_step_12 [string]
compute_step_13 [string]
compute_step_14 [string]
compute_step_15 [string]
compute_step_16 [string]
compute_step_17 [string]
compute_step_18 [string]
compute_step_19 [string]
compute_step_20 [string]
compute_step_21 [string]
compute_step_22 [string]
compute_step_23 [string]
compute_step_24 [string]
compute_step_25 [string]
compute_step_26 [string]
compute_step_27 [string]
compute_step_28 [string]
compute_step_29 [string]
compute_step_30 [string]
LifeCycleCost:Parameters
Provides inputs related to the overall life-cycle analysis. It establishes many of the assumptions used in computing the present value. It is important that when comparing the results of multiple simulations that the fields in the LifeCycleCost:Parameters objects are the same for all the simulations. When this object is present the tabular report file will contain the Life-Cycle Cost Report.

Fields

discounting_convention [string] (Default: EndOfYear)
inflation_approach [string] (Default: ConstantDollar)
real_discount_rate [number]
nominal_discount_rate [number]
inflation [number]
base_date_month [string] (Default: January)
base_date_year [number]
service_date_month [string] (Default: January)
service_date_year [number]
length_of_study_period_in_years [number]
tax_rate [number]
depreciation_method [string] (Default: None)
LifeCycleCost:RecurringCosts
Recurring costs are costs that repeat over time on a regular schedule during the study period. If costs associated with equipment do repeat but not on a regular schedule, use LifeCycleCost:NonrecurringCost objects instead.

Fields

category [string] (Default: Maintenance)
cost [number]
start_of_costs [string] (Default: ServicePeriod)
years_from_start [number]
months_from_start [number]
repeat_period_years [number] (Default: 1.0)
repeat_period_months [number] (Default: 0.0)
annual_escalation_rate [number]
LifeCycleCost:NonrecurringCost
A non-recurring cost happens only once during the study period. For costs that occur more than once during the study period on a regular schedule, use the LifeCycleCost:RecurringCost object.

Fields

category [string] (Default: Construction)
cost [number]
start_of_costs [string] (Default: ServicePeriod)
years_from_start [number]
months_from_start [number]
LifeCycleCost:UsePriceEscalation
Life cycle cost escalation factors. The values for this object may be found in the annual supplement to NIST Handbook 135 in Tables Ca-1 to Ca-5 and are included in an EnergyPlus dataset file.

Fields

lcc_price_escalation_name [string]
resource [string]
escalation_start_year [number]
escalation_start_month [string] (Default: January)
escalations [Array of {year_escalation}]
LifeCycleCost:UseAdjustment
Used by advanced users to adjust the energy or water use costs for future years. This should not be used for compensating for inflation but should only be used to increase the costs of energy or water based on assumed changes to the actual usage, such as anticipated changes in the future function of the building. The adjustments begin at the start of the service period.

Fields

resource [string]
multipliers [Array of {year_multiplier}]
"""
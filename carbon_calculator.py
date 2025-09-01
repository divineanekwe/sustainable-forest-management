# This script provides a model for calculating carbon sequestration.

def calculate_co2_sequestration(tree_biomass_growth_kg, carbon_content_percent = 0.5):
    """
    Calculates the amount of carbon dioxide sequestered by a tree.

    Args:
        tree_biomass_growth_kg (float): The annual increase in tree biomass in kilograms.
        carbon_content_percent (float): The percentage of biomass that is carbon. This is typically around 50% or 0.5.
    
    Returns:
        float: The amount of carbon dioxide sequestered in kilograms.
    """

    # Step 1: Calculate pure carbon sequestered
    sequestered_carbon_kg = tree_biomass_growth_kg * carbon_content_percent

    # Step 2: Convert carbon to carbon dioxide
    co2_conversion_factor = 3.67
    sequestered_co2_kg = sequestered_carbon_kg * co2_conversion_factor

    return sequestered_co2_kg

# Example usage:
# Let's say a young tree grows 50kg of biomass in one year.
biomass_growth = 50.0

# Calculate the sequestered carbon dioxide
carbon_dioxide_sequestered = calculate_co2_sequestration(biomass_growth)

print(f"Annual biomass growth: {biomass_growth} kg")
print(f"Annual carbon dioxde sequestered: {carbon_dioxide_sequestered:.2f} kg")
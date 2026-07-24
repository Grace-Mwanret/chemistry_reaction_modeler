class Compound:
    def __init__(self, name, formula, molar_mass):
        self.name = name
        self.formula = formula

        self.molar_mass = molar_mass
    def __str__(self):
        return f"Compound name: {self.name}\nFormula: {self.formula}\nMass: {self.molar_mass}g/mol"
    def moles_to_gram(self, moles):

        return moles * self.molar_mass

    def grams_to_moles(self, mass):
        return mass/self.molar_mass

class Reaction:
    def __init__(self, reactants, products):
        """
        reactants: list of (Compound, coefficient) tuples
        products: list of (Compound, coefficient) tuples
        """
        self.reactants = reactants
        self.products = products


    def __str__(self):
        reactants = " + ".join(
            f"{coefficient} {compound.formula}"
            for compound, coefficient in self.reactants
        )

        products = " + ".join(
            f"{coefficient} {compound.formula}"
            for compound, coefficient in self.products
        )

        return f"{reactants} ---> {products}"


    def total_mass_reactants(self):
        total = 0
        for compound, coefficient in self.reactants:
            total += compound.moles_to_gram(coefficient)
        return total


    def total_mass_products(self):
        total = 0
        for compound, coefficient in self.products:
            total += compound.moles_to_gram(coefficient)
        return total


    def is_balanced(self):
        if round(self.total_mass_reactants(), 4) == round(self.total_mass_products(), 4):
            return True
        else:
            return False

# Create compounds
hydrogen = Compound("Hydrogen", "H2", 2.016)
oxygen = Compound("Oxygen", "O2", 32.00)
water = Compound("Water", "H2O", 18.015)

# Test Compound.__str__()
print("=== Compound Information ===")
print(hydrogen)
print()
print(oxygen)
print()
print(water)

# Test moles_to_gram()
print("\n=== Moles to Grams ===")
print(f"2 moles of H2 = {hydrogen.moles_to_gram(2):.3f} g")
print(f"1 mole of O2 = {oxygen.moles_to_gram(1):.3f} g")
print(f"2 moles of H2O = {water.moles_to_gram(2):.3f} g")

# Test grams_to_moles()
print("\n=== Grams to Moles ===")
print(f"36.03 g of H2O = {water.grams_to_moles(36.03):.3f} mol")
print(f"64.00 g of O2 = {oxygen.grams_to_moles(64):.3f} mol")

# Create the reaction:
# 2H2 + O2 ---> 2H2O
reaction = Reaction(
    reactants=[
        (hydrogen, 2),
        (oxygen, 1)
    ],
    products=[
        (water, 2)
    ]
)

# Test Reaction.__str__()
print("\n=== Reaction ===")
print(reaction)

# Test total masses
print("\n=== Total Masses ===")
print(f"Reactants: {reaction.total_mass_reactants():.3f} g")
print(f"Products:  {reaction.total_mass_products():.3f} g")

# Test is_balanced()
print("\n=== Balanced? ===")
print(reaction.is_balanced())

# Test an UNBALANCED reaction
print("\n=== Unbalanced Reaction Test ===")
bad_reaction = Reaction(
    reactants=[
        (hydrogen, 1),   # only 1 mole of H2 instead of 2
        (oxygen, 1)
    ],
    products=[
        (water, 2)
    ]
)
print(bad_reaction)
print(f"Reactants: {bad_reaction.total_mass_reactants():.3f} g")
print(f"Products:  {bad_reaction.total_mass_products():.3f} g")
print(bad_reaction.is_balanced())


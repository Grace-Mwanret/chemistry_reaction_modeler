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



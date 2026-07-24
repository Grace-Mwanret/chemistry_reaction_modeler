# Chemical Reaction Calculator

## About

This project is a Python program that models chemical compounds and chemical reactions using object-oriented programming (OOP). It allows users to create compounds with their names, formulas, and molar masses, perform mole and gram conversions, and represent chemical reactions with reactants and products.

---

## What It Does

The program includes two main classes:

* **Compound**

  * Stores the compound's name, chemical formula, and molar mass.
  * Converts moles to grams.
  * Converts grams to moles.
  * Displays compound information in a readable format.

* **Reaction**

  * Stores the reactants and products of a chemical reaction.
  * Displays the reaction as a chemical equation.
  * Calculates the total mass of the reactants.
  * Calculates the total mass of the products.
  * Checks whether the reaction is balanced based on the total masses of the reactants and products.

---

## How to Run It

1. Make sure Python 3 is installed on your computer.
2. Save the project files.
3. Open a terminal or command prompt in the project folder.
4. Run the program using:

filename.py

Replace `filename.py` with the name of your Python file.

---

## What I Learned

Through this project, I learned how to:

* Create classes and objects in Python.
* Use constructors (`__init__`) to initialize objects.
* Write custom string representations using the `__str__` method.
* Build methods to perform calculations.
* Store and iterate through lists of tuples.
* Use tuple unpacking in `for` loops.
* Apply object-oriented programming concepts to solve chemistry-related problems.

---

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)

---

## Example input
### Create compounds
hydrogen = Compound("Hydrogen", "H2", 2.016)
oxygen = Compound("Oxygen", "O2", 32.00)
water = Compound("Water", "H2O", 18.015)

### Test Compound.__str__()
print("=== Compound Information ===")
print(hydrogen)
print()
print(oxygen)
print()
print(water)

### Test moles_to_gram()
print("\n=== Moles to Grams ===")
print(f"2 moles of H2 = {hydrogen.moles_to_gram(2):.3f} g")
print(f"1 mole of O2 = {oxygen.moles_to_gram(1):.3f} g")
print(f"2 moles of H2O = {water.moles_to_gram(2):.3f} g")

### Test grams_to_moles()
print("\n=== Grams to Moles ===")
print(f"36.03 g of H2O = {water.grams_to_moles(36.03):.3f} mol")
print(f"64.00 g of O2 = {oxygen.grams_to_moles(64):.3f} mol")

### Create the reaction:
### 2H2 + O2 ---> 2H2O
reaction = Reaction(
    reactants=[
        (hydrogen, 2),
        (oxygen, 1)
    ],
    products=[
        (water, 2)
    ]
)

### Test Reaction.__str__()
print("\n=== Reaction ===")
print(reaction)

### Test total masses
print("\n=== Total Masses ===")
print(f"Reactants: {reaction.total_mass_reactants():.3f} g")
print(f"Products:  {reaction.total_mass_products():.3f} g")

### Test is_balanced()
print("\n=== Balanced? ===")
print(reaction.is_balanced())

### Test an UNBALANCED reaction
print("\n=== Unbalanced Reaction Test ===")
bad_reaction = Reaction(
    reactants=[
(hydrogen, 1)
(oxygen, 1)
],
    products=(water, 2)
    ]
)
print(bad_reaction)
print(f"Reactants: {bad_reaction.total_mass_reactants():.3f} g")
print(f"Products:  {bad_reaction.total_mass_products():.3f} g")
print(bad_reaction.is_balanced())


## Example output

=== Compound Information ===
Compound name: Hydrogen
Formula: H2
Mass: 2.016g/mol

Compound name: Oxygen
Formula: O2
Mass: 32.0g/mol

Compound name: Water
Formula: H2O
Mass: 18.015g/mol

=== Moles to Grams ===
2 moles of H2 = 4.032 g
1 mole of O2 = 32.000 g
2 moles of H2O = 36.030 g

=== Grams to Moles ===
36.03 g of H2O = 2.000 mol
64.00 g of O2 = 2.000 mol

=== Reaction ===
2 H2 + 1 O2 ---> 2 H2O

=== Total Masses ===
Reactants: 36.032 g
Products:  36.030 g

=== Balanced? ===
False

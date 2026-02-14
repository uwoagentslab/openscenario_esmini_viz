from datasets import load_dataset
import os

# Load the dataset
dataset = load_dataset("Ammara66/openscenario-dataset")

# Get the first scenario
scenario = dataset['train'][0]
xml_content = scenario['completion']

# Save the scenario to a file
output_file = 'acc_demo_scenario.xosc'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(xml_content)

print(f"OpenSCENARIO file created: {output_file}")
print(f"\nScenario description from prompt:")
print(scenario['prompt'])

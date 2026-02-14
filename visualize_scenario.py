#!/usr/bin/env python3
"""
Script to create and visualize OpenSCENARIO scenarios from the Hugging Face dataset.
"""

import os
import sys
import subprocess
from datasets import load_dataset

def list_scenarios():
    """List all available scenarios in the dataset."""
    print("Loading dataset...")
    dataset = load_dataset("Ammara66/openscenario-dataset")
    
    print(f"\nAvailable scenarios (Total: {len(dataset['train'])}):\n")
    print("-" * 80)
    
    for idx, scenario in enumerate(dataset['train']):
        prompt = scenario['prompt']
        # Extract scenario name from prompt
        lines = prompt.split('\n')
        scenario_line = [l for l in lines if 'Scenario:' in l]
        if scenario_line:
            scenario_name = scenario_line[0].replace('- Scenario:', '').strip()
            print(f"{idx:2d}. {scenario_name}")
        else:
            print(f"{idx:2d}. Scenario {idx}")
    
    print("-" * 80)

def create_and_run_scenario(index):
    """Create and run a scenario from the dataset."""
    print(f"Loading scenario {index}...")
    dataset = load_dataset("Ammara66/openscenario-dataset")
    
    if index < 0 or index >= len(dataset['train']):
        print(f"Error: Index must be between 0 and {len(dataset['train'])-1}")
        return False
    
    scenario = dataset['train'][index]
    
    print("\nScenario Details:")
    print("=" * 80)
    print(scenario['prompt'])
    print("=" * 80)
    
    # Save the scenario
    output_file = 'esmini-demo/resources/xosc/dataset_scenario.xosc'
    xml_content = scenario['completion']
    
    # Fix paths in the XML to work with esmini structure
    xml_content = xml_content.replace('[[VEHICLE_CATALOG]]', '../Catalogs/Vehicles/')
    xml_content = xml_content.replace('[[ROAD_NETWORK]]', '')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(xml_content)
    
    print(f"\nScenario saved to: {output_file}")
    
    # Ask if user wants to run it
    response = input("\nRun this scenario with esmini? (y/n): ").strip().lower()
    
    if response == 'y':
        print("\nStarting esmini visualization...")
        print("Press ESC to quit, SPACE to pause/resume")
        print("-" * 80)
        
        # Run esmini
        try:
            subprocess.run([
                './esmini-demo/bin/esmini',
                '--window', '60', '60', '800', '400',
                '--osc', './esmini-demo/resources/xosc/dataset_scenario.xosc'
            ])
            print("\nVisualization complete!")
        except FileNotFoundError:
            print("Error: esmini not found. Make sure esmini-demo is in the current directory.")
        except Exception as e:
            print(f"Error running esmini: {e}")
    
    return True

def main():
    """Main function."""
    print("=" * 80)
    print("OpenSCENARIO Dataset Visualizer")
    print("=" * 80)
    print()
    
    if len(sys.argv) > 1:
        if sys.argv[1] == 'list':
            list_scenarios()
        else:
            try:
                index = int(sys.argv[1])
                create_and_run_scenario(index)
            except ValueError:
                print(f"Error: '{sys.argv[1]}' is not a valid index")
                print("Usage: python visualize_scenario.py [index|list]")
    else:
        print("Usage:")
        print("  python visualize_scenario.py list          - List all scenarios")
        print("  python visualize_scenario.py <index>       - Create and run scenario by index")
        print("\nExamples:")
        print("  python visualize_scenario.py list")
        print("  python visualize_scenario.py 0")
        print("  python visualize_scenario.py 5")

if __name__ == '__main__':
    main()

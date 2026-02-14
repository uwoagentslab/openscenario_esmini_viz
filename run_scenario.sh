#!/bin/bash

# Navigate to esmini directory
cd "$(dirname "$0")/esmini-demo"

# Run esmini with the ACC demo scenario
echo "Starting esmini visualization of ACC demo scenario..."
echo "==============================================="
echo ""
echo "Scenario: Demonstrate ACC controller"
echo "- White car (Ego) with ACC controller"
echo "- Red car (Target) performing maneuvers"
echo "- Watch the Ego vehicle maintain distance using ACC"
echo ""
echo "Controls:"
echo "  - Press ESC to quit"
echo "  - Press SPACE to pause/resume"
echo "  - Use arrow keys to move camera"
echo ""
echo "==============================================="
echo ""

# Run esmini
./bin/esmini --window 60 60 800 400 --osc ./resources/xosc/acc_demo_scenario.xosc

echo ""
echo "Visualization complete!"

# OpenSCENARIO Demo - ACC Controller Visualization

This project demonstrates creating and visualizing an OpenSCENARIO scenario using the Hugging Face dataset and esmini viewer.

## What's Included

### Files Created:
1. **acc_demo_scenario.xosc** - The OpenSCENARIO XML file demonstrating an ACC (Adaptive Cruise Control) controller
2. **run_scenario.sh** - Shell script to easily run the visualization
3. **explore_dataset.py** - Python script to explore the Hugging Face dataset
4. **create_scenario.py** - Python script to create scenario files from the dataset
5. **dataset_sample.csv** - CSV export of the dataset for reference

### Dataset Source
The scenario is based on data from: [Ammara66/openscenario-dataset](https://huggingface.co/datasets/Ammara66/openscenario-dataset)

This dataset contains 64 OpenSCENARIO examples with prompts and completions.

## Scenario Description

**Name:** ACC Controller Demonstration

**Description:** This scenario demonstrates an Adaptive Cruise Control (ACC) system where:
- A white car (Ego) is equipped with an ACC controller
- A red car (Target) performs various maneuvers ahead
- The Ego vehicle maintains a safe distance using ACC

**Sequence of Events:**
1. Both vehicles start on a straight 500m road
2. At t=5s: Target performs first lane change
3. At t=7s: Target performs second lane change (cut-in)
4. At t=11s: Target brakes hard
5. At t=17s: Target accelerates
6. At t=20s: Target brakes again

**Parameters:**
- EgoSpeed: 120 km/h
- TargetSpeed: 30 km/h
- Initial positions: Ego at 20m, Target at 100m
- Time gap for ACC: 1.0 seconds

## How to Run

### Prerequisites
- macOS (this demo uses the macOS version of esmini)
- Python 3.x (for dataset exploration)

### Running the Visualization

Simply execute the run script:

```bash
./run_scenario.sh
```

### Keyboard Controls During Visualization:
- **ESC** - Quit the simulation
- **SPACE** - Pause/Resume
- **Arrow Keys** - Move camera
- **TAB** - Switch camera mode
- **K** - Show/hide key information
- **I** - Show/hide info text

## Technical Details

### esmini
[esmini](https://github.com/esmini/esmini) is an open-source basic OpenSCENARIO player that provides:
- 3D visualization of scenarios
- Support for OpenSCENARIO 1.0, 1.1, and 1.2
- Vehicle dynamics simulation
- Controller support (including ACC)

### OpenSCENARIO
OpenSCENARIO is an open file format (XML) for the description of scenarios for driving simulation. It's used extensively in:
- Autonomous vehicle development
- ADAS (Advanced Driver Assistance Systems) testing
- Driver training simulation
- Safety validation

### File Structure
```
openscenario/
├── esmini-demo/              # esmini installation
│   ├── bin/                  # Executables (esmini, odrviewer, etc.)
│   └── resources/
│       ├── xosc/             # Scenario files (.xosc)
│       ├── xodr/             # Road network files (.xodr)
│       ├── models/           # 3D models
│       └── Catalogs/         # Vehicle and controller catalogs
├── run_scenario.sh           # Run script
├── explore_dataset.py        # Dataset exploration script
└── create_scenario.py        # Scenario creation script
```

## Exploring More Scenarios

The dataset contains 64 different scenarios. To explore them:

```bash
python explore_dataset.py
```

To create a different scenario from the dataset:

```python
from datasets import load_dataset

dataset = load_dataset("Ammara66/openscenario-dataset")

# Get a different scenario (index 0-63)
scenario = dataset['train'][5]  # Change index

# Save it
with open('my_scenario.xosc', 'w') as f:
    f.write(scenario['completion'])
```

## Resources

- [esmini GitHub](https://github.com/esmini/esmini)
- [OpenSCENARIO Standard](https://www.asam.net/standards/detail/openscenario/)
- [Dataset on Hugging Face](https://huggingface.co/datasets/Ammara66/openscenario-dataset)
- [OpenDRIVE Standard](https://www.asam.net/standards/detail/opendrive/) (for road networks)

## License

- The dataset is from Hugging Face (check dataset page for license)
- esmini is licensed under MPL 2.0
- This demo code is provided as-is for educational purposes

## Troubleshooting

### If the window doesn't appear:
1. Check that you're running on macOS
2. Ensure esmini has permissions to create windows
3. Try running from the esmini-demo directory directly:
   ```bash
   cd esmini-demo
   ./bin/esmini --osc resources/xosc/acc_demo_scenario.xosc
   ```

### If you see "file not found" errors:
- Make sure you're running from the openscenario directory
- Check that esmini-demo was extracted properly

### For other issues:
- Check the log file: `esmini-demo/log.txt`
- Consult [esmini documentation](https://esmini.github.io/)

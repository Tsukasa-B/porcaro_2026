# Porcaro 2026: Embodied AI Dual-Arm Drumming Project

This repository contains the official implementation of the paper:
*"Embodied Drumming: Sim-to-Real Reinforcement Learning for Pneumatic Musculoskeletal Robots via Generalized Rhythm Modeling"* (Submitted to IROS 2026).

This project simulates and trains **Porcaro**, a drumming robot driven by Pneumatic Artificial Muscles (PAMs), utilizing the highly parallelized **NVIDIA Isaac Lab** environment (Direct Workflow).

## 📁 Repository Structure

```text
porcaro_2026/
 ├── scripts/                         # Execution scripts for training and inference
 │   ├── rsl_rl/                      
 │   │   ├── train.py                 # Main training script
 │   │   └── play.py                  # Inference and visualization script
 ├── source/
 │   └── porcaro_2026/                # Core extension package
 │       ├── config/                  # Extension configuration (extension.toml)
 │       └── porcaro_2026/
 │           ├── assets/              # 3D models (USD files) and MIDI datasets
 │           ├── tasks/direct/porcaro_2026/
 │           │   ├── envs/            # Main environment definitions (DirectEnv)
 │           │   ├── actions/         # PAM dynamics & delayed action models (Model B)
 │           │   └── rewards/         # Event-based rhythm reward functions
 ├── pyproject.toml                   # Python package dependencies
 └── README.md
```


## 🛠️ Requirements & Installation
We recommend using Miniconda to manage your Python environment. By following these steps, you can set up the environment exactly as it was used in our experiments.

**0. Setup a Miniconda**
```bash
# 1. Create a directory for installation
mkdir -p ~/miniconda3

# 2. Download the installer for Linux (using wget)
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh

# 3. Run the installation in silent mode.
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3

# 4. Remove unnecessary installers
rm ~/miniconda3/miniconda.sh

# 5. Initialization settings to associate the conda command with a shell (for bash)
~/miniconda3/bin/conda init bash
```

**1. Create a Miniconda Environment**
```bash
conda create -n porcaro_env python=3.10
conda activate porcaro_env
```
**2. Install NVIDIA Isaac Lab**

This project is built as an extension for NVIDIA Isaac Lab. You must install the core Isaac Lab framework first.
Please follow the Official Isaac Lab Installation Guide.

(Note: Ensure Isaac Lab is installed in your porcaro_env conda environment).

**3. Install the Porcaro 2026 Repository**

Once Isaac Lab is successfully installed, clone this repository and install it as an editable python package.
```bash
# Clone the repository
git clone [https://github.com/Tsukasa-B/porcaro_2026.git](https://github.com/Tsukasa-B/porcaro_2026.git)
cd porcaro_2026

# Install the extension into your Isaac Lab environment
# (Replace the path below with your actual Isaac Lab path)
/path/to/IsaacLab/isaaclab.sh -p -m pip install -e source/porcaro_2026
```

*That's it! The environment is now fully linked and ready to run.*

## 🎮 Usage
You can launch the training and evaluation scripts directly from the terminal. We use rsl_rl for highly optimized Proximal Policy Optimization (PPO).

Training
To train the dual-arm drumming policy from scratch:
```bash
python scripts/rsl_rl/train.py --task=Isaac-Porcaro-Dual-Direct-v0
```

Evaluation (Playing)
To watch the trained agent perform in the simulation GUI:
```bash
python scripts/rsl_rl/play.py --task=Isaac-Porcaro-Dual-Direct-v0
```

## 🤖 3D Assets & MIDI Datasets
The required 3D robot models (.usd) and the evaluation MIDI datasets (Groove MIDI Dataset format) are included in the source/porcaro_2026/porcaro_2026/assets/ directory. The environment will automatically load them upon initialization.
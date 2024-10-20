import argparse
import os
from pathlib import Path


def run_xtb_command(folder, charge, system_to_calculate, xtb_method):
    """
    Runs the xtb command for a given folder, charge, and system.
    
    Args:
        folder (str): Path to the folder containing the files.
        charge (int): Charge for the specified system.
        system_to_calculate (str): System to calculate ('receptor', 'ligand', or 'combined').
        xtb_method (str): xtb method to use ('gfnff' or 'gfn2').
    """
    # Prepare xtb method
    method_flag = "--gfnff" if xtb_method == "gfnff" else ""

    # Determine the file based on system to calculate
    if system_to_calculate == "receptor":
        system_file = f"{Path(folder).stem}_receptor"
    elif system_to_calculate == "ligand":
        system_file = f"{Path(folder).stem}_ligand"
    else:
        system_file = f"{Path(folder).stem}_combined"

    # Full path to the xyz file
    xyz_file = os.path.join(folder, f"{system_file}.xyz")
    output_file = os.path.join(folder, f"{system_file}_gfnff.txt")

    # Prepare charge flag (if non-zero)
    charge_flag = f"--chrg {charge}" if charge != 0 else ""

    # Construct xtb command
    command_combined = f"xtb {method_flag} {xyz_file} --hess --gbsa water {charge_flag} > {output_file}"

    # Print the final xtb command
    print(f"xtb command: {command_combined}")

    # Execute the xtb command
    os.system(command_combined)

def main():
    """
    Main function to parse arguments and run the xtb command.
    """
    # Parser for directory, xtb method, and system to calculate
    parser = argparse.ArgumentParser(description="Script to process XYZ files and run xtb commands")
    parser.add_argument(
        "-folder", 
        type=str, 
        default="M01/",
        help="Path to the folder containing the XYZ files."
    )
    parser.add_argument(
        "-method", 
        type=str, 
        choices=["gfnff", "gfn2"],
        default="gfnff", 
        help="XTB method to use ('gfnff' or 'gfn2')."
    )
    parser.add_argument(
        "-system", 
        type=str, 
        choices=["receptor", "ligand", "combined"],
        default="combined", 
        help="Specify whether to calculate the 'receptor', 'ligand', or 'combined' system."
    )
    parser.add_argument(
        "-charge", 
        type=int, 
        default=0,
        help="Charge of the specified system."
    )
    
    args = parser.parse_args()
    folder = args.folder
    xtb_method = args.method
    system_to_calculate = args.system
    charge = args.charge

    # Run xtb command for the specified system and method
    run_xtb_command(folder, charge, system_to_calculate, xtb_method)

if __name__ == "__main__":
    main()
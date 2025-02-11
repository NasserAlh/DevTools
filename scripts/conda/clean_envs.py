#!/usr/bin/env python3

import subprocess
import json
import sys
import os

def get_conda_environments():
    """Get list of all conda environments."""
    try:
        # Run conda env list --json to get environment information
        result = subprocess.run(['conda', 'env', 'list', '--json'], 
                              capture_output=True, text=True, check=True)
        env_data = json.loads(result.stdout)
        return env_data['envs']
    except subprocess.CalledProcessError as e:
        print(f"Error getting conda environments: {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error parsing conda environment data: {e}")
        sys.exit(1)

def remove_environment(env_path):
    """Remove a conda environment."""
    env_name = os.path.basename(env_path)
    print(f"\nRemoving environment: {env_name}")
    try:
        # Run without capturing output to show progress in real-time
        process = subprocess.run(['conda', 'env', 'remove', '--name', env_name, '--yes'],
                               check=True)
        print(f"Successfully removed {env_name}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error removing environment {env_name}: {e}")
        return False

def main():
    print("Starting conda environment cleanup...")
    
    # Get all environments
    envs = get_conda_environments()
    
    # Get base environment path
    base_prefix = sys.prefix
    
    # Filter out the base environment
    envs_to_remove = [env for env in envs if env != base_prefix]
    
    if not envs_to_remove:
        print("No environments to remove (only base environment exists).")
        return
    
    print(f"\nFound {len(envs_to_remove)} environment(s) to remove:")
    for env in envs_to_remove:
        print(f"- {os.path.basename(env)}")
    
    print("\nProceeding with removal...")
    
    # Remove each environment
    success_count = 0
    for env in envs_to_remove:
        if remove_environment(env):
            success_count += 1
    
    print(f"\nCleanup complete!")
    print(f"Successfully removed {success_count} out of {len(envs_to_remove)} environments.")

if __name__ == "__main__":
    main() 
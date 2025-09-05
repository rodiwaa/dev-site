#!/usr/bin/env python3.11

import subprocess
import os
import sys
import argparse
from dotenv import load_dotenv, find_dotenv, dotenv_values

load_dotenv(find_dotenv())

def env_test():
    env_path = find_dotenv()
    if env_path:
        env_vars = dotenv_values(env_path)
        for key, value in env_vars.items():
          print(f"{key} - {value}")

def run_command(command, shell=False):
    """Helper function to execute shell commands and handle errors."""
    try:
        if shell:
            subprocess.run(command, shell=True, check=True, text=True)
        else:
            subprocess.run(command, check=True, text=True)
        print(f"Successfully executed: {command}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing {command}: {e}")
        sys.exit(1)

def sync_s3():
    """Syncs current directory content to S3 bucket."""
    bucket_name = os.getenv("S3_BUCKET_NAME")  # Assumes bucket name is in env variable
    if not bucket_name:
        print("Error: S3_BUCKET_NAME environment variable not set.")
        sys.exit(1)
    
    command = ["aws", "s3", "sync", ".", f"s3://{bucket_name}"]
    run_command(command)

def serve_html():
    """Serves HTML files using Python's built-in HTTP server."""
    command = [sys.executable, "-m", "http.server", "8000"]
    print("Serving website on http://localhost:8000 (Ctrl+C to stop)")
    run_command(command)

def activate_venv():
    """Activates the virtual environment."""
    venv_path = os.path.join(os.getcwd(), "venv", "bin", "activate")
    if not os.path.exists(venv_path):
        print("Error: Virtual environment not found at ./venv")
        sys.exit(1)
    
    # Since we can't source in subprocess directly, inform user to run it
    print("To activate the virtual environment, run:")
    print(f"source {venv_path}")
    print("Note: This script can't activate the venv in the current shell.")
    print("After activation, rerun your command.")

def main():
    """Main function to handle command-line arguments."""
    parser = argparse.ArgumentParser(description="Website deployment management tool")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Subcommand: s3-sync
    subparsers.add_parser("s3-sync", help="Sync folder content to S3 bucket")

    # Subcommand: serve
    subparsers.add_parser("serve", help="Serve HTML files locally")

    # Subcommand: venv
    subparsers.add_parser("venv", help="Activate virtual environment")

    # Subcommand: env
    subparsers.add_parser("env", help="Tests .env variables")


    args = parser.parse_args()

    if args.command == "s3-sync":
        sync_s3()
    elif args.command == "serve":
        serve_html()
    elif args.command == "venv":
        activate_venv()
    elif args.command == "env":
        env_test()
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()
import ollama
import os
import subprocess

def get_sar_files():
    """
    Get a list of SAR files in the /var/log/sa directory.

    Returns:
        list: A list of SAR file paths.
    """
    sar_files = []
    for filename in os.listdir("/var/log/sa"):
        if filename.startswith("sa"):
            sar_files.append(os.path.join("/var/log/sa", filename))
    return sar_files

def parse_sar_file(filepath):
    """
    Parse a SAR file and return its content as a string.

    Args:
        filepath (str): The path to the SAR file.

    Returns:
        str: The content of the SAR file.
    """
    try:
        # Run the sar command to read the file
        result = subprocess.run(["sar", "-A", "-f", filepath], capture_output=True, text=True)
        return result.stdout
    except FileNotFoundError:
        return f"Error: 'sar' command not found. Please install the 'sysstat' package."
    except Exception as e:
        return f"An error occurred: {e}"

def ingest_data_to_ollama(data):
    """
    Ingest data into Ollama.

    Args:
        data (str): The data to ingest.
    """
    try:
        ollama.embeddings(model='llama2', prompt=data)
        print("Data ingested successfully.")
    except Exception as e:
        print(f"An error occurred while ingesting data into Ollama: {e}")

def main():
    """
    Main function to execute the SAR data ingestion process.
    """
    sar_files = get_sar_files()
    if not sar_files:
        print("No SAR files found in /var/log/sa.")
        return

    for sar_file in sar_files:
        print(f"Parsing SAR file: {sar_file}")
        sar_data = parse_sar_file(sar_file)
        if sar_data:
            print("Ingesting data into Ollama...")
            ingest_data_to_ollama(sar_data)

if __name__ == "__main__":
    main()

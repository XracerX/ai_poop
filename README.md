# SAR Data Ingestion with Ollama

This project provides a Python script to ingest system statistics from `sar` files into an Ollama instance. This allows you to use natural language queries to analyze system performance and troubleshoot issues.

## How it Works

The script works in three main stages:

1.  **File Discovery:** The script scans the `/var/log/sa` directory to find all `sar` data files.
2.  **Data Parsing:** It uses the `sar` command-line tool to parse each data file.
3.  **Data Ingestion:** The parsed data is then sent to an Ollama instance to be indexed for retrieval.

Here is a diagram of the process:

```
+------------------+      +------------------+      +-----------------+
|   SAR Data Files |----->|  sar_ingest.py   |----->|     Ollama      |
| (/var/log/sa/*)  |      | (Data Processor) |      | (LLM Instance)  |
+------------------+      +------------------+      +-----------------+
```

## Requirements

*   Python 3
*   `ollama` Python library
*   `sysstat` package (which provides the `sar` command)

## Installation

1.  **Install `sysstat`:**

    On Debian/Ubuntu:
    ```bash
    sudo apt-get update
    sudo apt-get install sysstat
    ```

    On Red Hat/CentOS:
    ```bash
    sudo yum install sysstat
    ```

2.  **Install Python libraries:**
    ```bash
    pip install ollama
    ```

## Usage

1.  **Ensure Ollama is running:**

    Make sure your Ollama instance is up and running. You can check its status by running:
    ```bash
    ollama list
    ```

2.  **Run the script:**
    ```bash
    python sar_ingest.py
    ```

    The script will automatically find your `sar` files, process them, and ingest the data into Ollama.

## How to Query Your Data

Once the data has been ingested, you can use the Ollama CLI or API to ask questions about your system's performance. For example:

```bash
ollama run llama2 "What were the top 5 processes with the highest CPU usage yesterday?"
```

```bash
ollama run llama2 "Were there any unusual memory usage patterns last week?"
```

## Contributing

Contributions are welcome! If you have any ideas for improvements or find any bugs, please open an issue or submit a pull request.


# Salesforce Data Model Hierarchy Extractor

## Introduction
The Salesforce Data Model Hierarchy Extractor is a tool designed to simplify the understanding of relationships within a Salesforce organization's data model. Often, comprehending the intricate parent-child relationships in a Salesforce org can be challenging, especially when dealing with complex data structures. This tool aims to alleviate this challenge by providing a straightforward method to extract and visualize these relationships.

## Functionality
The extractor takes as input a CSV file representing a Lucidchart diagram, which is typically publicly available from Salesforce. Lucidchart is a widely used tool for creating diagrams, including entity relationship diagrams (ERDs) representing Salesforce data models. The extractor then analyzes this diagram and produces a CSV file outlining the hierarchy of parent-child relationships within the Salesforce data model.

## Implementation Details
- This application is implemented in Python.
- It utilizes the pandas library for data processing.
- Flask is used to implement a lightweight front-end, allowing users to upload the CSV file and retrieve the hierarchy relationships.

## Use Cases
### Business Analysts
For business analysts tasked with understanding the intricacies of a Salesforce org's data model, this tool provides a clear and concise representation of parent-child relationships. By having a structured hierarchy at their disposal, analysts can more effectively analyze and interpret the data model, aiding in decision-making processes and system optimizations.

### Data Migration Specialists
Data migration projects often require a deep understanding of the relationships between different data entities. With the hierarchy extracted by this tool, data migration specialists can accurately map data fields between source and target systems. This ensures a smooth and efficient data migration process, minimizing the risk of data loss or corruption.

## Getting Started
To use the Salesforce Data Model Hierarchy Extractor, simply clone the repository and follow the instructions in the README. Ensure that you have the necessary dependencies installed, and provide the Lucidchart diagram CSV file as input. The extractor will then generate a CSV file containing the hierarchy of parent-child relationships within the Salesforce data model.

## Contributions
Contributions to the project are welcome! If you encounter any bugs, have feature requests, or would like to contribute code improvements, please open an issue or submit a pull request on GitHub. Your contributions help make this tool more robust and valuable to the community.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


--------------------------------

## Running the Application:

1.Create Virtual Environment (use <code>python</code> or <code>python3</code> ):

    ```bash
    python -m venv venv
    ```
2. Activate the virtual environment:

    ```bash
    source venv/bin/activate
    ```

3. Start the application:

    ```bash
    python app.py
    ```

4. Open your web browser and navigate to the following URL:

    ```
    http://127.0.0.1:5000
    ```

You can now use the web interface to upload your Lucidchart CSV file and retrieve the hierarchy relationships.

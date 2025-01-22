# TextToSQL

TextToSQL is a project that aims to convert natural language text into SQL queries. This can be useful for users who are not familiar with SQL but need to interact with databases.

## Features

- Convert natural language questions into SQL queries
- Support for multiple database systems
- Easy to integrate with existing applications

## Installation

To install the TextToSQL project, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/TextToSQL.git
    ```
2. **Navigate to the project directory**:
    ```sh
    cd TextToSQL
    ```
3. **Create a Virtual Environment**:
    ```sh
    python -m venv myenv
    ```
4. **Activate the virtual environment**:
    - **Windows**:
      ```sh
      .\myenv\Scripts\Activate
      ```
    - **macOS/Linux**:
      ```sh
      source myenv/bin/activate
      ```
5. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Setup Instructions

### Prerequisites

- **Python**: Ensure you have Python 3.7 or later installed. You can download it from [python.org](https://www.python.org/downloads/).
- **pip**: Ensure you have pip installed. It usually comes with Python, but you can upgrade it using:
  ```sh
  python -m pip install --upgrade pip
  ```

### Step-by-Step Setup

1. **Create a Virtual Environment**
Create a virtual environment to manage dependencies:

```sh
python -m venv venv
```

Activate the virtual environment:

```sh
.\venv\Scripts\activate
```

After activating the virtual environment, your command prompt should look something like this:

(venv) C:\Users\XXXXX\XXXX\TextToSql>

2. **Install Dependencies**
Install the required Python packages:

If requirements.txt is not available, manually install the necessary packages:

3. **Set Up Environment Variables**
Create a .env file in the root directory of the project and add your Azure OpenAI and database credentials:

4. **Run the Streamlit Application**
Run the Streamlit application:

5. **Verify the Setup**
Open your web browser and navigate to the URL provided by Streamlit (usually http://localhost:8501). You should see the Streamlit app running.

## Troubleshooting

- **ODBC Driver Error**: Ensure you have the ODBC Driver 18 for SQL Server installed. You can download it from the Microsoft website.
- **Environment Activation**: If you have trouble activating the virtual environment, ensure you are using the correct command for your operating system.

## Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [pandas Documentation](https://pandas.pydata.org/pandas-docs/stable/)
- [pyodbc Documentation](https://github.com/mkleehammer/pyodbc/wiki)
```

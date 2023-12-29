# Arboretum
Arboretum is a project developed by Greenway Global, a company operating on the principles of multilevel marketing. In this business model, partners, who are also clients of the company, attract new customers and receive various bonuses for their efforts. Each partner has their own tree structure of partners/clients, and by developing it, they can increase their status within the organization. However, it is not always clear which branch of the tree to focus on to improve one's status. The goal of the project is to create a recommender system that helps partners make informed decisions about the development of their tree structure. The recommendations should be actionable steps, specifying what, to whom, and in what volume needs to be sold to improve their qualification.

## Repository Structure

- **api**: Contains the FastAPI implementation for serving predictions.
  - **endpoints**: Specific endpoints for different functionalities.
- **dashboard**: Houses the Dash web interface for user interaction.
- **services**: Holds the services related to business logic, such as the `model_service`.
- **notebooks**: Jupyter notebook for model training.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **README.md**: Project documentation.
- **poetry.lock**: Dependency lock file for Poetry.
- **pyproject.toml**: Poetry project configuration file.

## Getting Started Locally

### Prerequisites
Make sure you have Python installed. It is recommended to use a virtual environment.

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies
Install the required Python packages using Poetry:

```bash
poetry install
```

### Running the FastAPI Server
Navigate to the `api` directory and run the FastAPI server:

```bash
cd api
uvicorn main:app --reload
```

The API will be accessible at http://127.0.0.1:8000.

### Running the Dash Web Interface
Open a new terminal window, navigate to the `dashboard` directory, and run the Dash app:

```bash
cd dashboard
python dashboard.py
```

Access the web interface at http://127.0.0.1:8050.

## Model Training
For model training, refer to the Jupyter notebook in the `notebooks` directory:

```bash
jupyter notebook notebooks/lgo_prediction.ipynb
```


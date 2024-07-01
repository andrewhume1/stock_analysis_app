# Stock Analysis App

A Docker-based stock analysis app that downloads price history and calculates basic stock metrics.

## Getting Started

### Clone the Repository

To get started, clone the repository by running the following command in your terminal:

```
git clone https://github.com/andrewhume1/stock-analysis-app.git
```

### Build the Docker Image

To build the Docker image, navigate to the cloned repository and run the following command:

```
docker build - t stock_analysis_app
```

This will create a Docker image with the tag `stock_analysis_app`.

### Run the Docker Container

To run the Docker container, use the following command:

```
docker run -p 80:5000 stock-analysis-app
```
This will start a new container from the `stock-analysis-app` image and map port 80 on your local machine to port 5000 in the container. You can access the app by visiting `http://localhost:8080` in your web browser.


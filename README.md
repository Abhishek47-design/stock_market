# Real-Time Stock Market Data Pipeline

## Overview

Built an end-to-end real-time stock market data pipeline using Kafka, Databricks, PySpark, Delta Lake, and Databricks Workflows.

## Architecture

Finnhub API → Kafka → Raw JSON Files → Databricks Auto Loader → Bronze Layer → Silver Layer → Gold Layer → Workflow Orchestration

## Technologies Used

* Python
* Kafka
* Docker
* Databricks
* PySpark
* Delta Lake
* Databricks Auto Loader
* Databricks Workflows

## Features

* Real-time stock data ingestion
* Kafka-based streaming architecture
* Medallion Architecture (Bronze/Silver/Gold)
* Incremental file ingestion using Auto Loader
* ETL orchestration using Databricks Workflows
* Stock analytics and aggregation layer

## Future Improvements

* Real-time streaming with Structured Streaming
* Market anomaly detection
* News sentiment integration
* Power BI/Tableau dashboards

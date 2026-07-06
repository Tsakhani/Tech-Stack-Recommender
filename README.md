# TechStack AI - Intelligent Career Recommendation Engine

## Overview

**TechStack AI** is an AI-powered career recommendation platform that helps aspiring and experienced technology professionals discover career paths that align with their existing technical skills.

The application analyses a user's current skills, compares them against a curated dataset of technology job roles, and recommends the careers that best match the user's profile. Instead of relying on predefined rules or keyword matching, the recommendation engine leverages **Natural Language Processing (NLP)** techniques using **TF-IDF vectorization** and **Cosine Similarity** to measure how closely a user's skill set aligns with various technology careers.

The project was designed to demonstrate the integration of machine learning concepts, backend API development, database management, and frontend web development into a complete full-stack application.

---

# Project Objectives

The primary objective of this project is to provide users with intelligent career recommendations based on their technical skill set.

The system aims to:

* Assist users in identifying technology careers that best suit their existing skills.
* Demonstrate the practical application of Natural Language Processing within a recommendation engine.
* Provide a scalable architecture capable of supporting future machine learning enhancements.
* Showcase modern full-stack software engineering practices using Python.

---

# Features

* AI-powered career recommendations
* TF-IDF based text vectorization
* Cosine Similarity recommendation engine
* User skill validation
* PostgreSQL database integration
* SQLAlchemy ORM
* FastAPI REST API
* Flask web frontend
* Tailwind CSS responsive interface
* Recommendation history persistence
* Modern modular software architecture

---

# How the Recommendation Engine Works

The recommendation engine follows a multi-stage pipeline to generate career recommendations.

## Step 1 - User Input

The user enters a minimum of three technical skills.

Example:

```text
Python

SQL

Docker
```

---

## Step 2 - Input Validation

The system validates that:

* At least three skills are provided.
* Empty values are removed.
* Duplicate skills are ignored.

---

## Step 3 - Text Preprocessing

The user skills are converted into a single textual document.

Example:

```text
Python SQL Docker
```

The same preprocessing performed on the dataset is applied to the user input to ensure consistency during comparison.

---

## Step 4 - TF-IDF Vectorization

The application converts both:

* the user's skill profile
* every job role in the dataset

into numerical feature representations using **Term Frequency–Inverse Document Frequency (TF-IDF)**.

TF-IDF assigns greater importance to skills that are more unique and informative across the dataset while reducing the influence of overly common terms.

---

## Step 5 - Cosine Similarity

After vectorization, the application calculates the cosine similarity between the user's skill profile and every job role contained within the dataset.

Cosine similarity measures how closely two documents point in the same direction within the feature space.

A similarity score closer to **1.0** indicates a stronger match between the user's skills and the job role.

---

## Step 6 - Ranking

The recommendation engine sorts every job role according to its similarity score.

The highest-scoring careers become the recommended career paths presented to the user.

---

## Step 7 - Database Storage

The application stores:

* User skills
* Recommended careers
* Recommendation scores

inside PostgreSQL for future retrieval and analysis.

---

# System Architecture

```text
                  User

                    │

                    ▼

          Flask Frontend (UI)

                    │

                    ▼

             FastAPI Backend

                    │

                    ▼

       Recommendation Service Layer

                    │

                    ▼

       Recommendation Engine

                    │

        TF-IDF + Cosine Similarity

                    │

                    ▼

          Job Role Dataset

                    │

                    ▼

             PostgreSQL Database
```

---

# Project Structure

```text
tech-stack-recommender/

│

├── app/

│   ├── api.py

│   ├── database.py

│   ├── models.py

│   ├── services.py

│   ├── recommendation_engine.py

│   ├── validators.py

│   ├── data_loader.py

│   └── main.py

│

├── frontend/

│   ├── app.py

│   ├── templates/

│   ├── static/

│

├── data/

│   ├── cleaned_job_role_dataset.csv

│

├── requirements.txt

│

└── README.md
```

---

# Technology Stack

## Programming Language

* Python

---

## Machine Learning

* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity

---

## Backend

* FastAPI

---

## Frontend

* Flask
* Tailwind CSS
* HTML
* CSS
* JavaScript

---

## Database

* PostgreSQL
* SQLAlchemy ORM

---

## Version Control

* Git
* GitHub

---

# Why TF-IDF Instead of Deep Learning?

This project intentionally uses TF-IDF and Cosine Similarity rather than a deep neural network.

The recommendation problem focuses on measuring textual similarity between user skills and predefined job descriptions rather than learning complex patterns from large-scale data.

TF-IDF provides:

* Fast execution
* Low memory consumption
* High interpretability
* Excellent performance for text-based recommendation tasks

This approach keeps the recommendation engine lightweight while producing accurate and explainable recommendations.

---

# Database Design

The project uses PostgreSQL to persist user interactions.

The primary entities include:

### Users

Stores:

* User ID
* Skills entered

### Recommendations

Stores:

* Recommendation ID
* User ID
* Recommended job role
* Similarity score

A one-to-many relationship exists between Users and Recommendations, allowing each user to have multiple recommendation records.

---

# API Workflow

The FastAPI backend exposes an endpoint that receives a JSON payload containing user skills.

Example request:

```json
{
    "skills": [
        "Python",
        "SQL",
        "Docker"
    ]
}
```

The backend:

1. Validates the request.
2. Executes the recommendation engine.
3. Stores the recommendation results.
4. Returns the recommendations as JSON.

---

# User Workflow

1. Launch the Flask frontend.
2. Enter at least three technical skills.
3. Submit the request.
4. The frontend sends the skills to FastAPI.
5. FastAPI executes the recommendation engine.
6. PostgreSQL stores the recommendation history.
7. The recommended careers are displayed on the interface.

---

# Software Engineering Principles

The project follows several software engineering best practices, including:

* Separation of concerns
* Modular architecture
* Layered application design
* Reusable business logic
* RESTful API design
* ORM-based database interaction
* Input validation
* Maintainable project structure

---

# Future Enhancements

Potential future improvements include:

* User authentication and profile management
* Career bookmarking
* Learning path recommendations
* Certification recommendations
* Salary insights
* Technology trend analysis
* Integration with live job posting APIs
* Personalized recommendations based on recommendation history
* Advanced machine learning models using transformer embeddings
* Cloud deployment using AWS

---

# Learning Outcomes

This project demonstrates practical experience in:

* Natural Language Processing
* Recommendation Systems
* Backend API Development
* Frontend Web Development
* Database Design
* SQLAlchemy ORM
* REST API Architecture
* Machine Learning Pipelines
* Software Architecture
* Full-Stack Python Development

---

# Author

**Thiyisani Tsakhani Tsumele**

Bachelor of Science in Information Technology (Robotics)

Cloud Computing | Machine Learning | Software Engineering

---

# License

This project is intended for educational and portfolio purposes.

Feel free to fork, study, and extend the project while providing appropriate attribution.

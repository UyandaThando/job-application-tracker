# Job Application Tracker

A Python and SQLite job application tracking system designed to help job seekers organise and manage their job applications.

## Overview

The Job Application Tracker is a command-line application developed using Python and SQLite. It allows users to store, view, search, update, and delete job application records from a local database.

The project was developed as a practical software engineering project to apply programming, database management, validation, error handling, testing, and version control concepts.

## Features

- Add new job applications
- View all saved applications
- Search applications by company
- Update application status
- Delete applications
- Validate required input fields
- Validate application status
- Validate application dates
- Handle invalid application IDs
- Store application data using SQLite
- Persistent local database storage

## Technology Stack

- **Python** — application logic and user interaction
- **SQLite** — database management and persistent data storage
- **VS Code** — development environment
- **Git** — version control
- **GitHub** — source code hosting and project version management

## Database

The application uses SQLite to store job application records locally.

Each application contains:

| Field | Description |
|---|---|
| `application_id` | Unique identifier for the application |
| `company_name` | Name of the company |
| `job_title` | Position applied for |
| `status` | Current application status |
| `date_applied` | Date the application was submitted |
| `job_description` | Description of the position |

The application uses CRUD operations:

- **Create** — Add a new application
- **Read** — View and search applications
- **Update** — Change an application's status
- **Delete** — Remove an application

## Application Statuses

The application currently supports the following job application statuses:

- `Applied`
- `Interview`
- `Rejected`
- `Offer`

## How to Run the Project

### Requirements

- Python 3
- VS Code or another Python-compatible code editor

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/UyandaThando/job-application-tracker.git
2. Navigate into the project folder:
   ```bash
   cd job-application-tracker
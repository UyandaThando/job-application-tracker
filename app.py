from datetime import datetime
import sqlite3

# Connect to database
connection = sqlite3.connect("job_applications.db")

cursor = connection.cursor()


# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS job_applications (
        application_id INTEGER PRIMARY KEY,
        company_name TEXT,
        job_title TEXT,
        status TEXT,
        date_applied DATE,
        job_description TEXT
    )
""")



# ------------------------- # DATABASE FUNCTIONS # -------------------------


def add_application(company_name, job_title, status, date_applied, job_description):
    cursor.execute("""
        INSERT INTO job_applications
        (company_name, job_title, status, date_applied, job_description)
        VALUES (?, ?, ?, ?, ?)
    """, (company_name, job_title, status, date_applied, job_description))


def get_applications():
    cursor.execute("""
        SELECT * FROM job_applications
    """)
    applications = cursor.fetchall()
    return applications

def search_by_company(company_name):
    cursor.execute("""
        SELECT * FROM job_applications
        WHERE company_name = ?
    """, (company_name,))

    applications = cursor.fetchall()
    return applications

def update_status(application_id, new_status):
    cursor.execute("""
        UPDATE job_applications
        SET status = ?
        WHERE application_id = ?
    """, (new_status, application_id))

    connection.commit()
    return cursor.rowcount

def delete_application(application_id):
    cursor.execute("""
        DELETE FROM job_applications
        WHERE application_id = ?
    """, (application_id,))

    connection.commit()
    return cursor.rowcount




# ------------------------- # PROGRAM SETUP # -------------------------
print("Database connected!")

valid_statuses = ["Applied", "Interview", "Rejected", "Offer"]

while True:

    choice = input("""
1. Add application
2. View applications
3. Search applications by company
4. Update application status
5. Delete application
6. Exit

Choose an option: 
""")

    # ------------------------- # ADD APPLICATION # -------------------------

    if choice == "1":
        company_name = input("Company name: ").strip()
        if not company_name:
            print("Company name cannot be empty.")
            continue



        job_title = input("Job title: ").strip()
        if not job_title:
            print("Job title cannot be empty.")
            continue


        status = input("Status: ").strip()
        

        if status not in valid_statuses:
            print("Invalid status.")
            continue

            
        date_applied = input("Date applied: ").strip()

        if not date_applied:
            print("Date applied cannot be empty.")
            continue

        try:
            datetime.strptime(date_applied, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            continue


        job_description = input("Job description: ").strip()

        if not job_description:
            print("Job description cannot be empty.")
            continue

        add_application(
            company_name,
            job_title,
            status,
            date_applied,
            job_description
        )

        connection.commit()
        print("Application added successfully!")


# ------------------------- # VIEW APPLICATIONS # -------------------------

    elif choice == "2":
        
        applications = get_applications()

        if not applications:
            print("No applications found.")

        else:
            for application in applications:

                application_id, company_name, job_title, status, date_applied, job_description = application

                print("ID:", application_id)
                print("Company:", company_name)
                print("Job Title:", job_title)
                print("Status:", status)
                print("Date Applied:", date_applied)
                print("Job Description:", job_description)
                print("-------------------------")



# ------------------------- # SEARCH APPLICATIONS # -------------------------

    elif choice == "3":
        company_name = input("Enter the company name to search for: ").strip()

        if not company_name:
            print("Company name cannot be empty.")
            continue
        
        applications = search_by_company(company_name)
        
        if not applications:
            print("No applications found for that company.")
            
        else:
            for application in applications:
                
                application_id, company_name, job_title, status, date_applied, job_description = application
                
                print("ID:", application_id)
                print("Company:", company_name)
                print("Job Title:", job_title)
                print("Status:", status)
                print("Date Applied:", date_applied)
                print("Job Description:", job_description)
                print("-------------------------")

            
# ------------------------- # UPDATE APPLICATION STATUS # -------------------------

    elif choice == "4":

        try:
            application_id = int(
            input("Enter the ID of the application to update: ")
            )

            new_status = input("Enter the new status: ").strip()
        
            if new_status not in valid_statuses:
                print("Invalid status.")
                continue

            updated = update_status(
                application_id,
                new_status
            )
            if updated == 1:
                print("Application status updated!")
            else:
                print("Application not found.")
                
        except ValueError:
            print("Invalid ID. Please enter a number.")

        
# ------------------------- # DELETE APPLICATION # -------------------------

    elif choice == "5":

        try:
            application_id = int(
                input("Enter the ID of the application to delete: ")
            )
            
            deleted = delete_application(application_id)
            
            if deleted == 1:
                print("Application deleted!")
            else:
                print("Application not found.")
                
        except ValueError:
            print("Invalid ID. Please enter a number.")

# ------------------------- # EXIT # -------------------------

    elif choice == "6":
        
        print("Goodbye!")
        break
    
# ------------------------- # INVALID MENU OPTION # -------------------------
    else:
        print("Invalid option. Please choose a number from 1 to 6.")
        
# Close database connection

connection.close()
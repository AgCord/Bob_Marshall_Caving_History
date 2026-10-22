Bob Marshall Caving History - WBS

1. Database Design & Setup
   1.1 Write project proposal + create GitHub repo - DONE
   1.2 Build initial ER diagram - DONE
   1.3 Revise ER diagram - DONE
   1.4 Install MariaDB on VM - DONE
   1.5 Create bmcaving database - DONE

2. Database Implementation
   2.1 Create tables based on ERD - DONE
   2.2 Insert sample data - DONE
   2.3 Normalize tables to 3NF - DONE
   2.4 Save build script - DONE

3. SQL Queries & Access
   3.1 Write SELECT queries - DONE
   3.2 Write JOIN queries - DONE
   3.3 Set up Python environment (.venv, .env for login) - DONE
   3.4 Build command-line Python app (app.py, Unit 8) - DONE

4. Web Integration
   4.1 Install Flask in .venv - DONE
   4.2 Create Flask app (web.py) with test route - DONE
   4.3 Serve static HTML page (person.html) - DONE

5. Remaining Work
   5.1 Fill Flask pages from the database (templates) - Medium
       Depends on: 4.3
   5.2 CRUD in Flask for one table (Person) - Large
       Depends on: 5.1
   5.3 CRUD in Flask for many-to-many (Person-Expedition) - Large
       Depends on: 5.2
   5.4 Database considerations: limited-permission DB user,
       prepared statements, input sanitization (XSS) - Medium
       Depends on: 5.2 (build alongside CRUD)
   5.5 Prepare final presentation/demo - Small
       Depends on: 5.3, 5.4
  5.6 After class: polish repo and README for employers - Medium
    Depends on: 5.5
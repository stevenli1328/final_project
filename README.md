# final_project
Our CS 195 final project, an employee management system. 

Employee Management System Software Requirements Specification
By Kirk Spaseff and Steven Li
Introduction
Overview and Goals

The purpose of our Employee Management Software is to provide a standalone system for employees, managers, and administrators at a workplace to communicate, schedule, and access resources such as pay history. 

The goals are to simplify and centralize the operations of a workplace and to streamline the communication between employees. Any company that has between 1 and thousands of employees should benefit from this software. 

Requirements
Functional Requirements
Administrator
An administrator type user shall be able to access a login page and login with their credentials. 
Administrators shall be able to create new employee type users.
Creating an employee shall save their information to a database of employees.
Administrators should be able to edit employee information, but not access sensitive information such as SSN.
Administrators shall be able to access an employee database with all present and former employees.
Administrators shall be able to access a PTO page where they can view, edit, approve, deny, and sort PTO requests from employees.
Administrators shall be able to access a tasks page that can create company tasks that can be assigned to everyone or individual employees. 
Administrators shall be able to access a payroll page that allows them to access payroll history and add employees to payroll groups.
	
Employee
An employee type user shall be able to access a login page and login with their credentials
An employee shall be able to access a PTO page where they can view and edit their own PTO requests both historical and current.
An employee shall be able to view a tasks page where tasks assigned to them are viewable.
An employee shall be able to access a payroll page that allowed them to access payroll history (i.e. previous pay stubs), view tax information, and see upcoming pay dates. 

Dashboard
The dashboard shall be the first page seen by all users on the site once logged in. 
The dashboard shall have buttons to take the user to the various pages available to the user depending on access. 
The dashboard shall provide a summary of recent activity and notifications of any upcoming events such as tasks to be completed soon or PTO start date. 
Tasks
The tasks page shall be viewable in calendar or list format.
The tasks view shall be organized into ‘upcoming’ and ‘finished’ sections.
Only administrator type users shall have the ability to create company-wide tasks.
Employees should be able to create their own tasks. 
The employee tasks shall have the option to ‘complete’ them by the employee themselves.
The tasks themselves shall be categorized into ‘upcoming’, ‘in-progress’, or ‘complete’.
 PTO
PTO requests shall be viewable in calendar or list format.
Administrators shall be able to see all PTO requests from all users.
Administrators shall be able to go into an individual request and see options such as edit, comment, approve, or delete.
Payroll
The payroll page shall have payroll history viewable for all employees (if an administrator type user) or personal history (if an employee-type user).


Use Cases
Inaction
A user logs on and leaves the dashboard open and idle. 
The application kicks the user out for inactivity after a period of time. 
Administrator fires an employee
An administrator-type user visits the site and clicks login from the display page
They are taken to a login site and enter their information successfully, then taken to a dashboard page.
They navigate to the employees page by clicking the employees button.
They navigate to the employee page they wish to terminate by clicking the employees name from a list of current employees displayed.
They select the fire employee button, which prompts them to verify their credentials again and ensure they wish to fire the employee. 
The employee’s status is changed in the database to former instead of active.
Employee login, editing settings, and add PTO request
An employee-type user visits the site/app:
They go to the site/app and are prompted to login
They enter the wrong information. Red text pops up that notifies them and are given the option of retrieving their password if forgotten.
They successfully login and are taken to the dashboard page. 
The user clicks their name which takes them to their account settings
They click the change password button, which takes them to a new page where they have to enter their old password and their new password twice.
They click submit, which takes them back to their preferences page with a banner that tells them their password is successfully changed.
The user clicks a “home” or “dashboard” button which takes them back to that page. 
The user goes to the PTO page via a link.
They click “Add new PTO request” which takes them to a page where they can add all relevant details some of which are required (start date and end date), others of which are optional (comments) 
They click submit, giving them a page that indicates they successfully requested time off and the ability to view all time off requests. 
The user clicks their profile and clicks the logout button.

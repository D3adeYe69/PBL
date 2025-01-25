📅 Changelog

🚀 Pre-Development
September 3 - September 5, 2024:
Created a project mock-up
💬 Comment: The mock-up helped define the user interface, allowing us to visualize the application flow and gather initial feedback before development.

(September 6 - September 10), 2024:
Sketched the initial database design
💬 Comment: This database sketch outlined the necessary tables, relationships, and data structure to support the application's habit-tracking functionality.

(September 11 - September 16), 2024:
Created the first version of the login and sign-up front-end pages
💬 Comment: These initial pages provided the foundation for user authentication, enabling users to create accounts and log into the application.

🗓️ (September 18 - September 21, 2024)
Initial Setup:
Created the database in MySQL
💬 Comment: The initial database setup provided a structured storage solution to manage user data, habits, and progress tracking. MySQL was chosen for its ease of setup and familiarity.

Started backend development in Flask
💬 Comment: Flask was initially selected as the backend framework due to its simplicity and quick setup, allowing us to rapidly prototype our backend features.
![App.py](/images/image4.png)
![App.py](/images/image5.png)
![Add user to data base](/images/image6.png)

Linked MySQL with Flask
💬 Comment: Connecting Flask to MySQL allowed us to store and retrieve data from our database, laying the foundation for dynamic data handling.
![Env file for database linking](/images/image7.png)

Frontend Setup:
Created the login page
💬 Comment: The login page was essential for user authentication, providing a secure entry point to track individual progress and personalize the experience.

Created the sign-up page
💬 Comment: The sign-up page enabled new users to create accounts, allowing personalized habit tracking and progress management.

Created the front page
💬 Comment: The front page served as the main interface, allowing users to navigate the application easily and access their habit-tracking dashboard.

🗓️ (September 22 - September 28, 2024)
Backend Transition:
Changed the backend framework from Flask to Django
💬 Comment: We migrated from Flask to Django to take advantage of Django’s built-in ORM, which simplifies database management and ensures better scalability as the project grows.
![Changed to Django](/images/image8.png)

Recreated the database structure in Django
💬 Comment: Recreating the database in Django allowed us to leverage Django's ORM for easier model management and integrated data validation.

Database Enhancements:
Added additional tables to the database
💬 Comment: New tables were added to support features like tracking habit steps and user progress, enhancing the functionality and data structure of the app.
![Created the tables](/images/image9.png)

Populated half of the database with necessary information
💬 Comment: Adding sample data was important for testing and development, helping us verify that data retrieval and user progress tracking worked as intended.
![Snippet of pupulating the database](/images/image10.png)

Frontend Adjustments:
Minor changes and improvements to the front end
💬 Comment: Minor adjustments improved the user experience and refined the look and feel of the application based on early testing and feedback.

🗓️ (September 29 - October 5, 2024)
Habit Tracking Pages:
Created pages for each habit's steps
💬 Comment: Individual habit pages allowed users to focus on specific steps and track their progress more intuitively, promoting effective habit-building.

Added a calendar to display user progress and track the number of days spent on each habit
💬 Comment: The calendar was added to visually represent daily progress, which motivates users by showing streaks and consistent habit completion.

User Progress Features:
Implemented sequential task completion, requiring users to complete tasks day-by-day
💬 Comment: This feature encouraged consistent practice by enforcing daily progress, which aligns with habit-building principles.

Displayed the current date and total days a user has spent on a habit
💬 Comment: Showing these details helps users see how long they've been working on a habit, reinforcing a sense of achievement.

Added checkboxes for users to mark tasks as complete
💬 Comment: Checkboxes offered a simple, interactive way for users to mark each step as done, enhancing engagement and satisfaction.

🗓️ (November 5 - November 7, 2024)
Backend-Frontend Integration:
Linked the database with the backend to retrieve specific steps for each habit
💬 Comment: Integrating the backend with the frontend ensured users could view and interact with their specific habit steps, making the application fully functional.

Ensured that user progress is saved in the database, allowing for accurate tracking of completed tasks
💬 Comment: Saving progress data was crucial for persistence, so users could return to the app and see their previously completed tasks and days tracked.

🗓️ (November 8, 2024)
Database Completion:
Fully populated the database with all required information for complete functionality, and made some changes to make it compatible with the front-end and be able to use it dynamically
💬 Comment: Completing the database population finalized the project’s backend, ensuring all habits and steps were available for tracking, making the app ready for real-world use.

🗓️ (November 16, 2024)
Frontend updates:
Updated the front-end.
💬 Comment: Updating the front-end  ensured a polished user interface, ready for backend integration and testing.
![Account.html (User page)](/images/image11.png)
![Settings page](/images/image12.png)
![Support page](/images/image13.png)

🗓️ (November 19, 2024)
Feature Enhancements:
Created the Habit History page, Forgot Password page, and most Habit Creation pages (Front-end only).
💬 Comment: Adding these pages expanded the app's functionality by enabling users to recover accounts, review their progress, and set up new habits more efficiently.
![Page for informations how to edit the password](/images/image14.png)
![Page for statistics](/images/image15.png)

User Account Management:
Added the front sliding notification and implemented account deletion.
💬 Comment: These features improved user experience by providing dynamic feedback and allowing users to manage their accounts effectively.
![Some debugging in the index function](/images/image16.png)
![Delete account function in views.py](/images/image17.png)

🗓️ (November 22, 2024)
Password Reset Implementation:
Made changes to the reset password functionality using the user's email.
💬 Comment: Updating the reset password feature ensured a secure and user-friendly process for recovering accounts.
![Few changes in the front end logic of this page](/images/image18.png)

🗓️ January 25, 2025
Bug Fixes and New Features:
Fixed some issues with the account HTML and change password HTML pages that displayed incorrect data by retrieving the admin's credentials instead of the user’s.
💬 Comment: Corrected these issues to ensure proper display of user-specific data.
<div style="text-align: center;">
    <img src="/images/image19.png" alt="Account details" style="max-width: 100%;"/>
  </div>

Created functionality for the 'Edit Info' part, enabling users to change their username, email, and current password.
💬 Comment: This feature enhances user control over their account details, improving the overall user experience.
<div style="text-align: center;">
    <img src="/images/image20.png" alt="Edit info page" style="max-width: 100%;"/>
  </div>

Added a 'Report a Problem' page where users can submit reports that are sent directly to our email.
💬 Comment: This feature allows users to report issues, helping to improve the app's functionality and user support.
<div style="text-align: center;">
    <img src="/images/image21.png" alt="Report a problem page" style="max-width: 100%;"/>
  </div>

Made minor changes to page redirects for a smoother navigation experience.
💬 Comment: These changes ensure more intuitive page transitions and user flow throughout the app.





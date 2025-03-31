<!-- Project: Diary
Mood tracker:
1. Mood selection + description.
2. Mood change graph by days.
3. Trend analysis (e.g. which days of the week are the mood worse/better).
Frontend:
1 MoodService: gets data from the server.
2 MoodEntry class: defines the mood entry type.
3 Chart.js graph for visualizing moods.
4 Input form [(ngModel)] for selecting a mood.
5 Event (click) for saving a mood.
6 Using ngFor for rendering a list of past moods.
Backend:
1 MoodEntry model (date, mood, note, ForeignKey(user)).
2 MoodSerializer serializer (ModelSerializer).
3 MoodAPIView CBV (APIView) for working with mood entries.
4 Linking entries to the current user (request.user).
Habit tracker:
1. Adding habits (reading, sports, meditation).
2. Progress by days (for example, coloring the calendar).
3. Filtering by habit type.
Frontend:
1 HabitService for working with API.
2 Habit interface (name, goal, status).
3 ngx-calendar calendar component.
4 Form for adding a habit [(ngModel)].
5 Events (click) for creating and deleting habits.
6 We use ngIf to display completed habits.
Backend:
1 Habit model (name, frequency, user).
2 HabitLog model (date of execution, connection to Habit).
3 FBV get_habits and create_habit.
4 CBV HabitAPIView (APIView) for working with data.
Wishlist:
1.Categories (material, travel, education).
2.Execution status (waiting, in progress, completed).
3.Ability to attach links, images.
Frontend:
1 WishlistService: API requests.
2 WishlistItem class (title, status, photo).
3 Photo upload (Firebase Storage or Django + ngModel).
4 Events (click) for adding/removing a wish.
5 ngFor for displaying the list.
Backend:
1 WishlistItem model (title, category, status, ForeignKey(user)).
2 WishlistSerializer serializer (ModelSerializer).
3 CBV WishlistAPIView (APIView).
4 Function for deleting an item (FBV delete_wishlist_item).
Task Manager:
1.Creating tasks with date and event binding.
2. Displaying tasks on the calendar.
Frontend:
1 TaskService: API requests.
2 Task interface (name, date, status).
3 FullCalendar calendar.
4 ngModel for the task creation form.
5 click for adding/editing tasks.
Backend:
1 Task model (name, date, status, ForeignKey(user)).
2 TaskSerializer serializer (ModelSerializer).
3 FBV get_tasks and create_task.
4 CBV TaskAPIView (APIView).
5 Filtering tasks by user.
6 Reminders via Celery and Redis (optional).

Authentication
Backend:
1 JWT (Django Simple JWT).
2 LoginView view (FBV) for logging in.
3 LogoutView (FBV) view for logging out.
4 Token interception in Angular via interceptor.
Frontend:
1 Token saving in localStorage.
2 Authorization via AuthService.
3 click event for login/logout.
4
 API request interception (JWT interceptor).
------------------------------------------------------
Members:
Ibatova Shugyla 23b031314
Khusainova Karina 23b031477
Asyljanova Inara
----------------------------------------------------
Time: Wednesday 15-17:00 -->

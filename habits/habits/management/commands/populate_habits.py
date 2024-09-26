from django.core.management.base import BaseCommand
from habits.models import Language, Habit, Step  # Make sure to import Step

class Command(BaseCommand):
    help = 'Populate the database with initial data for languages, habits, and steps'

    def handle(self, *args, **kwargs):
        # Adding languages
        languages_data = [
            {'language_code': 'en', 'language_name': 'English'},
            {'language_code': 'ro', 'language_name': 'Romanian'},
            {'language_code': 'ru', 'language_name': 'Russian'}
        ]
        for lang in languages_data:
            Language.objects.get_or_create(language_code=lang['language_code'], defaults={'language_name': lang['language_name']})

        self.stdout.write(self.style.SUCCESS('Successfully added languages'))

        # Adding habits
        habits_data = [
            {'language_code': 'en', 'habit_name': 'Smoking', 'habit_type': 'bad', 'description': 'We help you quit smoking'},
            {'language_code': 'en', 'habit_name': 'Underslept', 'habit_type': 'bad', 'description': 'We help you get more sleep'},
            {'language_code': 'en', 'habit_name': 'Alcohol', 'habit_type': 'bad', 'description': 'We help you get rid of your alcohol addiction'},
            {'language_code': 'en', 'habit_name': 'Overeating', 'habit_type': 'bad', 'description': 'We help you control your appetite'},
            {'language_code': 'en', 'habit_name': 'Procrastination', 'habit_type': 'bad', 'description': 'We help you get over procrastination'},
            {'language_code': 'en', 'habit_name': 'Reading', 'habit_type': 'good', 'description': 'We help you get into reading'},
            {'language_code': 'en', 'habit_name': 'Savings', 'habit_type': 'good', 'description': 'We help you start saving more money'},
            {'language_code': 'en', 'habit_name': 'Gym', 'habit_type': 'good', 'description': 'We help you get into shape'},
            {'language_code': 'en', 'habit_name': 'Nutrition', 'habit_type': 'good', 'description': 'We help you eat better'},
            {'language_code': 'en', 'habit_name': 'Breakfasting', 'habit_type': 'good', 'description': 'We help you start eating breakfast every day'}
        ]
        for habit in habits_data:
            Habit.objects.get_or_create(
                language_code_id=habit['language_code'],  # Foreign key relation
                habit_name=habit['habit_name'],
                habit_type=habit['habit_type'],
                defaults={'description': habit['description']}
            )

        self.stdout.write(self.style.SUCCESS('Successfully added habits'))

        # Adding steps
        steps_data = [
            'Write down 3 tasks you’ve been putting off',
            'Describe how you feel when you think about doing those tasks (fear, boredom, overwhelmed?)',
            'Schedule 10 minutes for one small task today',
            'Pick the easiest task from your list (5-10 minutes)',
            'Work on it for 2 minutes only. Continue if you feel motivated',
            'Once the task is complete, treat yourself (snack, walk, or break)',
            'Set aside two 20-minute slots for the most important tasks',
            'Mute your phone and block distractions for these 20 minutes',
            'After each block, write down how it felt to focus',
            "Select a task you've been avoiding",
            'Divide the task into 3 smaller, manageable steps',
            'Focus on completing just one small part',
            'Set short deadlines for both (e.g., finish by 4 PM)',
            'Tell someone your deadlines for accountability',
            'Focus on meeting your deadlines today',
            'Choose two tasks that require focus',
            'Set a timer for 25 minutes and work on the first task. Then take a 5-minute break',
            'Use the Pomodoro technique for the second task',
            'Review the week. How much have you completed?',
            "Reward yourself for the small wins you've achieved",
            'Write down what was hardest and where you need to improve',
            'Create a list of 5 tasks, ranking them in order of importance',
            'Start with the most important (or hardest) task first',
            'Avoid multitasking. Focus on finishing one task before moving to the next',
            'Share your top 3 tasks for the day with a friend or family member',
            'Arrange for that person to check in with you later in the day',
            'Aim to complete at least 2 tasks before your check-in time',
            'Spend 10 minutes cleaning your desk or workspace',
            'Make a list of your common distractions and how to avoid them',
            'Create an environment conducive to focus (turn off notifications, keep a glass of water nearby, etc.)',
            'Picture yourself completing a task and the relief/satisfaction it brings',
            'Write a step-by-step plan for completing a task today',
            'Start working on the task by following the roadmap',
            'Choose a task and aim to complete it “good enough” rather than perfectly',
            'Give yourself 30 minutes to finish the task, aiming for progress, not perfection',
            'Once the 30 minutes are up, move on to the next task',
            'For one day, write down what you spend time on every hour',
            'Highlight where you wasted time or procrastinated',
            'Make adjustments for tomorrow to reduce wasted time.',
            'Reflect on what you’ve accomplished over the last two weeks',
            'Write down what held you back or caused you to procrastinate',
            'Create goals for the next week, based on what you’ve learned so far',
            'Include a focus on your top task for the day',
            'Review what you accomplished and plan for tomorrow',
            'Follow both routines today',
            'Group similar tasks (e.g., emails, calls, small admin work)',
            'Set a time to complete all similar tasks in one go',
            'Work through all the grouped tasks without interruption',
            'Write down what activities or people often distract you',
            'Learn to say “no” or set limits to these distractions',
            'When distractions arise today, practice saying “no.”',
            'Pay attention to when you feel most energized throughout the day',
            'Record the time and number of cigarettes you smoke today',
            'Note the situation and emotions that led to each cigarette',
            'Reflect on why you want to quit—write down three reasons',
            'Decide on reducing your daily intake by 1-2 cigarettes',
            'Write down your quit date and share it with someone for support',
            'Plan small rewards for hitting milestones (e.g., a nice coffee, movie)',
            'Wait 30 minutes before smoking your first cigarette',
            'Distract yourself with a short walk or breathing exercises',
            'Track how delaying affects your craving',
            'Clear out lighters, ashtrays, and cigarettes from visible spaces',
            'Clean your smoking area to remove the smell of smoke',
            'Reward yourself for creating a smoke-free environment',
            'Swap one smoking break with a 5-minute walk or drink a glass of water',
            'Chew gum or snack on something healthy instead of smoking',
            'Write down how you felt after skipping a cigarette',
            'Select one cigarette time to skip today (e.g., after meals)',
            'Practice deep breathing to manage cravings',
            'Reflect on how your body feels with fewer cigarettes',
            'Calculate how many cigarettes you’ve cut down this week',
            'Write down any positive changes (e.g., better breathing, less coughing)',
            'Set a goal to reduce even further next week',
            'Pick two smoking times to skip today',
            'Use distractions like reading or a quick workout to avoid cravings',
            'Track how you felt throughout the day without those cigarettes',
            'Wait 10-15 minutes longer before each cigarette',
            'Focus on controlling cravings with breathing exercises',
            'Write down if delaying made it easier to smoke less',
            'Swap a smoking break for a healthy snack or activity (e.g., stretching)',
            'Spend 5 minutes doing deep breathing to relax',
            'Reflect on how you feel after choosing not to smoke',
            'Only smoke at specific times (e.g., after meals) and avoid casual smoking',
            'Avoid smoking in certain places (e.g., indoors, in the car)',
            'Reflect on how limiting when and where you smoke affects cravings',
            'Write down three ways your health has improved since cutting down',
            'Replace another cigarette with a 10-minute walk or relaxing activity',
            'Remind yourself of your reasons for quitting whenever you feel a craving',
            'Decide on a time of day to skip smoking entirely',
            'Practice mindfulness or meditation to cope with any stress',
            'Track how your cravings are evolving with fewer cigarettes',
            'Note how many cigarettes you’ve cut this week compared to last week',
            'Plan how you’ll continue cutting down further next week',
            'Reward yourself for sticking with your plan (e.g., treat, fun activity)',
            'Cut another 1-2 cigarettes from your daily routine',
            'Avoid smoking at a specific time of day (e.g., morning)',
            'Write down how this reduction is making you feel physically',
            'Use deep breathing or stretching exercises when you feel stressed',
            'Avoid using cigarettes as a way to cope with difficult situations',
            'Reflect on how alternative stress-relief techniques are working',
            'Wait at least 1 hour after feeling the urge to smoke before lighting up',
            'Distract yourself by doing something productive (e.g., work, hobby)',
            'Note how you felt after delaying and distracting yourself',
            'Choose one more cigarette to eliminate from your routine',
            'Replace the time you’d spend smoking with a healthy snack or drink',
            'Write down any positive physical changes you’re noticing',
            'Avoid smoking when around others who are smoking',
            'Choose a non-smoking activity with friends (e.g., coffee, sports)',
            'Reflect on how being around non-smokers helps you stick to your goal',
            'Replace two smoking breaks with a new activity or short walk',
            'Use deep breathing or mindfulness to reduce cravings',
            'Write down how skipping multiple cigarettes affected your cravings',
            'Plan how you’ll handle cravings on your quit day (e.g., gum, distractions)',
            'Remind yourself of your reasons for quitting and focus on your progress',
            'Set your final quit date and mentally prepare for the upcoming week',
            'Don’t smoke any cigarettes—today is your quit day',
            'Distract yourself with activities or hobbies when cravings hit',
            'Write down how it feels to go without smoking for an entire day',
            'Use nicotine alternatives (gum, lozenges) if needed to manage cravings',
            'Stay busy with fun, smoke-free activities (e.g., sports, socializing)',
            'Reflect on how well you managed cravings without smoking',
            'Replace smoking breaks with new, positive habits (e.g., stretching, reading)',
            'Engage in light physical activities to reduce stress and improve mood',
            'Write down any physical improvements (e.g., breathing, energy levels)',
            'Stay away from environments where you used to smoke',
            'Hang out with non-smokers or supportive friends',
            'Track how your cravings are decreasing as you avoid triggers',
            'When cravings hit, drink water or chew gum instead of smoking',
            'Practice mindfulness and deep breathing to reduce stress',
            'Reflect on how your overall mood and health are improving',
            'Avoid situations that might tempt you to smoke',
            'Remind yourself of your long-term health goals and benefits of quitting',
            'Reward yourself for each day of staying smoke-free',
            'Reflect on your journey and how long you’ve been smoke-free',
            'Treat yourself to something special as a reward for quitting',
            'Plan how to maintain your smoke-free lifestyle going forward'

            
        ]
        for step in steps_data:
            Step.objects.get_or_create(
                language_code_id='en',  # Foreign key relation
                description=step
            )

        self.stdout.write(self.style.SUCCESS('Successfully added steps'))

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
            'Plan your hardest tasks during high-energy periods',
            'Use short breaks to recharge during low-energy periods',
            'List the tasks you’ve completed and progress you’ve made since Day 1',
            'Think about the biggest challenges you’ve overcome so far',
            'Give yourself a meaningful reward for sticking to the process',
            'Write down any tasks or projects you need to tackle in the upcoming weeks',
            'Create deadlines and time blocks for those tasks now',
            'Make a habit of reviewing tasks at the end of each day',
            'Develop a simple system to track your daily tasks and habits (e.g., a checklist or app)',
            'Set a weekly review time to adjust your habits and goals',
            'Write a short statement about why you’ll continue with these new habits and systems'
        ]
        for step in steps_data:
            Step.objects.get_or_create(
                language_code_id='en',  # Foreign key relation
                description=step
            )

        self.stdout.write(self.style.SUCCESS('Successfully added steps'))

from django.core.management.base import BaseCommand
from habits.models import Habit, Step, HabStep

class Command(BaseCommand):
    help = 'Add foreign keys to HabStep table'

    def add_foreign_keys(self, constant_key, second_key_start, second_key_end):
        third_key = 1  # Step order starts at 1
        counter = second_key_start

        while counter <= second_key_end:
            # Fetch the corresponding Habit and Step objects using the keys
            try:
                habit = Habit.objects.get(habit_id=constant_key)
                step = Step.objects.get(step_id=counter)

                # Insert the HabStep record
                hab_step = HabStep(habit=habit, step=step, step_order=third_key)
                hab_step.save()

                self.stdout.write(self.style.SUCCESS(
                    f"Added: Habit ID {constant_key}, Step ID {counter}, Step Order {third_key}"))

            except Habit.DoesNotExist:
                self.stdout.write(self.style.ERROR(
                    f"Habit with ID {constant_key} does not exist"))
            except Step.DoesNotExist:
                self.stdout.write(self.style.ERROR(
                    f"Step with ID {counter} does not exist"))

            # Increment the counter
            counter += 1

            # Every 3 iterations, increment the step order
            if (counter - second_key_start) % 3 == 0:
                third_key += 1

    def handle(self, *args, **kwargs):
        # Call the function with parameters
        self.add_foreign_keys(constant_key=21, second_key_start=260, second_key_end=343)
        self.add_foreign_keys(constant_key=22, second_key_start=344, second_key_end=427)
        self.add_foreign_keys(constant_key=23, second_key_start=428, second_key_end=508)
        self.add_foreign_keys(constant_key=24, second_key_start=509, second_key_end=571)
        self.add_foreign_keys(constant_key=25, second_key_start=572, second_key_end=634)
        self.add_foreign_keys(constant_key=26, second_key_start=635, second_key_end=718)
        self.add_foreign_keys(constant_key=27, second_key_start=719, second_key_end=802)
        self.add_foreign_keys(constant_key=28, second_key_start=803, second_key_end=886)
        self.add_foreign_keys(constant_key=29, second_key_start=887, second_key_end=949)
        self.add_foreign_keys(constant_key=30, second_key_start=950, second_key_end=1012)


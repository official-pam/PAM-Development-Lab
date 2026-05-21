"""
PÄM COMMAND CENTER - Mechatronics Engineering Student Dashboard
A console application demonstrating OOP concepts, PrettyTable, and project management
Author: PÄM Tech Systems
Date: 2024
"""

# Import required libraries
from prettytable import PrettyTable
from datetime import datetime
import random


# ============================================================================
# CLASS 1: Project - Represents a technical project
# ============================================================================
class Project:
    """
    Project class represents a technical project that PÄM is working on.
    Each project has a name, description, status, and technologies used.
    """

    def __init__(self, name, description, status, technologies):
        """
        Constructor - Initializes a new Project object

        Args:
            name (str): Project name
            description (str): What the project does
            status (str): Planning, In Progress, Completed, On Hold
            technologies (list): List of technologies used
        """
        self.name = name
        self.description = description
        self.status = status
        self.technologies = technologies
        self.created_date = datetime.now().strftime("%Y-%m-%d")

    def display_info(self):
        """Return a formatted string of project information"""
        tech_str = ", ".join(self.technologies)
        return f"{self.name} | {self.status} | {tech_str}"

    def update_status(self, new_status):
        """Update the project's status"""
        self.status = new_status
        return f"✅ Project '{self.name}' status updated to: {self.status}"


# ============================================================================
# CLASS 2: Skill - Represents a technical skill
# ============================================================================
class Skill:
    """
    Skill class represents a technical competency.
    Each skill has a name, category, proficiency level (1-10), and learning resource.
    """

    def __init__(self, name, category, proficiency, learning_resource):
        """
        Constructor - Initializes a new Skill object

        Args:
            name (str): Skill name (e.g., "Python")
            category (str): Category (e.g., "Programming", "AI", "Robotics")
            proficiency (int): Proficiency level from 1-10
            learning_resource (str): Where to learn this skill
        """
        self.name = name
        self.category = category
        self.proficiency = proficiency  # 1-10 scale
        self.learning_resource = learning_resource
        self.last_updated = datetime.now().strftime("%Y-%m-%d")

    def improve_proficiency(self, increase_by=1):
        """Increase proficiency level (max 10)"""
        if self.proficiency < 10:
            self.proficiency = min(10, self.proficiency + increase_by)
            return f"✅ {self.name} proficiency increased to {self.proficiency}/10!"
        return f"⚠️ {self.name} is already at maximum proficiency!"

    def get_proficiency_bar(self):
        """Create a visual progress bar for proficiency"""
        filled = "█" * self.proficiency
        empty = "░" * (10 - self.proficiency)
        return f"[{filled}{empty}] {self.proficiency}/10"


# ============================================================================
# CLASS 3: Goal - Represents a learning or career goal
# ============================================================================
class Goal:
    """
    Goal class represents objectives PÄM wants to achieve.
    Each goal has a description, deadline, and completion status.
    """

    def __init__(self, description, deadline, category):
        """
        Constructor - Initializes a new Goal object

        Args:
            description (str): What the goal is
            deadline (str): Target completion date
            category (str): Learning, Project, Career, Personal
        """
        self.description = description
        self.deadline = deadline
        self.category = category
        self.completed = False
        self.completed_date = None
        self.created_date = datetime.now().strftime("%Y-%m-%d")

    def mark_complete(self):
        """Mark this goal as completed"""
        self.completed = True
        self.completed_date = datetime.now().strftime("%Y-%m-%d")
        return f"🎉 Goal completed: {self.description}!"

    def get_status_emoji(self):
        """Return emoji based on completion status"""
        return "✅" if self.completed else "⏳"

    def display_goal(self):
        """Return formatted goal string"""
        status = "COMPLETED" if self.completed else "IN PROGRESS"
        return f"{self.get_status_emoji()} {self.description} ({status})"


# ============================================================================
# CLASS 4: PamCommandCenter - Main application class
# ============================================================================
class PamCommandCenter:
    """
    Main application class that manages all projects, skills, and goals.
    This is the command center that handles user interaction and data management.
    """

    def __init__(self):
        """
        Constructor - Initializes the command center with sample data
        Sets up all the lists and loads initial content
        """
        self.projects = []
        self.skills = []
        self.goals = []
        self.user_name = "PÄM"

        # Load sample data
        self.load_sample_projects()
        self.load_sample_skills()
        self.load_sample_goals()

        # Display welcome message with motivational quote
        self.show_welcome_message()

    def load_sample_projects(self):
        """Initialize with sample mechatronics projects"""
        sample_projects = [
            Project(
                "AquaLife Water Quality Monitoring System",
                "IoT system monitoring pH, turbidity, and temperature in water bodies",
                "In Progress",
                ["Python", "Arduino", "Sensors", "IoT", "Data Visualization"]
            ),
            Project(
                "FX Trading Bot",
                "Algorithmic trading bot for Forex markets using technical indicators",
                "Planning",
                ["Python", "Pandas", "NumPy", "Backtrader", "APIs"]
            ),
            Project(
                "Football Analytics Dashboard",
                "Interactive dashboard analyzing player performance and match statistics",
                "In Progress",
                ["Python", "Pandas", "Plotly", "Streamlit", "Football APIs"]
            ),
            Project(
                "Smart Home Robot",
                "Autonomous robot for home assistance using computer vision",
                "Planning",
                ["Python", "ROS", "OpenCV", "Raspberry Pi", "Motor Control"]
            )
        ]
        self.projects.extend(sample_projects)

    def load_sample_skills(self):
        """Initialize with sample technical skills"""
        sample_skills = [
            Skill("Python", "Programming", 8, "Angela Yu Course + Practice Projects"),
            Skill("Machine Learning", "AI/ML", 6, "Andrew Ng Course + Kaggle"),
            Skill("Robotics", "Mechatronics", 7, "ROS Tutorials + Project-based"),
            Skill("Git & GitHub", "Version Control", 8, "GitHub Learning Lab"),
            Skill("Data Analysis", "Data Science", 7, "Pandas + Real Projects"),
            Skill("Algorithmic Trading", "Finance", 5, "QuantConnect + Backtesting"),
            Skill("Computer Vision", "AI/ML", 6, "OpenCV + Deep Learning"),
            Skill("ROS (Robot OS)", "Robotics", 5, "ROS Documentation + Simulations")
        ]
        self.skills.extend(sample_skills)

    def load_sample_goals(self):
        """Initialize with sample learning goals"""
        sample_goals = [
            Goal("Complete Angela Yu Python Course", "2024-06-30", "Learning"),
            Goal("Build a Working Trading Bot", "2024-08-15", "Project"),
            Goal("Learn Machine Learning Fundamentals", "2024-07-31", "Learning"),
            Goal("Publish a Robotics Project on GitHub", "2024-09-30", "Career"),
            Goal("Contribute to Open Source", "2024-10-31", "Career"),
            Goal("Build Portfolio Website", "2024-07-15", "Project")
        ]
        self.goals.extend(sample_goals)

    def show_welcome_message(self):
        """Display motivational quote and welcome screen"""
        quotes = [
            "💡 'The only way to do great work is to love what you do.' - Steve Jobs",
            "🚀 'The future belongs to those who believe in the beauty of their dreams.' - Elon Musk",
            "🤖 'AI is the new electricity.' - Andrew Ng",
            "💻 'Code is poetry in motion.' - Unknown",
            "🎯 'Small daily improvements are the key to staggering long-term results.'"
        ]

        # Clear screen for clean display
        print("\n" * 2)
        print("=" * 70)
        print("     🎯 PÄM COMMAND CENTER v1.0 - Mechatronics Dashboard 🎯")
        print("=" * 70)
        print(f"\n👋 Welcome back, {self.user_name}!")
        print(f"📅 Today's Date: {datetime.now().strftime('%B %d, %Y')}")
        print(f"\n🌟 MOTIVATIONAL QUOTE:")
        print(f"   {random.choice(quotes)}")
        print("\n" + "-" * 70)
        input("\n⚡ Press ENTER to continue to main menu...")

    def display_projects(self):
        """
        Display all projects in a formatted PrettyTable
        Shows project name, description, status, and technologies
        """
        print("\n" * 2)
        print("📁 " + "=" * 60)
        print("📁 ACTIVE PROJECTS - Engineering Portfolio")
        print("=" * 60)

        # Create PrettyTable with custom styling
        table = PrettyTable()
        table.field_names = ["#", "Project Name", "Status", "Technologies", "Description"]
        table.align["Project Name"] = "l"
        table.align["Description"] = "l"
        table.max_width["Description"] = 40

        # Add each project to the table
        for idx, project in enumerate(self.projects, 1):
            # Add status emoji
            status_icon = {
                "Planning": "📋",
                "In Progress": "⚙️",
                "Completed": "✅",
                "On Hold": "⏸️"
            }.get(project.status, "🔧")

            tech_str = ", ".join(project.technologies[:3])  # Show first 3 techs
            if len(project.technologies) > 3:
                tech_str += f" +{len(project.technologies) - 3} more"

            table.add_row([
                idx,
                project.name,
                f"{status_icon} {project.status}",
                tech_str,
                project.description[:50] + "..." if len(project.description) > 50 else project.description
            ])

        print(table)
        print(f"\n📊 Total Projects: {len(self.projects)}")
        print(f"   In Progress: {sum(1 for p in self.projects if p.status == 'In Progress')}")
        print(f"   Planning: {sum(1 for p in self.projects if p.status == 'Planning')}")

    def display_skills(self):
        """
        Display all skills in a formatted PrettyTable with proficiency bars
        """
        print("\n" * 2)
        print("🛠️ " + "=" * 60)
        print("🛠️ TECHNICAL SKILLS - Competency Matrix")
        print("=" * 60)

        # Create PrettyTable
        table = PrettyTable()
        table.field_names = ["#", "Skill", "Category", "Proficiency", "Progress", "Learning Resource"]
        table.align["Skill"] = "l"

        # Sort skills by proficiency (highest first)
        sorted_skills = sorted(self.skills, key=lambda x: x.proficiency, reverse=True)

        for idx, skill in enumerate(sorted_skills, 1):
            progress_bar = skill.get_proficiency_bar()
            # Color coding based on proficiency
            prof_level = "🔴" if skill.proficiency < 4 else "🟡" if skill.proficiency < 7 else "🟢"

            table.add_row([
                idx,
                f"{prof_level} {skill.name}",
                skill.category,
                f"{skill.proficiency}/10",
                progress_bar,
                skill.learning_resource[:35] + "..." if len(skill.learning_resource) > 35 else skill.learning_resource
            ])

        print(table)

        # Display skill statistics
        avg_proficiency = sum(s.proficiency for s in self.skills) / len(self.skills)
        print(f"\n📊 Skill Statistics:")
        print(f"   Total Skills: {len(self.skills)}")
        print(f"   Average Proficiency: {avg_proficiency:.1f}/10")
        print(f"   Top Skill: {max(self.skills, key=lambda x: x.proficiency).name}")
        print(f"   Needs Improvement: {sum(1 for s in self.skills if s.proficiency < 5)} skills below 5/10")

    def display_goals(self):
        """
        Display all goals in a formatted PrettyTable
        Shows completion status and deadlines
        """
        print("\n" * 2)
        print("🎯 " + "=" * 60)
        print("🎯 LEARNING GOALS - Roadmap to Success")
        print("=" * 60)

        # Create PrettyTable
        table = PrettyTable()
        table.field_names = ["#", "Goal", "Category", "Status", "Deadline", "Created"]

        for idx, goal in enumerate(self.goals, 1):
            status_display = "✅ COMPLETED" if goal.completed else "⏳ IN PROGRESS"
            deadline_color = "🟢" if goal.completed else "🔴" if goal.deadline < datetime.now().strftime(
                "%Y-%m-%d") else "🟡"

            table.add_row([
                idx,
                goal.description[:40] + "..." if len(goal.description) > 40 else goal.description,
                goal.category,
                status_display,
                f"{deadline_color} {goal.deadline}",
                goal.created_date
            ])

        print(table)

        # Goal statistics
        completed_goals = sum(1 for g in self.goals if g.completed)
        total_goals = len(self.goals)
        completion_rate = (completed_goals / total_goals) * 100 if total_goals > 0 else 0

        print(f"\n📊 Goal Progress:")
        print(f"   Total Goals: {total_goals}")
        print(f"   Completed: {completed_goals}")
        print(f"   Completion Rate: {completion_rate:.1f}%")

        # Progress bar for goals
        filled = "█" * int(completion_rate / 10)
        empty = "░" * (10 - int(completion_rate / 10))
        print(f"   Progress: [{filled}{empty}] {completion_rate:.1f}%")

    def add_new_goal(self):
        """
        Allow user to add a new goal to track
        Interactive input with validation
        """
        print("\n" * 2)
        print("➕ " + "=" * 60)
        print("➕ ADD NEW GOAL")
        print("=" * 60)

        # Get goal details from user
        print("\n📝 Please enter the following information:")

        description = input("   Goal Description: ").strip()
        if not description:
            print("❌ Goal description cannot be empty!")
            return

        print("\n   Category Options:")
        print("      1. Learning")
        print("      2. Project")
        print("      3. Career")
        print("      4. Personal")

        category_map = {"1": "Learning", "2": "Project", "3": "Career", "4": "Personal"}
        category_choice = input("   Select category (1-4): ").strip()
        category = category_map.get(category_choice, "Learning")

        deadline = input("   Target completion date (YYYY-MM-DD): ").strip()

        # Create and add new goal
        new_goal = Goal(description, deadline, category)
        self.goals.append(new_goal)

        print(f"\n✅ Goal added successfully!")
        print(f"   📌 {description}")
        print(f"   📅 Deadline: {deadline}")
        print(f"   🏷️  Category: {category}")

        input("\n⚡ Press ENTER to continue...")

    def mark_goal_completed(self):
        """
        Allow user to mark a goal as completed
        Shows list of incomplete goals to choose from
        """
        print("\n" * 2)
        print("✅ " + "=" * 60)
        print("✅ MARK GOAL AS COMPLETED")
        print("=" * 60)

        # Get incomplete goals
        incomplete_goals = [g for g in self.goals if not g.completed]

        if not incomplete_goals:
            print("\n🎉 Congratulations! All goals are already completed!")
            input("\n⚡ Press ENTER to continue...")
            return

        # Display incomplete goals
        print("\n📋 Incomplete Goals:")
        for idx, goal in enumerate(incomplete_goals, 1):
            print(f"   {idx}. {goal.description}")

        # Get user choice
        try:
            choice = int(input("\n🔢 Select goal number to mark as completed (0 to cancel): "))
            if choice == 0:
                return
            if 1 <= choice <= len(incomplete_goals):
                selected_goal = incomplete_goals[choice - 1]
                result = selected_goal.mark_complete()
                print(f"\n{result}")

                # Check if user wants to add completion notes
                notes = input("📝 Add any notes about this accomplishment? (optional): ")
                if notes:
                    print(f"✅ Notes saved: {notes}")
            else:
                print("❌ Invalid selection!")
        except ValueError:
            print("❌ Please enter a valid number!")

        input("\n⚡ Press ENTER to continue...")

    def display_statistics(self):
        """
        Display comprehensive statistics dashboard
        Shows progress across all areas
        """
        print("\n" * 2)
        print("📊 " + "=" * 60)
        print("📊 PERFORMANCE DASHBOARD - Statistics")
        print("=" * 60)

        # Project statistics
        total_projects = len(self.projects)
        in_progress = sum(1 for p in self.projects if p.status == "In Progress")
        planning = sum(1 for p in self.projects if p.status == "Planning")

        # Skill statistics
        total_skills = len(self.skills)
        avg_skill = sum(s.proficiency for s in self.skills) / total_skills if total_skills > 0 else 0

        # Goal statistics
        total_goals = len(self.goals)
        completed_goals = sum(1 for g in self.goals if g.completed)
        goal_completion_rate = (completed_goals / total_goals) * 100 if total_goals > 0 else 0

        # Create statistics table
        stats_table = PrettyTable()
        stats_table.field_names = ["Category", "Metric", "Value", "Status"]
        stats_table.align["Metric"] = "l"

        stats_table.add_row(["📁 Projects", "Total Projects", total_projects, ""])
        stats_table.add_row(["📁 Projects", "In Progress", in_progress, "⚙️ Active"])
        stats_table.add_row(["📁 Projects", "Planning Phase", planning, "📋 Scheduled"])

        stats_table.add_row(["🛠️ Skills", "Total Skills", total_skills, ""])
        stats_table.add_row(["🛠️ Skills", "Average Proficiency", f"{avg_skill:.1f}/10", ""])
        stats_table.add_row(
            ["🛠️ Skills", "Mastered (8+)", sum(1 for s in self.skills if s.proficiency >= 8), "🌟 Expert"])

        stats_table.add_row(["🎯 Goals", "Total Goals", total_goals, ""])
        stats_table.add_row(["🎯 Goals", "Completed", completed_goals, "✅ Done"])
        stats_table.add_row(["🎯 Goals", "Completion Rate", f"{goal_completion_rate:.1f}%", ""])

        print(stats_table)

        # Overall Progress Bar
        print("\n📈 OVERALL LEARNING PROGRESS")

        # Calculate overall progress (weighted average)
        project_weight = 0.3
        skill_weight = 0.4
        goal_weight = 0.3

        project_score = (in_progress * 0.5 + planning * 0.25) / total_projects if total_projects > 0 else 0
        skill_score = avg_skill / 10
        goal_score = goal_completion_rate / 100

        overall_progress = (project_score * project_weight +
                            skill_score * skill_weight +
                            goal_score * goal_weight) * 100

        filled = "█" * int(overall_progress / 10)
        empty = "░" * (10 - int(overall_progress / 10))

        print(f"   Engineering Journey: [{filled}{empty}] {overall_progress:.1f}%")

        # Next milestone suggestions
        print("\n🎯 NEXT MILESTONES:")
        incomplete_goals = [g for g in self.goals if not g.completed]
        if incomplete_goals:
            print(f"   - Complete: {incomplete_goals[0].description}")
        low_skills = [s for s in self.skills if s.proficiency < 5]
        if low_skills:
            print(f"   - Improve: {low_skills[0].name} (currently {low_skills[0].proficiency}/10)")

        input("\n⚡ Press ENTER to continue...")

    def run(self):
        """
        Main application loop - Displays menu and handles user input
        This is the command center's control room
        """
        while True:
            # Clear screen for clean menu display
            print("\n" * 2)
            print("=" * 70)
            print("     🤖 PÄM COMMAND CENTER - Main Menu 🤖")
            print("=" * 70)
            print("""
    ╔══════════════════════════════════════════════════════════╗
    ║  📁 1. View Projects          🛠️  2. View Skills        ║
    ║  🎯 3. View Goals              ➕  4. Add New Goal       ║
    ║  ✅ 5. Mark Goal Completed     📊  6. View Statistics    ║
    ║  🚪 7. Exit                                            ║
    ╚══════════════════════════════════════════════════════════╝
            """)

            # Get user choice
            choice = input("🔢 Enter your choice (1-7): ").strip()

            # Process user choice
            if choice == "1":
                self.display_projects()
            elif choice == "2":
                self.display_skills()
            elif choice == "3":
                self.display_goals()
            elif choice == "4":
                self.add_new_goal()
            elif choice == "5":
                self.mark_goal_completed()
            elif choice == "6":
                self.display_statistics()
            elif choice == "7":
                self.exit_application()
                break
            else:
                print("\n❌ Invalid choice! Please enter a number between 1 and 7.")
                input("\n⚡ Press ENTER to continue...")

    def exit_application(self):
        """Display farewell message and exit"""
        print("\n" * 2)
        print("=" * 70)
        print("     🚀 THANK YOU FOR USING PÄM COMMAND CENTER 🚀")
        print("=" * 70)
        print("\n📚 Keep pushing forward! Every line of code brings you closer")
        print("   to your goals as a mechatronics engineer.")
        print("\n💡 Remember: 'The expert in anything was once a beginner.'")
        print("\n👋 Goodbye, and keep building amazing things!")
        print("=" * 70)
        print("\n")


# ============================================================================
# MAIN EXECUTION - Program entry point
# ============================================================================
if __name__ == "__main__":
    """
    This is where the program starts running.
    We create an instance of PamCommandCenter and run it.
    """
    try:
        # Create the command center
        command_center = PamCommandCenter()

        # Start the application
        command_center.run()

    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n\n👋 Exiting PÄM Command Center. Keep coding!")
    except Exception as e:
        # Handle any unexpected errors
        print(f"\n❌ An unexpected error occurred: {e}")
        print("Please restart the application.")

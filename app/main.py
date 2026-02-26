from app.models import Actor
from app.managers import ActorManager


def run_demo():
    # Initialize the manager with the database name and table name
    db_name = "cinema_db.sqlite"
    table_name = "actor_manager"
    manager = ActorManager(db_name, table_name)

    # Assign the manager to the Actor class (ORM style)
    Actor.objects = manager

    # 1. Add data (Create)
    print("Adding actors...")
    Actor.objects.create(first_name="Leonardo", last_name="DiCaprio")
    Actor.objects.create(first_name="Cate", last_name="Blanchett")

    # 2. Display results (Read)
    print("\nList of actors in the database:")
    for actor in Actor.objects.all():
        print(f"- {actor.first_name} {actor.last_name} (ID: {actor.id})")


if __name__ == "__main__":
    run_demo()

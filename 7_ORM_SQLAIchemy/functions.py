from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import logging

from classes import Base


# Setting up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_session(database):
    """Creates and returns a database session.

     Args:
         database (str): Database URL.

     Returns:
         sessionmaker: SQLAlchemy session object.
     """
    engine = create_engine(database)
    Base.metadata.create_all(engine)
    DBSession = sessionmaker(bind=engine)
    return DBSession()

@contextmanager
def get_session(database): 
    """Context manager for creating and closing a database session.

     Args:
         database (str): Database URL.

     Yields:
         Session: SQLAlchemy session.
     """
    session = create_session(database)
    try:
        yield session
    except Exception as e:  # logging
        logger.error("Error in session: %s", e)
        session.rollback()
        raise
    finally:
        session.close()


def get_id_item(session, id_column, name_column, table):
    query = session.query(id_column, name_column).select_from(table)
    result = query.all()

    input_text = "Please, select an item:\n"
    list_target_id = []
    for student_id, student_name in result:
        input_text += f"{student_id} - {student_name}\n"
        list_target_id.append(student_id)
    
    min_student_id = min(list_target_id)
    max_student_id = max(list_target_id)

    VALUE_RANGE = f"The acceptable range of values is between {min_student_id} and {max_student_id} and you can see it in the screen."
    INPUT = f"Enter a number between {min_student_id} and {max_student_id} and you can see it in the screen: "
    ERROR = "Error: Please enter a valid number."

    first_run = True
    while True:
        if first_run:
            print(input_text)
        try:
            selected_id = int(input(INPUT))
            if selected_id in list_target_id:
                return selected_id
            else:
                print(VALUE_RANGE)
        except ValueError:
            print(ERROR)
        
        first_run = False
# Lab 05: Functions and Error Handling

users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False}
]


def calculate_average_age(users):
    """
    Calculate the average age of users with valid integer ages.

    Parameters
    ----------
    users : list of dict
        A list of user dictionaries, each containing at least an 'age' key.

    Returns
    -------
    float
        The average age of users with valid integer ages. Returns 0.0 if the
        list is empty or contains no valid ages.

    Notes
    -----
    - Only users with integer age values are included in the calculation.
    - Non-integer age values (e.g., strings) are skipped.
    - Returns 0.0 if no valid ages are found to prevent ZeroDivisionError.
    """
    try:
        total_age = 0
        user_count_for_age = 0

        for user in users:
            if isinstance(user.get("age"), int):
                total_age += user["age"]
                user_count_for_age += 1

        if user_count_for_age == 0:
            return 0.0

        return total_age / user_count_for_age
    except ZeroDivisionError:
        print("error: cannot calculate average age of an empty list.")
        return 0.0


def get_active_user_emails(users):
    """
    Extract emails from active users.

    Parameters
    ----------
    users : list of dict
        A list of user dictionaries, each potentially containing 'is_active'
        and 'email' keys.

    Returns
    -------
    list of str
        A list of email addresses from users that are active and have an
        email field. Returns an empty list if no active users with emails
        are found.

    Notes
    -----
    - Only includes users where both 'is_active' is True and 'email' exists.
    - Gracefully handles missing keys by using the .get() method.
    - Returns an empty list for an empty input list.
    """
    try:
        active_user_emails = []

        for user in users:
            if user.get("is_active") and user.get("email"):
                active_user_emails.append(user["email"])

        return active_user_emails
    except (KeyError, TypeError) as e:
        print(f"error: unable to process user data. {e}")
        return []


if __name__ == '__main__':
    # Call functions and print results
    avg_age = calculate_average_age(users)
    print(f"average user age: {avg_age:.2f}")

    active_emails = get_active_user_emails(users)
    print(f"active user emails: {active_emails}")

def create_budget(
    income,
    fixed_expenses=None,
    variable_expenses=None,
    savings_goal=0
):
    """
    Prepare structured budget information for the AI assistant.
    """

    if income is None or income < 0:
        return {
            "success": False,
            "message": "Valid income amount batao."
        }

    fixed_expenses = fixed_expenses or {}
    variable_expenses = variable_expenses or {}

    total_fixed = sum(fixed_expenses.values())
    total_variable = sum(variable_expenses.values())
    total_expenses = total_fixed + total_variable

    remaining = income - total_expenses

    budget_data = {
        "income": income,
        "fixed_expenses": fixed_expenses,
        "variable_expenses": variable_expenses,
        "total_expenses": total_expenses,
        "remaining": remaining,
        "savings_goal": savings_goal
    }

    return {
        "success": True,
        "message": "Budget information prepared.",
        "data": budget_data
    }
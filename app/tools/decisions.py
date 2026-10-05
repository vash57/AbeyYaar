def compare_decisions(options, criteria=None):
    """
    Prepare structured information for comparing different options.
    """

    if not options or len(options) < 2:
        return {
            "success": False,
            "message": "Decision compare karne ke liye kam se kam 2 options chahiye."
        }

    criteria = criteria or []

    decision_data = {
        "options": options,
        "criteria": criteria
    }

    return {
        "success": True,
        "message": "Decision information prepared.",
        "data": decision_data
    }
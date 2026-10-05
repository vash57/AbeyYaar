def create_roadmap(goal, current_level="beginner", duration="flexible"):
    """
    Create a structured roadmap request for the AI assistant.

    This tool prepares the roadmap context.
    Gemma generates the final natural-language response.
    """

    if not goal or not goal.strip():
        return {
            "success": False,
            "message": "Roadmap ke liye goal batao."
        }

    roadmap_data = {
        "goal": goal.strip(),
        "current_level": current_level,
        "duration": duration
    }

    return {
        "success": True,
        "message": "Roadmap information prepared.",
        "data": roadmap_data
    }
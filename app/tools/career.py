def create_career_profile(
    interests,
    skills=None,
    experience_level="beginner",
    preferred_field=None
):
    """
    Prepare structured career information for the AI assistant.
    """

    if not interests or not interests.strip():
        return {
            "success": False,
            "message": "Career guidance ke liye interests batao."
        }

    career_data = {
        "interests": interests.strip(),
        "skills": skills or [],
        "experience_level": experience_level,
        "preferred_field": preferred_field
    }

    return {
        "success": True,
        "message": "Career information prepared.",
        "data": career_data
    }
def create_resume_profile(
    name,
    education=None,
    skills=None,
    projects=None,
    experience=None,
    target_role=None
):
    """
    Prepare structured resume information for the AI assistant.
    """

    if not name or not name.strip():
        return {
            "success": False,
            "message": "Resume ke liye naam batao."
        }

    resume_data = {
        "name": name.strip(),
        "education": education or [],
        "skills": skills or [],
        "projects": projects or [],
        "experience": experience or [],
        "target_role": target_role
    }

    return {
        "success": True,
        "message": "Resume information prepared.",
        "data": resume_data
    }
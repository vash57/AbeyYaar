from enum import Enum


class Intent(str, Enum):
    GENERAL = "general"
    CAREER = "career"
    RESUME = "resume"
    BUDGET = "budget"
    ROADMAP = "roadmap"
    DECISION = "decision"


def detect_intent(message: str) -> Intent:
    """Detect the user's intent using lightweight keyword matching."""

    text = message.lower().strip()

    if any(word in text for word in [
        "resume", "cv", "curriculum vitae", "linkedin"
    ]):
        return Intent.RESUME

    if any(word in text for word in [
        "career", "job", "internship", "placement", "profession"
    ]):
        return Intent.CAREER

    if any(word in text for word in [
       "budget",
    "expense",
    "expenses",
    "money",
    "paise",
    "paisa",
    "saving",
    "savings",
    "bachat",
    "spend",
    "spending",
    "kharcha",
    "kharch",
    "manage paise",
    "paise manage"
    ]):
        return Intent.BUDGET

    if any(word in text for word in [
        "roadmap", "study plan", "plan bana",
        "preparation", "prepare", "schedule"
    ]):
        return Intent.ROADMAP

    if any(word in text for word in [
        "decision", "decide", "confused", "choose",
        "choice", "which one", "kya choose"
    ]):
        return Intent.DECISION

    return Intent.GENERAL
class SafetyChecker:
    """Basic safety checks for harmful and high-risk requests."""

    BLOCKED_PATTERNS = [
        "make a bomb",
        "build a bomb",
        "hack someone's account",
        "steal password",
        "steal someone's password",
        "bypass security",
    ]

    SELF_HARM_PATTERNS = [
        "kill myself",
        "suicide",
        "commit suicide",
        "want to die",
        "don't want to live",
        "dont want to live",
        "end my life",
        "end it all",
        "hurt myself",
        "harm myself",
        "self harm",
        "self-harm",
    ]

    def is_safe(self, message):
        """Return True only when the message does not indicate a blocked request."""

        if not message:
            return True

        text = message.lower().strip()

        for pattern in self.BLOCKED_PATTERNS:
            if pattern in text:
                return False

        for pattern in self.SELF_HARM_PATTERNS:
            if pattern in text:
                return False

        return True

    def get_message(self, message):
        """Return an appropriate response for an unsafe or high-risk message."""

        if not message:
            return None

        text = message.lower().strip()

        for pattern in self.SELF_HARM_PATTERNS:
            if pattern in text:
                return (
                    "Yaar, mujhe genuinely afsos hai ki tu itna heavy feel kar raha hai. "
                    "Abhi akela mat reh—kisi trusted friend, family member, teacher ya "
                    "counsellor ko turant bata ki tu kaisa feel kar raha hai. "
                    "Agar tujhe lag raha hai ki tu khud ko abhi hurt kar sakta hai, "
                    "to emergency services ya nearest emergency department se immediate help le."
                )

        for pattern in self.BLOCKED_PATTERNS:
            if pattern in text:
                return (
                    "Is request mein main help nahi kar sakta. "
                    "Kuch safe alternative ho to usmein help kar dunga."
                )

        return None
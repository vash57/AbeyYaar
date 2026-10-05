import { useState } from "react";
import "./App.css";

const API_URL = "http://127.0.0.1:8000";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async (text = input) => {
    const message = text.trim();

    if (!message || loading) return;

    setMessages((prev) => [
      ...prev,
      {
        sender: "user",
        text: message,
      },
    ]);

    setInput("");
    setLoading(true);

    try {
      const response = await fetch(`${API_URL}/api/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: message,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Backend request failed");
      }

      setMessages((prev) => [
        ...prev,
        {
          sender: "friend",
          text: data.response,
        },
      ]);
    } catch (error) {
      console.error("Chat error:", error);

      setMessages((prev) => [
        ...prev,
        {
          sender: "friend",
          text: "Yaar, backend se connection mein issue aa gaya.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="header">
        <div className="brand">
          <div className="logo">
            <span>A</span>
          </div>
          <div className="brand-text">
            <h1>AbeyYaar AI</h1>
            <p>Your local AI friend</p>
          </div>
        </div>

        <div className="status">
          <span className="dot" />
          <span className="status-text">
            <strong>Local AI</strong>
            <em>Ollama · Gemma</em>
          </span>
        </div>
      </header>

      <main className="chat">
        {messages.length === 0 && (
          <section className="welcome">
            <div className="hero-avatar">
              <span>A</span>
            </div>

            <h2>What's on your mind?</h2>
            <p className="subtitle">
              Talk to your AI friend about anything — studies, career,
              decisions, or just your day.
            </p>

            <div className="suggestions">
              <button onClick={() => sendMessage("Help me plan my GATE preparation")}>
                <span className="s-ico">🎯</span>
                Help me plan my GATE preparation
              </button>

              <button onClick={() => sendMessage("I'm confused about my career")}>
                <span className="s-ico">🧭</span>
                I'm confused about my career
              </button>

              <button onClick={() => sendMessage("Help me make a study roadmap")}>
                <span className="s-ico">🗺️</span>
                Help me make a study roadmap
              </button>

              <button onClick={() => sendMessage("Should I buy this laptop?")}>
                <span className="s-ico">💻</span>
                Should I buy this laptop?
              </button>

              <button onClick={() => sendMessage("Help me manage my budget")}>
                <span className="s-ico">💰</span>
                Help me manage my budget
              </button>

              <button onClick={() => sendMessage("I need help making a decision")}>
                <span className="s-ico">🤔</span>
                I need help making a decision
              </button>
            </div>

            <div className="capabilities">
              <div className="cap-card career">
                <div className="cap-icon">◆</div>
                <h4>Career</h4>
                <p>Guidance · Resume · Placement</p>
              </div>

              <div className="cap-card learning">
                <div className="cap-icon">▲</div>
                <h4>Learning</h4>
                <p>GATE · Study plans · Skills</p>
              </div>

              <div className="cap-card decisions">
                <div className="cap-icon">●</div>
                <h4>Decisions</h4>
                <p>Pros &amp; cons · Buying</p>
              </div>

              <div className="cap-card life">
                <div className="cap-icon">■</div>
                <h4>Student Life</h4>
                <p>College · Budget · Daily</p>
              </div>

              <div className="cap-card wellbeing">
                <div className="cap-icon">♥</div>
                <h4>Wellbeing</h4>
                <p>Stress · Support · Feelings</p>
              </div>
            </div>
          </section>
        )}

        <div className="messages">
          {messages.map((message, index) => (
            <div
              key={index}
              className={`message-row ${message.sender}`}
            >
              {message.sender === "friend" && (
                <div className="msg-avatar">A</div>
              )}

              <div className="message">
                <span className="label">
                  {message.sender === "friend" ? "Friend" : "You"}
                </span>
                <p>{message.text}</p>
              </div>
            </div>
          ))}

          {loading && (
            <div className="message-row friend">
              <div className="msg-avatar">A</div>
              <div className="message thinking">
                <span className="label">Friend</span>
                <p>
                  Thinking
                  <span className="dots">
                    <i>.</i>
                    <i>.</i>
                    <i>.</i>
                  </span>
                </p>
              </div>
            </div>
          )}
        </div>
      </main>

      <div className="input-area">
        <input
          type="text"
          placeholder="Talk to your friend..."
          value={input}
          disabled={loading}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              sendMessage();
            }
          }}
        />

        <button
          onClick={() => sendMessage()}
          disabled={loading}
          aria-label="Send message"
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true">
            <path
              d="M4.5 12L20 4.5L14 20L11.5 13.5L4.5 12Z"
              fill="currentColor"
            />
          </svg>
        </button>
      </div>
    </div>
  );
}

export default App;
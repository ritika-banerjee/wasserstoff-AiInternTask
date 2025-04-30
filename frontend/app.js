const API_BASE = "https://wasserstoff-aiinterntask-production-5a3d.up.railway.app";

async function submitGuess() {
  const guess = document.getElementById("guessInput").value.trim();
  const persona = document.getElementById("persona").value;
  const responseMsg = document.getElementById("responseMsg");
  const scoreDisplay = document.getElementById("scoreDisplay");
  const globalCount = document.getElementById("globalCount");
  const guessHistory = document.getElementById("guessHistory");

  if (!guess) {
    responseMsg.innerText = "❗Please enter a guess.";
    return;
  }

  try {
    const res = await fetch(`${API_BASE}/guess?persona=${persona}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "host-persona": persona
      },
      body: JSON.stringify({ guess })
    });

    const data = await res.json();

    responseMsg.innerText = data.message;

    if (data.status === "success") {
      scoreDisplay.innerText = `Score: ${data.score}`;
      guessHistory.innerText = data.last_five.join(" → ");

      // Extract global guess count from message
      const match = data.message.match(/has been guessed (\d+) times/i);
      if (match) {
        globalCount.innerText = `🌎 Global guess count: ${match[1]}`;
      }
    }

    if (data.status === "game_over") {
      responseMsg.innerText += " 💀 Game Over.";
    }

  } catch (err) {
    console.error(err);
    responseMsg.innerText = "⚠ Server error.";
  }
}

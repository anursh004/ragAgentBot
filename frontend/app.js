const form = document.getElementById("ticket-form");
const eventStream = document.getElementById("event-stream");
const finalResponse = document.getElementById("final-response");

const apiBase = "http://localhost:8000";

const renderEvents = (events) => {
  eventStream.innerHTML = "";
  events.forEach((event) => {
    const li = document.createElement("li");
    li.innerHTML = `
      <strong>${event.agent}</strong>
      <span>${event.step}</span>
      <pre>${JSON.stringify(event.payload, null, 2)}</pre>
    `;
    eventStream.appendChild(li);
  });
};

const fetchEvents = async () => {
  const response = await fetch(`${apiBase}/events`);
  const data = await response.json();
  renderEvents(data.events || []);
};

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const formData = new FormData(form);
  const payload = {
    ticket_id: formData.get("ticketId"),
    text: formData.get("ticketText"),
    source: "support",
  };

  finalResponse.textContent = "Running agents...";
  const response = await fetch(`${apiBase}/orchestrate`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  const result = await response.json();
  finalResponse.textContent = result.final_response;
  await fetchEvents();
});

setInterval(fetchEvents, 3000);

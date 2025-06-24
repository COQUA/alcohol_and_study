document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("form");
  const resultadoDiv = document.getElementById("resultado");

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    resultadoDiv.textContent = "Calculando...";

    // Construir objeto de entrada
    const data = {};
    new FormData(form).forEach((value, key) => {
      data[key] = Number(value);
    });

    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        const err = await response.json();
        throw new Error(err.detail || "Error en la predicción");
      }

      const json = await response.json();
      resultadoDiv.textContent = `Nota estimada (G3): ${json.predicted_G3}`;
    } catch (error) {
      resultadoDiv.textContent = `Error: ${error.message}`;
      console.error("Error al predecir:", error);
    }
  });
});
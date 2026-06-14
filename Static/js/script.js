const predictionCtx = document.getElementById("predictionChart");

if (predictionCtx) {
  const temperature = Number(predictionCtx.dataset.temperature);

  const humidity = Number(predictionCtx.dataset.humidity);

  const windspeed = Number(predictionCtx.dataset.windspeed);

  const rain = Number(predictionCtx.dataset.rain);

  new Chart(predictionCtx, {
    type: "bar",
    data: {
      labels: ["Temperature", "Humidity", "Wind Speed", "Rain"],
      datasets: [
        {
          label: "Prediction Input Values",
          data: [temperature, humidity, windspeed, rain],
          backgroundColor: ["#3b82f6", "#22c55e", "#f59e0b", "#ef4444"],
          borderRadius: 8,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          labels: {
            color: "white",
          },
        },
      },
      scales: {
        x: {
          ticks: {
            color: "white",
          },
        },
        y: {
          ticks: {
            color: "white",
          },
        },
      },
    },
  });
}

// Auto-refresh health score badge colour based on value
document.addEventListener("DOMContentLoaded", () => {
    const healthCard = document.querySelector(".stat-card.health .stat-value");
    if (!healthCard) return;

    const score = parseFloat(healthCard.textContent);

    if (score >= 90) {
        healthCard.style.color = "#68d391";   // green
    } else if (score >= 60) {
        healthCard.style.color = "#f6e05e";   // yellow
    } else {
        healthCard.style.color = "#fc8181";   // red
    }
});
